from masonite.controllers import Controller
import pusher
from pprint import pprint
import datetime
import json

class PusherController(Controller):

    def __init__(self):
        self.app_id='1175747'

    def text_sendPusherNotification(self):
        print('do something here')

        pusher_client = pusher.Pusher(
            app_id=self.app_id,
            key='1082958fa2c8f9f47aa2',
            secret='9c8a0fe23892937b97c4',
            cluster='eu',
            ssl=True)

        example = {
            'date': '2016-05-03',
            'account_id': '6n5qv9bh1bk7jfo4kc0j2noa5',
            'status': '200',
            'method': 'PUT',
            'endpoint': '/messages',
            'type': 'API Request',
            'time': '0.66',
            'sent': {"message_id": [
                "23k7cyy79qi8bdk0mknaxtkhl"
            ]}
        }
        pusher_client.trigger('my-channel', 'my-event', example)


    def sendPusherNotification(self, data):

        print("******* Send notification")

        pusher_client = pusher.Pusher(
            app_id='1175747',
            key='1082958fa2c8f9f47aa2',
            secret='9c8a0fe23892937b97c4',
            cluster='eu',
            ssl=True)

        # receivedSample = json.loads(data['received'])

        # if 'messages' in data['url']:
        #      top5 = receivedSample[:5]
        #      for item in top5:
        #          item['body'] = '_body_removed_by_demo_center_'

        example = {
                    'date': '2016-05-03',
                    # 'account_id': receivedSample[0]['account_id'],
                    'status_code': data['status'],
                    'method': data['method'],
                    'endpoint': data['url'],
                    'type':  data['type'],
                    'time': str(datetime.datetime.now()),
                    'duration':data['elapsed'],
                    'sent': {"message_id": ["23k7cyy79qi8bdk0mknaxtkhl"]},
                    # 'response': top5
            }

        pusher_client.trigger('my-channel', 'my-event', example)
