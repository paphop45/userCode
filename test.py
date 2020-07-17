# Mass student's userCode generator for API
# Edit records for record amount
# Edit studentCode to change format

records = 5
studentCode = 6100000
i = 0

text_file = open("userCodeList.txt", "w")

while i < records:
	studentCode = studentCode+1
	i = i+1
	print'u' "%d," %studentCode
	text_file.write('U' "%d," %studentCode)

	if i == records:
		break

text_file.close()