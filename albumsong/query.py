def get_id_album(email):
    return f"""
    SELECT a.judul, a.jumlah_lagu, a.total_durasi
    FROM LABEL as l, ALBUM as a
    WHERE a.id_label = l.id AND email = \'{email}\'
    """
