# READ ME
# Receiving 0 means that there is a communication error with modbus self
# Receiving 1 means current Test Passed and wanted result happend
# Receiving 2 means current Test Failed

from pymodbus.client import ModbusTcpClient
import time

time.sleep(60)
client = ModbusTcpClient('192.168.1.205',port=502)
if client.connect():
    print("Connected to PLC")


    write_response = client.write_register(address= 0x8000 ,value=3,slave = 1) #to start test
    if write_response.isError():
        print("Error writing registers")
    else:
        print("Write succes")
    time.sleep(1)

    time.sleep(600) #600 second wait for batteryresults
    print("Testcase Estop 1.1 Default situation:\n")
    response = client.read_holding_registers(address= 0x8001 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers[0] == 1:
        print("PASS: Estops are okay\n")
    elif response.registers[0] == 2:
        print("FAILED: Estops are in error mode\n")
    else:
        print("failed: " ,response.registers)
    time.sleep(1)