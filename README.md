# Image to Sketch Converter

A lightweight, beginner-friendly Python mini-project that converts any digital photograph into a realistic pencil sketch using **OpenCV** and **NumPy**.

Designed for computer vision fundamentals, flipped learning evaluations, and academic mini-projects without requiring deep learning frameworks, web interfaces, or external APIs.

---

## 📌 Project Overview

Digital image sketching simulates the effect of graphite pencil drawings on paper. The algorithm relies on classic spatial domain filtering and arithmetic blending:

1. **Luminance Extraction**: Converting 3-channel color (BGR) into 1-channel grayscale.
2. **Negative Inversion**: Inverting pixel values to highlight shadow boundaries.
3. **Gaussian Blurring**: Diffusing high-frequency edges to simulate soft pencil shading.
4. **Color Dodge (Divide Blending)**: Mathematically balancing high-frequency edge contrasts against low-frequency shaded tones.

---

## 🚀 Features

- **Realistic Pencil Sketch Effect**: Produces clean line-work and smooth pencil shading.
- **Modular Code Architecture**: Clean separation between processing logic (`sketch.py`) and application execution (`main.py`).
- **Comprehensive Inline Documentation**: Every step is thoroughly explained with academic-grade comments.
- **Robust Error Handling**: Gracefully reports missing files, corrupted images, and unreadable formats.
- **Zero External Overhead**: Runs locally in milliseconds with minimal dependencies.

---

## 🛠️ Technologies & Tools Used

- **Language**: Python 3.8+ (Tested on Python 3.13)
- **Computer Vision Library**: `opencv-python` (`cv2`)
- **Matrix Operations**: `numpy`
- **Architecture**: Pure Modular CLI

---

## 📂 Project Structure

```text
image_formation/
├── main.py            # Main application script (handles file I/O & user feedback)
├── sketch.py          # Core transformation module (Grayscale, Invert, Blur, Divide)
├── requirements.txt   # Required Python packages (opencv-python, numpy)
├── statement.md       # Project scope, requirements, target users, and workflow
├── README.md          # Project documentation and execution instructions
├── input.jpg          # Sample input image
└── output.jpg         # Generated pencil sketch image
```

---

## ⚙️ Installation & Setup

### 1. Clone or Open the Project

Ensure you are in the project root directory:

```bash
git clone https://github.com/muditjain2204/image_formation.git
cd image_formation
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 💻 How to Run the Project

### Option A: Using the Default Sample Image
Place any image named `input.jpg` in the project directory and run:

```bash
python main.py
```

### Option B: Providing a Custom Image Path
You can specify the path to any image via a command-line argument:

```bash
python main.py path/to/your_photo.jpg
```

Upon successful execution, the sketch will be saved to `output.jpg` in the current folder.

---

## 🧪 Instructions for Testing

1. **Verify Default Conversion**:
   ```bash
   python main.py
   ```
   *Expected Result*: Console outputs step-by-step progress, and `output.jpg` is generated.

2. **Verify Error Handling (Missing File)**:
   ```bash
   python main.py non_existent_file.jpg
   ```
   *Expected Result*: The application displays a clear error message explaining that the file was not found, with helpful troubleshooting advice instead of crashing.

---

## 📐 Algorithmic Explanation

The pencil sketch pipeline is broken down into four core mathematical steps:

| Step | Operation | Formula / Function | Purpose |
|---|---|---|---|
| **1** | Grayscale Conversion | $Y = 0.299R + 0.587G + 0.114B$ | Strips color information to focus exclusively on intensity and lighting. |
| **2** | Inversion | $I_{\text{inv}} = 255 - I_{\text{gray}}$ | Produces a photographic negative, turning highlights dark and shadows bright. |
| **3** | Gaussian Blur | $G(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}$ | Smooths out high-frequency noise and creates smooth gradient shadows. |
| **4** | Divide Blend (Color Dodge) | $\text{Sketch} = \frac{I_{\text{gray}}}{255 - I_{\text{blur}}} \times 256$ | Divides the original image by the inverted blurred image to accentuate edges. |

---

## 📜 License & Academic Integrity

Created for educational purposes and mini project evaluation under VITyarthi guidelines.