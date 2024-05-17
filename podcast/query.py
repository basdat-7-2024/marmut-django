def get_konten_podcast(email):
    return f"SELECT id_konten FROM PODCAST WHERE email_podcaster = \'{email}\'"

def get_information_podcast(id_konten):
    return f"SELECT judul, tanggal_rilis, tahun, durasi, id FROM KONTEN WHERE id = \'{id_konten}\'"

def get_episode_podcast(id_konten_podcast):
    return f"SELECT judul, deskripsi, durasi, tanggal_rilis FROM EPISODE WHERE id_konten_podcast = \'{id_konten_podcast}\'"

def get_detail_podcast(id_podcast):
    return f"""SELECT K.judul, P.email_podcaster, K.tanggal_rilis, G.genre, K.durasi, K.tahun
    FROM KONTEN as K, PODCAST as P, GENRE as G
    WHERE (K.id = P.id_konten AND K.id = G.id_konten) AND K.id = \'{id_podcast}\';
    """

def create_konten_podcast(id, judul, tanggal_rilis, tahun, durasi):
    return f"""
    INSERT INTO KONTEN
    VALUES (\'{id}\', \'{judul}\', \'{tanggal_rilis}\', \'{tahun}\', \'{durasi}\');
    """

def create_tabel_podcast(id, email):
    return f"""
    INSERT INTO PODCAST
    VALUES (\'{id}\', \'{email}\');
    """

def create_genre_podcast(id, genre):
    return f"""
    INSERT INTO GENRE
    VALUES (\'{id}\', \'{genre}\');
    """

def delete_podcast_from_id_konten(id):
    return f"""
    DELETE FROM KONTEN WHERE id = \'{id}\';
    """

def get_episode_from_tabel(id_konten_podcast):
    return f"""
    SELECT * FROM EPISODE WHERE id_konten_podcast = \'{id_konten_podcast}\';
    """

def create_episode_on_tabel(id_episode, id_podcast, judul, deskripsi, durasi, tanggal_rilis):
    return f"""
    INSERT INTO EPISODE
    VALUES (\'{id_episode}\', \'{id_podcast}\', \'{judul}\', \'{deskripsi}\', \'{durasi}\', \'{tanggal_rilis}\');
    """

def delete_episode_from_tabel(id):
    return f"""
    DELETE FROM EPISODE WHERE id_episode = \'{id}\';
    """