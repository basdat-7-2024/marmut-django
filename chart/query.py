def get_chart():
    return f"""
    SELECT * FROM CHART;
    """

def get_detail_chart(id_playlist):
    return f"""
    SELECT K.judul, A.nama, K.tanggal_rilis, S.total_play
    FROM PLAYLIST_SONG as PS, SONG as S, KONTEN as K,ARTIST as AR, AKUN as A
    WHERE (PS.id_song = S.id_konten AND S.id_konten = K.id AND S.id_artist = AR.id AND AR.email_akun = A.email)
    AND PS.id_playlist = \'{id_playlist}\'
    ORDER BY S.total_play DESC;
    """