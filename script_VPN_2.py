import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass()

# my_vpn_2 should be only R1 and R3
IPs = open("my_vpn_2")

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

    tn.write(b"router bgp 1\n")
    tn.write(b"address-family ipv4 vrf OFFICE1\n")
    tn.write(b"redistribute ospf 2\n")
    tn.write(b"exit\n")
    tn.write(b"router ospf 2\n")
    tn.write(b"redistribute bgp 1 subnets\n")
    
    tn.write(b"end\n")
    tn.write(b"wr\n")

print(tn.read_all().decode('ascii'))
