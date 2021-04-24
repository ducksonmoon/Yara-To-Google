# Yara-To-Google

![Image](https://s19.picofile.com/file/8431697034/yara144_3682aa33_1_.png)

## What the heck is this?

The funny thing is, i was lazy as hell and I didn't want to check my university's website every day for deadlines, so i wrote this to collect all the practices and add them to my google calendar.

## What do I need to do?

~~~~~~~~
  git clone https://github.com/M-b850/Yara-To-Google.git
  cd Yara-To-Google
  pip3 install -r requirements.txt
  python3 yara
~~~~~~~~

## Customize

By default, this program adds events to your **primary** google calendar, if you want to add them to a specific google calendar, 
simply add the appropriate **calendar id** to the **CALENDAR_ID** file.

## Change saved user and password

First time that you have enter your username and password we save it in fileds file,
you can change it by editing this file as this schema:
~~~~~~~
    username:password
    example ->
    98121021:mypassword123
~~~~~~~
## Note

This program only works for [Yara Platform](https://yara.mazust.ac.ir).
