import datetime


def get_playlist_info_from_id(id):
    return f"select email_pembuat, id_user_playlist, judul, jumlah_lagu, tanggal_dibuat, id_playlist, total_durasi, nama, deskripsi from (SELECT * FROM user_playlist WHERE id_playlist = \'{id}\') t1 left join (select email, nama from akun) t2 on t1.email_pembuat=t2.email;"

def get_playlist_songs_from_id(id):
    return f"SELECT id,judul,durasi, (SELECT nama from akun where email in (SELECT email_akun from artist where id in (SELECT id_artist FROM song WHERE id_konten in (select id_song from playlist_song where id_playlist=\'{id}\')))) as artist FROM konten WHERE id IN (select id_song from playlist_song where id_playlist=\'{id}\')"

def insert_into_akun_play_user_playlist(email_pemain, id_user_playlist, email_pembuat):
    # email_pemain id_user_playlist email_pembuat waktu
    timezone_offset = 0  # UTC
    tzinfo = datetime.timezone(datetime.timedelta(hours=timezone_offset))
    datetime.datetime.now
    time_now =  datetime.datetime.now(tzinfo)
    return f"insert into akun_play_user_playlist (email_pemain, id_user_playlist, email_pembuat, waktu) values (\'{email_pemain}\', \'{id_user_playlist}\', \'{email_pembuat}\', \'{time_now}\')"