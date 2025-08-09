from PIL import Image

import argparse 

def main():

    parser = argparse.ArgumentParser(description="Remove metadata from a PNG image.")
    parser.add_argument("image_path", help="Path to the PNG image")
    parser.add_argument('--output', required=False, default=None, 
                        help="Where to output the image. By default this overwrites the input file.")

    args = parser.parse_args()

    withMetadata = Image.open(args.image_path)

    channels = []

    for x in range(len(withMetadata.mode)):
        channels.append(withMetadata.getchannel(x))

    noMetadata = Image.merge(withMetadata.mode, channels)

    if args.output:
        output_path = args.output
    else: 
        output_path = args.image_path

    noMetadata.save(output_path)

if __name__ == "__main__":
    main()