import socket
import sys
import time


class IRC:
    """A class to have an IRC Client
    server (string): Server Name ("XXX.XXX.XXX.XXX") # Can be an IP or an hostname
    port (int): 6667 by default, the port to connect to
    channel (string): channel name must start by # or ! or &
    botnick (string): the bot's nickname
    botnickpass (string): the bot's password, we use nickaserv, set to None if None
    """

    irc = socket.socket()

    def __init__(self, server, channel, botnick, port=6667, botnickpass=None):
        # Define the socket
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.channel = channel
        self.port = port
        self.botnick = botnick
        self.botnickpass = botnickpass
        self.first_ping = True
        self.has_joined = False

    def send(self, msg):
        # Transfer data
        self.irc.send(bytes(f"PRIVMSG {self.channel} {msg}\n", "UTF-8"))

    def connect(self):
        # Connect to the server
        print(f"Connecting to: {self.server}")
        self.irc.connect((self.server, self.port))

        # Perform user authentication
        self.irc.send(
            bytes(
                f"USER {self.botnick} {self.botnick} {self.botnick} :Hello From the World\n",
                "UTF-8",
            )
        )
        self.irc.send(bytes(f"NICK {self.botnick}\n", "UTF-8"))
        if self.botnickpass:
            self.irc.send(
                bytes(f"NICKSERV IDENTIFY {self.botnickpass}\n", "UTF-8")
            )

    def join(self):
        # Join the channel
        self.irc.send(bytes(f"JOIN {self.channel}\n", "UTF-8"))

    def get_response(self):
        time.sleep(1)
        # Get the response
        response = self.irc.recv(2040).decode("UTF-8")

        response = response.strip("\r")
        response = response.split("\n")

        for resp in response:
            if resp.find("PING") == 0:
                self.irc.send(
                    bytes("PONG " + resp[resp.find("PING") + 5 :], "UTF-8")
                )
                if self.first_ping:
                    self.first_ping = False
                    return response
                if not self.has_joined:
                    self.join()
        return response
