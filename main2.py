def encoder(password):
    new_password = ""
    for i in password:
        new_password = new_password + str(int(i) + 3)
    return new_password


def decoder(password):
    new_password = ""
    for i in password:
        new_password = new_password + str(int(i) - 3)
    return new_password