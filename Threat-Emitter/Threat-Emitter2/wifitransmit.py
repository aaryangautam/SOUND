import scapy.all as scapy 
  

def wifitransmit(type, input_text):
    if type == "TCP":
        packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.TCP(sport=80, dport=80)/scapy.Raw(f"{input_text}")
        packet.show()
        scapy.sendp(packet, count=100)
        #print("hello")
    else:
        packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.UDP(sport=80, dport=80)/scapy.Raw(f"{input_text}")
        packet.show()
        scapy.sendp(packet, count=100)

for i in range(10):
    wifitransmit("TCP", "hello")
    wifitransmit("UDP", "hello")