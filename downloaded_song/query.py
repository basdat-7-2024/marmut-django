def get_downloaded_song(email):
    return f"""
        SELECT 
            k.id, k.judul
        FROM 
            downloaded_song d
            JOIN song s ON d.id_song = s.id_konten
            JOIN konten k ON s.id_konten = k.id
        WHERE 
            d.email_downloader = '{email}'
        ORDER BY 
            k.judul ASC;
    """


def delete_downloaded_song(email, song_id):
    return f"""
        BEGIN;
        DELETE FROM downloaded_song 
        WHERE email_downloader = '{email}' 
        AND id_song = '{song_id}';
        
        UPDATE song 
        SET total_download = total_download - 1 
        WHERE id_konten = '{song_id}';
        COMMIT;
    """
