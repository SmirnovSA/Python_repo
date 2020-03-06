# -*- coding: utf-8 -*-
"""
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

from task_11_1 import parse_cdp_neighbors
from pprint import pprint
from draw_network_graph import draw_topology
from glob import glob

def create_network_map(filenames):
    result = {}
    files = [ f for f in os.listdir('.') if os.path.isfile(f)]
    for file in filenames:
        with open(file, 'r') as f:
            file = f.read()
            parse_cdp_neighbors(file)
            result.update(file)
    return result
    
def create_network_map(filenames):
    result = {}
    for file in filenames:
        with open(file, 'r') as f:
            file = f.read()
            connection = parse_cdp_neighbors(file)
            result.update(connection)
    return result
if __name__ == "__main__":
    filenames = [f for f in glob('*.txt')]
    pprint(create_network_map(filenames))
#    draw_topology(i)
"""
from task_11_1 import parse_cdp_neighbors
from pprint import pprint
from draw_network_graph import draw_topology
from glob import glob

def create_network_map(filenames):
    result = {}
    data = {}
    for file in filenames:
        with open(file, 'r') as f:
            file = f.read()
            connection = parse_cdp_neighbors(file)
            result.update(connection)
    for key,value in result.items():
        if data.get(value) == key:
            continue
        else:
            data[key] = value
    return data
if __name__ == "__main__":
    filenames = glob('*.txt')
    total = (create_network_map(filenames))
    draw_topology(total)





'''
result = {}
filenames = glob('*.txt')
for file in filenames:
    with open(file, 'r') as f:
        file = f.read()
        connection = parse_cdp_neighbors(file)
        result.update(connection)
data = {}
for key,value in result.items():
    if data.get(value) == key:
        continue
    else:
        data[key] = value
pprint(data)'''


    
    



            

    
