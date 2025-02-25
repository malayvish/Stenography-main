import cv2
import os
import string

img = cv2.imread("mypic.png")  # Replace with correct image path

if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

height, width, _ = img.shape
n, m, z = 0, 0, 0

for i in range(len(msg)):
    if n >= height:
        n = 0
        m += 1
    if m >= width:
        print("Error: Image too small to encode message.")
        exit()
    
    img[n, m, z] = d[msg[i]]
    n += 1
    z = (z + 1) % 3  # Cycle through BGR channels

cv2.imwrite("encryptedImage.png", img)

# Open the encrypted image
import platform
if platform.system() == "Windows":
    os.system("start encryptedImage.png")
elif platform.system() == "Darwin":  # macOS
    os.system("open encryptedImage.png")
else:  # Linux
    os.system("xdg-open encryptedImage.png")

message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        if n >= height:
            n = 0
            m += 1
        if m >= width:
            print("Error: Decryption out of bounds.")
            exit()
        
        message += c[img[n, m, z]]
        n += 1
        z = (z + 1) % 3  # Cycle through BGR channels
    
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")

