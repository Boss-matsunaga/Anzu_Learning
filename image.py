from PIL import Image
import glob
import os
import cv2

dirnamelist = ['images_1','images_2','images_3','images_4']

def jpg_chenge():
    count = 1
    for imgname in dirnamelist:
        imgname = glob.glob('images/' + imgname +'/*')
        for j in imgname:
            img = Image.open(j)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save('images/ALLimage/' + str(count).zfill(5) + '.jpg')
            print('done', count)
            count += 1

def makefaceimage():
    classifier = cv2.CascadeClassifier('lbpcascade_animeface.xml')
    count = 1
    for imgname in glob.glob('images/ALLimage/*'):
        image = cv2.imread(imgname)
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(gray_image)
        for i, (x,y,w,h) in enumerate(faces):
            face_image = image[y:y+h, x:x+w]
            output_path = os.path.join('images/face_image/',str(count).zfill(5) + '.jpg')
            cv2.imwrite(output_path,face_image)
            print('done', count)
            count += 1

if __name__ == '__main__':
    #jpg_chenge()
    makefaceimage()