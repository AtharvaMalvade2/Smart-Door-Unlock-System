# 🔐 Smart Door Unlock System

A secure and intelligent **Smart Door Unlock System** that uses **Face Recognition and Computer Vision** to automatically detect and authenticate authorized users. This system enhances security by allowing access only to recognized individuals.

---

## 📂 Project Structure

- `door/` : Contains trained face data and recognition resources  
- `images/` : Stores captured images for training and recognition  
- `Main_Window.py` : Main application file that runs the smart door system  
- `collectingdata.py` : Script used to collect face images for training  
- `facelook.py` : Face recognition logic implementation  
- `README.md` : Project documentation  

---

## 🏗️ Tech Stack

| Component | Technologies Used |
|----------|-------------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Face Recognition | LBPH Face Recognizer |
| GUI | Tkinter |
| Data Handling | NumPy |
| Image Processing | OpenCV |

---

## 🚀 Key Features

- ✅ Face Recognition-based Door Unlock System  
- ✅ Automatic detection of authorized users  
- ✅ Secure authentication using Computer Vision  
- ✅ Real-time camera-based face detection  
- ✅ Easy face data collection and training  
- ✅ GUI-based system interface  

---

## 🛠️ Setup & Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/AtharvaMalvade2/Smart-Door-Unlock-System.git
cd Smart-Door-Unlock-System
```

### Step 2: Install Dependencies

```bash
pip install opencv-python
pip install numpy
pip install pillow
```

### Step 3: Collect Face Data

Run the following to collect authorized user face data:

```bash
python collectingdata.py
```

This will capture face images and store them in the dataset.

---

### Step 4: Run the Smart Door System

```bash
python Main_Window.py
```

The system will start the camera and unlock the door when an authorized face is detected.

---

## 🧠 How It Works

1. Face images are collected using webcam  
2. Images are stored and used to train the face recognition model  
3. The system uses OpenCV and LBPH algorithm for recognition  
4. When an authorized face is detected, access is granted  
5. Unauthorized users are denied access  

---

## 📊 System Requirements

- Python 3.x  
- Webcam  
- OpenCV  
- NumPy  
- Pillow  

---

## 🛫 Deployment

This system can be deployed on:

- Personal Computer with Webcam  
- Raspberry Pi with Camera Module  
- Embedded Security Systems  

---

## 🎯 Future Enhancements

- Add password backup authentication  
- Add mobile app integration  
- Add cloud-based face database  
- Improve recognition accuracy using Deep Learning  
- Add real door lock hardware integration  

---

## 👨‍💻 Author

Atharva Malvade  

GitHub: https://github.com/AtharvaMalvade2  

---

## ⭐ Support

If you like this project, please star ⭐ the repository.
