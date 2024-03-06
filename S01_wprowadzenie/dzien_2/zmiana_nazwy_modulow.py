# import os
# os.getcwd()
# source = r"C:\\Users\\AndrejeI1\\AppData\\Roaming\\JetBrains\\PyCharm2023.2\\scratches\\12.2022_raport_2.docx"
# for i in range(1, 10):
#     if i< 10:
#          i = "0" + str(i)
#
#     target = rf"C:\\Users\\AndrejeI1\\AppData\\Roaming\\JetBrains\\PyCharm2023.2\\scratches\\{i}.2023_raport_3.docx"
#
#     shutil.copyfile(source, target)
#
#

import os

# Zakładając, że masz pliki od slajd1.py do slajd5.py
# i chcesz zmienić ich nazwy na slajd2.py do slajd6.py
for i in range(47, 30, -1):
    print(i)
    stara_nazwa = f'slajd{i}.py'
    nowa_nazwa = f'slajd{i+1}.py'
    print(stara_nazwa, nowa_nazwa)
    os.rename(stara_nazwa, nowa_nazwa)