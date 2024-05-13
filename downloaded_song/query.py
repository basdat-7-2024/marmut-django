def get_downloaded_song(email):
    return f"""
        SELECT 
            k.judul AS Judul,
            k.id AS id_konten,
            TO_CHAR(d.timestamp_downloaded, 'DD/MM/YYYY') AS Tanggal_Download
        FROM 
            downloaded_song d
            JOIN song s ON d.id_song = s.id
            JOIN konten k ON s.id_konten = k.id
        WHERE 
            d.email_downloader = '{email}'
        ORDER BY 
            d.timestamp_downloaded DESC;
    """
