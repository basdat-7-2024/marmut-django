def get_user_playlist_info_from_id(id):
    return f"select email_pembuat, id_user_playlist, judul, jumlah_lagu, tanggal_dibuat, id_playlist, total_durasi, nama, deskripsi from (SELECT * FROM user_playlist WHERE id_playlist = \'{id}\') t1 left join (select email, nama from akun) t2 on t1.email_pembuat=t2.email"

def get_user_playlist_songs_from_id(id):
    return f"SELECT id,judul,durasi, (SELECT nama from akun where email in (SELECT email_akun from artist where id in (SELECT id_artist FROM song WHERE id_konten in (select id_song from playlist_song where id_playlist=\'{id}\')))) as artist FROM konten WHERE id IN (select id_song from playlist_song where id_playlist=\'{id}\')"

def update_playlist(id, judul, deskripsi):
    return f"update user_playlist set judul=\'{judul}\', deskripsi=\'{deskripsi}\' where id_playlist=\'{id}\'"

def delete_playlist(id):
    return f"delete from user_playlist where id_playlist=\'{id}\'"

def get_user_playlist(email):
    return f"""
    SELECT UP.judul, UP.jumlah_lagu, UP.total_durasi
    FROM USER_PLAYLIST as UP, AKUN as A
    WHERE UP.email_pembuat = A.email AND A.email = \'{email}\';
    """