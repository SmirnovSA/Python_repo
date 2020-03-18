# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды l.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку,
а затем передать строку как аргумент функции.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
"""
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
"""

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from pprint import pprint
'''def parse_cdp_neighbors(command_output):
    dict1 = {}
    for line in command_output.split('\n'):
        device = ','.join([s for s in line.split() if s.isdigit() and len(s) == 3])
        if device in line.split():
            device = line.split()[0:1]
            intf_switch = (line.split()[1] + line.split()[2]).split()
            intf_rout = (line.split()[-2] + line.split()[-1]).split()
            listkey = tuple(device + intf_rout)
            listval = tuple(switch + intf_switch)
            dict1[listval] = listkey
        elif '>' in line:
            switch = [line.split()[0].replace('>show','')]
    return dict1
if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt', 'r') as f:
        command_output = f.read()
        pprint(parse_cdp_neighbors(command_output))
'''
def parse_cdp_neighbors(command_output):
    result = {}
    for line in command_output.split("\n"):
        line = line.strip()
        if ">" in line:
            hostname = line.split(">")[0]
        elif line and line[-1].isdigit():
            # В other собираются все остальные элементы,
            # которые явно не присваиваются
            r_host, l_int, l_int_num, *other, r_int, r_int_num = line.split()
            result[(hostname, l_int + l_int_num)] = (r_host, r_int + r_int_num)
    return result
if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt', 'r') as f:
        command_output = f.read()
        pprint(parse_cdp_neighbors(command_output))



    
