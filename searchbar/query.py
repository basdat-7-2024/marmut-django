# query.py

def get_search_query():
    return """
    SELECT 'Song' AS type, konten.judul AS judul, akun.nama AS oleh, konten.id AS id
    FROM song
    JOIN konten ON song.id_konten = konten.id
    JOIN artist ON song.id_artist = artist.id
    JOIN akun ON artist.email_akun = akun.email
    WHERE LOWER(konten.judul) LIKE LOWER(%s)
    
    UNION ALL
    
    SELECT 'Podcast' AS type, konten.judul AS judul, akun.nama AS oleh, konten.id AS id
    FROM podcast
    JOIN konten ON podcast.id_konten = konten.id
    JOIN podcaster ON podcast.email_podcaster = podcaster.email
    JOIN akun ON podcaster.email = akun.email
    WHERE LOWER(konten.judul) LIKE LOWER(%s)
    
    UNION ALL
    
    SELECT 'Playlist' AS type, user_playlist.judul AS judul, akun.nama AS oleh, playlist.id
    FROM user_playlist
    JOIN playlist ON user_playlist.id_playlist = playlist.id
    JOIN akun ON user_playlist.email_pembuat = akun.email
    WHERE LOWER(user_playlist.judul) LIKE LOWER(%s);
    """
