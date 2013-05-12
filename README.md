Atomic
======
Atomic is a househould reactor; (the beginning of!) a project to automate my 
flat.  Currently, it provides an interface for sending wake-on-lan (WOL) 
packets; the idea being externally-driven events (say, a smartphone entering 
home wifi range) can wake up our computers.

Over time, this will evolve to incorporate control of LimitlessLED bulbs, access
to various sensors, etc.

You Will Need
-------------
Python, pip, and virtualenv.  Using

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Will get a development/deployment environment running.  Better packaging support
will come along as the project evolves (pull requests welcome!).

Licensing
---------
Freely available for all and sundry under the MIT license!
