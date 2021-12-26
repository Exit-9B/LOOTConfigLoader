from mobase import IPlugin
from .lootconfigmapper import LOOTConfigMapper


def createPlugin() -> IPlugin:
    return LOOTConfigMapper()
