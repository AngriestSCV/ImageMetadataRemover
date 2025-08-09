#!python

from PIL import Image

import argparse 
import traceback
import sys

version = (1, 0, 0)

def strip(image):
    channels = []

    for x in range(len(image.mode)):
        channels.append(image.getchannel(x))

    ret = Image.merge(image.mode, channels)
    return ret


def main():

    parser = argparse.ArgumentParser(description="Remove metadata from a PNG image.")
    parser.add_argument("image_path", nargs="*", help="Path to the PNG image")
    parser.add_argument("--no-overwrite")

    args = parser.parse_args()

    print(f"Version {version[0]}.{version[1]}.{version[2]}")

    for img_path in args.image_path:
        output_path = img_path
        if args.no_overwrite:
            output_path = output_path+"_no_metadata.png"

        withMetadata = Image.open(img_path)
        noMetadata = strip(withMetadata)
        noMetadata.save(output_path)
        print("Stripped metadata from ", img_path)
    
    print(f"Finished stripping {len(args.image_path)} images")

if __name__ == "__main__":
    try:
        main()
        code = 0
    except Exception as e:
        print("There was a catastropic error. Please report this to the maintainer of this tool")
        print(e)
        print(traceback.format_exc())
        code = 1

    input("Press enter to exit")
    sys.exit(code)
