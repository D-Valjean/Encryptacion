from cryptography.fernet import Fernet

def load_key():
    # ruta donde cargara la llave de encryptacion
    file = open("C:\\key2.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    dictory_view = 'Z:\\Vault\\passwords2.md'  # directorio para ver instancia
    with open(dictory_view, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, msjs, passw = data.split("|")
            print("User:", fer.decrypt(user.encode()).decode(), "| Mensaje:", fer.decrypt(msjs.encode()).decode(), "| Password:",
                  fer.decrypt(passw.encode()).decode()+"\n")


def add():
    # directorio para crear/agregar instancia
    dictory_add = 'Z:\\Vault\\passwords2.md'
    name = input('Account Name: ')
    msjs = input('>_: ')
    pwd = input("Password: ")
    encrypted_name = fer.encrypt(name.encode()).decode()
    encrypted_msjs = fer.encrypt(msjs.encode()).decode()
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open(dictory_add, 'a') as f:
        f.write(encrypted_name + "|" + encrypted_msjs +
                "|" + encrypted_pwd + "\n")


while True:
    mode = input("\n" +
                 "Escoja una opcion a Realizar (ver, add). \nPara salir escribe (q) \n>_ ").lower()
    if mode == "q":
        break

    if mode == "ver":
        view()
    elif mode == "add":
        add()
    else:
        print("Comando invalido.")
        continue
