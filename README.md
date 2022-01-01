# An IRC Bot program to rule them all

I wrote this little software because I needed an IRC bot for #chilling-coding,
here is the basic bot, you can extend or adapt to any need.  
Enjoy!

# Documentation

Here is the technical documentation, this is a pure python bot.

## Connect your bot

```python
from irc import IRC

irc = IRC("irc.swiftirc.net", "#FreshChat", "TestBOT938")
irc.connect()
```  

## Disconnect your bot

```python
from irc import IRC

irc = IRC("irc.swiftirc.net", "#FreshChat", "TestBOT938")
irc.disconnect()
```  

## Update the users list

```python
from irc import IRC

irc = IRC("irc.swiftirc.net", "#FreshChat", "TestBOT938")
irc.get_users_list()

# The users list is now accessible over self.users_list[]
```  

### The user object

An object from self.users_list[] has these attributes:

```python
return {
    "type": "352",  # Object type
    "headers": headers,  # raw headers
    "body": body,  # raw body
    "sender": headers[0],  # the server who sent the message
    "me": headers[2],  # your nickname
    "channel": headers[3],  # the channel where the user is
    "username": headers[4],  # user's username
    "hostname": headers[5],  # user's hostname
    "nickname": headers[7],  # user's nickname
    "tokens": headers[8],  # user's token
    "is_registered": False, # is the user registered
    "description": body,  # user's description
}
```

## Interacting with PRIVMSG

Here is how to structure messages like:

```python
{
    'headers': 'cGIfl301!~dragonfly@Swift-12B59164.w82-120.abo.wanadoo.fr PRIVMSG #HereIsTheTestChannel',
    'sender': 'cGIfl301!~dragonfly@Swift-12B59164.w82-120.abo.wanadoo.fr',
    'sender_nickname': 'cGIfl301',
    'sender_hostname': 'Swift-12B59164.w82-120.abo.wanadoo.fr',
    'to': '#HereIsTheTestChannel',
    'body': 'hello\r'}
```  

You can use the __split_new_raw(line)__ function this way:

```python
from irc import IRC
from split_raw_message import split_raw_message

irc = IRC("irc.swiftirc.net", "#HereIsTheTestchannel", "TestBOT938")
irc.connect()

exit_trigger = False
message = ""

while not exit_trigger:

    response = irc.get_response()

    for line in response:

        # print(f"RAW: {line}")

        message = split_raw_message(line)

        if message is None:
            continue

        # From this point, you have the headers and the body message

        if message["type"] == "352":
            irc.users_list.append(message)

        if message["type"] == "PRIVMSG":
            sender_nickname = message["sender_nickname"]

            if message["body"].find("hello") == 0:
                print("I see an hello!")
                irc.send(f"Hello! {sender_nickname}\n")

            if message["body"].find("disconnect") == 0:
                print("I have to disconnect baby.")
                irc.disconnect()
                exit_trigger = True

            if message["body"].find("get_users_list") == 0:
                print("Time has come to get the list of users.")
                irc.users_list = []
                irc.get_users_list()
```  

# Copyright (C)

Copyright (C) 2021 - 2022 cGIfl300 <cgifl300@cgifl300.com>

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.