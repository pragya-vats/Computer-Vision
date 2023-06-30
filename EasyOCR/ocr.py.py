
# import the modules
import os
from os import listdir
import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
import pyshine as ps
 
# get the path/directory
folder_dir = "C:/Users/excep/Documents/Job_assignment/license images"
output = "C:/Users/excep/Documents/Job_assignment/License Outputs"

start_index = 0

for images in os.listdir(folder_dir):
 
    #img = cv2.imread(images)
    img = cv2.imread(os.path.join(folder_dir,images))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # instance text detector
    reader = easyocr.Reader(['en'], gpu=False)

    # detect text on image
    text_ = reader.readtext(img)

    threshold = 0.25
    #To display the text on the original image or show bounding boxes
    #we need the coordinates for the text. So make sure the detail=1 above, readtext.
    # display the OCR'd text and associated probability
    for (bbox, text, prob) in text_:
        
        #Define bounding boxes
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        
        #Put rectangles and text on the image
        cv2.rectangle(img, tl, br, (0, 0, 255), 2)
        cv2.putText(img, text, (tl[0], tl[1] - 10), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (51, 204, 51), 2)
        #ps.putBText(img, text, text_offset_x=tl[0], text_offset_y=tl[1]-5, vspace=5, hspace=5, font_scale=0.5, background_RGB=(0,0,0), text_RGB=(0, 255, 0))
    filename = "task_3_partial_output"
    # Generate the filename for the saved image
    save_filename = f'{filename}_{start_index:02}.png'
    cv2.imwrite(os.path.join(output , save_filename), img)
    # Increment the serial number index
    start_index += 1