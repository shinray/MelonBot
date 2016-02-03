import socket
import time #apparently sleep() isn't defined

#variables
#NICK = "shinray_"
NICK = "shinray"
#PASS = "oauth:wz4y8oo998go6vq71rqzpcm8b0kmzz"
PASS = "oauth:5nbnxz8uog825p6j5rlvcq3zmzjur4"
HOST = "irc.twitch.tv"
PORT = 6667
CHAN = "#shinray"

def chat(sock, msg):
	sock.send("PRIVMSG {} :{}\r\n".format(CHAN,msg))

#open socket
s = socket.socket()

#connect
s.connect((HOST, PORT))

s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

noodles = 0
print("connected")
#s.send("PRIVMSG #shinray :{}\r\n".format("MrDestructoid BOT ONLINE MrDestructoid").encode("utf-8"))
chat(s, "MrDestructoid BOT ONLINE MrDestructoid")

#main loop
while True:
	response = s.recv(1024).decode("utf-8")

	#ping-pong
	if response == "PING :tmi.twitch.tv\r\n":
		s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
		chat(s,"pong")
	elif "!test" in response:
		print("received !test")
		#s.send("PRIVMSG #shinray :toast\r\n".encode("utf-8"))
		chat(s,"toast")
	elif "!noodles" in response:
		print("kicking hingle")
		s.send("PRIVMSG #shinray :.timeout hinglehingle 1\r\n".encode("utf-8"))
	elif "!secret" in response:
		noodles += 1000
	elif "!allen" in response:
		s.send("PRIVMSG #shinray :allenmelon has -{} noodles\r\n".format(noodles).encode("utf-8"))
	else:
		#print(response)
		pass
	print(response)
	time.sleep(0.1)

