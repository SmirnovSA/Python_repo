# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.
result = {}
    for intf,vlan in intf_vlan_mapping.items():
        vlan = ','.join(str(x) for x in vlan)
        for command in trunk_template:
            result[intf] = (f'{command}')
            if command.endswith('allowed vlan'):
                 result[intf] = (f'{command} {vlan}')
    return result
"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

from pprint import pprint
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = {}
    for intf,vlan in intf_vlan_mapping.items():
        result[intf] = {}
        vlan = ','.join(str(x) for x in vlan)
        value = []
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                value.append(f'{command} {vlan}')
            else:
                value.append(command)
        result[intf] = value
    return result
pprint(generate_trunk_config(trunk_config, trunk_mode_template))
