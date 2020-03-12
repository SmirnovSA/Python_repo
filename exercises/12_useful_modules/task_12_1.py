# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
def ping_ip(ip_address):
    reply = subprocess.run(
        ["ping", "-c", "3", "-n", ip_address],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr
def ping_ip_addresses(ip_address):
    result_ok = []
    result_nok = []
    total = tuple([result_ok] + [result_nok])
    for ip in ip_address:
        success, func_result = ping_ip(ip)
        if success:
            result_ok.append(ip)
        else:
            result_nok.append(ip)
    return total
if __name__ == "__main__":
    ip_address = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    print(ping_ip_addresses(ip_address))



    
