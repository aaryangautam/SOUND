import scapy.all as scapy 
  

<<<<<<< HEAD
def tcpTransmit(input_text):
    packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.TCP(sport=80, dport=80)/scapy.Raw(f"{input_text}")
    packet.show()
    scapy.sendp(packet, count=100)
    print("hello")
def udpTransmit(input_text):
    packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.UDP(sport=80, dport=80)/scapy.Raw(f"{input_text}")
    packet.show()
    scapy.sendp(packet, count=100)
=======
def wifitransmit(type, input_text):
    if type == "TCP":
        packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.TCP(sport=80, dport=80)/scapy.Raw(f"{input_text}")
        packet.show()
        scapy.sendp(packet)
        #print("hello")
    else:
        packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.UDP(sport=80, dport=80)/scapy.Raw(f"{input_text}")
        packet.show()
        scapy.sendp(packet)
>>>>>>> c2c1c10f77f48671243739732bd28ad2f17c7ad4

# for i in range(10):
#     tcpTransmit("hello")
#     udpTransmit("hello")