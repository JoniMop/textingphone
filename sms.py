from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = TwilioRestClient(account_sid, auth_token)

my_msg = "".join(["Texting!!!\n" for i in range(10)])

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
