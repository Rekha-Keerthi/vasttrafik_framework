REM :: provide browser name e.g. "chrome" or "Edge" as an argument to the script

echo CURRENT_WORKSPACE=%WORKSPACE%

call python -m venv venv
echo PYTHON VIRTUAL ENVIRONMENT CREATED

call venv\Scripts\activate.bat
echo PYTHON VIRTUAL ENVIRONMENT ACTIVATED

pip install -r requirements.txt
echo Installed python requirements

REM :: The argument to the script is used here as an option to pytest call
echo RUNNING PYTESTS
pytest testfiles --capture=tee-sys --browser_name %1
