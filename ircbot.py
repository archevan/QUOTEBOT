"""
       Book Quote
         IRC BOT                             
  Created By: Evan Seils

"""
import socket
import quotes
import book
import password

server = "irc.freenode.net"
#server = "irc.snoonet.org"
port = 6667
botnick = "BOOKQUOTEBOT"
channel = "#books"

#basic irc functionality
def joinChannel(c):
	s.send("JOIN " + c + "\n")
def sendMessage(c, msg):
	s.send("PRIVMSG " + c + " :" + msg + "\n")
def hello(c):
	s.send("PRIVMSG " + c + " :Hey!\n")
def pong():
	s.send("PONG :pong\n")
def sendQuote(c):
	quote = quotes.newQuote()
	s.send("PRIVMSG "+c+" :"+quote+"\n")
def recommendBook(c):
	goodbook = book.newBook()
	s.send("PRIVMSG "+c+" :You should try "+goodbook+"\n")

#init new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to freenode
s.connect((server, port))
#user auth
s.send("USER " + botnick + " " + botnick + " " + botnick + " :This is a quote bot that gives famous bookquotes\n")
#set nickname for bot
s.send("NICK " + botnick + "\n")
#more auth
s.send("PRIVMSG NickServ :identify "+password.password+"\n")
#join
joinChannel(channel)

#check for response and commands
while True:
	chatdata = s.recv(2048)
	#remove junk
	chatdata = chatdata.strip('\n\r')
	print chatdata
	if chatdata.find("PING :") != -1:
		pong()
	if chatdata.find(":Hello " + botnick) != -1:
		hello(channel)
	if chatdata.find(":!help") != -1:
		sendMessage(channel, "Commands:\n")
		sendMessage(channel, "!quote\n")
		sendMessage(channel, "!help\n")
	if chatdata.find(':!quote') != -1:
		sendQuote(channel)
	if chatdata.find(":!recommend") != -1:
		recommendBook(channel)






