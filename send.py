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
Test_case = plc.read_by_name('MAIN.ID_Number', pyads.PLCTYPE_USINT)
""""
	ElectricalLimits_ID: UDINT := 16#18FFCAF3;
	ElectricalLimits_Length: USINT := 8;
	
	ElectricalLimits_rx0: USINT := 255;
	ElectricalLimits_rx1: USINT := 147;
	ElectricalLimits_rx2: USINT := 150;
	ElectricalLimits_rx3: USINT := 0;
	ElectricalLimits_rx4: USINT := 255;
	ElectricalLimits_rx5: USINT := 140;
	ElectricalLimits_rx6: USINT := 255;
	ElectricalLimits_rx7: USINT := 80;

	ElectricalPackCharac_ID: UDINT := 16#18FFC9F3;
	ElectricalPackCharac_Length: USINT := 6;
	ElectricalPackCharac_rx1: USINT := 136;
	ElectricalPackCharac_rx0: USINT := 136;
	ElectricalPackCharac_rx2: USINT := 107;
	ElectricalPackCharac_rx3: USINT := 255;
	ElectricalPackCharac_rx4: USINT := 36;
	ElectricalPackCharac_rx5: USINT := 201;

	ElectricalSystemCharac_ID: UDINT := 16#18FFC1F3;
	ElectricalSystemCharac_Length: USINT := 8;
	ElectricalSystemCharac_rx0: USINT := 120;
	ElectricalSystemCharac_rx1: USINT := 110;
	ElectricalSystemCharac_rx2: USINT := 255;
	ElectricalSystemCharac_rx3: USINT := 140;
	ElectricalSystemCharac_rx4: USINT := 255;
	ElectricalSystemCharac_rx5: USINT := 210;
	ElectricalSystemCharac_rx6: USINT := 125;
	ElectricalSystemCharac_rx7: USINT := 120;
	
	EnergyUsed_ID: UDINT := 16#18FFCDF3;
	EnergyUsed_Lenght: USINT := 1;
	EnergyUsed_rx0: USINT := 64;
	
	ElectricalCellCharacVol1_ID: UDINT := 16#18FFC3F3;
	ElectricalCellCharacVol1_Lenght: USINT := 8;
	ElectricalCellCharacVol1_rx0: USINT := 60;
	ElectricalCellCharacVol1_rx1: USINT := 50;
	ElectricalCellCharacVol1_rx2: USINT := 180;
	ElectricalCellCharacVol1_rx3: USINT := 190;
	ElectricalCellCharacVol1_rx4: USINT := 20;
	ElectricalCellCharacVol1_rx5: USINT := 10;
	ElectricalCellCharacVol1_rx6: USINT := 100;
	ElectricalCellCharacVol1_rx7: USINT := 150;
	
	ElectricalCellCharacVol2_ID: UDINT := 16#18FFC4F3;
	ElectricalCellCharacVol2_Lenght: UINT := 6;
	ElectricalCellCharacVol2_rx0: USINT := 130;
	ElectricalCellCharacVol2_rx1: USINT := 100;
	ElectricalCellCharacVol2_rx2: USINT := 65;
	ElectricalCellCharacVol2_rx3: USINT := 145;
	ElectricalCellCharacVol2_rx4: USINT := 50;
	ElectricalCellCharacVol2_rx5: USINT := 20;
	
	

	
	Contineus_NonContineusCharac_ID: UDINT := 16#18FFC2F3;
	Contineus_NonContineusCharac_Lenght: UINT := 8;
	Contineus_NonContineusCharac_rx0: USINT := 180;
	Contineus_NonContineusCharac_rx1: USINT := 165;
	Contineus_NonContineusCharac_rx2: USINT := 60;
	Contineus_NonContineusCharac_rx3: USINT := 123;
	Contineus_NonContineusCharac_rx4: USINT := 36;
	Contineus_NonContineusCharac_rx5: USINT := 114;
	Contineus_NonContineusCharac_rx6: USINT := 136;
	Contineus_NonContineusCharac_rx7: USINT := 77;

	ChargeCharac_ID: UDINT := 16#18FFC5F3;
	ChargeCharac_Lenght: UINT := 4;
	ChargeCharac_rx0: USINT := 145;
	ChargeCharac_rx1: USINT := 96;
	ChargeCharac_rx2: USINT := 70;
	ChargeCharac_rx3: USINT := 125;

	PackStatusInformation_ID: UDINT := 16#18FFCEF3;
	PackStatusInformation_Length: UINT := 5;
	PackStatusInformation_rx0: USINT := 125;
	PackStatusInformation_rx1: USINT := 2#01110011;
	PackStatusInformation_rx2: USINT := 95;
	PackStatusInformation_rx3: USINT := 2#00101011;
	PackStatusInformation_rx4: USINT := 182;
	
	TMSSTATUS_rx7: USINT := 2#01000010;
	TMSSTATUS_rx6: USINT := 170;
	TMSSTATUS_rx4: USINT := 130;
	TMSSTATUS_rx2: USINT := 200;
	TMSSTATUS_rx1: USINT := 120;
	TMSSTATUS_rx0: USINT := 2#1111;
	TMSSTATUS_lenght: UINT := 8;
	TMSSTATUS_ID: UDINT := 16#18FFC13A;
	BMSState_rx7: USINT := 2#00001111;
	BMSState_rx3: USINT := 2#00001010;
	BMSState_rx2: USINT := 2#00001011;
	BMSState_rx1: USINT := 2#11011111;
	BMSState_rx0: USINT := 2#1101001;
	BMSState_Length: UINT := 8;
	BMSState_ID: UDINT := 16#CFFC8F3;
	ElectricalCellCharac_rx5: USINT := 125;
	ElectricalCellCharac_rx4: USINT := 145;
	ElectricalCellCharac_rx3: USINT := 120;
	ElectricalCellCharac_rx2: USINT := 170;
	ElectricalCellCharac_rx1: USINT := 185;
	ElectricalCellCharac_rx0: USINT := 124;
	ElectricalCellCharac_Lenght: UINT := 6;
	ElectricalCellCharac_ID: UDINT := 16#18FFCBF3;
	ParametersPhysicalBattery_rx7: USINT := 2#0101;
	ParametersPhysicalBattery_rx5: USINT := 100;
	ParametersPhysicalBattery_rx4: USINT := 50;
	ParametersPhysicalBattery_rx3: USINT := 180;
	ParametersPhysicalBattery_rx2: USINT := 100;
	ParametersPhysicalBattery_rx1: USINT := 2#101100;
	ParametersPhysicalBattery_rx0: USINT := 2#10010110;
	ParametersPhysicalBattery_Length: UINT := 8;
	ParametersPhysicalBattery_ID: UDINT := 16#18FFC0F3;
"""

#write ack
plc.write_by_name('MAIN.ID_Number', 1)
Test_case = plc.read_by_name('MAIN.ID_Number', pyads.PLCTYPE_USINT)

Test_case = plc.read_by_name('MAIN.ID_Number', pyads.PLCTYPE_USINT)
seen_cases = set();
while Test_case in {0,1,2}:
	match Test_case:
		case 0 if 0 not in seen_cases:
			print("Current TestCase is " + str(Test_case))
			print("Nothing is getting tested")
			seen_cases.add(0)
		case 1 if 1 not in seen_cases:
			print("Current TestCase is " +str(Test_case))
			print("HV battery is getting tested")
			seen_cases.add(1)
		case 2 if 2 not in seen_cases:
			print("Current TestCase is " +str(Test_case))
			print("MCD is getting tested")
			seen_cases.add(2)
		# case _:
		# 		print("ERROR OUTOFBOUND ID NUMBER")
