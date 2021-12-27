# LOOT Config Loader for Mod Organizer
This is a plugin for [Mod Organizer 2](https://www.modorganizer.org/) that
allows for virtualization of [LOOT](https://loot.github.io/) config files.
This makes it possible to have instance-specific LOOT configs, which are
respected by the Sort button in Mod Organizer. You can use this to ship your
LOOT config with a [Wabbajack](https://www.wabbajack.org/) modlist and have it
work automatically when the list is installed.

## Installation
Extract the `lootconfigloader` folder to the Mod Organizer plugins folder.

The resulting folder hierarchy should be
`<MO2 DIR>\plugins\lootconfigloader`, with the python scripts inside it.

## Usage
When you first start Mod Organizer with the plugin installed, it should create
a folder called `LOOT Config Files` in your instance. Any files you place here
will be virtualized to `%LOCALAPPDATA%\LOOT`. Typically, you would add
`settings.toml` and `<game name>\userlist.yaml` here. Make sure your settings
don't contain any private personal information if you will be sharing them!

### Removing the masterlist
Mod Organizer will complain if you try to blank out the masterlist repository,
so if you wish you remove the masterlist, you should provide a dummy repository
instead. In your LOOT settings, set the Masterlist Repository URL to
`https://github.com/Exit-9B/loot-dummy-masterlist.git` and the Masterlist
Repository Branch to `main`.
