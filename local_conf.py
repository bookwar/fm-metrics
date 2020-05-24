AMQP_URL = "amqps://fedora:@rabbitmq.fedoraproject.org/%2Fpublic_pubsub" 

UUID = "989139bf-69ec-437c-8dfa-05d2d07a72de"

QUEUES = {
    UUID: {
        'durable': False,
        'auto_delete': False,
        'exclusive': False,
        'arguments': {},
    },
}

BINDINGS = [
    {
    'exchange': 'amq.topic',
    'queue': UUID,  
    'routing_keys': ['org.centos.prod.ci.#','org.fedoraproject.prod.ci.#'],
    },
]

METRICS_PATH = b"metrics"
METRICS_PORT = "8080"
