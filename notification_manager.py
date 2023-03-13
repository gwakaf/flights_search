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
    # TODO: implement email sending method
    # def send_emails(self, emails, message, google_flight_link):
    #     with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_PASSWORD)
    #         for email in emails:
    #             connection.sendmail(
    #                 from_addr=MY_EMAIL,
    #                 to_addrs=email,
    #                 msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
    #             )