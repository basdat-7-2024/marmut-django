def get_information_album_label(email):
    return f"""
    SELECT a.judul, a.jumlah_lagu, a.total_durasi
    FROM LABEL as l, ALBUM as a
    WHERE a.id_label = l.id AND l.email = \'{email}\'
    """

def get_information_lagu(email):
    return f"""
    SELECT k.judul, s.total_play, s.total_download
    FROM SONG as s, ARTIST as a, KONTEN as k
    WHERE a.id = s.id_artist AND k.id = s.id_konten AND a.email_akun = \'{email}\'
    """
    
def get_information_songwriter(email):
    return f"""
    SELECT k.judul, s.total_play, s.total_download
    FROM SONGWRITER as sw, SONG as s, KONTEN as k, SONGWRITER_WRITE_SONG as sws
    WHERE sw.id = sws.id_songwriter AND k.id = s.id_konten AND sws.id_song = s.id_konten AND sw.email_akun = \'{email}\'
    """


