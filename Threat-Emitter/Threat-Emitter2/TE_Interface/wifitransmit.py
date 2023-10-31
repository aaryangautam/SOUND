import scapy.all as scapy 
  

def wifitransmit():
    packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.IP(dst="255.255.255.255")/scapy.TCP(sport=80, dport=80)
    scapy.sendp(packet)
