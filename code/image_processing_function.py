import cv2
import numpy as np
import matplotlib.pyplot as plt

## mask วงพื้นที่วงกลมบน fisheye lens (พื้นหลัง mask เป็นสีดำ)
def mask_circle(image_path):
    image = cv2.imread(image_path)
    r1 = image.shape[1]
    r2 = image.shape[0]
    mask = np.zeros((r2, r1), dtype=np.uint8)

    cv2.circle(mask, (int(r1/2), int(r2/2)), int(r2/2), (255, 255, 255), -1, 8, 0)

    masked = cv2.bitwise_and(image, image, mask=mask)

    return masked

## Crop images
def crop_image(input):
    img = cv2.imread(input)
    cutted_img = img[55:1340, 340:1650]
    return cutted_img

def mask_gray(image):
    crop_mask = cv2.imread('./crop_mask3.png')
    if image.shape[2] == 1:
        gray_3_channel = cv2.merge((image, image, image))
        