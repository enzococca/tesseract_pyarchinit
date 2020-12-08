#! /usr/bin/env python
# -*- coding: utf-8 -*-

#######################
### pyArchInit ODINO ##
##################  ###
#########    ###  #####
#######          ######
######          #######
####            #######
###  #          #######
##  ###        ########
#  ####################
 ######################



import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'# funziona meglio quello a 32 bit
img = cv2.imread(r'C:\Users\Utente\Desktop\pyarchinit_odino-master\pyarchinit_odino-master\venv\US 4_.jpg')### importo una foto
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)## setto il colore rgb



boxes = pytesseract.image_to_data(img) #######do in pasto a tesseract
#############################################
#### Detecting Words  ######
#############################################
#[   0          1           2           3           4          5         6       7       8        9        10       11 ]
#['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']
# crea una tabella di 11 colonne. questo non è necessario al fine del riconoscimento del testo 
for a,b in enumerate(boxes.splitlines()):
        print(b)
        if a!=0:
            b = b.split()
            if len(b)==12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)

########### cerco area e us se esistono nel box e le stampo#######

area= str('AREA 1')
us = str('US 4')
if area or us in boxes:
    print(area[5])
    print (us[3])
##############visualizzo l'immagine con il testo evidenziato#############
cv2.imshow('img', img)
cv2.waitKey(0)                