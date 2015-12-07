# CleanCloud
Mini project for the Cloud Computing course in HES-SO Master. This PyQt program aims to easily detect and remove unused resources in your AWS.

## Developement
### versions used
- Python 3.5
- PyQt 5.5.1
- SIP 4.17 (PyQt dependency)
- Boto 2.38.0
 
## Sources directories
- controllers: where the controllers are
- credentials: skeleton for pre-filled credentials
- gen: compiled xml ui files in python
- handlers: log messages handlers for controllers
- res: contains xml gui files generated with Qt Creator
- tools: python script that read credentials file and fill GUI
- views: python compiled views
- requirements.txt: contains all libs required by CleanCloud

## Setup
### Auto-filled credentials
To use pre-filled credentials feature, just copy credentials_skeleton.ini in credentials.ini and edit it with your own credentials

### Compile ui files into python
You must have pyuic5 installed and use it like this:
``` bash
pyuic5 main.ui -o main.py
```
Otherwise, you can simply use our script _compile_ui_files.sh_

