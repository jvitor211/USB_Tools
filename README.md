# USB Camera Blocker - Device Security and Control

## 📌 Description
The **USB Camera Blocker** is a software designed to **monitor, list, disable, and re-enable USB devices**, including **cameras, microphones, audio devices, and networks**. Additionally, it allows **corrupting files** that are being recorded by cameras and microphones to enhance privacy. It is compatible with **Windows 7, 10, and 11**, using **PowerShell commands** for advanced device management.

## 🛠 Features
✅ **Lists USB devices** (cameras, microphones, audio, network) organized into tabs.  
✅ **Disables and re-enables selected devices individually.**  
✅ **Compatible with Windows 7, 10, and 11** using `PowerShell Get-PnpDevice`.  
✅ **Monitors disabled devices** in a separate tab.  
✅ **Modern and intuitive graphical interface** built with `tkinter`.  
✅ **Corrupts files** being recorded by cameras and microphones.  
✅ **Can be executed directly from a USB flash drive** for portable security.

## 🎨 Interface
The **USB Camera Blocker** graphical interface is divided into **5 tabs**, each displaying a specific type of device:

- **Cameras** 🎥
- **Microphones** 🎙
- **Audio (Headphones, Speakers)** 🎧
- **Network (Wi-Fi, Ethernet)** 🌐
- **Disabled Devices** 🚫

Each tab allows **selecting a device and disabling or re-enabling it** easily.

## 📂 Folder Structure
```
usb-camera-blocker/
│── main.py                  # Main script to run the application
│── utils/
│   │── __init__.py           # Utility functions
│   │── device_manager.py     # Device management logic (enable, disable, corrupt files)
│── assets/
│   │── icon.ico              # Application icon (optional)
│── requirements.txt          # Project dependencies
│── README.md                 # Project documentation
```

## 💻 Technologies Used
- **Python 3.12**
- **tkinter** (for GUI)
- **subprocess** (to interact with `PowerShell`)
- **Windows Management Instrumentation (WMI)**

## 🔧 Installation
### 1️⃣ **Prerequisites**
Before running the **USB Camera Blocker**, make sure:
- You have **Python 3.12** installed.
- You have **Administrator permissions** on Windows.

### 2️⃣ **Clone the repository**
```sh
git clone https://github.com/youruser/usb-camera-blocker.git
cd usb-camera-blocker
```

### 3️⃣ **Install dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run the application**
```sh
python main.py
```
⚠️ **Important:** The program must be run as **Administrator**!

## 🚀 Running from a USB Flash Drive
The **USB Camera Blocker** can be executed directly from a **USB drive**, making it a portable security solution. Simply copy the project folder to a USB stick and run `main.py` from there.

## 🚀 Creating an Executable
To convert the **USB Camera Blocker** into a `.exe` file, use **PyInstaller**:
```sh
pip install pyinstaller
pyinstaller --onefile --windowed --icon=assets/icon.ico main.py
```
The executable will be located in the `dist/` folder.

## 🔥 File Corruption Functionality
Besides device blocking, the software allows **corrupting files being recorded** by cameras and microphones. This feature can:
- **Replace file content with random data.**
- **Zero out the file size.**
- **Rename the file to an unrecognizable name.**
- **Permanently delete the file.**

### 📌 How does it work?
1. The program **detects active recording processes.**
2. It locates **files being recorded by those processes.**
3. The user can **manually corrupt the files** via the graphical interface.

## 📜 License
This project is distributed under the MIT license. Feel free to contribute and improve the tool! 🛠🚀

