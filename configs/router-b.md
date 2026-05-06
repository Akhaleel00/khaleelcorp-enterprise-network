Router-B#sh running-config

Building configuration...

  

  

Current configuration : 1950 bytes

!

! Last configuration change at 21:20:27 UTC Tue Apr 28 2026

!

version 16.6

service timestamps debug datetime msec

service timestamps log datetime msec

platform qfp utilization monitor load 80

no platform punt-keepalive disable-kernel-core

!

hostname Router-B

!

boot-start-marker

boot-end-marker

!

!

vrf definition Mgmt-intf

 !

 address-family ipv4

 exit-address-family

 !

 address-family ipv6

 exit-address-family

!         

!         

no aaa new-model

!         

!         

!         

!         

!         

!         

!         

ip domain name khaleel.local

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

subscriber templating

!         

!         

!         

!         

!         

!         

!         

multilink bundle-name authenticated

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

license udi pid ISR4331/K9 sn FLM24440DC5

diagnostic bootup level minimal

spanning-tree extend system-id

!         

!         

!         

username admin privilege 15 secret 5 $1$uLT5$Nb1ZgySwtaYAxocA1Z/gy.

!         

redundancy

 mode none

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

!         

interface Loopback0

 ip address 10.0.2.1 255.255.255.0

!         

interface GigabitEthernet0/0/0

 ip address 10.0.101.2 255.255.255.252

 negotiation auto

!         

interface GigabitEthernet0/0/1

 no ip address

 shutdown 

 negotiation auto

!         

interface GigabitEthernet0/0/2

 no ip address

 negotiation auto

!         

interface GigabitEthernet0

 vrf forwarding Mgmt-intf

 no ip address

 shutdown 

 negotiation auto

!         

router ospf 1

 router-id 2.2.2.2

 network 10.0.2.0 0.0.0.255 area 0

 network 10.0.101.0 0.0.0.3 area 0

!

ip forward-protocol nd

no ip http server

no ip http secure-server

ip tftp source-interface GigabitEthernet0

!

ip ssh version 2

!

!

!

!

!

control-plane

!

!

mgcp behavior rsip-range tgcp-only

mgcp behavior comedia-role none

mgcp behavior comedia-check-media-src disable

mgcp behavior comedia-sdp-force disable

!

mgcp profile default

!

!

!

!

!

!

line con 0

 transport input none

 stopbits 1

line aux 0

 stopbits 1

line vty 0 4

 login local

 transport input ssh

line vty 5 15

 login local

 transport input ssh

!

wsma agent exec

!

wsma agent config

!

wsma agent filesys

!

wsma agent notify

!

!

end