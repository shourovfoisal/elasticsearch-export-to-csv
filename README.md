Install the following dependencies  
```bash
pip install elasticsearch==x.x.x pandas
```
<hr >

It's good to create a **python virtual environment** before installing dependencies.  

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

<hr>

**Alternatively**, the `manage_venvs.sh` shell file from this project can be used to create and manage virtual environments.

Firstly, copy the `manage_venvs.sh` file to the $HOME (~) directory.  

Then make the file executable
```bash
chmod +x manage_venvs.sh
```

After that, add the alias to `.bashrc`
```bash
alias venvwizard="source $HOME/manage_venvs.sh"
```

Finally, run the file like the following
```bash
# list all
./manage_venvs.sh list
# create
./manage_venvs.sh create env_name
# activate
./manage_venvs.sh activate env_name
# delete
./manage_venvs.sh delete env_name
```

Or, by using the alias
```bash
venvwizard list
venvwizard create env_name
venvwizard activate env_name
venvwizard delete env_name
```
