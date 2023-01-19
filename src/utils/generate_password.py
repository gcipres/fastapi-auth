import random

def generate_password():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%$/&";
    password_generated = ""
		
    for i in range(17):
        password_generated += random.choice(characters)
    
    return password_generated