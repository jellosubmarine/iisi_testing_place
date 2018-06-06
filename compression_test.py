import cv2
import numpy as np
from numpy import unique
from scipy.stats import entropy as scipy_entropy
from huffman import HuffmanCoding
import os

def shannon_entropy(image, base=2):
    _, counts = unique(image, return_counts=True)
    return scipy_entropy(counts, base=base)

# def huffman_encode(img):
#     return

# def huffman_decode(img):
#     return

def delta_encode(img):
    encoded = np.zeros_like(img)
    encoded = encoded.astype(np.int)
    print "Image entropy: "
    print shannon_entropy(img)
    last = 0
    for i in range(0, encoded.shape[0]):
        for j in range(0, encoded.shape[1]):
            current = int(img[i,j])
            encoded[i,j] = current - last
            last = current
    
    print "Encoded entropy: "
    print shannon_entropy(encoded)
    
    return encoded

def delta_decode(img):
    decoded = np.zeros_like(img)
    decoded = decoded.astype(np.int)
    img = img.astype(np.int)
    last = 0
    for i in range(0, decoded.shape[0]):
        for j in range(0, decoded.shape[1]):
            current = int(img[i,j])
            decoded[i,j] = current + last

            last = decoded[i,j]
    decoded = decoded.astype(np.uint8)
    return decoded


img = cv2.imread("images/amazon_gray.png")
img = img[:,:,0]
# img.tofile(os.getcwd() + "/raw.bin")
#show original
# cv2.namedWindow("original", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("original", 1000, 1000)
# cv2.imshow("original", img)

# #show delta
# img, converting_factor, first_orig = delta_encode(img)
# cv2.namedWindow("delta", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("delta", 1000, 1000)
# cv2.imshow("delta", img)
# print converting_factor

img = delta_encode(img)

# #Huffman encoding
h = HuffmanCoding(img, os.getcwd() + "/test")
h.compress()
img = h.decompress(os.getcwd()+"/test.bin")
# output_path = h.compress()
# img = h.decompress(output_path)

# #convert back to original
img = delta_decode(img)

cv2.namedWindow("deltaback", cv2.WINDOW_NORMAL)
cv2.resizeWindow("deltaback", 1000, 1000)
cv2.imshow("deltaback", img)

print "Redecoded entropy: "
print shannon_entropy(img)

cv2.waitKey(0)
cv2.destroyAllWindows()