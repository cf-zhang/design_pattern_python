#! /usr/bin/python

import logging
from collections import defaultdict

class Broker:
    """Message Broker / Middle-ware that hosts the message queue and is responsible for making communication possible \
    between publishers and subscribers, without them knowing about each other"""

    def __init__(self):
        """Initializes the Message Queue broker with an empty resource set - message queue and subscriber/topic mapping.
           This will happen only once in time (hopefully) when the message queue is first started and should run continually"""

        self.messaging_queue = []
        self.topic_subscription_mapping = defaultdict(lambda:[])


    def run_loop(self):
        """This is the main code in the broker which always runs until message queue has more messages to pass\
        else, it waits for any more messages. """

        for message in self.messaging_queue:
            message, topic = self.process_message(message)
            subscribers = self.get_subscribers_for_topic(topic)
            self.push_message_to_subscribers(subscribers, message)


    def on_message(self, message):
        """This is like an event that will be fired on receipt of a new message by the broker, but is implemented\
         as a method in current context of non-network based implementation. Drops message if message is lacking a topic"""

        if len(message.split(";")) >= 2:
            self.messaging_queue.append(message)
            logger.info("Message received by queue :  " + message)
        else:
            pass


    def process_message(self, message):
        """Cleans the messages received by the broker from the publishers."""

        message_parts = message.split(";")
        return message_parts[0], message_parts[1]


    def get_subscribers_for_topic(self, topic):
        """This method in the broker gets the mapping of subscribers to a given topic"""

        subscribers = self.topic_subscription_mapping[topic]
        return subscribers


    def push_message_to_subscribers(self, subscribers, message):
        """This is like a method implemented using a socket for sending the information/messages to subscribers using ther addresses\
        but is like a method called on their instance in this case."""

        for subscriber in subscribers:
            subscriber.on_message(message)


    def subscribe_to_topic(self, subscriber, topic):
        """Populates the mapping of subcribers to topics"""

        self.topic_subscription_mapping[topic].append(subscriber)


    def topic_data(self, subscriber, topic):
        """Aggregates messages on a given topic, upon request of a subscriber and prepares it for sending"""

        messages_for_topic = [self.process_message(message)[0] for message in self.messaging_queue if self.process_message(message)[1] == topic]
        message_aggregator = ""
        for message in messages_for_topic:
            message_aggregator += message + "..."
        self.push_message_to_subscribers([subscriber], message_aggregator)



class Publisher:
    """Publisher that publishes topic wise content into the message broker"""

    def __init__(self, name, broker):
        """Initializes a publisher and provide it the details of broker to send its topic based messages to"""

        self.name = name
        self._Broker = broker


    def publish(self, message, topic):
        """Method used by publishers to publish a message on a topic to subscribers via message broker"""

        _message = message + ";" + topic
        logger.info(self.name + "  , Publishing a message : " + message + " in topic :  " + topic)
        self._Broker.on_message(_message)



class Subscriber:
    """Subscriber that subscribes to topics with the broker"""

    def __init__(self, name, broker):
        """Initializes the subscriber and provides it the broker details to subscribe to"""

        self.name = name
        self._Broker = broker


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

        logger.info(self.name + "  , Received a message : " + message)


def main():
    """ A scenario is played in the main method to test/exemplify the working of this implementation.
    Logs are written to a separate file upon executing this code named, pub_sub.log using logger module in python"""

    logger.info("Starting Message Broker Service")

    broker = Broker()

    s1 = Subscriber("subscriber 1", broker)
    s2 = Subscriber("subscriber 2", broker)
    s3 = Subscriber("subscriber 3", broker)
    p1 = Publisher("publisher 1", broker)
    p2 = Publisher("publisher 2", broker)

    s1.subscribe("Sports")
    s1.subscribe("Politics")
    s2.subscribe("Sports")
    s2.subscribe("Politics")
    s3.subscribe("Politics")

    p1.publish("Message 1", "Politics")
    p1.publish("Message 2", "Sports")
    p1.publish("Message 4", "Politics")
    p1.publish("Message 5", "Politics")
    p1.publish("Message 7", "Politics")

    broker.run_loop()

    s3.get_topic_data("Politics")

    logger.info("Ending Message Broker Service")


if __name__ == "__main__":
    # Setting logging parameters to record log in a given file in same directory as main file with INFO level

    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('../testprj/pub_sub.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    main()