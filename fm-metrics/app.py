from twisted.application import service

from fm_service import add_fm_service
from metrics_service import add_metrics_service

application = service.Application("Main")

add_fm_service(application)
add_metrics_service(application)
