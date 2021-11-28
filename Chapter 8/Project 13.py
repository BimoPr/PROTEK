nilaiMhs = [{'nim': 'A01', 'nama': 'Amir', 'mid': 50, 'uas': 80}, 	      {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim': 'A03', 'nama': 'Cici', 'mid': 50, 'uas': 50},
            {'nim': 'A04', 'nama': 'Dedi', 'mid': 20, 'uas': 30},
	        {'nim': 'A05', 'nama': 'Fifi', 'mid': 70, 'uas': 40}]

def nilai():
    i = 0
    j = {}
    for x in nilaiMhs:
        uas = x.get('uas')
        mid = x.get('mid')
        nilaiTertinggi = (mid + 2*uas)/3
        if nilaiTertinggi > i:
            i = nilaiTertinggi
            j['nama'] =  x.get('nama')
            j['nim'] = x.get('nim')
    print('Mahasiswa yang memiliki nilai akhir tertinggi yaitu ' + j['nim'] + ' ' + j['nama'])
nilai()