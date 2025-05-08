# SpaceX and Nasa pictures

This is a telegram bot that automatically sends a random number of images from SpaceX launches or pictures of the day from Nasa with a description. And it does it all the time with a preset delay.

## How to install

Download and unzip the code. Python must already be installed. Then use pip to install the dependencies.

```
pip install -r requirements.txt
```

## How to launch

Create a file "config.py" and fill it out.
```
tg_chat_id = "abc"
tg_token = "abc"
token_nasa = "abc"
delay = 100
```

Write the api token to the "token_nasa" variable 'https://api.nasa.gov/'. 
And in the "tg_token" variable, write the token from the telegram bot. 
tg_chat_id - ID of the Telegram channel. (Bot must be as an administrator in channel.)
delay - Each time after the specified number of seconds, messages will be sent to telegram.

To run the program, you need to write in the terminal
```
python main.py
```
