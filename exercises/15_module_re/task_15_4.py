# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

import re
def get_ints_without_description(filename):
    result_no_desc = []
    regex = r"interface (?P<intf>\S+)\n( .*\n)"
    with open(filename,'r') as f:
        result = ([match.groups() for match in re.finditer(regex,f.read())])
        for line in result:
            first,*last = line
            if 'description' in ''.join(last):
                continue
            else:
                result_no_desc.append(first)
        return result_no_desc
if __name__ == "__main__":
    print(get_ints_without_description('config_r1.txt'))


'''
import re

def get_ints_without_description(config):
    
    result = []
    with open(config, 'r') as f:
        for line in f:
            match = re.match('interface \S+', line)
            if match:
                intf = str(match.group())
                intf = intf.replace('interface','')
                result.append(intf.strip())
                continue
            match = re.match(' description', line)
            if match:  
                result.pop(-1)
                continue
    return result
    
if __name__ == "__main__":
    result = get_ints_without_description('config_r1.txt')
    print (result)

'''
