#!/usr/bin/python3

from base64 import b64encode
from nacl import encoding, public
import os

def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

def process(args):
    SECRET_NAME = args.secretname
    VALUE = encrypt(os.getenv('VALUE')) # None
    if not VALUE: raise ValueError("Missing secret")

    # execute command
    stream = os.popen('curl \
        -X PUT \
        -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/orgs/ORG/actions/secrets/{SECRET_NAME} \
        -d \'{"encrypted_value":"{VALUE}"}\'')

    output = stream.read()
    output

import argparse
parser = argparse.ArgumentParser(description="Stream from microphone to DeepSpeech using VAD")

parser.add_argument('-r', '--repo', type=string, default="loic-roux-404", required=True,
                    help="Set the repo name")
parser.add_argument('-o', '--org', type=string, default=None, required=True,
                    help="Org name")
parser.add_argument('-s', '--secretname', type=string, default=None, required=True,
                    help="Org name")

ARGS = parser.parse_args()
process(ARGS)
