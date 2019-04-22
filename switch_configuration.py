import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass()

IPs = open("myswitches")

for idxIP, IP in enumerate(IPs):
    idxIP = idxIP + 1
    IP = IP.strip()
    print("Configuring Switch " + (IP))

    HOST = IP
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"en\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")

    tn.write(b"int lo0\n")
    tn.write(b"ip add " + str(idxIP).encode('ascii') + "." + str(idxIP).encode('ascii') + "." + str(idxIP).encode('ascii') + "." + str(idxIP).encode('ascii') + " 255.255.255.255\n")
    tn.write(b"ip ospf 1 area 0\n")
    tn.write(b"exit\n")

    ports = ["0/0", "0/1", "0/2", "0/3", "1/0", "1/1", "1/2", "1/3", "2/0", "2/1"]

    for idxPort, port in enumerate(ports):
        tn.write(b"int g" + str(port).encode('ascii') + "\n")
        tn.write(b"ip address 192.168.122.1" + str(idxIP).encode('ascii') + str(idxPort).encode('ascii') + "\n")
        tn.write(b"no shut\n")
        tn.write(b"ip ospf 1 area 0\n")
        tn.write(b"exit\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
