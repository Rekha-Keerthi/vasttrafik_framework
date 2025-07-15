# Vasttrafik Framework

This project demonstrates a basic Python setup with virtual environment management and dependency installation using `requirements.txt`.

## 📦 Features

- Clean, modular Python code
- Easy setup and environment isolation
- Dependency management with `pip` and `requirements.txt`

---

## 🚀 Quick Start Guide

Follow these steps to get the project up and running on your machine.

---

### 🛠 1. Clone the Repository (optional)

Open your terminal and run:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 🐍 2. Create a Virtual Environment

Create a virtual environment named venv.

On macOS/Linux:
```bash
python3 -m venv venv
```

On Windows:
```bash
python -m venv venv
```

If there are multiple versions of Python installed, use the full path to the version. For example,
```bash
C:\Users\rekha\AppData\Local\Programs\Python\Python313\python.exe -m venv venv
```

### ⚡️ 3. Activate the Virtual Environment

macOS/Linux:
```bash
source venv/bin/activate
```

Windows (CMD):
```bash
venv\Scripts\activate.bat
```

#Jenkins poll test
Windows (PowerShell): 
```bash
venv\Scripts\Activate.ps1
```

### 📦 4. Install Dependencies
With the virtual environment activated, install the required Python packages:
```bash
pip install -r requirements.txt
```
### ▶️ 5. Run the Application

To execute the project (supported browsers are chrome and edge):
```bash
pytest testfiles --capture=tee-sys --browser_name chrome
```
### ❎ 6. Deactivate the Virtual Environment
When you're finished working:
```bash
deactivate
```

### 🙋‍♂️ Contact
Created by [Your Name] – your.email@example.com
