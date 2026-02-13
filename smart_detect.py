from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/best.pt")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    results = model(frame, conf=0.6)
    clamp_count = len(results[0].boxes) # Count the detected boxes
    
    # Display the count on the screen
    cv2.putText(frame, f"Clamps Found: {clamp_count}", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Smart Inventory", results[0].plot())
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
