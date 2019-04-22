import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass()

# my_vpn_1 should be only R1 and R3
IPs = open("my_vpn_1")

for idxIP, IP in enumerate(IPs):
    IP = IP.strip()
    print("Configuring VPN " + (IP))

    HOST = IP
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"en\n")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")

    tn.write(b"ip vrf OFFICE1\n")
    tn.write(b"rd 4:4\n")
    tn.write(b"route-target both 4:4\n")

    ports = ['f0/0', 'f0/1', 'f1/0', 'f1/1', 'g2/0']
    for idxPort, port in enumerate(ports):
    	tn.write(b"int " + str(port).encode('ascii') + b"\n")
    	tn.write(b"ip vrf forwarding OFFICE1\n")
    	tn.write(b"int " + str(port).encode('ascii') + b"\n")
    	# tn.write(b"ip add 192.168.1.1 255.255.255.255\n")
    	tn.write(b"ip ospf 2 area 2\n")

    tn.write(b"end\n")
    tn.write(b"wr\n")

print(tn.read_all().decode('ascii'))
