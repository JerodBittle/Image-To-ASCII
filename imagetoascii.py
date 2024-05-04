import cv2

image_file = r"C:\Users\TheBi\OneDrive\Desktop\main-qimg-6f49af888808d9f7203ae80b31d2a75e-lq.jpg"
image_processd = cv2.imread(image_file)
image_processdd = cv2.rotate(image_processd, cv2.ROTATE_90_COUNTERCLOCKWISE)
image_process = cv2.resize(image_processdd, (500, 500))
height, width, channel = image_process.shape

f = open("ascii_file.txt", "w")

for y in range(height):
    for x in range(width):
        r, g, b = image_process[x, y]
        brightness = (int(r) + int(g) + int(b)) // 3
        if brightness in range(0, 50):
            f.write("#")
        elif brightness in range(50, 100):
            f.write("&")
        elif brightness in range(100, 150):
            f.write("/")
        elif brightness in range(150, 200):
            f.write(":")
        elif brightness in range(200, 250):
            f.write(" ")
        if x == 499:
            f.write("\n")

f.close()








