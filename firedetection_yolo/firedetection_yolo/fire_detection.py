from ultralytics import YOLO

# Load the trained model
model = YOLO("best.pt")

# Run detection on camera feed
results = model(source=0, show=True, conf=0.3, save=True)