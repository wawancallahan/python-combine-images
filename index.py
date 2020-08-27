import cv2

# Bigger
image1 = cv2.imread('./assets/kny.jpg') 

# Smaller
image2 = cv2.imread('./assets/peko.png') 

image1Height, image1Width = image1.shape[:2]
image2Height, image2Width = image2.shape[:2]

max_width = image1Width / 2
max_height = image1Height / 2

if (image2Height >= max_height):
    image2 = cv2.resize(image2, (0,0), fx=image2.shape[1], fy=max_height, interpolation=cv2.INTER_AREA)

if (image2Width >= max_width):
    image2 = cv2.resize(image2, (0,0), fx=max_width, fy=image2.shape[0], interpolation=cv2.INTER_AREA)

grid_offset = [
    [0, 0], # TOP LEFT
    [image1Width - image2Width, 0], # TOP RIGHT,
    [image1Width - image2Width, image1Height - image2Height], # BOTTOM RIGHT,
    [0, image1Height - image2Height], # BOTTOM LEFT
]

for offset in grid_offset:
    y1, y2 = offset[1], offset[1] + image2Height
    x1, x2 = offset[0], offset[0] + image2Width
    for c in range(0, 2):
        image1[y1:y2, x1:x2] = image2

cv2.imshow("test", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()