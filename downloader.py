# Image downloader from URL text file
# Oyesh Singh
# 04/15/2017

# Usage:
# $ python downloader.py <filename.txt>

import sys
import os
from urllib.request import urlretrieve
import urllib.request

fileName = sys.argv[1]

firstName = os.path.splitext(fileName)[0]

print ("Downloading images from ", firstName)

imageCounter = 1

if not os.path.exists(firstName):
            os.mkdir(firstName)

with open(fileName) as file:
	for url in file:
		fName = firstName + "_" + str(imageCounter) + ".jpg"
		fullPath = os.path.join(firstName, fName)
		try:
			urlretrieve(url.strip(), fullPath)
		except urllib.error.HTTPError as e:
			continue
		imageCounter = imageCounter + 1
		



