import cv2
#image conveersion project colour image into grayscale
path=input("Enter the path and name of the image==")
print("Entered Path By You is==",path)

#now read the image
img1=cv2.imread(path,0)
img1=cv2.resize(img1,(500,500))#width,height
cv2.imshow("Converted image==",img1)
k=cv2.waitKey()
if k==ord("s"):
    cv2.imwrite("D:\\balcknwhite.png", img1)
else:    
    cv2.destroyAllWindows()
