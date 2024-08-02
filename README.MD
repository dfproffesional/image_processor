# 🖼️ Image Thresholding CLI
Welcome to the Image Thresholding CLI! This tool helps you apply different thresholding techniques to your images right from the command line. 📸✨

## Features
Simple Thresholding: Apply a basic threshold to your image.
Adaptive Thresholding: Use adaptive methods for more complex images.
Otsu Thresholding: Automatically determine the best threshold value.
Image Resizing: Resize your image to the desired width or height.
Installation
First, make sure you have Python and OpenCV installed. You can install OpenCV using pip:

```bash
pip install opencv-python
```

Usage
Here’s how you can use the CLI:

```bash
python image_threshold_cli.py --input <path_to_image> --simple --output <output_path>
```

## Options
```bash
--input: Path to the input image (required).
--simple: Apply simple thresholding.
--adaptive: Apply adaptive thresholding.
--otsu: Apply Otsu thresholding.
--width: Resize image to the specified width.
--height: Resize image to the specified height.
--output: Path to save the output image (default: thresholded_image.png).
--threshold_value: Custom threshold value for simple thresholding (default: 128).
```

### Example
```
python image_threshold_cli.py --input example.jpg --simple --threshold_value 150 --output result.png
```

This command will apply simple thresholding with a threshold value of 150 to example.jpg and save the result as result.png.

Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome! 🎉

License
This project is licensed under the MIT License. 📜
