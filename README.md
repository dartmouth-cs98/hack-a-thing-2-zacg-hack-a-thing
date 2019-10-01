# Hack-a-Thing 2 - TextBomb - Zac Gottschall

## What I attempted to build
Since I was in high school, I've always wanted a macOS application to send a 'Text Bomb.' For those who are unfamiliar with the term, a 'Text Bomb' is when you send hundreds (potentially thousands) of messages to one person at once. I've wanted this application for several reasons: (1) for revenge on scammers; it'd be great to have a way to flood their phone with thousands of nonsense messagges as payback; (2) a prank on a good friend :)

For example, I used this app to send my friend the entire Bee Movie script word by word over iMessage.

I built this application in Python. To take it a step further, I wanted to make it an installable macOS application, so that I could share it with my friends and the world. 

## Who did what
I worked by myself.

## What you learned
I learned how to write an Apple Script. I wrote a script that takes 2 arguments (recipient number and word to send them). The script then sends the word provided over iMessage.

I then wrote a python script that parses a string word by word and calls this Apple Script for every word.

I then learned how to use PyQt to build a simple user interface. (I didn't want people to have to use the command-line.)

I then used py2app to build a standalone macOS application. I used the following tutorial: http://www.marinamele.com/from-a-python-script-to-a-portable-mac-application-with-py2app

I then used the following Medium tutorial to build a macOS installer. This way, users can install the application and its necessary scripts (the sendMessage Apple Script).

## How does this hack-a-thing inspire or relate to other project ideas?

Going into this hack-a-thing, I wanted to build a standalone macOS app. I don't know what exactly I'm going to build as my final project in this class yet, but I think there is a high potential that it is a desktop app. Now, I know how to build a macOS app and an installer!

## What didn't work

With my program, you can only text bomb people with iMessage. 

## To install application
Open`TextBomb-macos-installer-x64-1.0.0.pkg` and follow instructions.

## To run application
Two options:
- (1) if you installed the application, open and run it
- (2a) open `TextBomb.py` and change line 23 to `os.system('osascript sendMessage.scpt ' + self.number + ' ' + word)`.
- (2b) run `python3 TextBomb.py`

## To build application
`$ cd src`
`$ rm -rf build dist`
`$ python3 setup.py py2app`

## to build macOS installer
`$ cd macOS-x64/application/`
`$ sudo rm -rf TextBomb.app`
`$ cd ../..`
`$ sudo cp -r ./pythonFiles/dist/ ./macOS-x64/application/`
`$ cd macOS-x64`
`$ bash ./build-macos-x64.sh TextBomb 1.0.0`

The macOS installer will be located in `macOS-x64/target/pkg`.

