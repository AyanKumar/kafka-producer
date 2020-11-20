#Import the flask module
from flask import  Flask, request, render_template
from kafka import KafkaConsumer, KafkaProducer
import os


#Create a Flask constructor. It takes name of the current module as the argument
app = Flask(__name__)

#Create a route decorator to tell the application, which URL should be called for the #described function and define the function

@app.route('/', methods =["GET", "POST"])
def send_message():
    if request.method == "POST":
        #return "Hello World"
        topic_name = request.form.get("topic")
        message = request.form.get("message")
        kafka_producer= connect_kafka_producer()
        publish_message(kafka_producer, topic_name, 'raw', message.strip())
        if kafka_producer is not None:
            kafka_producer.close()
        return "Message Published"
    return render_template("index.html")


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))

def connect_kafka_producer():
    _producer = None
    kafkaCluster = os.getenv("KafkaCluster", "localhost:9092")
    print(kafkaCluster)
    try:
        _producer = KafkaProducer(bootstrap_servers=[kafkaCluster], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

#Create the main driver function
if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)