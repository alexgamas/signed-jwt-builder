import jwt
import json
import os.path
import pprint

from datetime import datetime
from datetime import timedelta

# pretty printer
__pp = pprint.PrettyPrinter(indent=4)

__payload_json_file = 'payload.json'
__private_key_file = './keys/private_key.pem'
__public_key_file = './keys/public_key.pem'
__expiration_time_hours = 240
__algorithm = 'RS256'


def pp(obj):
    __pp.pprint(obj)

def get_expiration_timestamp(hours):
    now = datetime.now()
    expiration = now + timedelta(hours=hours)
    print("Token will expire at: ", expiration.strftime("%d/%m/%Y, %H:%M:%S"))
    return (int(datetime.timestamp(now)), int(datetime.timestamp(expiration)))

def get_key_pair():
    if not os.path.exists(__private_key_file):
        raise Exception('Private key file not found [{}]. Generate keys and try again.'.format(__private_key_file))

    private_key_file = open(__private_key_file, 'rb')
    

    if not os.path.exists(__public_key_file):
        raise Exception('Public key file not found [{}]. Generate keys and try again.'.format(__public_key_file))

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

    print('\nJWT ------------------------------------------')
    print(encoded.decode('utf-8'))
    print('/JWT ------------------------------------------')

    decoded = jwt.decode(encoded, public_key, algorithms=__algorithm)

    valid = decoded==payload

    print("\nCheck: ", "VALID" if valid else "INVALID")

    if valid:
        print("\nPayload: ")
        pp(decoded)
        print("\n")
