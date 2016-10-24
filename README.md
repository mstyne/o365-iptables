# o365-iptables

Microsoft publishes its IP address listings for various services here:

https://support.content.office.net/en-us/static/O365IPAddresses.xml

Using this list, I can generate iptables firewall rules to only allow incoming SMTP traffic from Microsoft, and hopefully keep my ruleset updated automatically when they change things.

I'm using the XPath support in xml.etree.ElementTree, and I experimented until I got what I wanted, so it's possible there's a better way.

I wrote this (badly?) in Python because hey, who doesn't want to learn how to mangle XML in another language?
