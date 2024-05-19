def get_information_royalti_label(email):
    return f"""
SELECT 
    k.judul AS judul_lagu, 
    a.judul AS judul_album, 
    s.total_play, 
    s.total_download, 
    r.jumlah AS total_royalti
FROM 
    ROYALTI r
JOIN 
    SONG s ON r.id_song = s.id_konten
JOIN 
    ALBUM a ON s.id_album = a.id
JOIN 
    Konten k ON s.id_konten = k.id
JOIN 
    LABEL l ON a.id_label = l.id
WHERE l.email = \'{email}\'
    """

def get_information_royalti_artist(email):
    return f"""SELECT 
    k.judul AS judul_lagu,
    a.judul AS judul_album,
    s.total_play,
    s.total_download,
    r.jumlah AS total_royalti
FROM 
    ROYALTI r
INNER JOIN 
    SONG s ON r.id_song = s.id_konten
INNER JOIN 
    ALBUM a ON s.id_album = a.id
INNER JOIN 
    ARTIST ar ON s.id_artist = ar.id
INNER JOIN 
    Konten k ON s.id_konten = k.id
WHERE ar.email_akun = \'{email}\'
    """


def get_information_royalti_songwriter(email):
    return f"""
    SELECT 
    k.judul AS judul_lagu,
    a.judul AS judul_album,
    s.total_play,
    s.total_download,
    r.jumlah AS total_royalti
FROM 
    ROYALTI r
INNER JOIN 
    SONG s ON r.id_song = s.id_konten
INNER JOIN 
    ALBUM a ON s.id_album = a.id
INNER JOIN 
    SONGWRITER_WRITE_SONG sws ON s.id_konten = sws.id_song
INNER JOIN 
    SONGWRITER sw ON sws.id_songwriter = sw.id
INNER JOIN 
    Konten k ON s.id_konten = k.id
WHERE sw.email_akun = \'{email}\'
    """
