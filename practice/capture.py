import cv2

video = cv2.VideoCapture(0) 
## if it is a video file you can input a path "" between the brackets 

check, frame = video.read()
# check if boolean, frame is np.array 
# good use of check is to see if the script is actually running or not 

time.sleep(3) # will wait for 3 second


video.release()