#!python


import subprocess
import os

args = ["pyinstaller", "--onefile" , "src/main.py", 
        "--icon", "icon.png"]
subprocess.run(args)

os.rename("dist/main.exe", "dist/ImageMetadataRemover.exe")

