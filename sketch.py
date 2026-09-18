"""
=============================================================================
Module: sketch.py
Project: Image to Sketch Converter
Description: Contains the core computer vision processing pipeline to convert 
             a standard digital photograph into a realistic pencil sketch effect.
=============================================================================
"""

import cv2
import numpy as np


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Step 1: Convert BGR color image to Grayscale.
    
    Why this step is needed:
    A digital color photo is composed of 3 channels (Blue, Green, Red).
    Pencil sketches rely on light and dark tones rather than chromatic color.
    Grayscale conversion computes luminance using standard weights:
    Y = 0.299*R + 0.587*G + 0.114*B.
    
    :param image: Input color image in BGR format (numpy ndarray).
    :return: 2D single-channel grayscale image.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def invert_image(image: np.ndarray) -> np.ndarray:
    """
    Step 2: Invert pixel intensities.
    
    Why this step is needed:
    Inversion flips pixel values (0 becomes 255, 255 becomes 0).
    Inverting highlights shadows and prepares the image for Gaussian blur
    so that when blended back, sharp edges will be accentuated.
    
    :param image: Grayscale image.
    :return: Negative (inverted) grayscale image.
    """
    # Equivalent to 255 - image or cv2.bitwise_not(image)
    inverted_image = cv2.bitwise_not(image)
    return inverted_image


def apply_gaussian_blur(image: np.ndarray, kernel_size: tuple = (21, 21), sigma_x: float = 0) -> np.ndarray:
    """
    Step 3: Apply Gaussian Blur.
    
    Why this step is needed:
    Gaussian blur smoothens the inverted image by averaging neighboring pixels 
    using a Gaussian bell-curve kernel. This removes high-frequency noise and
    spreads out tone transitions, which mimics hand-shaded pencil strokes.
    
    Note: The kernel size must be odd numbers (e.g., 21x21, 31x31). A larger kernel 
    creates softer pencil shading, while a smaller kernel retains sharper lines.
    
    :param image: Inverted grayscale image.
    :param kernel_size: Tuple containing odd dimensions (width, height).
    :param sigma_x: Gaussian kernel standard deviation along X-axis. 0 = auto-calculated.
    :return: Blurred inverted image.
    """
    blurred_image = cv2.GaussianBlur(image, ksize=kernel_size, sigmaX=sigma_x, sigmaY=0)
    return blurred_image


def divide_blend(gray_image: np.ndarray, blurred_inverted_image: np.ndarray) -> np.ndarray:
    """
    Step 4: Generate pencil sketch effect using Divide Blending (Color Dodge).
    
    Why this step is needed:
    The "Color Dodge" blend mode in image editing divides the base image (grayscale)
    by the inverse of the blend image (inverted blurred image):
        Sketch = (Grayscale / (255 - Blurred_Inverted)) * 256
        
    Since (255 - Blurred_Inverted) restores the blurred version of the original image,
    dividing the sharp grayscale image by its blurred counterpart emphasizes 
    edges where there are abrupt intensity changes while washing out flat areas to white.
    
    OpenCV provides an optimized function cv2.divide() which handles division by zero
    and value saturation (clipping values to 255) automatically.
    
    :param gray_image: Original grayscale image (base layer).
    :param blurred_inverted_image: Gaussian blurred inverted image (blend layer).
    :return: Final pencil sketch image as a 2D grayscale ndarray.
    """
    # 255 - blurred_inverted_image recovers the blurred grayscale image
    inverted_blur = 255 - blurred_inverted_image
    
    # Perform element-wise division and scale by 256 for 8-bit depth
    sketch_image = cv2.divide(gray_image, inverted_blur, scale=256.0)
    return sketch_image


def image_to_sketch(image: np.ndarray, blur_kernel: tuple = (21, 21)) -> np.ndarray:
    """
    High-level pipeline coordinating all transformation steps:
    1. Grayscale conversion
    2. Inversion of grayscale
    3. Gaussian blur of inverted image
    4. Divide blending (Color Dodge)
    
    :param image: Input BGR image read via cv2.imread().
    :param blur_kernel: Kernel size for Gaussian blur (default: 21x21).
    :return: Resulting pencil sketch image.
    """
    # Step 1: Grayscale
    gray = convert_to_grayscale(image)
    
    # Step 2: Inversion
    inverted = invert_image(gray)
    
    # Step 3: Gaussian Blur
    blurred = apply_gaussian_blur(inverted, kernel_size=blur_kernel)
    
    # Step 4: Divide Blending
    sketch = divide_blend(gray, blurred)
    
    return sketch
