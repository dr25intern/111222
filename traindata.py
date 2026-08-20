from ultralytics import YOLO

# Initialize YOLOv12 model architecture (e.g., small or nano)
model = YOLO("yolov12/ultralytics/cfg/models/v12/yolov12s.yaml")

# Train the model
results = model.train(
    data="Feature-Extraction-2/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    device=0,  # 0 for GPU, 'cpu' for CPU
    project="runs/detect",
    name="yolov12_custom_run",
)