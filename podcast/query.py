def get_konten_podcast(email):
    return f"SELECT id_konten FROM PODCAST WHERE email_podcaster = \'{email}\'"

def get_information_podcast(id_konten):
    return f"SELECT judul, tanggal_rilis, tahun, durasi FROM KONTEN WHERE id = \'{id_konten}\'"

def get_episode_podcast(id_konten_podcast):
    return f"SELECT judul, deskripsi, durasi, tanggal_rilis FROM EPISODE WHERE id_konten_podcast = \'{id_konten_podcast}\'"