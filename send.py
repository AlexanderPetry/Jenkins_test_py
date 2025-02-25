import pyads
#192.168.1.120.1.1 #5.108.194.44.1.1
AMSNETID = '5.108.194.44.1.1'
#IP =  '169.254.0.76'
#LocalNetID = '192.168.1.120.1.1'

plc = pyads.Connection(AMSNETID,pyads.PORT_TC3PLC1)
#print('Connecting to TwinCAT PLC..')
plc.open()
print('Current connection status:',plc.is_open)
print('Current Status:',plc.read_state())

device_name, version = plc.read_device_info()
print(str(device_name) + ' ' + str(version))

#read a boolean
bReadCommand = plc.read_by_name('MAIN.bReadCmd', pyads.PLCTYPE_BOOL)
print(bReadCommand)

#write ack
plc.write_by_name('MAIN.bACKFromPython', bReadCommand)

#read int number
int_number = plc.read_by_name('MAIN.nMyNumber', pyads.PLCTYPE_INT)
print(int_number)

#read real number
real_number = plc.read_by_name('MAIN.fMyRealNumber', pyads.PLCTYPE_REAL)
print(real_number)

#read string
message_from_twincat = plc.read_by_name('MAIN.sMessageToPython', pyads.PLCTYPE_STRING)
print(message_from_twincat)

#write string
if len(message_from_twincat) > 1:
    message_to_twincat = 'Hi TwinCAT! I KNOW YOUR SECRETS'
    plc.write_by_name('MAIN.sMessageFromPython', message_to_twincat, plc_datatype=pyads.PLCTYPE_STRING)

# close connection
plc.close()
