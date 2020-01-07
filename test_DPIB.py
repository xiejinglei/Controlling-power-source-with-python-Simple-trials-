import visa
import time

rm = visa.ResourceManager()
print(rm.list_resources())

my_instrument = rm.open_resource('GPIB0::5::INSTR')

print('*IDN?')
print(my_instrument.query('*IDN?'))

print('*RST')
my_instrument.write('*RST')

print('OUTPut1:STATe 1')
my_instrument.write('OUTPut1:STATe 1')

time.sleep(1)

my_instrument.write('VOLT 10')  #reaches the working voltage of DPM8600
print(my_instrument.query("MEAS:VOLT:ACDC?"))
print(my_instrument.query("FETC:VOLT:DC?"))

time.sleep(5)

my_instrument.write('VOLT 3')
print(my_instrument.query("MEAS:VOLT:ACDC?"))
print(my_instrument.query("FETC:VOLT:DC?"))

time.sleep(1)

print('OUTPut1:STATe 0')
my_instrument.write('OUTPut1:STATe 0')

print('*RST')
my_instrument.write('*RST')

print(my_instrument.query("SYSTem:ERRor?"))
