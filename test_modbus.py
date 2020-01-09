import modbus_tk
import serial
import logging
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
import time


ser = serial.Serial('COM3', 9600, bytesize=8, parity='N', stopbits=1)
master = modbus_rtu.RtuMaster(ser)
master.set_timeout(5.0)
master.set_verbose(True)

print("Instrument connected.")

master.execute(2, cst.WRITE_SINGLE_REGISTER, 0x0000, 0x0001)
print("Output on.")

time.sleep(3)

master.execute(2, cst.WRITE_SINGLE_REGISTER, 0x0000, 0x0003)
print("Output off.")

time.sleep(3)

master.close()
print("Instrument disconnected.")

'''

from power_dpm8600_modbus import inst_dpm8600
import time

inst = inst_dpm8600('COM3', 9600, 2)

inst.dpm8600_on()
time.sleep(1)
inst.dpm8600_off()
time.sleep(1)
inst.dpm8600_close()
'''