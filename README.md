

# Ahmed Osama style generator (Backend)

>

## Build Setup (suggested)

# set up environment
```
$ pip3 install -r requirements.txt
```
You MUST also set a data.csv file in the root folder, same folder
where main.py lies. This will be the data file that gets the images

# install dependencies
```bash
$ export MONGODB_PASSWORD=password
$ export MONGODB_PORT=port
$ export MONGODB_SERVER=server
$ export MONGODB_USERNAME=username
$ export FLASK_APP=main.py
```
you can also use docker for all this.

# running the server

The most basic way to run the server is by executing
```
    flask run
```
That will print out something like

```
 * Serving Flask app "main.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 259-008-034

```
