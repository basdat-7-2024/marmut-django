def get_downloaded_song(email):
    return f"""
        SELECT 
            k.judul AS Judul
        FROM 
            downloaded_song d
            JOIN song s ON d.id_song = s.id_konten
            JOIN konten k ON s.id_konten = k.id
        WHERE 
            d.email_downloader = '{email}'
        ORDER BY 
            k.judul ASC;
    """
