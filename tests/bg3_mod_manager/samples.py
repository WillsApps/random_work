GUSTAV_X_MOD = {
    "@id": "ModuleShortDesc",
    "attribute": [
        {
            "@id": "Folder",
            "@type": "LSString",
            "@value": "GustavX",
        },
        {
            "@id": "MD5",
            "@type": "LSString",
            "@value": "34a0c6d5bef9658123228d6a19a5cc00",
        },
        {
            "@id": "Name",
            "@type": "LSString",
            "@value": "GustavX",
        },
        {
            "@id": "PublishHandle",
            "@type": "uint64",
            "@value": "0",
        },
        {
            "@id": "UUID",
            "@type": "guid",
            "@value": "cb555efe-2d9e-131f-8195-a89329d218ea",
        },
        {
            "@id": "Version64",
            "@type": "int64",
            "@value": "145241302737902957",
        },
    ],
}
PARSED_XML_ONE_MOD_NO_MOD_ORDER = {
    "save": {
        "version": {
            "@major": "4",
            "@minor": "8",
            "@revision": "0",
            "@build": "200",
        },
        "region": {
            "@id": "ModuleSettings",
            "node": {
                "@id": "root",
                "children": {
                    "node": {
                        "@id": "Mods",
                        "children": {"node": GUSTAV_X_MOD},
                    }
                },
            },
        },
    }
}

PARSED_XML_TWO_MODS_NO_MOD_ORDER = {
    "save": {
        "version": {
            "@major": "4",
            "@minor": "8",
            "@revision": "0",
            "@build": "200",
        },
        "region": {
            "@id": "ModuleSettings",
            "node": {
                "@id": "root",
                "children": {
                    "node": {
                        "@id": "Mods",
                        "children": {
                            "node": [
                                GUSTAV_X_MOD,
                                GUSTAV_X_MOD,
                            ]
                        },
                    }
                },
            },
        },
    }
}

PARSED_XML_ONE_MOD_EMPTY_MOD_ORDER = {
    "save": {
        "version": {
            "@major": "4",
            "@minor": "8",
            "@revision": "0",
            "@build": "200",
        },
        "region": {
            "@id": "ModuleSettings",
            "node": {
                "@id": "root",
                "children": {
                    "node": [
                        {"@id": "ModOrder"},
                        {
                            "@id": "Mods",
                            "children": {"node": GUSTAV_X_MOD},
                        },
                    ]
                },
            },
        },
    }
}

PARSED_XML_TWO_MODS_EMPTY_MOD_ORDER = {
    "save": {
        "version": {
            "@major": "4",
            "@minor": "8",
            "@revision": "0",
            "@build": "200",
        },
        "region": {
            "@id": "ModuleSettings",
            "node": {
                "@id": "root",
                "children": {
                    "node": [
                        {"@id": "ModOrder"},
                        {
                            "@id": "Mods",
                            "children": {
                                "node": [
                                    GUSTAV_X_MOD,
                                    GUSTAV_X_MOD,
                                ]
                            },
                        },
                    ]
                },
            },
        },
    }
}


MOD_NODE_5E_SPELLS = {
    "@id": "ModuleShortDesc",
    "attribute": [
        {"@id": "Name", "@type": "LSString", "@value": "5eSpells"},
        {
            "@id": "UUID",
            "@type": "guid",
            "@value": "fb5f528d-4d48-4bf2-a668-2274d3cfba96",
        },
        {"@id": "Folder", "@type": "LSString", "@value": "5eSpells"},
        {"@id": "Version64", "@type": "int64", "@value": "1"},
        {"@id": "PublishHandle", "@type": "uint64", "@value": "0"},
    ],
}


MOD_NODE_MOD_CONFIGURATION = {
    "@id": "ModuleShortDesc",
    "attribute": [
        {
            "@id": "Name",
            "@type": "LSString",
            "@value": "Mod Configuration Menu",
        },
        {
            "@id": "UUID",
            "@type": "guid",
            "@value": "755a8a72-407f-4f0d-9a33-274ac0f0b53d",
        },
        {"@id": "Folder", "@type": "LSString", "@value": "BG3MCM"},
        {"@id": "Version64", "@type": "int64", "@value": "40391659157979136"},
        {
            "@id": "MD5",
            "@type": "LSString",
            "@value": "405322d230c88a287892f76f0dfb9a4a",
        },
        {"@id": "PublishHandle", "@type": "uint64", "@value": "0"},
    ],
}

MOD_LIST = [GUSTAV_X_MOD, MOD_NODE_5E_SPELLS, MOD_NODE_MOD_CONFIGURATION]


XML_WITH_NO_MOD_ORDER = {
    "save": {
        "version": {
            "@major": "4",
            "@minor": "8",
            "@revision": "0",
            "@build": "200",
        },
        "region": {
            "@id": "ModuleSettings",
            "node": {
                "@id": "root",
                "children": {
                    "node": {
                        "@id": "Mods",
                        "children": {"node": MOD_LIST},
                    }
                },
            },
        },
    }
}
XML_WITH_EMPTY_MOD_ORDER = {
    "save": {
        "version": {
            "@major": "4",
            "@minor": "8",
            "@revision": "0",
            "@build": "200",
        },
        "region": {
            "@id": "ModuleSettings",
            "node": {
                "@id": "root",
                "children": {
                    "node": [
                        {"@id": "ModOrder"},
                        {
                            "@id": "Mods",
                            "children": {"node": MOD_LIST},
                        },
                    ]
                },
            },
        },
    }
}
