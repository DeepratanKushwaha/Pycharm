import sys

from cx_Freeze import *

includefiles = ['cal.ico']
base = None
if sys.platform == "win64":
    base = "Win64GUI"

shortcut_table = [
    ("DesktopShortcut",                   # shortcut
     "DesktopFolder",                     # directory
     "My Calculator",                     # Name
     "TARGETDIR",                         # component
     "[TAEGETDIR]\smartcalculator.exe",   # target
     None,         # Arguments
     None,         # Description
     None,         # Hotkey
     None,         # Icon
     None,         # IconIndex
     None,         # ShowCmd
     "TARGETDIR",  #WKDir
    )
]
msi_data = {"Shortcut": shortcut_table}

# change some default msi options the use of the above defined tables

bdist_msi_options = {'date': msi_data}
setup(
    version="0.1",
    description="My Calculator",
    author="Deep",
    name="My Calculator",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="Calculator.py",
            base=base,
            icon='cal.ico'
        )
    ]
)