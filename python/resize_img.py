import cv2

read = input("image path: ")
img = cv2.imread(f"{read}",cv.IMREAD_UNCHANGED)

height = img.shape[0]
width = ing.shape[1]

print('Image Height : ',height)
print('Image Width  : ',width)

resize = input("resize? (yes/no) ")
if resize == "yes":
  new_h = int(input("new height? "))
  new_w = int(input("new width? "))
  img = cv2.resize(img,(new_h,new_w))

