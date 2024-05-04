Simple code that when ran will take a raw file path of an image and create a new text file that recreates the image into ASCII art. 
Using cv2 the image will be proccesed, the image will also be formatted into a correct size and orientation so whenever it is written into text it is displayed correctly.
A for loop is ran that goes through each pixel and detects the rgb value, the rgb value is added into one integer and then using a series of if statments, will write a certain character corresponding to that value.

