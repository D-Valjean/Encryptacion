from cryptography.fernet import Fernet
from difflib import get_close_matches
import json


def load_key():
    # ruta donde cargara la llave de encryptacion
    file = open("C:\\key2.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def view():
    dictory_view = 'Z:\\Vault\\passwords3.md'  # directorio para ver instancia
    with open(dictory_view, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            commit, user, passw = data.split("|")
            print("\nPagina/Entorno: ", fer.decrypt(commit.encode()).decode(), " | User: ", fer.decrypt(user.encode()).decode(), " | Password: ",
                  fer.decrypt(passw.encode()).decode())


def add():
    # directorio para crear/agregar instancia
    dictory_add = 'Z:\\Vault\\passwords3.md'
    commit = input('Pagina/Entorno: ')
    name = input('Account Name: ')
    pwd = input("Password: ")
    encrypted_commit = fer.encrypt(commit.encode()).decode()
    encrypted_name = fer.encrypt(name.encode()).decode()
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open(dictory_add, 'a') as f:
        f.write(encrypted_commit + "|" + encrypted_name +
                "|" + encrypted_pwd + "\n")


def menu_passwords():
    while True:
        mode = input("\n" +
                     "Escoja un numero a Realizar \n1.ver Credenciales. \n2.Agregar. \nPara salir escribe (q) \n>_ ").lower()
        if mode == "q":
            break

        if mode == "1":
            view()
        elif mode == "2":
            add()
        else:
            print("Comando invalido.")
            continue


def menu():
    while True:
        option = input(
            "Escogue un numero, o precione ''Q'' para Salir. \n1.Passwords \n2. Bot \n\>_ ")
        if option == "1":
            menu_passwords()
        elif option == "2":
            chat_bot()
        elif option.lower() == "q":
            break
        else:
            print("Comando invalido.")


if __name__ == '__main__':
    menu()
