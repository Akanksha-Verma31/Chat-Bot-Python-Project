# Importing necessary modules:
import random
from tkinter import *

# defining a bot_name
bot_name = "Cobot"

# GUI class for the chat
class GUI:
    # class attributes/variables
    name = "Funny Bot 101"
    weather = "rainy"
    mood = "Happy"
    responses = {
        "Hi": [
            "Hi, there...",
            "Hello Dear...",
            "Hello Dear LPU Student..."],
        "what's your name?": [
            "They call me {0}".format(name),
            "I usually go by {0}".format(name),
            "My name is the {0}".format(name)],
        "what's today's weather?": [
            "The weather is {0}".format(weather),
            "It's {0} today".format(weather),
            "Let me check, it looks {0} today".format(weather)],
        "Are you a robot?": [
            "What do you think?",
            "Maybe yes, maybe no!",
            "Yes, I am a robot with human feelings.", ],
        "how are you?": [
            "I am feeling {0}".format(mood),
            "{0}! How about you?".format(mood),
            "I am {0}! How about yourself?".format(mood), ],
        " ": [
            "Hey! Are you there?",
            "What do you mean by saying nothing?",
            "Sometimes saying nothing tells a lot :)", ],
        "default": [
            "I'm still learning",
            "this is a default message"]}
    responses2 = {
        "Hi": [
            "Hi, there...",
            "Hello Dear...",
            "Hello Dear LPU Student..."],
        "what's your name?": [
            "They call me {0}".format(name),
            "I usually go by {0}".format(name),
            "My name is the {0}".format(name)],
        "what's today's weather?": [
            "The weather is {0}".format(weather),
            "It's {0} today".format(weather),
            "Let me check, it looks {0} today".format(weather)],
        "Are you a robot?": [
            "What do you think?",
            "Maybe yes, maybe no!",
            "Yes, I am a robot with human feelings.", ],
        "how are you?": [
            "I am feeling {0}".format(mood),
            "{0}! How about you?".format(mood),
            "I am {0}! How about yourself?".format(mood), ],
        " ": [
            "Hey! Are you there?",
            "What do you mean by saying nothing?",
            "Sometimes saying nothing tells a lot :)", ],
        "default": [
            "I'm still learning",
            "this is a default message"],
        "what is coronavirus?": [
            "Coronaviruses are a family of viruses that typically cause mild respiratory infections like the common cold but also more severe"],
        "what diseases are caused by coronavirus?": [
            "A coronavirus that originated in China led to the Severe Acute Respiratory Syndrome (SARS) outbreak in 2003. Another coronavirus emerged in 2012 in Saudi"],
        "wht and how should I seek medical attention?": [
            "If you develop any of the following emergency warning signs for COVID-19, get medical attention immediately by calling your doctor's office. Emergency warning signs include (but are not limited to):\nTrouble breathing\nPersistent pain or pressure in the chest\nNew confusion or inability to arouse\nBluish lips or face"],
        "how is coronavirus transmitted?": [
            "Coronaviruses are typically transmitted from person to person through exhalation of respiratory droplets (from the nose and mouth) and close contact. People can contract COVID-19 if they breathe in droplets from an infected person who coughs or exhales droplets. Those droplets can also land on objects and surfaces, and people can then catch the virus from touching those surfaces and then touching their eyes, nose, or mouth."],
        "Coronavirus *": [
            "I don't know...:("],
        "How does the virus spread": [
            "The virus that causes COVID-19 is thought to spread mainly from person to person, mainly through respiratory droplets produced when an infected person coughs, sneezes, or talks. These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs. Spread is more likely when people are in close contact with one another (within about 6 feet)."]
    }

    # constructor method
    def __init__(self):
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()

        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)
        # create a Label
        self.pls = Label(self.login, text="Please login to continue", justify=CENTER, font="Helvetica 14 bold")
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)
        # create a Label
        self.labelName = Label(self.login, text="Name: ", font="Helvetica 12")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.3)

        # create a entry box for
        # tyoing the message
        self.entryName = Entry(self.login, font="Helvetica 14")
        self.entryName.place(relwidth=0.5, relheight=0.12, relx=0.25, rely=0.3)

        # set the focus of the cursor
        self.entryName.focus()

        # create a Continue Button
        # along with action
        self.go = Button(self.login, text="GENERIC BOT", bg="#d6e1f4", fg="black",font="Helvetica 14 bold", command=lambda: self.goAhead(self.entryName.get()))
        self.go.place(relx=0.1,rely=0.55)
        self.goto_cobot = Button(self.login, text="COBOT", bg="#d6e1f4", fg="black", font="Helvetica 14 bold", command=lambda: self.goAhead2(self.entryName.get()))
        self.goto_cobot.place(relx=0.6, rely=0.55)
        self.Window.mainloop()
    # function to end the login window and open a new layout window for general chat
    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)

    # function to end the login window and open a new layout window for covid chat
    def goAhead2(self, name):
        self.login.destroy()
        self.layout2(name)

    # The main layout of the generic chatroom
    def layout(self, name):
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width=False,height=False)
        self.Window.configure(width=470, height=550, bg="#17202A")
        self.labelHead = Label(self.Window, bg="#17202A", fg="#EAECEE", text=self.name, font="Helvetica 13 bold",pady=5)
        self.labelHead.place(relwidth=1)
        self.line = Label(self.Window, width=450, bg="#ABB2B9")
        self.line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.textCons = Text(self.Window, width=20,height=2, bg="#17202A",fg="#EAECEE", font="Helvetica 14", padx=5, pady=5)
        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)
        self.labelBottom = Label(self.Window, bg="#ABB2B9", height=80)
        self.labelBottom.place(relwidth=1, rely=0.825)
        self.entryMsg = Entry(self.labelBottom, bg="#2C3E50", fg="#EAECEE", font="Helvetica 13")

        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.entryMsg.focus()

        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,text="Send",font="Helvetica 10 bold",width=20,bg="#ABB2B9",command=lambda: self._on_enter_pressed(None))
        self.buttonMsg.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)
        self.textCons.config(cursor="arrow")

        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)

        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state=DISABLED)

        # The main layout of the covid bot
    def layout2(self, name):
            self.name = name
            # to show chat window
            self.Window.deiconify()
            self.Window.title("COVID CHATROOM")
            self.Window.resizable(width=TRUE, height=TRUE)
            self.Window.configure(width=470, height=550, bg="#17202A")
            self.labelHead = Label(self.Window, bg="#17202A", fg="#EAECEE", text=self.name, font="Helvetica 13 bold",pady=5)
            self.labelHead.place(relwidth=1)
            self.line = Label(self.Window, width=450, bg="#ABB2B9")
            self.line.place(relwidth=1, rely=0.07, relheight=0.012)
            self.textCons = Text(self.Window, width=20, height=2, bg="#17202A", fg="#EAECEE", font="Helvetica 14",padx=5, pady=5)
            self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)
            self.labelBottom = Label(self.Window, bg="#ABB2B9", height=80)
            self.labelBottom.place(relwidth=1, rely=0.825)
            self.entryMsg = Entry(self.labelBottom, bg="#2C3E50", fg="#EAECEE", font="Helvetica 13")

            # place the given widget
            # into the gui window
            self.entryMsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
            self.entryMsg.focus()

            # create a Send Button
            self.buttonMsg = Button(self.labelBottom, text="Send", font="Helvetica 10 bold", width=20, bg="#ABB2B9", command=lambda: self._on_enter_pressed2(None))
            self.buttonMsg.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
            self.textCons.config(cursor="arrow")

            # create a scroll bar
            scrollbar = Scrollbar(self.textCons)

            # place the scroll bar
            # into the gui window
            scrollbar.place(relheight=1, relx=0.974)
            scrollbar.config(command=self.textCons.yview)
            self.textCons.config(state=DISABLED)

    def _on_enter_pressed(self, event):
        msg = self.entryMsg.get().strip()
        self._insert_message(msg, "You")

    def _on_enter_pressed2(self, event):
        msg = self.entryMsg.get().strip()
        self._insert_message2(msg, "You")

    def response(self,message):
        " " " function to match responses with the msg entered by the user " " "
        my_msg = self.entryMsg.get().strip()
        if message in self.responses:
            bot_message = random.choice(self.responses[message])
        elif message == " ":
            bot_message = "Sometimes saying nothing tells a lot :)"
        else:
            bot_message = random.choice(self.responses["default"])

        return bot_message

    def response2(self, message):
        my_msg = self.entryMsg.get().strip()
        if message in self.responses2:
            bot_message = random.choice(self.responses2[message])
        elif message == " ":
            bot_message = "Sometimes saying nothing tells a lot :)"
        else:
            bot_message = random.choice(self.responses2["default"])

        return bot_message

    # function to show the msg and response by the bot into the window
    def _insert_message(self, msg, sender):
        if not msg:
            return

        res = self.response(msg)
        self.entryMsg.delete(0, END)
        msg = f"{sender}: {msg}\n\n"
        self.textCons.configure(cursor="arrow", state=NORMAL)
        self.textCons.insert(END, msg)
        self.textCons.configure(state=DISABLED)

        msg2 = f"{bot_name}: {res}\n\n"
        self.textCons.configure(cursor="arrow", state=NORMAL)
        self.textCons.insert(END, msg2)
        self.textCons.configure(state=DISABLED)
        self.textCons.see(END)

    def _insert_message2(self, msg, sender):
        if not msg:
            return
        res = self.response2(msg)
        self.entryMsg.delete(0, END)
        msg = f"{sender}: {msg}\n\n"
        self.textCons.configure(cursor="arrow", state=NORMAL)
        self.textCons.insert(END, msg)
        self.textCons.configure(state=DISABLED)

        msg2 = f"{bot_name}: {res}\n\n"
        self.textCons.configure(cursor="arrow", state=NORMAL)
        self.textCons.insert(END, msg2)
        self.textCons.configure(state=DISABLED)
        self.textCons.see(END)


# create a GUI class object
g = GUI()