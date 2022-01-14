import os
from PIL import Image

blendimg = './blender/fire'
srcdir = './srcImages'
outputdirblend='./outputFiles/test/blend'
size = (400, 400)
count = 0
for x in range(1,6):
    for srcimg in os.listdir(srcdir):
        try:
            base_image_path_1 = srcdir+'/'+srcimg
            im1 = Image.open(blendimg+str(x)+".jpg")
            im2 = Image.open(base_image_path_1)
            im1 = im1.resize(size)
            im2 = im2.resize(size)
            im3 = Image.blend(im1, im2, 0.5)
            im3.save(outputdirblend+str(x)+"/"+srcimg)
            # count=count+1
            if count > 3:
                break
        except Exception as e:
            print(e)



