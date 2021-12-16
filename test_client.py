from irc import IRC

irc = IRC("irc.swiftirc.net", "#FreshChat", "TestBOT938")
irc.connect()

while True:
    response = irc.get_response()
    for line in response:
        print(line)
        if "PRIVMSG" in line and irc.channel in line and "hello" in line:
            irc.send("Hello!")
