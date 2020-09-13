from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

AES.block_size

#plaintext = "you captured the flag"
ciphertext_orig = "46beb3b832973495f79b860884245e431d73c2d3f7e3a7632dce894ed14ff62b"
iv = 'aabbccddeeff00998877665544332211'
iv = bytes.fromhex(iv)
ciphertext = bytes.fromhex(ciphertext_orig)

print("Ciphertext: ", ciphertext_orig)

f = open("file", "rb")
data = f.read()

plaintext = pad(data, AES.block_size)
print("plaintext:", plaintext)

f2 = open("words.txt", "r")
word_data = f2.read()

words = word_data.splitlines()

for word in words:
    if(len(word) < 16):
        num = 16 - len(word)
        adds = "#"*num
        padded_word = word + adds
        #print(len(padded_word), "\n")
    
    key = padded_word.encode('utf-8')
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphered_data = cipher.encrypt(plaintext)

    cipher_data_text = ciphered_data.hex()

    #iv = cipher.iv
    #d_cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    #decrypt_bytes = unpad(d_cipher.decrypt(ciphered_data), AES.block_size)
    #decrypt_text = decrypt_bytes.decode('utf-8', 'ignore')
    #print(decrypt_text)

    if(ciphertext_orig == cipher_data_text):
        print("Cipher: ", cipher_data_text)
        print("Correct Key is: ", word)
        break

    

