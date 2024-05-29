import time 

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-e8d6e75d-ef65-4d01-b9be-7711183b8704'
pnconfig.publish_key = 'pub-c-8fd736cc-2965-49d7-a92c-a48428520696'
pnconfig.user_id = 'test_user'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())

def main():
    time.sleep(1)

    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()

if __name__ == '__main__':
    main()