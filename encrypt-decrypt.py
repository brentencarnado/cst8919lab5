import datetime
import os
import base64

# need to set environment variable VAULT_URL with the URL of your key vault

from azure.identity import DefaultAzureCredential
from azure.keyvault.keys import KeyClient
from azure.keyvault.keys.crypto import CryptographyClient, EncryptionAlgorithm
from azure.keyvault.secrets import SecretClient

VAULT_URL = os.environ["VAULT_URL"]

credential = DefaultAzureCredential()

key_client = KeyClient(vault_url=VAULT_URL, credential=credential)

key = key_client.get_key("lab5key")
crypto_client = CryptographyClient(key, credential=credential)

#need to encode because CryptographyClient.encrypt takes bytes as second param
plaintext = input("Input string to encrypt: ").encode()

result = crypto_client.encrypt(EncryptionAlgorithm.rsa_oaep, plaintext)
ciphertext = result.ciphertext
print("Ciphertext = ", ciphertext)


secret_client = SecretClient(vault_url=VAULT_URL, credential=credential)
#converting password to basse64 encoding
#from https://www.geeksforgeeks.org/python-strings-decode-method/
ciphertext_encoded = base64.b64encode(ciphertext).decode()
secret = secret_client.set_secret("lab5secret", ciphertext_encoded)
print("Secret stored successfully. Secret Identifier = ", secret.id)


retrieved_secret = secret_client.get_secret("lab5secret")
#secret is stored in base64 encoding, this decodes the value of the secret back to original binary
secret_decoded = base64.b64decode(retrieved_secret.value) 
decrypted_result = crypto_client.decrypt(EncryptionAlgorithm.rsa_oaep, secret_decoded)
#convert thhe plaintext from bytes to string
print("Decrypted original string = ", decrypted_result.plaintext.decode())

