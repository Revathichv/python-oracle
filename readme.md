python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
 .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install oracledb
Please install https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html