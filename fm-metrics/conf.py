import uuid
import logging
from os import environ as env

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Queue id
UUID = env.get("FM_UUID", str(uuid.uuid4()))

# Public endpoint
AMQP_URL = env.get(
    "FM_URL", "amqps://fedora:@rabbitmq.fedoraproject.org/%2Fpublic_pubsub"
)

# Topics

TOPICS = []

prefixes = env.get("FM_PREFIX", "org.centos.prod.ci,org.fedoraproject.prod.ci").split(
    ","
)
for prefix in prefixes:
    TOPICS.append(f"{prefix}.#")

logger.info(
    f"Start listening for topics: {TOPICS} on endpoint {AMQP_URL} using UUID {UUID}"
)

# Metrics will be exposed on http://localhost:METRICS_PORT/METRICS_PATH
METRICS_PATH = b"metrics"
METRICS_PORT = "8080"

QUEUES = {
    UUID: {
        "durable": False,
        "auto_delete": False,
        "exclusive": False,
        "arguments": {},
    },
}

BINDINGS = [
    {
        "exchange": "amq.topic",
        "queue": UUID,
        "routing_keys": TOPICS,
    },
]
