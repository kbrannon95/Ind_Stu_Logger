import threading
import sys

from ind_studio_rabbitmq_client.rabbitmq import ind_studio_server
from ind_studio_rabbitmq_client import logger

if __name__ == "__main__":

    # Set UTF-8 as default encoding
    reload(sys)
    sys.setdefaultencoding('utf8')

    # Every module should call this to initiate log
    log = logger.get_module_logger(__name__)
    log.info('ANT Automation - Industrial Studio RabbitMQ client')


    # Wait threads
    rpc_thread = None

    # RabbitMQ server startup
    rpc_thread = threading.Thread(name='rabbitmq_srv', target=ind_studio_server.start)
    rpc_thread.start()
    rpc_thread.join()
