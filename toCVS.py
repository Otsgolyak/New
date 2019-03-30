import xlsxwriter


f = open('text3.txt', 'r')
a = f.readlines()
print(len(a))
data = []
for i in a:
    data1 = []
    data1 = i[:-1]
    data.append(data1)
    # print(data)

print(len(data))

workbook = xlsxwriter.Workbook('links.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write_column('A1', data)

workbook.close()