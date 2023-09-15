import os
from PIL import Image

def convert_png_to_ico(input_png, output_ico, size=(32, 32)):
    try:
        img = Image.open(input_png)
        
        # Check if the image is a valid PNG image
        if img.format != "PNG":
            raise Exception("Input image is not in PNG format")

        # Resize the image
        img = img.resize(size, Image.LANCZOS)

        # Save the resized image as an ICO file
        img.save(output_ico, format="ICO", sizes=[(size[0], size[1])])

        print(f"Conversion successful: {input_png} -> {output_ico}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    input_png = input("Enter the path to the input PNG image on your device: ")
    output_ico = os.path.join(os.path.expanduser("~"), "Downloads", "output.ico")
    size = (int(input("Enter the desired width of the output image in pixels: ")),
            int(input("Enter the desired height of the output image in pixels: ")))

    # Open the image file from the device
    img = Image.open(input_png)

    convert_png_to_ico(input_png, output_ico, size)

if __name__ == "__main__":
    main()
