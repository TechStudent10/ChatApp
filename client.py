from tkinter import *
from BasicServerAndClient.client import Client

class MainWindow(Tk):
	def __init__(self):
		super().__init__()

if __name__ == "__main__":
	mainWindow = MainWindow()
	mainWindow.title("Chat Application")
	mainWindow.mainloop()