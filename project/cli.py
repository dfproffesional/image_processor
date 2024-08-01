import argparse
import cv2

class ImageThresholdCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Image Thresholding CLI")
        self.parser.add_argument("--input", required=True, help="Path to input image")
        self.parser.add_argument("--simple", action="store_true", help="Apply simple thresholding")
        self.parser.add_argument("--adaptive", action="store_true", help="Apply adaptive thresholding")
        self.parser.add_argument("--otsu", action="store_true", help="Apply Otsu thresholding")
        self.parser.add_argument("--width", type=int, help="Resize image width")
        self.parser.add_argument("--height", type=int, help="Resize image height")
        self.parser.add_argument("--output", default="thresholded_image.png", help="Output image path")
        self.parser.add_argument("--threshold_value", type=int, default=128, help="Custom threshold value for simple thresholding")

    def apply_simple_threshold(self, image, threshold_value):
        _, img_threshold = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
        return img_threshold

    def apply_adaptive_threshold(self, image):
        img_adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        return img_adaptive

    def apply_otsu_threshold(self, image):
        _, img_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return img_otsu

    def resize_image(self, image, width=None, height=None):
        if width:
            new_height = int(image.shape[0] * (width / image.shape[1]))
            return cv2.resize(image, (width, new_height))
        elif height:
            new_width = int(image.shape[1] * (height / image.shape[0]))
            return cv2.resize(image, (new_width, height))
        else:
            return image

    def process_image(self):
        args = self.parser.parse_args()
        image = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)

        if args.simple:
            result = self.apply_simple_threshold(image, args.threshold_value)
        elif args.adaptive:
            result = self.apply_adaptive_threshold(image)
        elif args.otsu:
            result = self.apply_otsu_threshold(image)
        else:
            print("Please specify a thresholding method (--simple, --adaptive, or --otsu).")
            return

        resized_result = self.resize_image(result, width=args.width, height=args.height)
        cv2.imwrite(args.output, resized_result)
        print(f"Thresholded image saved as {args.output}")
    
def main():
    ImageThresholdCLI().process_image()

if __name__ == "__main__":
    main()
