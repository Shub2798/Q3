from os import listdir
from os.path import isfile, join
import cv2
def get_image_difference(image_1, image_2):
    querry_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
    search_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])
    img_hist_diff = cv2.compareHist(querry_image_hist, search_image_hist, cv2.HISTCMP_BHATTACHARYYA)
    img_template_probability_match = cv2.matchTemplate(querry_image_hist, search_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
    img_template_diff = 1 - img_template_probability_match
    commutative_image_diff = (img_hist_diff / 10) + img_template_diff
    return commutative_image_diff


mypath='database'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
temp=1
fileName=""
for n in range(0, len(onlyfiles)):
    image_1=cv2.imread('querry.jpg')
    image_2 = cv2.imread( join(mypath,onlyfiles[n]) )
    image_difference =get_image_difference(image_1,image_2)
    if (image_difference<temp):
        temp=image_difference
        fileName=onlyfiles[n]

print(fileName)

