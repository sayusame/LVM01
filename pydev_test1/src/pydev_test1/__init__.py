import cv2
#image = cv2.imread('C:/Users/jiangx/eclipse-workspace/pydev_test1/images/img_7398.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('C:/Users/jiangx/eclipse-workspace/pydev_test1/images/20191030142710-0001.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', image)
print(image.shape)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('C:/Users/jiangx/eclipse-workspace/pydev_test1/images/20191030142710-0001-gray.jpg', image)
    print("save successful")
    cv2.destroyAllWindows()
