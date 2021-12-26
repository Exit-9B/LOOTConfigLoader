from genericpath import exists
from PyQt5.QtWidgets import QMainWindow
from mobase import (
    IPluginFileMapper,
    IOrganizer,
    PluginSetting,
    VersionInfo,
    ReleaseType,
    Mapping,
)
from PyQt5 import QtCore
from typing import List, Optional
import os


class LOOTConfigMapper(IPluginFileMapper):
    def __init__(self):
        super().__init__()

    def author(self) -> str:
        return "Parapets"

    def description(self) -> str:
        return "Manages LOOT configs"

    def init(self, organizer: "IOrganizer") -> bool:
        self.organizer = organizer
        organizer.onUserInterfaceInitialized(self.setup_paths)
        return True

    def name(self) -> str:
        return "LOOT Config Loader"

    def settings(self) -> List["PluginSetting"]:
        return []

    def version(self) -> "VersionInfo":
        return VersionInfo(1, 0, 0, 0, ReleaseType.BETA)

    def mappings(self) -> List["Mapping"]:
        mappings = []
        loot_mapping = self.get_loot_mapping()
        if loot_mapping:
            mappings.append(loot_mapping)

        return mappings

    def get_source_path(self) -> str:
        return os.path.join(self.organizer.basePath(), "LOOT Config Files")

    def get_destination_path(self) -> str:
        localappdata = os.getenv("LOCALAPPDATA")
        if not localappdata:
            return ""

        return os.path.join(localappdata, "LOOT")

    def get_loot_mapping(self) -> Optional["Mapping"]:
        source = self.get_source_path()
        destination = self.get_destination_path()

        if destination:
            return Mapping(source, destination, True, False)
        else:
            return None

    def setup_paths(self, window: QMainWindow) -> None:
        source = self.get_source_path()
        if not os.path.exists(source):
            os.mkdir(source)

        destination = self.get_destination_path()

        if destination:
            game_name = self.organizer.managedGame().gameName()
            os.makedirs(os.path.join(destination, game_name), exist_ok=True)
