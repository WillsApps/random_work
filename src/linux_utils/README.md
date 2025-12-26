# Install .bash_aliases
```shell
vim ~/.bash_exports

# Insert
if [ -f ~/Code/random_work/src/linux_utils/.bash_aliases ]; then
    . ~/Code/random_work/src/linux_utils/.bash_aliases
    . ~/Code/random_work/src/linux_utils/.bash_exports
fi
```

# Setup Path Of Building folder access
```shell
sudo flatpak override community.pathofbuilding.PathOfBuilding --filesystem=$HOME/Code/random_work/src/poe_builds/
sudo flatpak override community.pathofbuilding.PathOfBuilding --filesystem=$HOME/Code/random_work/src/poe2_builds/
```
