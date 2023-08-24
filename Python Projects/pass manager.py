import getpass
import json
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

class PasswordManager:
    def __init__(self, file_path, key):
        self.file_path = file_path
        self.key = key
        self.passwords = {}
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                encrypted_data = f.read()
                if encrypted_data:
                    decrypted_data = self.decrypt(encrypted_data)
                    self.passwords = json.loads(decrypted_data)

    def save(self):
        data = json.dumps(self.passwords)
        encrypted_data = self.encrypt(data)
        with open(self.file_path, 'w') as f:
            f.write(encrypted_data)

    def set_password(self, service, username, password):
        if service not in self.passwords:
            self.passwords[service] = {}
        self.passwords[service][username] = password
        self.save()

    def get_password(self, service, username):
        if service in self.passwords and username in self.passwords[service]:
            return self.passwords[service][username]
        else:
            return None

    def remove_password(self, service, username):
        if service in self.passwords and username in self.passwords[service]:
            del self.passwords[service][username]
            if len(self.passwords[service]) == 0:
                del self.passwords[service]
            self.save()

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        return json.dumps({'iv': iv, 'ciphertext': ct})

    def decrypt(self, data):
        b64 = json.loads(data)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode()

def get_user_input():
    print('Welcome to the Password Manager!')
    print('Please choose an option:')
    print('1. Set a password')
    print('2. Get a password')
    print('3. Remove a password')
    print('4. Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        service = input('Enter the service name: ')
        username = input('Enter the username: ')
        password = getpass.getpass('Enter the password: ')
        return ('set', service, username, password)
    elif choice == '2':
        service = input('Enter the service name: ')
        username = input('Enter the username: ')
        return ('get', service, username)
    elif choice == '3':
        service = input('Enter the service name: ')
        username = input('Enter the username: ')
        return ('remove', service, username)
    elif choice == '4':
        return ('quit',)
    else:
        print('Invalid choice')
        return None

def main():
    file_path = 'passwords.json'
    key = os.urandom(16)
    pm = PasswordManager(file_path, key)
    while True:
        user_input = get_user_input()
        if user_input is None:
            continue
        operation, *args = user_input
        if operation == 'set':
            service, username, password = args
            pm.set_password(service, username, password)
            print('Password set successfully')
        elif operation == 'get':
            service, username = args
            password = pm.get_password(service, username)
            if password:
                print(f'Password: {password}')
            else:
                print('No password found')
        elif operation == 'remove':
            service, username = args
            pm.remove_password(service, username)
            print('Password removed successfully')
        elif operation == 'quit':
            break

if __name__ == '__main__':
    main()
