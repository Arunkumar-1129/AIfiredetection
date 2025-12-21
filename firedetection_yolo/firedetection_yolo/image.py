import os
from ultralytics import YOLO

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "best.pt")
model = YOLO(model_path)

# Specify the image path (update with your image path)
image_path = input("Enter the path to the image file: ")

# Check if file exists
if not os.path.exists(image_path):
    print(f"Error: Image file not found at {image_path}")
    exit(1)

# Run prediction
print(f"Running fire detection on: {image_path}")
results = model.predict(source=image_path, conf=0.3, save=True)

# Display results
for result in results:
    if result.boxes is not None:
        for box in result.boxes:
            class_name = model.names[int(box.cls)]
            confidence = float(box.conf)
            print(f"Detected: {class_name} with confidence: {confidence:.2%}")
    else:
        print("No fire or smoke detected in the image.")

print(f"\nResults saved to: {results[0].save_dir}")