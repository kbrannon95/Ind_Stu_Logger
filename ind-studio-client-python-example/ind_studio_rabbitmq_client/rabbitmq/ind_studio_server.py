import json
import zlib
import time

from ind_studio_rabbitmq_client.app_config import rabbitmq_settings
from ind_studio_rabbitmq_client import logger
from ind_studio_rabbitmq_client.rabbitmq.rabbit_mq_connection import RabbitMQConsumer

log = logger.get_module_logger(__name__)

def on_request(ch, method, props, body):
    try:
        log.info("Length [{}] bytes".format(len(body)))

        # decompress from gzip
        body_data = zlib.decompress(body, zlib.MAX_WBITS | 32)

        log.info("Body [{}]".format(body_data))
        json_body = json.loads(body_data)

        #iterate tags and print data
        for tag in json_body:
            log.info("Name:" + tag["Name"] + " Quality: " + str(tag["Quality"]) + " Timestamp: " + tag["Timestamp"] + " Value: " + str(tag["Value"]))

    except Exception as ex:
        log.error(ex)


def start():
    # for ever loop to keep connection alive and queue created.
    while True:
        # create connection instance
        rabbit_mq_consumer = RabbitMQConsumer(rabbitmq_settings["RABBITMQ_SERVER"])
        try:
            rabbit_mq_consumer._process_message_callback = on_request
            rabbit_mq_consumer.run()

        except KeyboardInterrupt:
            rabbit_mq_consumer.stop()
            break

        except Exception as e:
            log.error(e)
            retry_in = 10
            log.info("Retry RabbitMQ connection in {0} Seconds...".format(retry_in))
            time.sleep(retry_in)
