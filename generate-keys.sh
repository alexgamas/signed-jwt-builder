#!/bin/bash

keys_dir=./keys
private_rsa_key_file=$keys_dir/private.key
private_pem_key_file=$keys_dir/private_key.pem
public_pem_key_file=$keys_dir/public_key.pem

mkdir -p $keys_dir

openssl genrsa -out $private_rsa_key_file 2048

openssl pkcs8 -topk8 -inform pem -in $private_rsa_key_file -outform pem -nocrypt -out $private_pem_key_file

openssl rsa -in $private_rsa_key_file -outform PEM -pubout -out $public_pem_key_file