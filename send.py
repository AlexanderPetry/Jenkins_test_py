from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient('192.168.1.205',port=502)
if client.connect():
    print("Connected to PLC")

    
    write_response = client.write_register(address= 0x8000 ,value=1,slave = 1) #to start test
    if write_response.isError():
        print("Error writing registers")
    else:
        print("Write succes")
    time.sleep(1)
    write_response = client.write_register(address= 0x8000 ,value=0,slave = 1)
    client.close()

    time.sleep(180) #90 second wait for batteryresults
    print("Testcase Ress 1.1 Device malfunction:\n")
    response = client.read_holding_registers(address= 0x8001 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers == 1:
        print("BmsState is a Pass (Not Expected)\n")
    elif response.registers == 2:
        print("BmsState is a Error (Expected)\n")
    time.sleep(1)
    print("Testcase Ress 1.2 Power on after HV battery request:\n")
    response = client.read_holding_registers(address= 0x8002 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers == 1:
        print("Battery is on\n")
    elif response.registers == 2:
        print("Battery is off\n")
    time.sleep(1)
    print("Testcase Ress 1.3 Device Insulation error:\n")
    response = client.read_holding_registers(address= 0x8003 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers == 1:
        print("Battery is on\n")
    elif response.registers == 2:
        print("Battery is off\n")
    time.sleep(1)
    print("Testcase Ress 1.4 Communication error:\n")
    response = client.read_holding_registers(address= 0x8004 ,count=1,slave = 1)
    if response.isError():
        print("Error reading registers\n")
    elif response.registers == 1:
        print("BmsState is a Pass (Not Expected)\n")
    elif response.registers == 2:
        print("BmsState is a Error (Expected)\n")
    time.sleep(1)
    
else:
    print("Failed connect")





#example

# response = client.read_holding_registers(address= 0x8000 ,count=2,slave = 1)
    # if response.isError():
    #     print("Error reading registers")
    # else:
    #     print("Register Value: ", response.registers)
    #time.sleep(1)

#  write_response = client.write_register(address= 0x8000 ,value=1,slave = 1)
#     if write_response.isError():
#         print("Error writing registers")
#     else:
#         print("Write succes")
