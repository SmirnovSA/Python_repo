# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.
"Protocol:", "OSPF",
                            "Prefix:", values[1],
                            "AD/Metric:", values[2],
                            "Next-Hop:", values[4],
                            "Last update:", values[5],
                            "Outbound Interface:", values[6])
"""
output = "\n{:25} {}" * 6
with open('ospf.txt', 'r') as f:
    for line in f:
        values = line.split()
        print(output.format("Protocol:", "OSPF",
                            "Prefix:", values[1],
                            "AD/Metric:", values[2],
                            "Next-Hop:", values[4],
                            "Last update:", values[5],
                            "Outbound Interface:", values[6],))


    
            
        
            
            

    
