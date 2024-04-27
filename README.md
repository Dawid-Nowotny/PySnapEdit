# PySnapEdit
PySnapEdit is an image editing application that allows users to manipulate images. It provides essential functionalities for image editing.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
- Python 3.8 or later
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

### Installing
1. Clone the repository:
    ```bash
    git clone https://github.com/Dawid-Nowotny/PySnapEdit.git
    ```
    
2. (Optional) Create a virtual environment (recommended):
    ```bash
    # Windows
    python -m venv venv

    # Linux/macOS
    python3 -m venv venv
    ```

    Activate the virtual environment
    ```bash
    # Windows
    venv\Scripts\activate
    
    # Linux/macOS
    source venv/bin/activate
    ```
    
3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

4. Navigate to the application directory:
    ```bash
    cd src
    ```

5. Run the application:
   ```bash
    python main.py
   ```

## Functionality
- Load and explore images
  - Load images from file
  - Drag and drop images onto the application window
  - Paste images from the clipboard 
- Create new canvases
- Save images
- Work with multiple windows
- Apply filters
- Compress image
- Recognize text
- Analyze colors
- Manage windows
- Zoom in and out
- Draw and erase
- Clear the canvas
