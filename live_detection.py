from ultralytics import YOLO
import cv2
import requests
import numpy as np
import time

# Load model
model = YOLO("best.pt")

# ESP32 capture URL
url = "http://192.168.137.136/capture"  
print("Starting capture...")

while True:
    try:
        # Get frame from ESP32
        response = requests.get(url, timeout=5)

        img_array = np.frombuffer(response.content, dtype=np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if frame is None:
            continue

        print("Frame OK")
        frame = cv2.resize(frame, (640, 480))
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        frame = cv2.filter2D(frame, -1, kernel)

        results = model(frame, imgsz=640, conf=0.3)

        annotated = results[0].plot()

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])

                if conf > 0.3:
                    if cls == 0:
                        print(f"🟥 Crack detected ({conf:.2f})")
                    elif cls == 1:
                        print(f"🟦 Clamp detected ({conf:.2f})")

        cv2.imshow("YOLO Live Detection", annotated)
        time.sleep(0.5)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    except Exception as e:
        print("Retrying...", e)
        time.sleep(2)

cv2.destroyAllWindows() for this one?
