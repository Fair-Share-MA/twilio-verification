from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "SID"
# Your Auth Token from twilio.com/console
auth_token  = "TOK"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(account_sid, auth_token)

numbers_to_check = [
    "6178755972",
    "7814920782",
    "8579288028",
    "7816356795",
    "6174070081",
    "4134279835",
    "5087379061",
    "6176800409",
    "8572417211",
    "7818445964",
    "7815451891",
    "7819855848",
    "6172884038",
    "6175967344",
    "6175227983",
    "6172882520"
]

for idx, num in enumerate(numbers_to_check):
    phone_number = client.lookups.phone_numbers('+1' + num).fetch(type='carrier')
    print("Type: ", phone_number.carrier['type'])