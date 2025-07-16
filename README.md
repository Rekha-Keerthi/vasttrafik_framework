# Vasttrafik Framework

This project is a unit testing framework developed using Python, Selenium, and Pytest to automate https://www.vasttrafik.se/ web application following Page Object pattern, data parameterization, fixture setup, html reporting, and logging.

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
git clone https://github.com/Rekha-Keerthi/vasttrafik_framework.git
cd vasttrafik_framework
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
Created by Rekha Danappala Basavarajappa – rekha.nkk5@gmail.com
