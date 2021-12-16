# An IRC Bot program to rules them all  
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
irc.disconnect()
```  

## Interacting with PRIVMSG  
Here is how to structure messages like:  
```python
{'headers': 'cGIfl301!~dragonfly@Swift-12B59164.w82-120.abo.wanadoo.fr PRIVMSG #HereIsTheTestChannel',
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
```  

# Copyright (C)

Copyright (C) 2021  cGIfl300 <cgifl300@cgifl300.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.