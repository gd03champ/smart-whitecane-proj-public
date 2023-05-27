import numpy as np
import time
import cv2
import os
import imutils
import subprocess
import socket
from translate_tts import transnsay

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def say(des):
    if is_connected():
        print(des)
        transnsay(des,'ta')
    else:
        os.system(f'''espeak "{des}" ''')
        print(des)
LABELS = open("coco.names").read().strip().split("\n")
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
font = cv2.FONT_HERSHEY_PLAIN


ln = net.getLayerNames()
ln = [ln[i[0]-1] for i in net.getUnconnectedOutLayers()]

# initialize
cap = cv2.VideoCapture(0)

frame_count = 0
start = time.time()
first = True
frames = []
flag=1

while True:
	
	frame_count += 1
	ret, frame = cap.read()
	frames.append(frame)

	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
	if ret:
		key = cv2.waitKey(1)
		if frame_count % 60 == 0:
			end = time.time()

			(H, W) = frame.shape[:2]

			blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
				swapRB=True, crop=False)
			net.setInput(blob)
			layerOutputs = net.forward(ln)

			boxes = []
			confidences = []
			classIDs = []
			centers = []

			for output in layerOutputs:

				for detection in output:

					scores = detection[5:]
					classID = np.argmax(scores)
					confidence = scores[classID]

					if confidence > 0.5:

						box = detection[0:4] * np.array([W, H, W, H])
						(centerX, centerY, width, height) = box.astype("int")

						x = int(centerX - (width / 2))
						y = int(centerY - (height / 2))

						boxes.append([x, y, int(width), int(height)])
						confidences.append(float(confidence))
						classIDs.append(classID)
						centers.append((centerX, centerY))

			idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)

			for i in range(len(boxes)):
				if i in idxs:
					x, y, w, h = boxes[i]
					label = str(classes[classIDs[i]])
					confidence = confidences[i]
					color = colors[classIDs[i]]
					cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
					cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + 30), font, 3, color, 3)


			texts = ["The environment has following objects"]

			# ensure at least one detection exists
			if len(idxs) > 0:
				# loop over the indexes we are keeping
				for i in idxs.flatten():
					# find positions
					centerX, centerY = centers[i][0], centers[i][1]
					
					if centerX <= W/3:
						W_pos = "left "
					elif centerX <= (W/3 * 2):
						W_pos = "center "
					else:
						W_pos = "right "
					
					if centerY <= H/3:
						H_pos = "top "
					elif centerY <= (H/3 * 2):
						H_pos = "mid "
					else:
						H_pos = "bottom "

					texts.append(H_pos + W_pos + LABELS[classIDs[i]])
					flag=0

			print(texts)
	
			if (flag==0):
				description = ', '.join(texts)
				say(description)
				exit()

cap.release()
cv2.destroyAllWindows()
