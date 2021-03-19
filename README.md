Twisted App to count messages in Fedora Message bus
---------------------------------------------------

Dependencies
============

    dnf install \
	    fedora-messaging \
		python3-fedora-messaging \
		python3-twisted \
		python3-prometheus_client

Configuration
=============

    cp local_conf.py.example local_conf.py
	
Edit as needed.

Run
===

    PYTHONPATH=. twistd -n -y app.py
