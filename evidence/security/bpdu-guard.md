SW-ACCESS#sh running-config int fa0/1

Building configuration...

  

Current configuration : 316 bytes

!

interface FastEthernet0/1

 switchport access vlan 10

 switchport mode access

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 switchport port-security mac-address sticky 6c1f.f71b.6c74

 spanning-tree portfast

 spanning-tree bpduguard enable

end

  

SW-ACCESS#sh running-config int fa0/9

Building configuration...

  

Current configuration : 352 bytes

!

interface FastEthernet0/9

 switchport access vlan 20

 switchport mode access

 switchport port-security maximum 2

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 switchport port-security mac-address sticky 6c1f.f71b.6c74

 spanning-tree portfast

 spanning-tree bpduguard enable

end