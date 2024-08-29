import re


# check email
def is_email(email):
    email_pattern = r'\w+@\w+\.com(\.\w+)?'
    is_ok = re.search(email_pattern, email)
    if is_ok:
        print("Ok")
    else:
        print("there is an error in that address")


is_email('simon@x.com.as')


# check if say Hello
def check_hello(phrase):
    hello_pattern = re.search(r'^hola', phrase.lower())

    if hello_pattern:
        print("Ok")
    else:
        print("No has saludado")


check_hello('HOLa Capullo')


# Check Post code

def check_cp(cp):
    cp_pattern = r'\w{2}\d{4}'
    is_cp_ok = re.search(cp_pattern, cp)
    if is_cp_ok:
        print('Ok')
    else:
        print("El código postal ingresado no es correcto")

check_cp('as1232')
