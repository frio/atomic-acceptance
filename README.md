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

Acceptance Testing
------------------
Somewhere further down the line, I'll start writing unit tests.  For now, there's
some (one) very broad acceptance tests, written using Python's [behave], an 
implementation of Cucumber.  Simply type

    behave

At your prompt (once you've setup the environment!) to run the acceptance tests.

[behave]: http://pythonhosted.org/behave/

Licensing
---------
Freely available for all and sundry under the MIT license!
