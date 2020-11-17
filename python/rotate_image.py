# This script uses opencv to rotate images by 90 degrees clockwise or counter-clockwise
# Usage: python3 rotate.py <Original_Image_File_Name> <New_Image_File_Name> <clockwise/counter>

import cv2
import sys

if ((sys.argv[1] != "") or (sys.argv[1] != None)):
    img = cv2.imread(f"{sys.argv[1]}")

if ((sys.argv[2] != "") or (sys.argv[2] != None)):
    savename = str(sys.argv[2])

if (sys.argv[3] == "clockwise"):
    # rotating image clockwise
    img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(savename, img_rotate_90_clockwise)
    print(f"Your image was rotated clockwise and saved as {savename}")
elif (sys.argv[3] == "counter"):
    # rotating image counterclockwise
    img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(savename, img_rotate_90_counterclockwise)
    print(f"Your image was rotated counter clockwise and saved as {savename}")
else:
    print("You did not provide instructions to rotate any image")
