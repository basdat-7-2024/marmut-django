def get_artist_role(email):
    return f"SELECT * FROM ARTIST WHERE email_akun = \'{email}\'"

def get_songwriter_role(email):
    return f"SELECT * FROM SONGWRITER WHERE email_akun = \'{email}\'"

def get_podcaster_role(email):
    return f"SELECT * FROM PODCASTER WHERE email = \'{email}\'"

def get_premium_role(email):
    return f"SELECT * FROM PREMIUM WHERE email = \'{email}\'"

def get_nonpremium_role(email):
    return f"SELECT * FROM NONPREMIUM WHERE email = \'{email}\'"