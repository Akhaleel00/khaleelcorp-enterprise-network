Router-B>sh ip route

Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP

       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 

       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2

       E1 - OSPF external type 1, E2 - OSPF external type 2

       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2

       ia - IS-IS inter area, * - candidate default, U - per-user static route

       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP

       a - application route

       + - replicated route, % - next hop override, p - overrides from PfR

  

Gateway of last resort is 10.0.101.1 to network 0.0.0.0

  

O*E2  0.0.0.0/0 [110/1] via 10.0.101.1, 00:24:23, GigabitEthernet0/0/0

      10.0.0.0/8 is variably subnetted, 7 subnets, 3 masks

O        10.0.1.1/32 [110/3] via 10.0.101.1, 00:24:23, GigabitEthernet0/0/0

C        10.0.2.0/24 is directly connected, Loopback0

L        10.0.2.1/32 is directly connected, Loopback0

O        10.0.99.0/24 [110/2] via 10.0.101.1, 00:36:10, GigabitEthernet0/0/0

O        10.0.100.0/30 [110/2] via 10.0.101.1, 00:24:23, GigabitEthernet0/0/0

C        10.0.101.0/30 is directly connected, GigabitEthernet0/0/0

L        10.0.101.2/32 is directly connected, GigabitEthernet0/0/0

O     192.168.10.0/24 [110/2] via 10.0.101.1, 00:36:10, GigabitEthernet0/0/0

O     192.168.20.0/24 [110/2] via 10.0.101.1, 00:36:10, GigabitEthernet0/0/0

O     192.168.30.0/24 [110/2] via 10.0.101.1, 00:36:10, GigabitEthernet0/0/0

Router-B>