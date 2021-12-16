def split_raw_message(raw_message):
    """Split a raw message (ie.:
    :cGIfl301!~dragonfly@Swift-12B59164.w82-120.abo.wanadoo.fr
    PRIVMSG #HereIsTheTestChannel :hello)
    into an understandable object
    Restricted to PRIVMSG
    """
    raw_message = str(raw_message)
    # Split headers from body
    headers = raw_message[1 : raw_message.find(":", 1) - 1]
    body = raw_message[raw_message.find(":", 1) + 1 :]
    if "PRIVMSG" in headers:
        return {
            "headers": headers,
            "sender": headers.split()[0],
            "sender_nickname": headers.split()[0].split("!")[0],
            "sender_hostname": headers.split()[0].split("@")[1],
            "to": headers.split()[2],
            "body": body,
        }
    return None
