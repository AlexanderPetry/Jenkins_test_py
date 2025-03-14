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
    response = client.read_holding_registers(address= 0x8001 ,count=2,slave = 1)
    if response.isError():
        print("Error reading registers")
    else:
        print("Register Value: ", response.registers)
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
