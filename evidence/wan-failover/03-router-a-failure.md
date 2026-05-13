Router-A(config)#interface g0/0/0
Router-A(config-if)#shutdown
Router-A(config-if)#
*May 13 20:41:45.860: %OSPF-5-ADJCHG: Process 1, Nbr 3.3.3.3 on GigabitEthernet0/0/0 from FULL to DOWN, Neighbor Down: Interface down or detached
Router-A(config-if)#
*May 13 20:41:47.858: %LINK-5-CHANGED: Interface GigabitEthernet0/0/0, changed state to administratively down
*May 13 20:41:48.858: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0, changed state to down

Router-A#sh ip int brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   10.0.100.2      YES NVRAM  administratively down down    
GigabitEthernet0/0/1   10.0.0.249      YES DHCP   up                    up      
GigabitEthernet0/0/2   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0       unassigned      YES NVRAM  administratively down down    
Loopback0              10.0.1.1        YES NVRAM  up                    up      

