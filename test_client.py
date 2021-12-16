from irc import IRC
from split_raw_message import split_raw_message

irc = IRC("irc.swiftirc.net", "#HereIsTheTestchannel", "TestBOT938")
irc.connect()

exit_trigger = False
message = ""

while not exit_trigger:

    response = irc.get_response()

    for line in response:

        message = split_raw_message(line)

        if message:
            print(message)
        else:
            continue

        # From this point, you have the headers and the body message

        sender_nickname = message["sender_nickname"]

        if message["body"].find("hello") == 0:
            print("I see an hello!")
            irc.send(f"Hello! {sender_nickname}\n")

        if message["body"].find("disconnect") == 0:
            print("I have to disconnect baby.")
            irc.disconnect()
            exit_trigger = True

# To test, send "hello" it should reply "Hello! (your nickname)"
# Send nothing it shouldn't act
# Send "disconnect" to disconnect the bot, it should have a default quit
# message
