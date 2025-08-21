import cv2
import sys
import os

def img_Processing (img_path):
    
    if not os.path.isfile(img_path):
        print(f"Image '{img_path}' has not been found")
        return
    img = cv2.imread(img_path)
    
    if img is None:
        print("Failed to load image")
        return
    
    grayscaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _, binaryImg = cv2.threshold(grayscaleImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    
    base, ext = os.path.splitext(img_path)
    output_gray = f"{base}_gray{ext}"
    output_bin = f"{base}_bin{ext}"
    
    cv2.imwrite(output_gray, grayscaleImg)
    cv2.imwrite(output_bin, binaryImg)
    
    print(f"Images saved as '{output_gray}' and '{output_bin}'.")
    
    
if __name__ == "__main__":
    if len(sys.argv) < 2: 
        print("HELPER: use -> python ImageReduction.py path_to_your_image")
    else: 
        img_Processing(sys.argv[1])