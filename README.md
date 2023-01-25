# Splash-Page

## Set up Environment

I recommend you create python virtual environment for cleaner workplace:

Create new environment:
```
  python3 -m venv env/
```
Open the environment:
```
  source env/bin/active
```

Install python modules needed for this project
```
  pip install -r requirements.txt
```

You would need something to expose your local host to rest of the world. For testing and demo purposes I recommend [ngrok](https://dashboard.ngrok.com/get-started/setup), but for actual deployment you should get a better service (e.g. Heroku, AWS, Azure, etc...)

How to set up ngrok? https://dashboard.ngrok.com/get-started/setup

To use ngrok:
```
  ngrok http 5004
```
_Or any other port instead of 5004 (in this project I just picked 5004, but you can change that in the code if needed)_

