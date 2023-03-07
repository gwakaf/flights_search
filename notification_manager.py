import os
from twilio.rest import Client

# TWILIO_SID = "AC3d3ce1a117e4b6baaa72c0e22fc26019"
# TWILIO_AUTH_TOKEN = "16b746d0dc0f47ae6914c8706e2be68c"
# TWILIO_VIRTUAL_NUMBER = "+13853964657"
# MY_NUMBER = "+19254485075"
twilio_sid = os.environ.get("TWILIO_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_virtual_number = os.environ.get("TWILIO_VIRTUAL_NUMBER")
my_number = os.environ.get("MY_NUMBER")

class NotificationManager:
    def __init__(self):
        self.client = Client(twilio_sid, twilio_auth_token)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_virtual_number,
            to=my_number
        )
        print(message.sid)