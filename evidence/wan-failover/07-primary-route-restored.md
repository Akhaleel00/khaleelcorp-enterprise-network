Router-A(config-if)#no shutdown
Router-A(config-if)#
*May 13 21:04:39.411: %LINK-3-UPDOWN: Interface GigabitEthernet0/0/0, changed state to down
Router-A(config-if)#
*May 13 21:04:44.479: %LINK-3-UPDOWN: Interface GigabitEthernet0/0/0, changed state to up
*May 13 21:04:45.479: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0, changed state to up
Router-A(config-if)#

SW-DIST#sh ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       + - replicated route, % - next hop override

Gateway of last resort is 10.0.100.2 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 10.0.100.2
      10.0.0.0/8 is variably subnetted, 7 subnets, 3 masks
O        10.0.2.1/32 [110/2] via 10.0.101.2, 02:16:24, GigabitEthernet1/0/3
C        10.0.99.0/24 is directly connected, Vlan99
L        10.0.99.1/32 is directly connected, Vlan99
C        10.0.100.0/30 is directly connected, GigabitEthernet1/0/2
L        10.0.100.1/32 is directly connected, GigabitEthernet1/0/2
C        10.0.101.0/30 is directly connected, GigabitEthernet1/0/3
L        10.0.101.1/32 is directly connected, GigabitEthernet1/0/3
      192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.10.0/24 is directly connected, Vlan10
L        192.168.10.1/32 is directly connected, Vlan10
      192.168.20.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.20.0/24 is directly connected, Vlan20
L        192.168.20.1/32 is directly connected, Vlan20
      192.168.30.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.30.0/24 is directly connected, Vlan30
L        192.168.30.1/32 is directly connected, Vlan30
