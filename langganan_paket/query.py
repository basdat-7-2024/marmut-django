def get_jenis_paket():
    return f"""
    SELECT jenis, harga FROM PAKET;
    """

def get_history_paket(email):
    return f"""
        SELECT 
            jenis_paket AS Judul, 
            TO_CHAR(timestamp_dimulai, 'DD Mon YYYY, HH24:MI') AS Tanggal_Dimulai, 
            TO_CHAR(timestamp_berakhir, 'DD Mon YYYY, HH24:MI') AS Tanggal_Berakhir, 
            metode_bayar AS Metode_Pembayaran, 
            nominal AS Nominal 
        FROM transaction 
        WHERE email = '{email}' 
        ORDER BY timestamp_dimulai DESC;
    """