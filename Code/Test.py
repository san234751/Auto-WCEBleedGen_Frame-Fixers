import os
from ultralytics import YOLO
import cv2

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

imgs=load_images_from_folder('/home/sankit/Desktop/Frame-Fixers/Test Dataset 1/')

model_path='best.pt'

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

for image in imgs:

    results = model(image)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('Image: ',image)
    cv2.waitKey(0)

