import cv2
import numpy as np
from numpy import unique
from scipy.stats import entropy as scipy_entropy


def shannon_entropy(image, base=2):
    _, counts = unique(image, return_counts=True)
    return scipy_entropy(counts, base=base)

def huffman_encode(img):
    return

def huffman_decode(img):
    return

def delta_encode(img):
    encoded = np.zeros_like(img)
    encoded = encoded.astype(np.float)
    print "Image entropy: "
    print shannon_entropy(img)
    last = 0
    for i in range(0, encoded.shape[0]):
        for j in range(0, encoded.shape[1]):
            current = float(img[i,j])
            encoded[i,j] = current - last
            last = current
    

    first_orig = abs(encoded.min())
    converting_factor = first_orig
    encoded = encoded + converting_factor
    print "Encoded entropy: "
    print shannon_entropy(encoded)
    encoded = np.uint8(encoded)
    
    return encoded, converting_factor, first_orig

def delta_decode(img, converting_factor, first_orig):
    decoded = np.zeros_like(img)
    decoded = decoded.astype(np.float)
    img = img.astype(float)
    img = img - converting_factor
    last = first_orig
    for i in range(0, decoded.shape[0]):
        for j in range(0, decoded.shape[1]):
            current = float(img[i,j])
            decoded[i,j] = current + last
            # if decoded[i,j] > 255 or decoded[i,j] < 0:
            #     print "fuk"

            last = decoded[i,j]
    decoded = np.uint8(decoded)
    return decoded


img = cv2.imread("images/amazon_gray.png")
img = img[:,:,0]
#show original
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("original", 1000, 1000)
cv2.imshow("original", img)

#show delta
img, converting_factor, first_orig = delta_encode(img)
cv2.namedWindow("delta", cv2.WINDOW_NORMAL)
cv2.resizeWindow("delta", 1000, 1000)
cv2.imshow("delta", img)
print converting_factor
#convert back to original
img = delta_decode(img, converting_factor, first_orig)
cv2.namedWindow("deltaback", cv2.WINDOW_NORMAL)
cv2.resizeWindow("deltaback", 1000, 1000)
cv2.imshow("deltaback", img)

cv2.waitKey(0)
cv2.destroyAllWindows()