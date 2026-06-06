from PyUB.Types.Properties import *
from . import lang_consts as lc

class Settings(PropertyContainer):
    fields_switch_mode = ComboBoxProperty(items=(lc.FIELDSWITCH_MODE_OPTION1, lc.FIELDSWITCH_MODE_OPTION2),
                                          name=lc.FIELDSWITCH_MODE_NAME)
    ignore_empty_folders_m1 = BoolProperty(default_value=True,
                                           name=lc.IGNORE_EMPTY_FOLDERS_NAME,
                                           tooltip=lc.IGNORE_EMPTY_FOLDERS_DESC)
    add_subfolders_m1 =  BoolProperty(default_value=True,
                                      name=lc.ADD_NESTED_FOLDERS_NAME,
                                      tooltip=lc.ADD_NESTED_FOLDERS_DESC)
