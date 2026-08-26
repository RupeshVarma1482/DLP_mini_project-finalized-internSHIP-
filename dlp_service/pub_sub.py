import queue

class Broker:
    def __init__(self):
        self.topics = {}
    def Publish(self, topic, message):
        if topic not in self.topics:
            return
        for ind_queue in self.topics[topic]:
            ind_queue.put(message)
    def Subscribe(self, topic):
        new_queue = queue.Queue()
        if topic not in self.topics:
        # if !(topic in self.topics):
            self.topics[topic] = []
        self.topics[topic].append(new_queue)
        return new_queue
    def request_topics(self):
        return self.topics

ins1 = Broker()

q1 = ins1.Subscribe(topic = "user_login")

ins1.Publish(topic = "user_login", message = "respective file is available")

present_topics = ins1.request_topics()
print(f"present_topics: {present_topics}")

print(f"subscriber1 queue: {q1.get()}")