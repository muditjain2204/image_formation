# Project Statement: Image to Sketch Converter

## 1. Problem Statement
In computer vision, computational photography, and digital art, converting natural photographic imagery into artistic representations (such as pencil sketches) is often performed using computationally expensive neural networks or heavy graphic software suites (e.g., Adobe Photoshop). For educational purposes, embedded applications, and lightweight client processing, there is a strong need for an efficient, deterministic, and algorithmically sound method to generate pencil sketch drawings directly from raw pixel matrices using classical image processing principles without requiring bulky dependencies, machine learning models, cloud APIs, or external database infrastructure.

The **Image to Sketch Converter** solves this problem by utilizing foundational computer vision operators—color space transformation (Grayscale), pixel inversion, spatial Gaussian smoothing, and Color Dodge divide blending—to simulate pencil strokes and hand-drawn shading in real-time.

---

## 2. Scope of the Project
- **In Scope:**
  - Automated ingestion and validation of standard 2D image file formats (JPEG, PNG, BMP).
  - Transformation of multi-channel BGR images into single-channel luminance representation.
  - Frequency attenuation and edge extraction using Gaussian convolution.
  - Simulating hand-shaded sketches using pixel-wise mathematical division (Dodge blend).
  - Persisting processed outputs locally as `output.jpg`.
  - Clean, modular code structure across `main.py` and `sketch.py` accompanied by detailed inline explanations suitable for academic evaluation.

- **Out of Scope (By Design):**
  - Web frontend / graphical user interface (GUI).
  - Cloud / REST APIs or networked microservices.
  - Relational or NoSQL database storage.
  - User authentication, session management, or multi-tenant access control.
  - Heavy Deep Learning / Generative AI inference models.

---

## 3. Target Users
1. **Undergraduate Students & Academic Evaluators**: Learning core spatial domain filtering, kernel operations, and color transformations in Computer Vision and Digital Image Processing.
2. **Digital Artists & Hobbyists**: Requiring instant line-art and pencil sketches from portraits or architectural photos for tracing or printing.
3. **Developers & Prototypers**: Seeking lightweight, zero-overhead image transformation modules for command-line utilities and embedded micro-controllers.

---

## 4. High-Level Features
- **Deterministic Pencil Sketching**: Accurately reproduces hand-drawn pencil sketches with clear outlines and soft gradient shading.
- **Fast Execution**: Operates in milliseconds using OpenCV's vectorised C++ backend operations via NumPy arrays.
- **Zero Configuration**: Ready to run out of the box with minimal dependencies (`opencv-python`, `numpy`).
- **Flexible File Input**: Accepts command-line target paths or seamlessly falls back to a default `input.jpg`.
- **Robust Error Handling**: Checks for missing files, corrupted bytes, and invalid image formats with clear console notifications.

---

## 5. Functional Requirements (Three Modules)

### Module 1: Image Ingestion & Validation
- **FR-1.1**: The system must check if the input image path exists on the local filesystem.
- **FR-1.2**: The system must read and decode the image into a 3D NumPy array (BGR format) using OpenCV.
- **FR-1.3**: The system must reject non-image files or unreadable paths with graceful error messages and exit codes.

### Module 2: Image Transformation Pipeline (`sketch.py`)
- **FR-2.1 Grayscale Conversion**: Converts 3-channel BGR images to 1-channel Grayscale using standard perceptual luminance weights.
- **FR-2.2 Negative Inversion**: Computes the bitwise NOT (intensity inversion: $255 - I$) of the grayscale image.
- **FR-2.3 Gaussian Smoothing**: Applies a 2D Gaussian kernel (e.g., $21 \times 21$) over the inverted image to isolate low-frequency shading.
- **FR-2.4 Divide Blending (Color Dodge)**: Evaluates element-wise division $\frac{\text{Grayscale}}{255 - \text{Blur}} \times 256$ to enhance contrast and generate pencil outlines.

### Module 3: Export & Feedback System
- **FR-3.1 Output Persistence**: The system must write the resulting 2D matrix to disk as `output.jpg`.
- **FR-3.2 Progress Feedback**: The system prints step-by-step console logs indicating dimensions, pipeline progress, and output file destination.

---

## 6. Non-Functional Requirements

| Requirement | Specification |
|---|---|
| **Performance** | Must process typical standard-resolution images (e.g., 1080p) in under 1 second on standard consumer hardware. |
| **Reliability** | Must never crash abruptly with raw tracebacks on missing files or corrupt input; input must be validated before processing. |
| **Usability** | The command-line interface must provide clear, human-readable logging and troubleshooting advice. |
| **Maintainability & Modularity** | Separation of concerns: execution and CLI logic resides in `main.py`, while algorithmic transformations are decoupled in `sketch.py`. |
| **Resource Efficiency** | Minimal memory footprint; avoids redundant memory duplication by operating directly on NumPy views and arrays. |

---

## 7. System Workflow

```
[Input Image (e.g. input.jpg)]
           │
           ▼
┌───────────────────────────┐
│       1. cv2.imread       │ -> Load BGR Matrix
└──────────┬────────────────┘
           │
           ▼
┌───────────────────────────┐
│  2. Grayscale Conversion  │ -> cv2.cvtColor(BGR2GRAY)
└──────────┬────────────────┘
           │
           ▼
┌───────────────────────────┐
│   3. Invert Grayscale     │ -> cv2.bitwise_not (255 - Gray)
└──────────┬────────────────┘
           │
           ▼
┌───────────────────────────┐
│   4. Apply Gaussian Blur  │ -> cv2.GaussianBlur(kernel=21x21)
└──────────┬────────────────┘
           │
           ▼
┌───────────────────────────┐
│ 5. Divide Blending(Dodge) │ -> cv2.divide(Gray, 255-Blur, 256.0)
└──────────┬────────────────┘
           │
           ▼
┌───────────────────────────┐
│     6. cv2.imwrite        │ -> Write output.jpg to disk
└───────────────────────────┘
```
