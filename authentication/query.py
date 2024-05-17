def get_email_password_from_akun(email, password):
    return f"SELECT * FROM AKUN WHERE email = \'{email}\' AND password = \'{password}\'"

def get_email_password_from_label(email, password):
    return f"SELECT * FROM LABEL WHERE email = \'{email}\' AND password = \'{password}\'"

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

def get_id_label(email):
    return f"SELECT id FROM LABEL WHERE email = \'{email}\'"

def get_nama_label(email):
    return f"SELECT nama FROM LABEL WHERE email = \'{email}\'"

def get_kontak_label(email):
    return f"SELECT kontak FROM LABEL WHERE email = \'{email}\'"

def register_to_akun_to_tabel(email, password, nama, gender, tempat_lahir, tanggal_lahir, is_verified, kota_asal):
    return f"""
    INSERT INTO AKUN
    VALUES (\'{email}\', \'{password}\', \'{nama}\', \'{gender}\', \'{tempat_lahir}\', \'{tanggal_lahir}\', \'{is_verified}\', \'{kota_asal}\');
    """

def register_nonpremium_to_tabel(email):
    return f"""
    INSERT INTO NONPREMIUM
    VALUES (\'{email}\');
    """

def register_artist_to_tabel(id, email_akun, id_pemilik_hak_cipta):
    return f"""
    INSERT INTO ARTIST
    VALUES (\'{id}\', \'{email_akun}\', \'{id_pemilik_hak_cipta}\');
    """

def register_songwriter_to_tabel(id, email_akun, id_pemilik_hak_cipta):
    return f"""
    INSERT INTO SONGWRITER
    VALUES (\'{id}\', \'{email_akun}\', \'{id_pemilik_hak_cipta}\');
    """

def register_podcaster_to_tabel(email):
    return f"""
    INSERT INTO PODCASTER
    VALUES (\'{email}\');
    """

def register_label_to_tabel(id, nama, email, password, kontak, id_pemilik_hak_cipta):
    return f"""
    INSERT INTO LABEL
    VALUES (\'{id}\', \'{nama}\', \'{email}\', \'{password}\', \'{kontak}\', \'{id_pemilik_hak_cipta}\');
    """



