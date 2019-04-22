import getpass
import telnetlib

HOST = "localhost"
# user = input("Enter your telnet username: ")
password = getpass.getpass()

# my_QoS should be only R1, R2 and R3
IPs = open("my_QoS")

for idxIP, IP in enumerate(IPs):
    IP = IP.strip()
    print("Configuring QoS " + (IP))

    HOST = IP
    tn = telnetlib.Telnet(HOST)

    #tn.read_until(b"Username: ")
    #tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"en\n")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")

    tn.write(b"class-map match-all ef\n")
    tn.write(b"match ip dscp ef\n")
    tn.write(b"match ip dscp cs6\n")
    tn.write(b"class-map match-all cs6\n")
    tn.write(b"match ip dscp cs6\n")
    tn.write(b"exit\n")

    if idxIP == 1:
        ports = ["f0/0", "f0/1"]
    else:
        ports = ["f0/0"]

    for idxPort, port in enumerate(ports):
        tn.write(b"policy-map TO_CUSTMRSITE1\n")
        tn.write(b"class ef\n")
        tn.write(b"priority percent 15\n")
        tn.write(b"class cs6\n")
        tn.write(b"bandwidth remaining percent 15\n")
        tn.write(b"int " + str(port).encode('ascii') + b"\n")
        tn.write(b"service-policy output TO_CUSTMRSITE1\n")

    tn.write(b"end\n")
    tn.write(b"wr\n")

print(tn.read_all().decode('ascii'))
