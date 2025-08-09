#!python


import subprocess
import os

args = ["pyinstaller", "--onefile" , "src/main.py", 
        "--icon", "icon.png"]
subprocess.run(args)

try:
    os.remove("dist/ImageMetadataRemover.exe")
except FileNotFoundError: 
    pass
os.rename("dist/main.exe", "dist/ImageMetadataRemover.exe")

