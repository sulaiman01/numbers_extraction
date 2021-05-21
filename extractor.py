import os
import cv2
import pytesseract
import pandas as pd
import argparse
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# changing the directory to image folder
os.chdir('E:/sulaiman/work/numbers_extraction/extraction_folder')
img_dir = os.listdir()

parser = argparse.ArgumentParser(description='Number Extraction')
parser.add_argument('--output', metavar='OUTPUT',
                    help='input output file name',required=True)
args = parser.parse_args()

# Extract numbers from one image
def extract_numbers(img):
    text = pytesseract.image_to_string(img)
    text_list  = text.splitlines()
    filter_ = []
    for i in text_list:
        c = i
        o = len(i)
        for j in ['0','1','2','3','4','5','6','7','8','9','+']:
            c = c.replace(j,'')
        r = len(c)
        if o-r >= 10:
            for j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',')',']','@','.','©','&','»','™','|']:
                i = i.lower()
                i = i.replace(j,'')
            filter_.append(i)
    return filter_

# passing all the images for number extraction
final_list = []
i = 0
for address in img_dir:
    i = i+1
    image = cv2.imread(address)
    mid_list = extract_numbers(image)
    for num in mid_list:
        final_list.append(num)
    print('image-{}....... Done'.format(i))

# changing the directory back to main folder
os.chdir('E:/sulaiman/work/numbers_extraction')

# saving numbers as csv
data = pd.DataFrame(final_list,columns = ['numbers'])
data.to_csv(args.output)