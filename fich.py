#!/usr/bin/python3

fich = open("/etc/passwd", "r")

users = fich.readlines()

for user in users:
    tokens = user.split(':')
    print(tokens[0] + " usa la shell: " + tokens[-1], end='')
fich.close()
