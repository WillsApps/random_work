import json
import zipfile
from copy import deepcopy
from pathlib import Path

import rarfile
import xmltodict
from beartype.typing import Optional

from bg3_linux_mod_manager.constants import MODS_DIR, PUBLIC_XML, STEAM_XML, TEMP_DIR

public_example = """<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="8" revision="0" build="200"/>
    <region id="ModuleSettings">
        <node id="root">
            <children>
                <node id="ModOrder" />
                <node id="Mods">
                    <children>
                        <node id="ModuleShortDesc">
                            <attribute id="Folder" type="LSString" value="GustavX"/>
                            <attribute id="MD5" type="LSString" value="34a0c6d5bef9658123228d6a19a5cc00"/>
                            <attribute id="Name" type="LSString" value="GustavX"/>
                            <attribute id="PublishHandle" type="uint64" value="0"/>
                            <attribute id="UUID" type="guid" value="cb555efe-2d9e-131f-8195-a89329d218ea"/>
                            <attribute id="Version64" type="int64" value="145241302737902957"/>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>
"""


def extract_mod_files(mod_path: Path) -> tuple[Optional[Path], list[str]]:
    info_path = None
    if mod_path.suffix == ".zip":
        with zipfile.ZipFile(mod_path, "r") as zip_ref:
            info_path, pak_names = method_name(zip_ref, info_path)
    elif mod_path.suffix == ".rar":
        with rarfile.RarFile(mod_path, "r") as rar_ref:
            info_path, pak_names = method_name(rar_ref, info_path)
    return info_path, pak_names


def method_name(compressed_ref, info_path):
    pak_files = [f for f in compressed_ref.filelist if f.filename.endswith(".pak")]
    pak_names = []
    for pak_file in pak_files:
        compressed_ref.extract(pak_file, MODS_DIR)
        pak_names.append(pak_file.filename)
    info_file = [f for f in compressed_ref.filelist if f.filename == "info.json"]
    if info_file:
        compressed_ref.extract(info_file[0], TEMP_DIR)
        info_path = TEMP_DIR / info_file[0].filename
    return info_path, pak_names


def build_empty_mod_nodes(pak_names: list[str]) -> list[dict]:
    return build_mod_nodes({"mods": [{"name": pak_name, "folder": pak_name, "version": "1"} for pak_name in pak_names]})


def build_mod_nodes(info_json: dict) -> list[dict]:
    info_attribute_map = {
        "modname": "Name",
        "name": "Name",
        "uuid": "UUID",
        "foldername": "Folder",
        "folder": "Folder",
        "version": "Version64",
        "md5": "MD5",
    }

    attribute_type_map = {
        "Name": "LSString",
        "UUID": "guid",
        "Folder": "LSString",
        "Version64": "int64",
        "MD5": "LSString",
    }

    global_md5 = info_json.get("MD5")

    mod_nodes = []

    mods = info_json.get("mods", info_json.get("Mods", []))

    for mod in mods:
        mod_node = {"@id": "ModuleShortDesc", "attribute": []}
        for info_name, attribute_name in info_attribute_map.items():
            for key in list(mod.keys()):
                mod[key.lower()] = mod[key]
            value = mod.get(info_name)
            if not value or value == "":
                continue
            mod_node["attribute"].append(
                {
                    "@id": attribute_name,
                    "@type": attribute_type_map[attribute_name],
                    "@value": value,
                }
            )
        if global_md5 and "md5" not in mod.keys():
            mod_node["attribute"].append({"@id": "MD5", "@type": attribute_type_map["MD5"], "@value": global_md5})
        mod_node["attribute"].append({"@id": "PublishHandle", "@type": "uint64", "@value": "0"})
        mod_nodes.append(mod_node)
    return mod_nodes


def read_xml(source_xml: str) -> dict:
    return xmltodict.parse(source_xml)


def get_mods_list(parsed_xml: dict) -> list[dict]:
    mods = parsed_xml["save"]["region"]["node"]["children"]["node"]
    if isinstance(mods, list):
        mods = [node for node in mods if node["@id"] == "Mods"][0]
    mods = mods["children"]["node"]
    if isinstance(mods, dict):
        return [mods]
    return mods


def replace_mods_list(parsed_xml: dict, mods_list) -> dict:
    new_xml = deepcopy(parsed_xml)
    mods = new_xml["save"]["region"]["node"]["children"]["node"]
    if isinstance(mods, dict):
        new_xml["save"]["region"]["node"]["children"]["node"]["children"]["node"] = mods_list
    else:
        for _index, mod in enumerate(mods):
            if mod["@id"] == "Mods":
                break
        new_xml["save"]["region"]["node"]["children"]["node"][_index]["children"]["node"] = mods_list
    return new_xml


def get_mod_uuids(mods_list: list) -> list[str]:
    return []


def add_mod(mod_path: Path):
    info_path, pak_paths = extract_mod_files(mod_path)
    source_xml = PUBLIC_XML.read_text()
    # source_xml = public_example
    public_xml = read_xml(source_xml)
    mods_list = get_mods_list(public_xml)
    if info_path:
        info_json = json.loads(info_path.read_text())
        mods_list.extend(build_mod_nodes(info_json))
        public_xml = replace_mods_list(public_xml, mods_list)
    else:
        mods_list.extend(build_empty_mod_nodes(pak_paths))
        public_xml = replace_mods_list(public_xml, mods_list)

    raw = xmltodict.unparse(public_xml, short_empty_elements=True, pretty=True, indent="    ")
    PUBLIC_XML.write_text(raw)
    STEAM_XML.write_text(raw)


def main():
    # add_mod(
    #     Path.home()
    #     / "Downloads"
    #     / "Mod Configuration Menu 1.31.0-9162-1-31-0-1747588512.zip"
    # )
    # add_mod(Path.home() / "Downloads" / "5e Spells-125-2-3-0-0-1746891437.zip")
    # add_mod(Path("~/Downloads/Clear Map No Grid Transparent Shroud-2256-1-2-6-1744782367.zip"))
    add_mod(Path("~/Downloads/Vessnelle's Hair Collection pack 1-1420-1-0-1708501781.zip"))
    add_mod(Path("~/Downloads/Vessnelle's Hair Collection pack 2-1420-1-0-1708586487.zip"))
    add_mod(Path("~/Downloads/Vessnelle's Hair Collection pack 3-1420-1-0-1709577118.zip"))
    add_mod(Path("~/Downloads/Vessnelle's Hair Collection pack 4-1420-1-0-1711767563.zip"))


if __name__ == "__main__":
    main()
