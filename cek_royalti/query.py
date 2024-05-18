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
WHERE l.email = \'{email}\';
    """