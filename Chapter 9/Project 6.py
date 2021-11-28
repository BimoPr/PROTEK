nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("======================================================================")
print('|', 'NIM'.ljust(10), 'NAMA'.ljust(10), 'N.MID'.rjust(12), 'N.UAS'.rjust(10), 'N.AKHIR'.rjust(10), 'STATUS'.rjust(9), '|')

print("----------------------------------------------------------------------")

for data in nilai:
    nilaiAkhir = (data['mid'] + (2 * data['uas'])) / 3
       
    data['nilaiAkhir'] = round(nilaiAkhir, 1)

    if nilaiAkhir >= 60:
        data['status'] = 'LULUS'
    else:
        data['status'] = 'TIDAK LULUS'

    print('|', data['nim'].ljust(10),
          data['nama'].ljust(10),
          str(data['mid']).rjust(10),
          str(data['uas']).rjust(10),
          str(data['nilaiAkhir']).rjust(10), ''.rjust(5),
          data['status'].ljust(5), '|')

print("======================================================================")

