import getpass
import telnetlib

HOST = "192.168.122.71"
user = input("Enter your telnet username: ")
password = getpass.getpass()

print("Configuring Routers " + (HOST))

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"en\n")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"conf t\n")

tn.write(b"int lo0\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"ip ospf 1 area 0\n")
tn.write(b"exit\n")

ports = ["0/1", "0/2", "0/3"]
for idxPort, port in enumerate(ports):
    idxPort = idxPort + 1
    tn.write(b"int g" + str(port).encode('ascii') + b"\n")
    tn.write(b"ip address 192.168.122.10" + str(idxPort).encode('ascii') + b" 255.255.255.0\n")
    tn.write(b"no shut\n")
    tn.write(b"ip ospf 1 area 0\n")
    tn.write(b"mpls ldp autoconfig\n")
    tn.write(b"exit\n")

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
