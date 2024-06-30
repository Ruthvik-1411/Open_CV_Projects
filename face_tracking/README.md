## Face tracking using Pan/Tilt servo brackets

In this project a face tracking application is implemented. It uses [pan tilt mechanism](https://en.wikipedia.org/wiki/Pan%E2%80%93tilt%E2%80%93zoom_camera#:~:text=PTZ%20is%20an%20abbreviation%20for,with%20no%20physical%20camera%20movement.) to track the face.<br><br>
Here a pan tilt servo brackets have been used and the setup is as follows:<br><br>
<img src="https://github.com/Ruthvik-1411/Open_CV_Projects/blob/main/face_tracking/ft_im2.jpg" width = 150 height = 200 align="top">
<img src="https://github.com/Ruthvik-1411/Open_CV_Projects/blob/main/face_tracking/ft_im1.jpg" width = 150 height = 200>
<img src="https://github.com/Ruthvik-1411/Open_CV_Projects/blob/main/face_tracking/ft_im3.jpg" width = 150 height = 200><br><br>

The flow of the entire project is as follows : <br><br>
<img src="https://github.com/Ruthvik-1411/Open_CV_Projects/blob/main/face_tracking/ft_f1.jpg" width = 450 height = 200 align="top">
<img src="https://github.com/Ruthvik-1411/Open_CV_Projects/blob/main/face_tracking/ft_f2.jpg" width = 450 height = 200 align="top">

* Firstly the webcam captures the video and this data is passed through the _haar cascade classifier_ to identify any faces in the image. The function returns the coordinates of the face and the center of the face obtained from these coordinates is sent to the arduino.
* This data recieved from the python script is read from the serial buffer. The servos' in the above mentioned setup are physically restricted to move beyond a certain angle. So the coordinates recieved are mapped to their respective permissible ranges. The servos' are then given this angle to rotate. 
* The mapping is inverse here. That is the coordinates of the face lie between (0 - 640), (0 - 480). So if the face is located at the extreme right (in webcam feed i.e inverse to reality) then the aim of the tracker is to track the face so that the face is always located at the center to say. So the servo should move to the right as a  result. The mapping made here is [0 -> 640 ==> 179 -> 70]  

>The [python code](https://github.com/Ruthvik-1411/Open_CV_Projects/blob/main/face_tracking/tracking.py) and [arduino code](https://github.com/Ruthvik-1411/Open_CV_Projects/blob/main/face_tracking/face_tracking.ino) can be found above with comments.

>YouTube Video Link: https://youtu.be/z-2_2DfBp2M
