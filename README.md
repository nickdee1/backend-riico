# Ricco - 5. Longer life for furniture - BACKEND PART

Team Ricco at GreenHack hackathon would love to introduce you its lovely child - App for buying Spare Parts. Ricco app is a mobile platform that helps people to buy spare parts for their furniture or sell it back to IKEA.
## Project Description:

There will be project description...

## Installation and running
To successfully install and run Ricco app you would need to:
* clone this frontend repository to your local machine;
* install Expo app on your mobile device;
* install the requirements for the frontend client and run it.
Let's install and run the application step-by-step.

### 1. Pull the repository

```
git clone git@github.com:nickdee1/backend-riico.git <project_directory>
```

Where <project_directory> is your desired folder to clone the repository into.

### 2. Running of the backend server on your machine
### NOTE: You should not do it, because of our server is hosted on Heroku. Just go to Frontend part and use it :)

The project's backend is written in Python with the usage of Flask web framework and an SQLite database.
To install these, make sure that you have Python3.6 or higher and pip installed on your machine.
It is also recommended to create a new virtual environment for the project, so make sure to execute these:

```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

After the virtual environment was created, you can install requirements for the backend part:

```
(venv) pip3 install -r requirements.txt
```

Finally, to run the server, execute this:

```
(venv) python3 main.py
```
