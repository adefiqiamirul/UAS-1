from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("data.xls")
wb = copy(rb)
s = wb.get_sheet(0)

s.write(1.0,'Ade')
s.write(1.1,'Jl. Sunan Gj')
s.write(1.2,'Cirebon')

s.write(2.0,'Fiqi')
s.write(2.1,'Jl. Harapan')
s.write(2.2,'Majalengka')

s.write(3.0,'Amirul')
s.write(3.1,'Jl. Klayan')
s.write(3.2,'Kuningan')

wb.save("data.xls")