from irc import IRC

irc = IRC("irc.swiftirc.net", "#HereIsTheTestchannel", "TestBOT938")
irc.connect()

exit_trigger = False

while not exit_trigger:
    response = irc.get_response()
    for line in response:
        print(line)

        if "PRIVMSG" in line:
            if "hello" in line:
                print("I see an hello!")
                irc.send("Hello!\n")
            if "disconnect" in line:
                print("I have to disconnect baby.")
                irc.disconnect()
                exit_trigger = True

# To test, send "hello" it should reply "Hello!"
# Send nothing it shouldn't act
# Send "disconnect" to disconnect the bot, it should have a default quit message
