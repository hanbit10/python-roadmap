
from cryptography.fernet import Fernet



'''
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)'''

def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key


key = load_key() + pwd.encode()
fer = Fernet(key)


def view(): 
  with open('passwords.txt', 'r') as f:
    for line in f.readlines():
      data = line.rstrip()
      user, passw = data.split("|")
      print("User: ", user, "Password: ", fer.decrypt(passw.encode()))
  print(user)    
      
def add():
  name = input('Account Name: ')
  pwd = input("Password: ")
  key = load_key() + pwd.encode()
  fer = Fernet(key)
  with open('passwords.txt', 'a') as f:
    f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 



while True:
  mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
  if mode == "q":
    break
  elif mode == "view":
    print("This is view")
    view()   
  elif mode =="add":
    print("Account added")
    add()
  else:
    print("Invalid mode.")
    continue
