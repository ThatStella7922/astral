# *astral* Setup

## Pip
Take care of any packages by installing [requirements.txt](requirements.txt)

## dotenvs
In the root, create a .env containing the following:
```
TOKEN = <your bot token>
```


In the cogs folder, create another .env containing the following:
```
# basic bot info
botName = <your bot name>
```
This should satisfy any static info that is stored in dotenvs.

## Database
There is no database yet

## Run
Just run astral.py with Python 3.9 or later