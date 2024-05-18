def get_information_album_label(email):
    return f"""
    SELECT a.judul, a.jumlah_lagu, a.total_durasi
    FROM LABEL as l, ALBUM as a
    WHERE a.id_label = l.id AND l.email = \'{email}\'
    """

def get_information_album_artist(email):
    return f"""
    SELECT a.judul, a.jumlah_lagu, a.total_durasi
    FROM ARTIST as ar, ALBUM as a, SONG as s
    WHERE ar.id = s.id_artist AND s.id_album = a.id AND ar.email_akun = \'{email}\'
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


def get_information_lagu_album(email):
    return f"""SELECT
    k.judul AS judul_lagu,
    k.durasi,
    s.total_play,
    s.total_download
FROM
    ALBUM a
JOIN
    SONG s ON a.id = s.id_album
JOIN
    Konten k ON s.id_konten = k.id
WHERE
    a.judul = \'{email}\';
    """


def get_information_song_details(name):
    return f"""SELECT 
    k.judul AS judul_lagu,
    STRING_AGG(DISTINCT g.genre, ', ') AS genres,
    a.email_akun AS artist_email,
    STRING_AGG(DISTINCT sw.email_akun, ', ') AS songwriter_emails,
    k.durasi,
    k.tanggal_rilis,
    k.tahun,
    s.total_play,
    s.total_download,
    al.judul AS judul_album
FROM 
    SONG s
JOIN 
    Konten k ON s.id_konten = k.id
JOIN 
    ALBUM al ON s.id_album = al.id
JOIN 
    ARTIST a ON s.id_artist = a.id
JOIN 
    Genre g ON k.id = g.id_konten
LEFT JOIN 
    SONGWRITER_WRITE_SONG sws ON s.id_konten = sws.id_song
LEFT JOIN 
    SONGWRITER sw ON sws.id_songwriter = sw.id
WHERE 
    k.judul = \'{name}\'
GROUP BY 
    k.judul, a.email_akun, k.durasi, k.tanggal_rilis, k.tahun, s.total_play, s.total_download, al.judul;
    """


