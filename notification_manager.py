import os
from twilio.rest import Client

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