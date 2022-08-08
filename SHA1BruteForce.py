from urllib.request import urlopen, hashlib
sha1hash = input("Please enter the hash: ")
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt').read(), 'latin-1')
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == sha1hash:
        print("Decrypted String: ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Checking: ",str(guess))
print("Hash not found!")