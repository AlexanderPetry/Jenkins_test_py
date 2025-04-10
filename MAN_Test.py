# READ ME
# Receiving 0 means current Test Passed
# Receiving 1 means current Test Passed
# If Bit 9 isnt 1 then then previous statements could have happend because of a Communication Error

from pymodbus.client import ModbusTcpClient
import time
import sys

time.sleep(60)
client = ModbusTcpClient('192.168.1.205',port=502)
if client.connect():
    print("Connected to PLC")

    
    write_response = client.write_register(address= 0x8000 ,value=2,slave = 1) #to start test
    if write_response.isError():
        print("Error writing registers")
    else:
        print("Write succes")
    
    

    time.sleep(900) #90 second wait for batteryresults
    print("Testcase MAN-8 & 9 : Propulsion enable command\n")
    response = client.read_holding_registers(address= 0x8001 ,count=1,slave = 1)
    Answer = bin(response.registers[0])
    SizeOfAnswer = len(Answer)
    
   
    
    if SizeOfAnswer > 9:
        print("No Communication Error Check \n")
        
        print("Horn went off "  + Answer[SizeOfAnswer-1] + "\n")
        print("Vehicle Drives " + Answer[SizeOfAnswer-2]+"\n")
        print("Vehicle doesnt Drive " + Answer[SizeOfAnswer-3]+"\n")
    else:
        print("Communication Error Check \n")
    
    time.sleep(1)
    print("Testcase MAN-1 : Steering behaviour\n")
    response = client.read_holding_registers(address= 0x8002 ,count=1,slave = 1)
    Answer = bin(response.registers[0])
    SizeOfAnswer = len(Answer)
    
    
    
    if SizeOfAnswer > 9:
        print(" No Communication Error Check \n")
        
        print("Steering stick goes left (MAX 10 deg) "  + Answer[SizeOfAnswer-1] + "\n")
        print("Log check if Axle actual turns "  + Answer[SizeOfAnswer-2] + "\n")
        print("Steering stick goes right (MAX 10 deg) " + Answer[SizeOfAnswer-3]+"\n")
        print("Log check if Axle actual turns "  + Answer[SizeOfAnswer-4] + "\n")
    else:
        print(" Communication Error Check \n")
    
    time.sleep(1)
    print("Testcase MAN-2..7 : Speed behaviour\n")
    response = client.read_holding_registers(address= 0x8003 ,count=1,slave = 1)
    Answer = bin(response.registers[0])
    SizeOfAnswer = len(Answer)
    
    if SizeOfAnswer > 9:
        print("No Communication Error Check \n")
        
        print("1: 0.1m/s 2: 1m/s 3: 2m/s 4: 3m/s\n")

        print("Need Can card so temp offline\n")
        # print("Forwards speed 1 "  + Answer[SizeOfAnswer-1] + "\n")
        # print("Forwards speed 2 " + Answer[SizeOfAnswer-2]+"\n")
        # print("Forwards speed 3 " + Answer[SizeOfAnswer-3]+"\n")
        # print("Forwards speed 4 " + Answer[SizeOfAnswer-4]+"\n")
        # print("Backwards speed 1 " + Answer[SizeOfAnswer-5]+"\n")
        # print("Backwards speed 2 " + Answer[SizeOfAnswer-6]+"\n")
        # print("Backwards speed 3 " + Answer[SizeOfAnswer-7]+"\n")
        # print("Backwards speed 4 " + Answer[SizeOfAnswer-8]+"\n")
    else:
        print("Communication Error Check \n")
    
    time.sleep(1)
    print("Testcase MAN-10..13 : Steering modes\n")
    response = client.read_holding_registers(address= 0x8004 ,count=1,slave = 1)
    Answer = bin(response.registers[0])
    SizeOfAnswer = len(Answer)
    
    if SizeOfAnswer > 9:
        print("No Communication Error Check \n")
        print("Vehicle steers in crab mode "  + Answer[SizeOfAnswer-1] + "\n")
        print("Vehicle steers anti parallel " + Answer[SizeOfAnswer-2]+"\n")
        print("Only the front axle steers " + Answer[SizeOfAnswer-3]+"\n")
        print("Only the rear axle steers " + Answer[SizeOfAnswer-4]+"\n")
    else:
        print("Communication Error Check \n")
    
    time.sleep(1)
    print("Testcase MAN-14 : Release park brake\n")
    response = client.read_holding_registers(address= 0x8005 ,count=1,slave = 1)
    Answer = bin(response.registers[0])
    SizeOfAnswer = len(Answer)
    
   
    
    if SizeOfAnswer > 9:
        print("No Communication Error Check \n")
        print("Park Brake Release "  + Answer[SizeOfAnswer-1] + "\n")
    else:
        print("Communication Error Check \n")
    
    time.sleep(1)
    print("Testcase MAN-15 : Horn\n")
    response = client.read_holding_registers(address= 0x8006 ,count=1,slave = 1)
    Answer = bin(response.registers[0])
    SizeOfAnswer = len(Answer)

    
    if SizeOfAnswer > 9:
        print("No Communication Error Check \n")
        
        print("Horn went off "  + Answer[SizeOfAnswer-1] + "\n")
    else:
        print("Communication Error Check \n")
    
    
    time.sleep(1)
    response = client.read_holding_registers(address= 0x8000 ,count=1,slave = 1)
    while response != 0:
        time.sleep(1)
        
    client.close()
