from os import urandom
from hashlib import blake2b
from Heart.TweetNaCl.tweetnacl import (
    crypto_secretbox_xsalsa20poly1305_tweet,
    crypto_secretbox_xsalsa20poly1305_tweet_open,
    crypto_scalarmult_curve25519_tweet_base,
    crypto_box_curve25519xsalsa20poly1305_tweet_beforenm,
    )

class Nonce:
    def __init__(self, nonce=None, clientKey=None, serverKey=None):
        if not clientKey:
            if nonce:
                self._nonce = nonce
            else:
                self._nonce = urandom(24)
        else:
            b2 = blake2b(digest_size=24)
            if nonce:
                b2.update(bytes(nonce))
            b2.update(bytes(clientKey))
            b2.update(serverKey)
            self._nonce = b2.digest()
    
    def __bytes__(self):
        return self._nonce
    def __len__(self):
        return len(self._nonce)
    def increment(self):
        self._nonce = (int.from_bytes(self._nonce, 'little') + 2).to_bytes(24, 'little')

    
class Crypto:
    def __init__(self):
        self.server_private_key = bytearray(b'\x9e\xd9n\x05W\xf9\xde\xea\xccy\xb1\xe4;O]\xd9\x19!q\xb9w\xab\xcd\xf6\x0b\xb9\xb9\x16\x8c\x98k\x14')
        self.server_public_key = bytearray(32)
        self.client_public_key = None
        self.session_key = None
        self.shared_encryption_key = bytes(urandom(32))
        self.decryptNonce = None
        self.encryptNonce = Nonce(urandom(24))
        self.nonce = None
        self.s = bytearray(32)

    def decryptClient(self, packet_id, payload):
        if packet_id == 10100:
            return payload
        elif packet_id == 10101:
            self.client_public_key = bytes(payload[:32])
            payload = payload[32:]
            crypto_scalarmult_curve25519_tweet_base(self.server_public_key, self.server_private_key)
            self.nonce = Nonce(clientKey=self.client_public_key, serverKey=self.server_public_key)
            crypto_box_curve25519xsalsa20poly1305_tweet_beforenm(self.s, self.client_public_key, self.server_private_key)
            payload = bytearray(16) + bytearray(payload) 
            decrypted = bytearray(len(payload))
            crypto_secretbox_xsalsa20poly1305_tweet_open(decrypted, payload, len(payload), bytes(self.nonce), self.s)
            decrypted = decrypted[32:]
            self.decryptNonce = Nonce(bytes(decrypted[24:48]))
            return decrypted[48:]
        elif self.decryptNonce is None:
            return payload
        else:
            self.decryptNonce.increment()
            payload = bytearray(16) + bytearray(payload)
            decrypted = bytearray(len(payload))
            crypto_secretbox_xsalsa20poly1305_tweet_open(decrypted, payload, len(payload), bytes(self.decryptNonce), self.shared_encryption_key)
            return decrypted[32:]

    def encryptServer(self, packet_id, payload):
        if packet_id == 20100 or packet_id == 20103:
            return payload
        else:
            if packet_id == 20104:
                nonce = Nonce(bytes(self.decryptNonce), clientKey=self.client_public_key, serverKey=self.server_public_key)
                payload = bytes(self.encryptNonce) + self.shared_encryption_key + payload
                payload = bytearray(32) + bytearray(payload)
                encrypted = bytearray(len(payload))
                crypto_secretbox_xsalsa20poly1305_tweet(encrypted, payload, len(payload), bytes(nonce), self.s)
                return encrypted[16:]
            else:
                self.encryptNonce.increment()
                payload = bytearray(32) + bytearray(payload)
                encrypted = bytearray(len(payload))
                crypto_secretbox_xsalsa20poly1305_tweet(encrypted, payload, len(payload), bytes(self.encryptNonce), self.shared_encryption_key)
                return encrypted[16:]