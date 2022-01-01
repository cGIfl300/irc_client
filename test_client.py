from irc import IRC
from split_raw_message import split_raw_message

irc = IRC("server", "#channel", "bot_name")
irc.connect()

exit_trigger = False
message = ""
fortune = ""
secure_nick = "cGIfl301"
tmp_nickname = ""

while not exit_trigger:

    response = irc.get_response()

    for line in response:
        message = split_raw_message(line)

        if message is None:
            continue

        # From this point, you have the headers and the body message

        if message["type"] == "352":
            irc.users_list.append(message)
            tmp_nickname = message["nickname"]
            irc.irc.send(bytes(f"WHOIS {tmp_nickname}\n", "UTF-8"))

        if message["type"] == "307":
            irc.is_registered(message["nickname"])

        if message["type"] == "315":
            print("Users list completed.")
            irc.users_list_completed = True
            continue

        if message["type"] == "PRIVMSG":
            sender_nickname = message["sender_nickname"]
        else:
            continue

        if message["body"].find("$version") == 0:
            irc.send(
                "I am a bot, based on https://github.com/cGIfl300/irc_client .")

        if message["body"].find("$help") == 0:
            irc.send("Available: hello, cookie, disconnect")

        if message["body"].find("$hello") == 0:
            print("I see an hello!")
            irc.send(f"Hello! {sender_nickname}")

        if not message["sender_nickname"] == secure_nick:
            continue

        # These commands are restricted to the secure_nick

        if message["body"].find("$disconnect") == 0:
            print("I have to disconnect baby.")
            irc.disconnect()
            exit_trigger = True

        if message["body"].find("$get_users_list") == 0:
            print("Time has come to get the list of users.")
            irc.users_list_completed = False
            irc.users_list = []
            irc.get_users_list()
