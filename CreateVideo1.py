import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame=cv2.imread(images[0])

height,width,channals=frame.shape
size=(width,height)
print(size)

sunrisevid=cv2.VideoWriter("myvid.mp4",cv2.VideoWriter_fourcc(*'DIVX'),1,size)

for i in range(count-1,0,-1):
    frame=cv2.imread(images[i])
    sunrisevid.write(frame)

sunrisevid.release()
print('done')