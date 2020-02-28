# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
 """
ip = input('Введите адрес в формате x.x.x.x: ')
octet = ip.split('.')
oct1,oct2,oct3,oct4 = [
int(octet[0]),
int(octet[1]),
int(octet[2]),
int(octet[3])]
if oct1 >=1 and oct1 <= 223:
    print('Unicast')
elif oct1 >=224 and oct1 <= 239:
    print('Multicast')
elif ip == '0.0.0.0':
    print('unassigned')
elif ip == '255.255.255.255':
    print('local broadcast')
else:
    print('unused')


    
    

    
    
        
