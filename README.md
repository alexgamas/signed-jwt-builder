# Signed JWT builder guide

## Dependencies

python and pip version 3

```bash
pip3 install PyJWT
pip3 install cryptography --upgrade
```

## Generate keypair

```bash
$ ./generate-keys.sh

Generating RSA private key, 2048 bit long modulus
..........................+++
........................................................+++
e is 65537 (0x10001)
writing RSA key
```

> will output keyfiles inside ./keys/

|File|Description|
|-|-|
|private.key|RSA private key file|
|private_key.pem|Extracted pem private key file|
|public_key.pem|Public key file|

## Run

```bash
$ pip3 install -r requirements.txt

$ python3 ./create-jwt.py
Token will expire at:  28/09/2019, 23:48:39

JWT ------------------------------------------
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MjU1NTUxMjEyIiwiaXNzIjoiaHR0cHM6Ly93d3cuWW91ckJyYW5kLmNvbSIsInByZWZlcnJlZF91c2VybmFtZSI6IkpvaG5Eb2UiLCJwaG9uZV9udW1iZXIiOiIrMS0xMC0zNDQtMzc2NTMzMyIsImV4cCI6MTU2OTcyNTMxOSwiaWF0IjoxNTY4ODYxMzE5fQ.C_sD9QQRE24i6cHtKPaglFi9OdQNf15YVGZV09gQ8GQqXSTP2NhBpe3en4qFpdZ5rXfUQSPav81Ulz9-8SiQNcow1drJbTPBZ95Jk4HN6vNU-Qq5Cr-MAmP_eGvhs_yc43n-1WEEfrr7qrDMGbBrsKDjvi325imv0mj-lQurPIx6Iw_sh3y9VafE_SdHuQPC0Cs3d9Ul9EvgvgOKzYYVv0Sy5t_BKV2Rw6m7qkZqi-kP_T0tOoSUGGz3UeVpoii20ESp5mXE3sHBBcuMrqIJxXMP560JVJ-FxlVVsFSqMhnQvI-QnypsqnSwB6sY1Eax8pFi8wiz2BoZQpJTOhyxAw
/JWT ------------------------------------------

Check:  VALID

Payload:
{   'exp': 1569725319,
    'iat': 1568861319,
    'iss': 'https://www.YourBrand.com',
    'phone_number': '+1-10-344-3765333',
    'preferred_username': 'JohnDoe',
    'sub': '4255551212'}

```
