from collections import defaultdict, deque
import threading

class Message:
    def __init__(self, message, name):
        self.message = message
        self.name = name

class S1Message:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __str__(self):
        return str(self.a) + ' ' +str(self.b)

class S2Message:
    def __init__(self):
        self.c = '3'
        self.d = '4'

    def __str__(self):
        return self.c + ' ' + self.d




class Broker:
    def __init__(self):
        self.message_queue = deque(maxlen=200)
        self.topic_subscription_mapping = defaultdict(lambda: [])

    def process_message(self, message):
        return message.message, message.name

    def on_message(self, message):
        if isinstance(message, Message):
            self.message_queue.append(message)
        else:
            pass

    def get_subscribers_for_topic(self, topic: 'str'):
        subscribers = self.topic_subscription_mapping[topic]
        return subscribers

    def push_message_to_subscribers(self, subcribers, message):
        for subcriber in subcribers:
            subcriber.on_message(message)

    def run_loop(self):
        while True:
            if len(self.message_queue) > 1:
                message = self.message_queue.pop()
                message, topic = self.process_message(message)
                subscribers = self.get_subscribers_for_topic(topic)
                self.push_message_to_subscribers(subscribers, message)


    def subscribe_to_topic(self, subscriber, topic):
        self.topic_subscription_mapping[topic].append(subscriber)


    def topic_data(self, subscriber, topic):
        message_for_topic = [self.process_message(message)[0] for message in self.message_queue if
                         self.process_message(message)[1] == topic]
        message_aggregator = ''
        for message in message_for_topic:
            message_aggregator += message + '...'
        self.push_message_to_subscribers([subscriber], message_aggregator)


broker = Broker()


class Publisher:
    """Publisher that publishes topic wise content into the message broker"""

    def __init__(self, name):
        """Initializes a publisher and provide it the details of broker to send its topic based messages to"""
        global broker
        self.name = name
        self._Broker = broker

    def publish(self, message, topic):
        """Method used by publishers to publish a message on a topic to subscribers via message broker"""

        _message = Message(message,topic)
        print(self.name + "  , Publishing a message : " + str(message) + " in topic :  " + topic)
        self._Broker.on_message(_message)


class Subscriber:
    """Subscriber that subscribes to topics with the broker"""

    def __init__(self, name):
        """Initializes the subscriber and provides it the broker details to subscribe to"""

        global broker
        self.name = name
        self._Broker = broker
        self.count = 0

    def subscribe(self, topic):
        """Method used by the subscriber to subscribe to the message queue with a given topic to receive updates on it later
           This is actually supposed to be a network call to the broker IP, with a request to update this particular subscriber"""

        self._Broker.subscribe_to_topic(self, topic)

    def get_topic_data(self, topic):
        """Method used by subscriber to request all data/messages on a given topic at once. This is again supposed to be a network call"""

        self._Broker.topic_data(self, topic)

    def on_message(self, message):
        """On the subscriber node, this is a call-back event fired on receipt of a message on some port but in this implementation,
        it is like a function call on the given subscriber instance"""
        self.count += 1
        if isinstance(message, S1Message):
            print (self.name + 'count : '+str(self.count))
            print(self.name + "  , Received a message : " + str(message))

import time

def pub1():
    p1 = Publisher('publisher 1')
    cnt = 0
    while True:
        p1.publish(S2Message(), 'S2')
        time.sleep(4)
        p1.publish(S1Message(), 'S1')
        time.sleep(3)
        cnt += 1


def pub2():
    p2 = Publisher('publisher 2')
    cnt = 0
    while True:
        p2.publish(S1Message(), 'S1')
        time.sleep(2)
        p2.publish(S2Message(), 'S2')
        time.sleep(1)
        cnt += 1


def main():
    """ A scenario is played in the main method to test/exemplify the working of this implementation.
    Logs are written to a separate file upon executing this code named, pub_sub.log using logger module in python"""
    global broker
    print("Starting Message Broker Service")

    process = []
    # p1 = multiprocessing.Process(target=sub1)
    # process.append(p1)
    #
    # p2 = multiprocessing.Process(target=sub2)
    # process.append(p2)
    #
    # p3 = multiprocessing.Process(target=sub3)
    # process.append(p3)
    s1 = Subscriber('subscriber 1')
    s1.subscribe('S1')
    s2 = Subscriber('subscriber 2')
    s2.subscribe('S2')
    s3 = Subscriber('subscriber 3')
    s3.subscribe('S3')

    # p4 = multiprocessing.Process(target=pub1)
    p4 = threading.Thread(target=pub1)
    process.append(p4)

    # p5 = multiprocessing.Process(target=pub2)
    p5 = threading.Thread(target=pub2)
    process.append(p5)

    for proces in process:
        proces.start()
    broker.run_loop()

    for pr in process:
        pr.join()


if __name__ == "__main__":
    main()
