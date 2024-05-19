from datetime import datetime
import uuid


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

def get_user_playlist(email):
    return f"select * from user_playlist where email_pembuat = \'{email}\'"

def add_playlist(title, description, email_pembuat):
    id_playlist = uuid.uuid4()
    return f"insert into playlist (id) values (\'{id_playlist}\'); insert into user_playlist (email_pembuat, id_user_playlist, judul, deskripsi, jumlah_lagu, tanggal_dibuat, id_playlist, total_durasi) values (\'{email_pembuat}\', \'{uuid.uuid4()}\', \'{title}\', \'{description}\', 0, \'{datetime.today().strftime('%Y-%m-%d')}\', \'{id_playlist}\', 0)"