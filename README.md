# flights_search
Flights search project.

Data Manager:
+ requests data (list of cities user plans to visit plus price estimate) from google sheet: https://docs.google.com/spreadsheets/d/1PHK6ZcyhNZz6wRB8OFCuECmTgB1uLuqbhPm9tz5M-so/edit#gid=0 using Sheety API 
+ Add IATA code to the sheet if code is missing (using KIWI/TEQUILA API)

Flight Search:
+ using data from above mentioned google sheet requests flights data (like lowest price on some dates from required date range) using KIWI/TEQUILA API
+ put it into FlightData object

Notification Manager
+ Sends sms to MY_NUMBER using Twilio API if available price is lower than price in the google sheet

APIs links:
+ https://tequila.kiwi.com/portal/docs/user_guides/booking_api__general_information_
+ https://sheety.co/
+ https://www.twilio.com/docs/sms/quickstart/python
