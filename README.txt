README

Using a simple JabberBot to accept and parse XMPP Messages
http://thp.io/2007/python-jabberbot/

Setup as defined, with a new XMPP account from http://xmpp.net/

This will wait for messages from authorized XMPP accounts, if they begin with 'barista' the 'barista_bot_control' python script will attempt to parse your directions and if they match the form defined, start/stop coffee.

Glass messages sent from https://autofrenchpress.appspot.com/ unable to figure out how to send messages back to Glass, so I'm sending emails to myself when coffee is started/stopped/ready.  Oodles of looping messages have been stopped.

Source code for Glass service at https://github.com/efinkg/autofrenchpress.