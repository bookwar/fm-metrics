from fedora_messaging.twisted.service import FedoraMessagingServiceV2 as FMService

from callback import main_callback
import local_conf

def add_fm_service(application):
    fm_service = FMService(local_conf.AMQP_URL)
    fm_service._service.factory.consume(
        callback=main_callback,
        queues=local_conf.QUEUES,
        bindings=local_conf.BINDINGS,
    )

    fm_service.setServiceParent(application)
    return fm_service
