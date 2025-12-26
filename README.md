# Random Work
This is a place where I dump a bunch of random projects

## Setting Up Repo

### Install pyenv
```shell
sudo apt install libsqlite3-dev tk-dev python3-tk -y
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

### Install into to .bashrc
```shell
./$HOME/Code/random_work/src/linux_utils/install_into_bashrc.sh
```

### Install Python
```shell
pyenv install $(cat .python-version)
```

### Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup virtual environment
```shell
uv sync
```

### Setup Path Of Building folder access
```shell
sudo flatpak override community.pathofbuilding.PathOfBuilding --filesystem=$HOME/Code/random_work/src/poe_builds/
sudo flatpak override community.pathofbuilding.PathOfBuilding --filesystem=$HOME/Code/random_work/src/poe2_builds/
```
