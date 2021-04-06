import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

import Crypto
import Crypto.Random
from Crypton.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCSI1_v1_5

class Client:
    def _init_(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generated(1024, random)
        self._public_key = self._private_key.publickey()
        self.signer = PKCS1_v1_5.new(self._private_key)

@property
def identity(self):
    return
binascii.hexlify(self._public_key.exportKey(format = 'DER')).decode('ascii')