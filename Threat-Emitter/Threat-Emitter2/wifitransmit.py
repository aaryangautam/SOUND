import scapy.all as scapy 
  

def tcpTransmit(input_text):
    packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.TCP(sport=80, dport=80)/scapy.Raw(f"{input_text}")
    packet.show()
    scapy.sendp(packet)
    print("hello")
def udpTransmit(input_text):
    packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.UDP(sport=80, dport=80)/scapy.Raw(f"{input_text}")
    packet.show()
    scapy.sendp(packet)

for i in range(10):
    tcpTransmit("hello")
    udpTransmit("hello")