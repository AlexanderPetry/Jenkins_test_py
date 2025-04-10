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

    
    write_response = client.write_register(address= 0x8000 ,value=1,slave = 1) #to start test
    if write_response.isError():
        print("Error writing registers")
    else:
        print("Write succes")
    time.sleep(1)
   
    time.sleep(600) #90 second wait for batteryresults
    print("Testcase Ress 1.1 Device malfunction:\n")
    response = client.read_holding_registers(address= 0x8001 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers[0] == 1:
        print("PASS: BmsState is in error state\n")
    elif response.registers[0] == 2:
        print("FAILED: BMS isnt in error state\n")
    else:
        print("failed: " ,response.registers)
    time.sleep(1)
    print("Testcase Ress 1.2 Power on after HV battery request:\n")
    response = client.read_holding_registers(address= 0x8002 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers[0] == 1:
        print("PASSED: Battery is on\n")
    elif response.registers[0] == 2:
        print("FAILED: Battery is off\n")
    else:
        print("failed: " ,response.registers)
    time.sleep(1)
    print("Testcase Ress 1.3 Device Insulation error:\n")
    response = client.read_holding_registers(address= 0x8003 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers[0] == 1:
        print("PASSED: Battery is off\n")
    elif response.registers[0] == 2:
        print("FAILED: Battery is on\n")
    else:
        print("failed: " ,response.registers)    
    time.sleep(1)
    print("Testcase Ress 1.4 Communication error:\n")
    response = client.read_holding_registers(address= 0x8004 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers[0] == 1:
        print("PASSED: BmsState is in ERROR state\n")
    elif response.registers[0] == 2:
        print("FAILED:BMS isnt in error state\n")
    else:
        print("failed: " ,response.registers)
    time.sleep(1)
    
    client.close()
else:
    print("Failed connect")






