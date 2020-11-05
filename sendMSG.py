import os
from twilio.rest import Client


account_sid = 'AC00e211082338ead72dccd7e6000ddf71'
auth_token = '38f34d1369134e525af14b6b609555cc'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Se esta lendo isso é porque deu certo, mas nao me responde, prefiro o telegram!',
    from_='whatsapp:+14155238886',
    to='whatsapp:+5541995062619')


print(message.sid)
print(message)

