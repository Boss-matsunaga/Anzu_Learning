from PIL import Image
import glob

dirname = 'images/'
dirnamelist = ['images_1','images_2','images_3','images_4']

for i in dirnamelist:
    imgname = glob.glob(dirname + i +'/*')
    for j in imgname:
        img = Image.open(j)
        if img.format == 'JPEG':
            continue
        img.save(j,'jpg')