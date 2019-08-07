#!/usr/bin/env python

# import the necessary packages
import argparse
import sys,os
from PIL import Image
import pytesseract
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument(
        "-i", "--image",
        required=True,
        help="path to input image to be OCR'd"
        )

ap.add_argument(
        "-l",
        "--lang",
        type=str,
        default="por",
        help="language to be used"
        )
		
ap.add_argument(
        "-p",
        "--preprocess",
        type=str,
        default="thresh",
        help="type of processing to be done"
        )
		
ap.add_argument(
		"-o",
		"--out",
		type=str,
		default="output.txt",
		help="output file"
		)

args = vars(ap.parse_args())

image_file = args['image']
lang = args['lang']
output = args['out']
preprocess = args['preprocess']

# load the example image and convert it to grayscale
image = cv2.imread( image_file )
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# check to see if we should apply thresholding to preprocess the
# image
if preprocess == "thresh":
	gray = cv2.threshold(
						gray,
						0,
						255,
						cv2.THRESH_BINARY | cv2.THRESH_OTSU
						)[1]
 
# make a check to see if median blurring should be done to remove
# noise
elif preprocess == "blur": gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = os.path.join( 'testes', '{}-processed.png'.format( os.path.basename(image_file) ) )
print filename
cv2.imwrite(filename, gray)

#sys.exit(0)

#print image_file,lang,output

try:
	img = Image.open( filename )
	readed = pytesseract.image_to_string( img, lang=lang )
	with open( output, 'w' ) as fp: fp.write( readed.encode('utf-8') )
except Exception as err:
	print err.message
