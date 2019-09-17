import jwt
import json
from datetime import datetime
from datetime import timedelta

__payload_json_file = 'payload.json'
__private_key_file = './keys/private_key.pem'
__public_key_file = './keys/public_key.pem'
__expiration_time_hours = 24
__algorithm = 'RS256'

def get_expiration_timestamp(hours):
    now = datetime.now()
    expiration = now + timedelta(hours=hours)
    print("Token will expire at: ", expiration.strftime("%d/%m/%Y, %H:%M:%S"))
    return (datetime.timestamp(now), datetime.timestamp(expiration))

def get_key_pair():

    private_key_file = open(__private_key_file, 'rb')
    public_key_file = open(__public_key_file, 'rb')

    private_key = private_key_file.read()
    public_key = public_key_file.read()

    return (private_key, public_key)

def get_payload(exp, iat):
    json_file = open(__payload_json_file, 'r').read()
    payload = json.loads(json_file)
    payload['exp'] = exp
    payload['iat'] = iat
    return payload

if __name__ == "__main__":

    (iat, exp) = get_expiration_timestamp(__expiration_time_hours)

    (private_key, public_key) = get_key_pair()

    payload = get_payload(exp, iat)

    encoded = jwt.encode(
        payload,
        private_key,
        algorithm=__algorithm)

    print('JWT ------------------------------------------')
    print(encoded.decode('utf-8'))
    print('/JWT ------------------------------------------')

    decoded = jwt.decode(encoded, public_key, algorithms=__algorithm)

    print("Chack: ", "VALID" if decoded==payload else "INVALID")

