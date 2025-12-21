from ultralytics import YOLO
import os

# Get the correct path to best.pt in project root
model_path = os.path.join(os.path.dirname(__file__), "best.pt")
model = YOLO(model_path)
results = model(source=0, show=True, conf=0.3, save=True)