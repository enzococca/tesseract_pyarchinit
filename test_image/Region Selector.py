######### Seleziona la regione ###############################
"""
Questo script permette di raccogliere punti grezzi da un'immagine.
Gli input sono due clic del mouse uno in posizione x,y e
la seconda in w, h di un rettangolo.
Una volta selezionato un rettangolo, all'utente viene chiesto di inserire il tipo
e il Nome:
Il tipo può essere 'Testo' o 'CheckBox'.
Il nome può essere qualsiasi cosa
"""

import cv2
import random

path = r'C:\Users\Utente\Desktop\test_image\1_VRdP.png'##########immagine campione 
scale = 0.5
circles = []
counter = 0
counter2 = 0
point1=[]
point2=[]
myPoints = []
myColor=[]
def mousePoints(event,x,y,flags,params):
    global counter,point1,point2,counter2,circles,myColor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter==0:
            point1=int(x//scale),int(y//scale);
            counter +=1
            myColor = (random.randint(0,2)*200,random.randint(0,2)*200,random.randint(0,2)*200 )
        elif counter ==1:
            point2=int(x//scale),int(y//scale)
            type = input('Enter Type') ###########inserire il tipo se è text o box
            name = input ('Enter Name ')############inserire il nome della label
            myPoints.append([point1,point2,type,name])
            counter=0
        circles.append([x,y,myColor])
        counter2 += 1

img = cv2.imread(path)
img = cv2.resize(img, (0, 0), None, scale, scale)

while True:
    # To Display points
    for x,y,color in circles:
        cv2.circle(img,(x,y),3,color,cv2.FILLED)
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print(myPoints)
        break






