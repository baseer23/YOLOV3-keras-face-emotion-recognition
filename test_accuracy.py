from image_detect import YOLO
import os

yolo = YOLO()
count=0
total=0
emotions=['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']
for emotion in emotions:
  for filename in os.listdir('Val/'+emotion):
      if filename.endswith(".png") or filename.endswith(".jpg"): 
          r_image, ObjectsList = yolo.detect_img('Val/'+emotion+'/'+filename)
          #print(ObjectsList)
          if ObjectsList!=[]:
            for i in range(len(ObjectsList)):
              if ObjectsList[i][6].split()[0] == emotion:
                count+=1
                #print('count = ',count)
                print('emotionVal = '+emotion)
              total+=1
            #print('total = ',total)
            print('accuracy = ',count/total)
          
        
      else:
          continue
