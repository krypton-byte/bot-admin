def vcf(num):
	hasil=''
	for i in num:
		hasil+=f'BEGIN:VCARD\nVERSION:2.1\nN:;{i};;;\nFN:{i}\nTEL;CELL:{i}\nEND:VCARD\n'
	open('dump.vcf','w').write(hasil)
