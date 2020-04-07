'''
Created on Dec 9, 2019

@author: prnsoft
'''

import pandas as pd
import cv2
import numpy as np

image = cv2.imread('frame8518.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert sang grayscale

df = pd.DataFrame(gray)

## save to xlsx file

filepath = 'my_excel_file.xlsx'

df.to_excel(filepath, index=False)

if __name__ == '__main__':
    pass