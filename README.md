# Fast API with pretrained model predictions task.  
<p>
The code creates a simple Fast API and gets responses for images in json type requests which are predictions what animal is in the picture. For sending and posting requests we can you Postman (https://www.postman.com/downloads/).</p>

<p>
In the Param sections of the Postman you can put your image string that you can aquire from any image of your choice by running: </p>

import cv2\
import base64\
img = cv2.imread('image.jpg')\
string_img = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()\

&nbsp;
&nbsp;

