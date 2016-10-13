import sh,sys
from netaddr import *
from socket import *
from pysnmp.hlapi import *

community = 'public'
file = "resultat.txt"
SysObjectID = "iso.3.6.1.2.1.1.2.0"
publicCommunity = "public"
transmodeCommunity= "Pub3buc0m"

def get_snmp_enterpriseOID(address_enterpriseOID):
	SysObjectData = str(get_snmp_data(address_enterpriseOID,SysObjectID))
	try:
		enterpriseOID = int(SysObjectData[SysObjectData.find("enterprise")+12:][:(SysObjectData[SysObjectData.find("enterprise")+12:]).find("'")])
	except:
		enterpriseOID = int(SysObjectData[SysObjectData.find("enterprise")+12:][:(SysObjectData[SysObjectData.find("enterprise")+12:]).find(".")])
	return str(enterpriseOID)
	

def get_snmp_data(x,oid):
        errorIndication, errorStatus, errorIndex, varBinds = next(
                getCmd(SnmpEngine(),
                        CommunityData(community, mpModel=0),
#			UdpTransportTarget((x, 161)),
                        UdpTransportTarget((x, 161), timeout=2, retries=0),
                        ContextData(),
                        ObjectType(ObjectIdentity(oid)),
                        )
                )

        if errorIndication:
                print(errorIndication)
        elif errorStatus:
                print('%s at %s' % (
                        errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex)-1][0] or '?'
                        )
                )
        else:
                for varBind in varBinds:
#                        print(' = '.join([ x.prettyPrint() for x in varBind ]))
			return [ x.prettyPrint() for x in varBind ]

def extract_data_OID(original_data):
	data = (str(original_data)[str(original_data).find(", ")+3:])[:((str(original_data)[str(original_data).find(", ")+3:]).find("]"))-1]
	return (data)


####################################### Definition des equipements ##################################################################

def atemedr(equipmt_address):
	sys.stdout.write("Ateme DR ")
	equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.27338.5.2.2.0"))
	equipmt_SerialNumber = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.27338.5.2.3.0"))
	equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.27338.5.6.1.0"))
        return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)

def atemecm(equipmt_address):
        sys.stdout.write("Ateme CM ")
        equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.27338.4.2.2.0"))
        equipmt_SerialNumber = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.27338.4.2.3.0"))
        equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.27338.4.4.1.0"))
        return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)

def atemecmX101(equipmt_address):
        sys.stdout.write("Ateme CMX101 ")
        equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.2.1.1.1.0"))
        equipmt_SerialNumber = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.27338.1.2.1.0"))
        equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.27338.1.2.3.0"))
        return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)

def ericsson(equipmt_address):
	sys.stdout.write("Ericsson ")
	equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.1773.1.1.1.7.0"))
	equipmt_SerialNumber = ""
	equipmt_SoftwareVersion = ""
        equipmt_SerialNumber = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.1773.1.1.3.1.8.0"))
	equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.1773.1.1.3.1.4.0"))
        return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)

def cisco(equipmt_address):
	sys.stdout.write("Cisco ")
        equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.1482.20.1.12.4.0"))
        equipmt_SerialNumber = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.1482.20.1.16.1.1.0"))
        equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.1482.20.1.16.1.6.0"))
#	equipmt_BootCodeVersion = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.1482.20.1.16.1.7.0"))
        return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)

def novelsat(equipmt_address):
        sys.stdout.write("Novelsat ")
        equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.37576.2.3.1.5.1.2.3"))
        equipmt_SerialNumber = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.37576.2.3.2.2.0"))
#	equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.37576.2.3.1.3.0"))
	equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.37576.2.3.1.5.1.2.1"))
        return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)

def nevion(equipmt_address):
        sys.stdout.write("Nevion ")
        equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.22909.1.1.1.1.0"))
	equipmt_SerialNumber = (extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.22909.1.1.1.16.0"))) + "." + (extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.22909.1.1.1.10.0")))
	equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.22909.1.1.1.11.0"))
        return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)

def ntt(equipmt_address):
        sys.stdout.write("NTT ")
	if (str(get_snmp_data(equipmt_address, "iso.3.6.1.2.1.1.5.0")).find("HE5100")) != -1:
		#HE5100
		equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.3930.6.1.1.1.0"))
		equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.3930.6.1.1.4.0"))
	elif (str(get_snmp_data(equipmt_address, "iso.3.6.1.2.1.1.5.0")).find("HVE9100")) != -1:
		#HVE9100
		equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.3930.17.1.1.1.0"))
		equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.3930.17.1.1.4.0"))
	elif (str(get_snmp_data(equipmt_address, "iso.3.6.1.2.1.1.5.0")).find("HVE9200")) != -1:
		#HVE9200
		equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.3930.33.1.1.1.0"))
		equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.3930.33.1.1.4.0"))
	else:
		equipmt_Model = "NTT other"
		equipmt_SoftwareVersion = "n/a"
        return (equipmt_Model, equipmt_SoftwareVersion)

def newtec(equipmt_address):
	if (str(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.5835.5.2.100.1.1.4.0")).find("M6100")) != -1:
                sys.stdout.write("Newtec ")
                equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.5835.5.2.100.1.1.4.0"))
                equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.5835.5.2.100.1.1.9.0"))
                equipmt_SerialNumber = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.5835.5.2.100.1.1.2.0"))
                return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)
	else:
	        sys.stdout.write("Newtec ")
	        equipmt_Model = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.5835.3.1.1.1.12.0.1"))
		equipmt_SoftwareVersion = extract_data_OID(get_snmp_data(equipmt_address, "iso.3.6.1.4.1.5835.3.1.1.1.87.1.1"))
	        equipmt_SerialNumber = extract_data_OID(get_snmp_data(equipmt_address, ".1.3.6.1.4.1.5835.3.1.1.1.31.0.1"))
	        return (equipmt_Model, equipmt_SerialNumber, equipmt_SoftwareVersion)


def run():
	fichier = open(file, "w")
	fichier.write("fqdn,ip,Entr OID,Brand,Model,s/n,SW Version\n")
	print "Scanning..."

	for num in range(start_ip.value,stop_ip.value + 1):
		# declare ip address
		fqdn = IPAddress(num)
		address = str(IPAddress(num))
		# check if host is alive using PING
		sys.stdout.write(address + " ")
	 	try:
			# bash equivalent: ping -c 1 > /dev/null
			sh.ping(address, "-c 1 -w 1", _out="/dev/null")
			sys.stdout.write("ping OK ")
			ping = True
		except sh.ErrorReturnCode_1:
			sys.stdout.write("no ping ")
			dnsName = str(IPAddress(num))
			ping = False
			resultat = address + ",No ping"
		if ping:
			try:
				dnsName = getfqdn(str(fqdn))
				sys.stdout.write(dnsName + " ")
			except:
				sys.stdout.write("no fqdn ")
				dnsName = ""
			try:
				enterpriseOID = int(get_snmp_enterpriseOID (address))
			except:
				enterpriseOID = int(0)
				if ((str(get_snmp_data(address,SysObjectID)).find("zeroDotZero")) != -1):
					enterpriseOID = int(0)
############################### Ateme #############################
			if enterpriseOID == 27338:
				if (str(get_snmp_data(address, "iso.3.6.1.4.1.27338.4.2.2.0")).find("CM5000")) != -1:
                                        marque = "Ateme"
                                        Model, SerialNumber, SoftwareVersion = atemecm(address)
                                        resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
				else:
					marque = "Ateme"
					Model, SerialNumber, SoftwareVersion = atemedr(address)
					resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
############################### Ericsson ##########################
			elif enterpriseOID ==  1773:
				marque = "Ericsson"
				Model, SerialNumber, SoftwareVersion = ericsson(address)
				resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
############################### Cisco ##########################
                        elif enterpriseOID ==  1482:
                                marque = "Cisco"
                                Model, SerialNumber, SoftwareVersion = cisco(address)
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
############################### Novelsat #############################
			elif enterpriseOID == 37576:
                                marque = "Novelsat"
                                Model, SerialNumber, SoftwareVersion = novelsat(address)
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
############################### Nevion #############################
			elif enterpriseOID == 22909:
                                marque = "Nevion"
                                Model, SerialNumber, SoftwareVersion = nevion(address)
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
############################### NTT #############################
                        elif enterpriseOID == 3930:
                                marque = "NTT"
                                Model, SoftwareVersion = ntt(address)
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + ", ," + str(SoftwareVersion)
############################### Newtec/Ateme CM5000  #############################
                        elif enterpriseOID == 8072:
				if (str(get_snmp_data(address, "iso.3.6.1.4.1.27338.4.2.2.0")).find("CM5000")) != -1:
                                        marque = "Ateme"
                                        Model, SerialNumber, SoftwareVersion = atemecm(address)
                                        resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
				elif (str(get_snmp_data(address, "iso.3.6.1.2.1.1.1.0")).find("101")) != -1:
                                        marque = "Ateme"
                                        Model, SerialNumber, SoftwareVersion = atemecmX101(address)
                                        resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
				else:
	                                marque = "Newtec"
	                                Model, SerialNumber, SoftwareVersion = newtec(address)
	                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + str(Model) + "," + str(SerialNumber) + "," + str(SoftwareVersion)
			elif enterpriseOID == 1723:
				marque = "AVCom/LANtronix"
				resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
                        elif enterpriseOID == 21035:
                                marque = "DEV"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
			elif enterpriseOID == 1070:
                                marque = "DEV"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
                        elif enterpriseOID == 17163:
                                marque = "Riverbed"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
                        elif enterpriseOID == 901:
                                marque = "Unknown"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
                        elif enterpriseOID == 8708:
                                marque = "Transmode"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
                        elif enterpriseOID == 18458:
                                marque = "Omnitek"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
                        elif enterpriseOID == 1286:
                                marque = "ECI"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
                        elif enterpriseOID == 4466:
                                marque = "Unkown"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
                        elif enterpriseOID == 2928:
                                marque = "Net Insight"
                                resultat = address + "," + str(enterpriseOID) + "," + str(marque) + "," + "," + ","
			else:
				sys.stdout.write("Brand not found")
				marque = "Ping OK,Brand not found"
				resultat = address + "," + str(enterpriseOID) + "," + str(marque)
#			print resultat
		resultat = str(dnsName) + "," + resultat + "\n"
		fichier.write(resultat)
		sys.stdout.write("\n")
	fichier.close()

if __name__ == '__main__':
	file = str(raw_input('File name: '))
	start_ip = IPAddress(str(raw_input('First IP: ')))
	stop_ip = IPAddress(str(raw_input('Last IP: ')))
	run()