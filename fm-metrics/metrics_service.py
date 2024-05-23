from prometheus_client.twisted import MetricsResource

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.application import internet, service, strports
from twisted.web import server

import conf


def add_metrics_service(application):
    root = Resource()
    root.putChild(conf.METRICS_PATH, MetricsResource())
    site = Site(root)
    i = strports.service("tcp:{0}".format(conf.METRICS_PORT), site)

    sc = service.IServiceCollection(application)
    i.setServiceParent(sc)

    return sc
