from tkinter import *
from tkinter.scrolledtext import ScrolledText as St
from BasicServerAndClient.client import Client
from _thread import *

import socket

class ChatLog(St):
	def __init__(self, master, border=0, **kw):
		super().__init__(master, border=border, **kw)

		self.disableTyping()

	def enableTyping(self):
		self.config(state="normal")

	def disableTyping(self):
		self.config(state="disabled")

	def _insertText(self, text=""):
		self.insert(END, text)

	def log(self, log=""):
		self.enableTyping()
		self._insertText(log)
		self.disableTyping()

class MainWindow(Tk):
	def __init__(self):
		super().__init__()

		self.client = Client(socket.gethostbyname(socket.gethostname()))

		self.chatLog = ChatLog(self, font=("calibri", 12))
		self.chatLog.pack(fill=BOTH, expand=1)

		self.messageVar = StringVar()
		self.chatBox = Entry(self, border=0, textvariable=self.messageVar, bg="grey")
		self.chatBox.pack(fill=X, expand=1, side="bottom")

		self.bind("<Return>", self.sendMessage)

	def sendMessage(self, e):
		message = self.chatBox.get()
		self.client.sendMessage("TechStudent10: " + message + "\n")
		#self.chatLog.log("TechStudent10: " + message)

	def addMessages(self):
		while 1:
			message = self.client.getMessages()
			print(message)
			if len(message) != 0:
				self.chatLog.log(message)

if __name__ == "__main__":
	mainWindow = MainWindow()
	mainWindow.resizable(False, False)
	mainWindow.title("Chat Application")
	start_new_thread(mainWindow.addMessages, ())
	mainWindow.mainloop()
	#start_new_thread(mainWindow.mainloop, ())