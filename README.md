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

$ python3 create-jwt.py

Token will expire at:  17/09/2019, 23:42:36
JWT ------------------------------------------
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MjU1NTUxMjEyIiwiaXNzIjoiaHR0cHM6Ly93d3cuWW91ckJyYW5kLmNvbSIsInByZWZlcnJlZF91c2VybmFtZSI6IkpvaG5Eb2UiLCJwaG9uZV9udW1iZXIiOiIrMS0xMC0zNDQtMzc2NTMzMyIsImV4cCI6MTU2ODc3NDU1Ni42MTkxMTUsImlhdCI6MTU2ODY4ODE1Ni42MTkxMTV9.0Tw9NCjm4rq3zVnQF5FY2lQlwspvHbvwKRprb3S0eoTKOMKggp8wDCukSSQle37tAS_LHLvZFhdLyA6GsUuhwNSPbE2hcW9fFLYT2tTCGymGjI7dXtxEU_kfqp_v3RVwmlMxH5-vJnCgoVhjvxVGzCotrfnC0ES8wn7uPOegNEIAshAocn9rJQmGwPG2vI49uVo9dqyVAomFzetduY8wSEv0wtF0IjLcE5ORQgLHxRYfTzGQnDIunl48W0f46PpeOF96TlSf4SVb-BgJRX-qCrbMLcOa5alyEiemdGNmF0P-P7NAfFIKb9kJJogcqMYXWlEZXrBjbu_jz0XmtgbC4Q
/JWT ------------------------------------------
Chack:  VALID
```
