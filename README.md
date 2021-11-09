# Implementation of a simple Chat Bot
Simple chatbot implementation with the help of same basic library modules

- The implementation should be easy to follow for beginners and provide a basic understanding of chatbots.
- The implementation is straightforward with lists of some predefined responses.
- Customization for your own use case is super easy. Just modify `responses`(list) with possible patterns and responses and re-run the main_bot.py (see below for more info).

The approach is inspired by the articles/videos mentioned below:
- Basic infomation about chatbot [https://www.freshworks.com/live-chat-software/chatbots/what-is-a-chatbot/].
- Fun with Data Science [https://youtu.be/ko7KKy5WB-Y].
- Misbah Mohammed [https://youtu.be/uN50y7L_6Qk].
- Python Engineer [https://youtu.be/RNEcewpVZUQ].

## What is a ChaT Bot?
<p>
Chatbots, as the name suggests, are computer programs built to simulate human conversations— whether that is on a website, a messaging app, or a virtual assistant. With today’s customers expecting immediacy and personalization in their interactions with brands, the addition of chatbots as a communication channel has become critical to business growth.
</p>
<p>
In its simplest form, chatbots can be programmed to answer specific, frequently asked questions, offering an easy way to engage with visitors. On the other hand, Artificial Intelligence (AI) - powered chatbots can learn from user behavior and previous agent interactions to predict visitor behavior and offer relevant information. Using chatbots can help automate interactions and offer instant accessibility across sales, marketing, and customer service functions.</p>

## Initial Setup
Run the following command in terminal
```console
pip install tkinter
```
## Import modules
Tkinter - Most commonly used library for developing GUI (Graphical User Interface) in Python. It is a standard Python interface to the Tk GUI toolkit shipped with Python. As Tk and Tkinter are available on most of the Unix platforms as well as on the Windows system, developing GUI applications with Tkinter becomes the fastest and easiest.
Random -  In-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these are not truly random. This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc.
```console
from tkinter import *
import random
```
## Create class GUI 
For implementing GUI part we are using a class called GUI
```console
class GUI:
```
Defining attributes/class-variables
```console
name = "Funny Bot 101"
    weather = "rainy"
    mood = "Happy"
```
...and 'responses' as in the form of a 'dictionary' having keys as string and value as in the form of list.
