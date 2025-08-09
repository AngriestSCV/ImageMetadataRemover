#!python


import subprocess
import os

args = ["pyinstaller", "--onefile" , "src/main.py", 
        "--icon", "icon.png"]
subprocess.run(args)

import src.main as mm

version = mm.version

vstring = f"{version[0]}.{version[1]}.{version[2]}"

os.rename("dist/main.exe", f"dist/ImageMetadataRemover.{vstring}.exe")

