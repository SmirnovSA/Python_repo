# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re
def convert_ios_nat_to_asa(filename_ios,filename_asa):
    #ip nat inside source static tcp 10.66.0.13 995 interface GigabitEthernet0/1 995l
    regex = re.compile("(?P<ip>\d+\.\S+)\s(?P<port>\d+)\s\w+\s+\S+\s(?P<port1>\d+)")
    asa_template = (
                "object network LOCAL_{ip}\n"
                " host {ip}\n"
                " nat (inside,outside) static interface service tcp {lport} {outside_port}\n"
    )
    with open(filename_ios,'r') as f:
        for line in f:
            match = regex.search(line)
            if match:
                ip = match.group('ip')
                lport = match.group('port')
                outside_port = match.group('port1')
            with open(filename_asa,'a') as p:
                p.write(asa_template.format(ip=ip,lport=lport,outside_port=outside_port))
if __name__ == "__main__":
    convert_ios_nat_to_asa('cisco_nat_config.txt','cisco_asa_config.txt')
        


