def checkpassword(password):
    if len(password)<5:
        return "Weak Password "
    elif len(password)<10:
        return "Medium Secure PAssword"
    else:
        return "Strong Password"