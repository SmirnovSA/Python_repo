# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
'''from pprint import pprint
def get_int_vlan_map(intf, vlan):
    with open('config_sw1.txt', 'r') as f:
    for line in f:
        if 'FastEthernet' in line:
            intf = line.split()[-1]
        if 'access vlan' in line:
            vlan = line.split()[-1]
            result[intf] = vlan
        if 'allowed vlan' in line:
            vlan = line.split()[-1]

    return result
pprint(generate_trunk_config(trunk_config, trunk_mode_template))



zip

'''
from pprint import pprint
def get_int_vlan_map(config_filename):
    with open(config_filename, 'r') as f:
        dict1 = {}
        dict2 = {}
        for line in f:
            if 'FastEthernet' in line:
                intf = line.split()[-1]
            if 'access vlan' in line:
                vlan = int(line.split()[-1])
                dict1[intf] = vlan
            if 'allowed vlan' in line:
                vlan = line.split()[-1].split(',')
                vlan = [int(x) for x in vlan]
                dict2[intf] = vlan
            result = (dict1,dict2)
        return result
pprint(get_int_vlan_map('config_sw1.txt'))



