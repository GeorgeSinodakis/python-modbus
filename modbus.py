import minimalmodbus
import serial

instrument = minimalmodbus.Instrument("COM3", 1) #port, address

instrument.serial.baudrate = 9600         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 2
instrument.serial.timeout  = 0.05          # seconds

instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
instrument.clear_buffers_before_each_transaction = True

temperature = instrument.read_register(289, 1)  # Registernumber, number of decimals
print(temperature)