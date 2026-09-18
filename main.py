"""
=============================================================================
Module: main.py
Project: Image to Sketch Converter
Description: Entry point script for the Image to Sketch conversion application.
             Handles image loading, pipeline orchestration, saving the final
             output, and terminal user feedback.
=============================================================================
"""

import os
import sys
import cv2
from sketch import image_to_sketch


def main():
    """
    Main function executing the image-to-sketch pipeline:
    1. Determines input image file path.
    2. Validates and reads the image using OpenCV.
    3. Invokes sketch conversion pipeline from sketch.py.
    4. Saves the resulting sketch to 'output.jpg'.
    """
    print("=" * 60)
    print("         IMAGE TO SKETCH CONVERTER (MINI PROJECT)          ")
    print("=" * 60)

    # 1. Determine input file path:
    # If passed as command line argument (e.g., python main.py my_photo.jpg), use it.
    # Otherwise, fallback to the default 'input.jpg' in the current working directory.
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = "input.jpg"

    print(f"\n[INFO] Target input image: '{input_path}'")

    # 2. Check if the specified file exists on disk
    if not os.path.exists(input_path):
        print(f"[ERROR] The file '{input_path}' was not found.")
        print("[TIP] Please place an image named 'input.jpg' in this directory or run:")
        print("      python main.py <path_to_your_image>")
        sys.exit(1)

    # 3. Read the image using OpenCV
    # Note: cv2.imread loads the image in BGR (Blue-Green-Red) color space by default.
    print("[INFO] Reading image using OpenCV...")
    image = cv2.imread(input_path)

    # Ensure OpenCV was able to decode the image file properly
    if image is None:
        print(f"[ERROR] Could not decode '{input_path}'. Please ensure it is a valid image file (JPG, PNG, etc.).")
        sys.exit(1)

    height, width, channels = image.shape
    print(f"[SUCCESS] Image loaded successfully! Dimensions: {width}x{height} pixels, Channels: {channels}")

    # 4. Process image through the sketch conversion algorithm
    print("[INFO] Applying pencil sketch transformations:")
    print("       -> Converting to Grayscale...")
    print("       -> Inverting Grayscale Image...")
    print("       -> Applying Gaussian Blur...")
    print("       -> Performing Color Dodge / Divide Blending...")

    sketch_result = image_to_sketch(image)

    # 5. Save the resulting sketch to output.jpg
    output_filename = "output.jpg"
    print(f"\n[INFO] Saving output sketch as '{output_filename}'...")
    save_success = cv2.imwrite(output_filename, sketch_result)

    if save_success:
        print("=" * 60)
        print(f"[SUCCESS] Sketch created and saved to: {os.path.abspath(output_filename)}")
        print("=" * 60)
    else:
        print(f"[ERROR] Failed to save output image to '{output_filename}'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
