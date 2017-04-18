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

print ("Download started ", firstName)

imageCounter = 1

if not os.path.exists(firstName):
            os.mkdir(firstName)

with open(fileName) as file:
	for url in file:
		fName = firstName + "_" + str(imageCounter) + ".jpg"
		fullPath = os.path.join(firstName, fName)
		try:
			print ("Downloading .... ")
			urllib.request.urlopen(url, timeout=5)
			urlretrieve(url.strip(), fullPath)
			print ("Image downloaded ", imageCounter)			
			imageCounter = imageCounter + 1			
		except urllib.error.HTTPError as e:
			print("HTTP Error")
			continue
		except timeout:
			print("Timeout Error")
			continue
		except urllib.error.URLError as err:
			print("URL Error")
			continue

		



