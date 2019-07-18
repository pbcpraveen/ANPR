import cv2
import os
j=1
for filename in os.listdir('in'):
	print(filename)
	filename = 'in/'+filename
	dest = 'train/img'+str(j)+'.png'
	os.rename(filename,dest)
	print(dest)
	j+=1


