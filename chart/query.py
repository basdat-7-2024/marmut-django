def get_chart():
    return f"""
    SELECT * FROM CHART;
    """

def get_all_chart():
    return f"""
    SELECT K.judul, A.nama, K.tanggal_rilis, S.total_play
    FROM SONG as S, KONTEN as K,ARTIST as AR, AKUN as A
    WHERE (S.id_konten = K.id AND S.id_artist = AR.id AND AR.email_akun = A.email)
    AND S.total_play != 0
    ORDER BY S.total_play DESC
    LIMIT 20;
    """