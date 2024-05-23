from fedora_messaging.message import Message
from prometheus_client import Counter
import logging

logger = logging.getLogger(__name__)


COUNTERS_DATA = [
    {
        'topic': 'org.fedoraproject.prod.buildsys.tag',
        'name': 'fedora_tag',
        'description': "Count Fedora tag messages",
        'labels': ['tag'],
     },
    {
        'topic': 'org.centos.prod.buildsys.tag',
        'name': 'centos_tag',
        'description': "Count CentOS tag messages",
        'labels': ['tag'],
    },
    {
        'topic': 'DEFAULT',
        'name': 'simple',
        'description': "Count all messages",
        'labels': ['topic'],
    },
]


class CounterRegistry:

    def __init__(self, counters_data=[]):
        self.counters={}

        for counter_data in counters_data:
            self.add_counter(**counter_data)

    def add_counter(self, name, description, topic, labels):
        if topic in self.counters:
            logger.warning("Counter for {topic} already exists")
            return self.counters[topic]

        counter = Counter(
            name,
            description,
            labels,
        )

        self.counters[topic] = counter
        return counter

    def get_counter(self, topic):
        if topic in self.counters:
            return self.counters[topic]
        else:
            return self.counters['DEFAULT']

CR = CounterRegistry(COUNTERS_DATA)


def get_labels(message, labels):
    result = {}
    for label in labels:
        result[label] = getattr(message,
                                label,
                                message.body.get(label,
                                                 message._headers.get(label, "")
                                                 )
                                )
    return result

def count_message(message):
    message_counter = CR.get_counter(message.topic)
    message_labels = get_labels(message, message_counter._labelnames)
    message_counter.labels(**message_labels).inc()
