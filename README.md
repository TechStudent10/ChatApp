# ChatApp

 A chat application using my Client and Server repo.

---

To use, run the `server.py` file on the machine you want to run it on. Then open `client.py`  and modify this line: `self.client = Client(socket.gethostbyname(socket.gethostname()))` to say `self.client = Client("YOUR IPV4 ADDRESS")` "YOUR IPV4 ADDRESS" is your IPV4 address. You can find it by opening the Command Prompt, Powershell or Terminal etc and typing (on Windows) `ipconfig` or (on Mac) `ifconfig` and finding IPV4 or your network adapter. Linux users, I hope you know how to do this. You can leave this the same if you are running this on the same machine. Now just run the `client.py` file and you are good to go!
