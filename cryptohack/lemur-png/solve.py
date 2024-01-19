import cv2

# Read two images. The size of both images must be the same.
img1 = cv2.imread('flag_7ae18c704272532658c10b5faad06d74.png')
img2 = cv2.imread('lemur_ed66878c338e662d3473f0d98eedbd0d.png')

# compute bitwise XOR on both images
xor_img = cv2.bitwise_xor(img1,img2)

# display the computed bitwise XOR image
cv2.imshow('Bitwise XOR Image', xor_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
