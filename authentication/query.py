def get_email_password(email, password):
    return f"SELECT * FROM AKUN WHERE email = \'{email}\' AND password = \'{password}\'"

def get_nama_akun(email):
    return f"SELECT nama FROM AKUN WHERE email = \'{email}\'"

def get_gender_akun(email):
    return f"SELECT gender FROM AKUN WHERE email = \'{email}\'"

def get_tempat_lahir_akun(email):
    return f"SELECT tempat_lahir FROM AKUN WHERE email = \'{email}\'"

def get_tanggal_lahir_akun(email):
    return f"SELECT tanggal_lahir FROM AKUN WHERE email = \'{email}\'"

def get_is_verified_akun(email):
    return f"SELECT is_verified FROM AKUN WHERE email = \'{email}\'"

def get_kota_asal_akun(email):
    return f"SELECT kota_asal FROM AKUN WHERE email = \'{email}\'"