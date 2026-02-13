# 🧲 YOLO Clamp Detection System
> **Vibe:** "The Lazy Legend's Guide to Computer Vision." 
> Why work hard when you can teach a computer to do the looking for you?

---

## 📖 Project Overview
This project is a beginner-friendly pipeline to train a custom **YOLOv8** model to detect industrial clamps. It covers everything from setting up your environment to running a live webcam feed with your "custom brain."

### Features:
* **One-Click Training:** Simple Python scripts to start the learning process.
* **Real-Time Detection:** Smooth inference on webcam or video files.
* **Beginner Friendly:** No PhD in Math required. Just photos and a bit of patience.

---

## 📂 Project Hierarchy
To keep the AI from getting confused, we use this specific folder structure. **Consistency is key!**

```text
YOLO_Clamp_Project/
├── datasets/                 
│   └── clamp_data/           
│       ├── train/            # The "Study Material" (80% of data)
│       │   ├── images/       # Your clamp photos (.jpg, .png)
│       │   └── labels/       # YOLO format text files (.txt)
│       ├── val/              # The "Practice Test" (20% of data)
│       │   ├── images/
│       │   └── labels/
│       └── data.yaml         # The "GPS" that tells YOLO where files are
├── runs/                     # Created automatically (Contains your results)
├── train.py                  # The script that trains the model
├── inference.py              # The script that runs the live detection
└── README.md                 # You are currently reading this!
