# cst8919lab5

To set up the Azure Key Vault I used the portal, and while creating it, I also created the vault access policy, which gave my account access full control over keys and secrets in that key vault.
![Screenshot 2024-03-31 141011](https://github.com/brentencarnado/cst8919lab5/assets/44175005/8f0b6e67-30f4-430c-b381-9e8a11b48de1)

To generate the key, I went to the newly created key vault and clicked on "Keys" in the side menu. I then generated a key called lab5key.
![Screenshot 2024-03-31 141945](https://github.com/brentencarnado/cst8919lab5/assets/44175005/5b1ebc1e-dd8b-4e13-9da0-9f6b14bf9e01)


# How the program encrypts, stores, retrieves, and decrypts data
A KeyClient object is created to deal with the Key Vault keys. The KeyClient's get_key() method retrieves the lab5key from the Key Vault. A CryptographyClient is then created using that key to create the unique encryption method. The user is then prompted to input a string that is then encoded to bytes for the CryptographyClient's encrypt() method. This encoded string is then encrypted using an algorithm.
A Secret Client obeject is created to deal with the Key Vault secrets. The cipher text then needs to be encoded into base64 format in order for Key Vault to accept it as a secret. The SecretCient's set_secret() method is then used to store the base64 encoded ciphertext in the Key Vault as a secret.
To retrieve the data, SecretClient's get_secret() method is used to retrieve the secret by name, where it is then decoded back to its original encrypted ciphertext format. The ciphertext is then decrypted using the CryptographyClient that was created with the key.

# Issues Encountered
Figuring out the whole encoding and decoding process for storage and displaying was difficult, but the following link was helpful in solving te problem: https://www.geeksforgeeks.org/python-strings-decode-method/

Working with the encrypt/decrypt methods was confusing but this link helped: https://github.com/Azure/azure-sdk-for-python/tree/azure-keyvault-secrets_4.8.0/sdk/keyvault/azure-keyvault-keys#cryptographic-operations

# Working Output
![Screenshot 2024-03-31 235511](https://github.com/brentencarnado/cst8919lab5/assets/44175005/05057af2-3e81-4c74-83fd-acc702dab7aa)
