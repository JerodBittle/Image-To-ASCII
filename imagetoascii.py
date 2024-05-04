import cv2

#Enter file path into the image_file raw string
image_file = r""

#Reads the file
image_processd = cv2.imread(image_file)
image_processdd = cv2.rotate(image_processd, cv2.ROTATE_90_COUNTERCLOCKWISE)
image_process = cv2.resize(image_processdd, (500, 500))
height, width, channel = image_process.shape

#Opens new text file to store ASCII art
f = open("ascii_file.txt", "w")

#Loops through each pixel in the image and detects a brightness level for the pixels, depending on the brightness a different character is wrtten.
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








