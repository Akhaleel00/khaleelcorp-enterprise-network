SW-DIST#show running-config interface vlan 10

Building configuration...

  

Current configuration : 124 bytes

!

interface Vlan10

 description RECEPTION-GATEWAY

 ip address 192.168.10.1 255.255.255.0

 ip helper-address 10.0.100.2

end

  

SW-DIST#show running-config interface vlan 20

Building configuration...

  

Current configuration : 124 bytes

!

interface Vlan20

 description SALES-OPS-GATEWAY

 ip address 192.168.20.1 255.255.255.0

 ip helper-address 10.0.100.2

end

  

SW-DIST#show running-config interface vlan 30

Building configuration...

  

Current configuration : 95 bytes

!

interface Vlan30

 description IT-SERVERS-GATEWAY

 ip address 192.168.30.1 255.255.255.0

end

  

SW-DIST#show running-config interface vlan 99

Building configuration...

  

Current configuration : 92 bytes

!

interface Vlan99

 description MANAGEMENT-GATEWAY

 ip address 10.0.99.1 255.255.255.0

end

  

SW-DIST#