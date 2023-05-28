import slixmpp

class Messenger(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.start)

    def start(self, event):
        self.send_presence()
        self.get_roster()
        self.disconnect()

    def send_my_message(self, recipient, message):
        self.send_message(mto=recipient, mbody=message, mtype='chat')


def sender_xmpp(jid, passw, recipient, mess):
    # xmpp = Messenger('tester@local.at', 'password')
    xmpp = Messenger(jid, passw)
    xmpp.connect()
    xmpp.send_my_message(recipient, mess)
    xmpp.process(forever=False)
