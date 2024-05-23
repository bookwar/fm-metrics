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

You can edit conf.py or pass environment variables for common config options.

Supported variables are:

* `FM_UUID` - unique id of the application. If not set the random UUID
  string will be generated for every run of the application.
* `FM_PREFIX` - comma-separated list of prefixes for topics. Default:
  `org.centos.prod.ci,org.fedoraproject.prod.ci`
* `FM_URL` - AMQP endpoint. Default: Fedora Messaging Public broker.

Run
===

    FM_PREFIX=org.centos.prod.ci,org.fedoraproject.prod.ci PYTHONPATH=./fm-metrics twistd -n -y ./fm-metrics/app.py
