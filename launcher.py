"""import tkinter as tk
from tkhtmlview import HTMLLabel
import requests
import os

app = tk.Tk()
app.title("Minecraft Launcher [DEV-ONLY]")

HTMLLabel(app, html=requests.get("https://exalpha-dev.github.io").text).pack()
tk.Button(app, text="Play [CONSOLE]", command=lambda: os.system("run.bat")).pack()
tk.Button(app, text="Change username [CONSOLE]", command=lambda: os.system("username.py")).pack()

app.mainloop()
"""
import json
import eel


class Config:
    def __init__(self, file):
        self.file = file
        with open(file) as read:
            self.data = json.load(read)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value
        with open(self.file, "w") as file:
            json.dump(self.data, file)


@eel.expose
def login(name):
    print(name)


config = Config("config.json")
eel.init("resources")
eel.start("app.html", port=1425, size=(707, 432))
