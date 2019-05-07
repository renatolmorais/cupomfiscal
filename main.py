#!/usr/bin/env python

# import the necessary packages
import argparse
import os

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
        default="eng",
        help="language to be used"
        )
		
ap.add_argument(
		"-o",
		"--out",
		type=str,
		default="output.txt",
		help="output file"
		)

args = vars(ap.parse_args())

print args