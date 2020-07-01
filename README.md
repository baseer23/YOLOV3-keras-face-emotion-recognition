# YOLO-keras-face-emotion-recognition

These are the instructions to run the project...

1.Run--->wget https://pjreddie.com/media/files/yolov3.weights

2.Run --->python convert.py model_data/yolov3.cfg model_data/yolov3.weights model_data/yolo_weights.h5

3.Put the training data folders(Angry,Suprise,...)in the train folder,check annotations.txt

4.Run pip install -r requirements.txt

5.Run train.py

6.Put the test data(unseen) folders in val folder

7.Run test_accuracy.py to get accuracy and graph of accuracy w.r.t classes

8.Use webcam_detect.py to perform realtime recognition


contact :    abdulbaseermohammedkhan@gmail.com     if you have any problem running the code
