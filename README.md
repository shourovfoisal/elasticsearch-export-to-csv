Install the following dependencies  
```bash
pip install elasticsearch==x.x.x pandas
```
<hr >

It's good to create a python virtual environment before installing dependencies.  

First, create a directory to hold all the virtual environments in one place.  
```bash
mkdir -p ~/venvs
```

Then create a virtual environment  
```bash
python3 -m venv ~/venvs/es-export-env
```

After that, activate the environment
```bash
source ~/venvs/es-export-env/bin/activate
```

Finally, run the script
```bash
python3 export.py
``` 