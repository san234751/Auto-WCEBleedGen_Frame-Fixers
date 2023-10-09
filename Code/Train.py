import os
from ultralytics import YOLO

ROOT_DIR="path/to/your/training-data"
data_yaml_path="/path/to/your/data.yaml"
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data=os.path.join(ROOT_DIR, data_yaml_path), epochs=10000)
