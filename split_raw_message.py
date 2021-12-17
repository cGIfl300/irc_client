def split_raw_message(raw_message):
    """Split a raw message (ie.:
    :cGIfl301!~dragonfly@Swift-12B59164.w82-120.abo.wanadoo.fr
    PRIVMSG #HereIsTheTestChannel :hello)
    into an understandable object
    Restricted to PRIVMSG
    """
    # Split headers from body
    headers = raw_message[1 : raw_message.find(":", 1) - 1]
    body = raw_message[raw_message.find(":", 1) + 1 :]

    if "PRIVMSG" in headers:
        return {
            "type": "PRIVMSG",
            "headers": headers,
            "sender": headers.split()[0],
            "sender_nickname": headers.split()[0].split("!")[0],
            "sender_hostname": headers.split()[0].split("@")[1],
            "to": headers.split()[2],
            "body": body,
        }

    if "352" in headers:
        headers = headers.split()
        return {
            "type": "352",
            "headers": headers,
            "body": body,
            "sender": headers[0],
            "me": headers[2],
            "channel": headers[3],
            "username": headers[4],
            "hostname": headers[5],
            "nickname": headers[7],
            "tokens": headers[8],
            "description": body,
        }
    return None
