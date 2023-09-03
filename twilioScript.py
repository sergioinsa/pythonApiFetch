from twilio.rest import Client

from api_clima import *
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER


account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)
PHONE_TO_SEND = '' # completar con el número a enviar.

message = client.messages.create(
    body='Pronóstico de hoy ' + forecastday['date'] + ' -Condición: ' + condicion + ' -Máxima: ' +
    str(max_temp) + ' -Mínima: ' + str(min_temp) + '.' + '-------------' 'Pronóstico de Lluvia -> ' + str(df_rain),
    from_=PHONE_NUMBER,
    to=PHONE_TO_SEND
)

print(f"mensaje enviado {message.sid}")
