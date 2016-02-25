import os
from sheet import *
from multiprocessing import Pool

filename = 'test2.json'
aa = read_json(filename)

P = Pool(processes=4)
key = "1M3qsO6IkPoVFBHYkqVgDlC18KQmeP9RaU3TbGuFEqk0"
sheet = access_sheet(key)

jobs = [(sheet, worksheet) for worksheet in aa]
# for i in aa:
# 	print i
# 	raw_input()
x = {'worksheet': 'AssetsTbl_Entity1', 'Percentage': '13.0', 'Legend': '', 'Equity': 'International Fixed Interest'}
# P.map(update_sheet, jobs)
# print jobs
filename = 'record'
create_file(filename)
parameter = sheet, x
update_sheet(parameter)
remove_file(filename)