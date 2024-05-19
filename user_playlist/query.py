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

def get_song_detail_info_from_id(id):
    return f"select id_konten, id_artist, id_album, total_play, total_download, judul, tanggal_rilis, tahun, durasi, nama_album, artist from (select * from song where id_konten=\'{id}\') song left join lateral (select * from konten where id_konten=song.id_konten) konten on song.id_konten=konten.id left join lateral (select judul as nama_album from album where id=song.id_album) album on song.id_konten=konten.id inner join lateral (select nama as artist from akun where email in (select email_akun from artist where id=song.id_artist)) artist on song.id_konten=konten.id"

def get_songwriter_from_id(id):
    return f"select nama from akun where email in (select email_akun from songwriter where id in (select id_songwriter from songwriter_write_song where id_song=\'{id}\'))"

def get_genre_from_id(id):
    return f"select genre from genre where id_konten=\'{id}\'"