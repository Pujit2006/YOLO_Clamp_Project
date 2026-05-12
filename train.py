from ultralytics import YOLO

model = YOLO("yolov8n.pt") 

model.train(
    data="datasets/clamp_data/data.yaml", 
    epochs=100,      # Give it more time to learn
    imgsz=640,
    # --- AUGMENTATION SETTINGS ---
    degrees=15.0,    # Rotate images by up to 15 degrees
    flipud=0.5,      # 50% chance to flip the image upside down
    fliplr=0.5,      # 50% chance to flip left-to-right
    mosaic=1.0,      # Combine 4 images into 1 (Great for small objects!)
    mixup=0.2,       # Blends two images together to handle "clutter"
    hsv_v=0.4,       # Randomly change brightness (Good for shadows)
    # -----------------------------
    patience=20,     # If it stops improving for 20 rounds, stop early
    save=True
)
