import random
import time
import os
import json

def __input():
    i = 0
    list = ""
    hostname = input("Write hostname: ")
    dc = input("Write dc: ")
    rack = input("Write rack: ")
    serial = input ("Write serial: ")
    ip = input("Write IP: ")
    while i < 2:
        result = '{"hostname": "' + hostname + '", "customProperties": {"dc": "'+ dc +'", "rack": "'+ rack +'", "serial": "'+ serial +'", "ip": "'+ ip +'"}}'
        if i < 1:
            list = list + result +" ,"
        else:
            list = list + result
        i = i + 1
#    print ("[%s]"%(list))
    return "["+list+"]"
def main():
    i = 0
    with open("test.json") as file:
        data = file.read()
    y = json.loads(data)
    for item in y:
        print (item)
    print (y)
    file.close()
def test():
    data = __input()
    file = open('test.json','w')
    file.write(data)
    file.close()
#__input()
#test()
main()
