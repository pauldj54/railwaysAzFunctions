import logging

import azure.functions as func


def main(event: func.EventHubEvent, msg: func.Out[func.QueueMessage]):
    body = event.get_body().decode('utf-8')

    if body != '':
        msg.set(body)
        logging.info('Python EventHub trigger processed an event: %s', body)
    else:
        logging.info('Python EventHub trigger error')



    
    
