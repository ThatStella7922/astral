# *astral* Setup
These instructions are for Linux-based OSes and macOS.

## OS support
astral has been tested on Debian 11 x86_64 as well as macOS 13 arm64, but you should be fine if your OS supports a recent Python.

Windows *should* work as well, but I haven't tested it yet.

## Installation
Start off by running the following commands in your terminal.
```bash
cd ~
git clone https://github.com/ThatStella7922/astral.git
cd astral
```
These commands clone aastral into your home folder at `~/astral`, and change directory into the new installation.

At this point, you can create a virtualenv for the python packages installed in the next step, but this isn't necessary and astral will work all the same without it.

Now, install the requred python packages with the collowing command:
```bash
pip install -r requirements.txt
```

## Configuration
In the root, create a .env containing the following:
```
TOKEN = <your bot token>
OWNERID = <your own discord user id>
```


In the cogs folder, create another .env containing the following:
```
# basic bot info
botName = <your bot name>
```
This should satisfy any static info that is stored in dotenvs.

## Database
The required packages for this are installed with the instructions above. (astral uses dataset to interface with sqlite for now.)

## Run
Run astral.py with Python 3.9 or later.
```bash
cd ~/astral
python3 astral.py
```

If astral started up and is running properly, you should see the following in your terminal:
```
astral
[√] Database connection: probably worked fine
[√] Bot sucessfully initialized as MyBot#7922
```
Of course, the bot's name will differ depending on what you have set up for your bot account.