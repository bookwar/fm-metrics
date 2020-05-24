from fedora_messaging.twisted.service import FedoraMessagingServiceV2 as FMService

import local_conf
from count import count_message


def main_callback(message):
    """
    Main callback for the message queue.

    Counts every incoming message.

    Args:
        message (fedora_messaging.message.Message): The message we received
            from the queue.
    """

    count_message(message)

def add_fm_service(application):
    fm_service = FMService(local_conf.AMQP_URL)
    fm_service._service.factory.consume(
        callback=main_callback,
        queues=local_conf.QUEUES,
        bindings=local_conf.BINDINGS,
    )

    fm_service.setServiceParent(application)
    return fm_service
