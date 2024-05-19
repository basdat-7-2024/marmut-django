#kalo butuh id tinggal ambil aja dari tabel User_playlist zi
#tapi tolong ditaruh di belakang biar gangacauin urutan list, tenks
#Select up.judul, up.jumlah_lagu, up.total_durasi, up.id_playlist.... (llanjut aja kalo butuh data lain)
def get_user_playlist(email):
    return f"""
    SELECT UP.judul, UP.jumlah_lagu, UP.total_durasi
    FROM USER_PLAYLIST as UP, AKUN as A
    WHERE UP.email_pembuat = A.email AND A.email = \'{email}\';
    """