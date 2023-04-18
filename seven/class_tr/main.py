from library.kontr_n import KontrN
from library.input_napr import InputNapr
from library.new_file_test import NewFileTest
from library.input_nmod import InputNmod
from library.read_napr import ReadNapr
from library.kontr_napr import KontrNapr

# Создание объектов классов
input_nmod = InputNmod(4)
kontr_n = KontrN("Введите число от 1 до 10: ", range(1, 11))
input_napr = InputNapr()
new_file_test = NewFileTest("filename.txt", "Это первая строка", ["Napr1", "Napr2", "Napr3"])
read_napr = ReadNapr("filename.txt")
kontr_napr = KontrNapr("filename.txt")

# Вызов методов объектов классов
nmod = input_nmod.setNmod()
input_nmod.setKo()
num = kontr_n.setNum()
kontr_n.setKo()
napr = input_napr.setNapr()
new_file_test.createFile()
napr = read_napr.setNapr()
read_napr.setKo()
name_napr = kontr_napr.setNameNapr()
#kontr_napr.setKo()
rn = ReadNapr(kontr_napr.filename)
rn.setKo()


