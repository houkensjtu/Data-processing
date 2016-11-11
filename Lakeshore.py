import visa
import time

f = open("log.dat","w")
rm = visa.ResourceManager()

ls = rm.get_instrument("gpib0::12::INSTR")

while True:
    ls.write("KRDG?")
    temp = ls.read()
#    ls.write("DATETIME?")
#    ti = ls.read()
    print(temp[0:15])
    f = open("log.dat","a")
    f.write(temp[0:15] + "\n")
    f.close()
    time.sleep(60)
