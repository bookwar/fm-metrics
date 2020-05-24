from prometheus_client import Counter


class Message:

    LABELS = [
        'topic',
        'testcase',
        'status',
        'result',
    ]
    
    def __init__(self, message):
        self.topic = message.topic
        
        if "test" in message.body:
            self.testcase = ".".join([
                message.body["test"]["namespace"],
                message.body["test"]["category"],
                message.body["test"]["type"],
            ])
            self.result = message.body["test"].get("result", "undefined")
        else:
            self.testcase = "undefined"
            self.result = "undefined"

        self.status = message.topic.split(".")[-1]
            
    def labels(self):
        return { label: self.__getattribute__(label) for label in self.LABELS}


MessageCounter = Counter(
    'messages',
    'Count messages',
    Message.LABELS,
)

def count_message(message):
    m = Message(message)
    MessageCounter.labels(**m.labels()).inc()

