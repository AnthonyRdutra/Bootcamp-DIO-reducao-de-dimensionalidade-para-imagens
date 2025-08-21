# Image Dimensionality Reduction Project

This project was developed as part of the **BairesDev Bootcamp on Machine Learning**.  
The main goal is to demonstrate a simple approach to **dimensionality reduction in images** by transforming them into **grayscale** and **binary (black & white)** representations using **OpenCV**.

---

## 📌 About the Project

Images are often represented with three color channels (Red, Green, Blue - RGB).  
Reducing them to **grayscale** or **binary** significantly lowers the dimensionality, making them easier and faster to process in **Machine Learning** and **Computer Vision** tasks.  

This project provides a Python script that:
1. Loads an image from the given path.  
2. Converts the image to **grayscale**.  
3. Applies **Otsu's Binarization** to generate a black & white version.  
4. Saves both results as separate files.

---

## ⚙️ Requirements

- Python 3.8+
- OpenCV library

To install OpenCV:
```bash
pip install opencv-python
