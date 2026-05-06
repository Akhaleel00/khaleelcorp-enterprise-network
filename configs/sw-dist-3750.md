SW-DIST#sh running-config

Building configuration...

  

Current configuration : 4425 bytes

!

! Last configuration change at 00:24:03 UTC Mon Mar 1 1993

!

version 15.0

no service pad

service timestamps debug datetime msec

service timestamps log datetime msec

no service password-encryption

!

hostname SW-DIST

!

boot-start-marker

boot-end-marker

!

!

!

username admin privilege 15 secret 5 $1$MGB/$I77iFH7RLmTxAr3XpY9ct/

no aaa new-model

switch 1 provision ws-c3750g-24ts-1u

system mtu routing 1500

ip routing

ip domain-name khaleel.local

!         

!         

!         

!         

!         

crypto pki trustpoint TP-self-signed-3409861632

 enrollment selfsigned

 subject-name cn=IOS-Self-Signed-Certificate-3409861632

 revocation-check none

 rsakeypair TP-self-signed-3409861632

!         

!         

crypto pki certificate chain TP-self-signed-3409861632

 certificate self-signed 01

  3082022B 30820194 A0030201 02020101 300D0609 2A864886 F70D0101 05050030 

  31312F30 2D060355 04031326 494F532D 53656C66 2D536967 6E65642D 43657274 

  69666963 6174652D 33343039 38363136 3332301E 170D3933 30333031 30303032 

  34335A17 0D323030 31303130 30303030 305A3031 312F302D 06035504 03132649 

  4F532D53 656C662D 5369676E 65642D43 65727469 66696361 74652D33 34303938 

  36313633 3230819F 300D0609 2A864886 F70D0101 01050003 818D0030 81890281 

  8100C2A8 CE899665 97EC4BC0 9449666D 487514F1 6FE61756 C54A671F 1E756D3F 

  1BE03474 801585B2 9E59C256 4D559A81 050F1035 82E9DF7D 821880E5 8211FEC6 

  89646A92 807D3CE5 D32E38E8 39418C20 51AE5590 4382346A A188B316 4BC86507 

  25BCC32B 64718FC7 52AEDE21 ADCD39A6 0D4EDEA5 6F3586C5 0B581C91 2A3E9565 

  3EC70203 010001A3 53305130 0F060355 1D130101 FF040530 030101FF 301F0603 

  551D2304 18301680 14CAAEAA DEE0850C E0814724 7DB7003A 4FB7B5A7 98301D06 

  03551D0E 04160414 CAAEAADE E0850CE0 8147247D B7003A4F B7B5A798 300D0609 

  2A864886 F70D0101 05050003 81810033 12569DC5 879CE66F 05A662D2 E9B763FC 

  33743741 3BD6E7A9 D55F645C 031BA872 08F630E3 D3FABCD6 82295AD8 2D3F6217 

  BE849F73 787C85EE 5F301829 AAA54D96 232C9649 824AD858 333E407D 723579A6 

  CA900869 1C03448F E9E35CF2 17AF7684 270AC6EC 20BAF902 D1C18E0C FE64A9F7 

  9C73A3C0 A7305DC8 BFA923EA 8EF354

        quit

!         

!         

!         

!         

!         

!         

spanning-tree mode pvst

spanning-tree extend system-id

spanning-tree vlan 10,20,30,99 priority 4096

!         

vlan internal allocation policy ascending

!         

ip ssh version 2

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

interface GigabitEthernet1/0/1

 switchport trunk encapsulation dot1q

 switchport trunk allowed vlan 10,20,30,99

 switchport mode trunk

!         

interface GigabitEthernet1/0/2

 no switchport

 ip address 10.0.100.1 255.255.255.252

 ip ospf 1 area 0

!         

interface GigabitEthernet1/0/3

 no switchport

 ip address 10.0.101.1 255.255.255.252

 ip ospf 1 area 0

!         

interface GigabitEthernet1/0/4

!         

interface GigabitEthernet1/0/5

!         

interface GigabitEthernet1/0/6

!         

interface GigabitEthernet1/0/7

!         

interface GigabitEthernet1/0/8

!         

interface GigabitEthernet1/0/9

!         

interface GigabitEthernet1/0/10

!         

interface GigabitEthernet1/0/11

!         

interface GigabitEthernet1/0/12

!         

interface GigabitEthernet1/0/13

!         

interface GigabitEthernet1/0/14

!         

interface GigabitEthernet1/0/15

!         

interface GigabitEthernet1/0/16

!         

interface GigabitEthernet1/0/17

!         

interface GigabitEthernet1/0/18

!         

interface GigabitEthernet1/0/19

!         

interface GigabitEthernet1/0/20

!         

interface GigabitEthernet1/0/21

!         

interface GigabitEthernet1/0/22

!         

interface GigabitEthernet1/0/23

!         

interface GigabitEthernet1/0/24

!         

interface GigabitEthernet1/0/25

!         

interface GigabitEthernet1/0/26

!         

interface GigabitEthernet1/0/27

!         

interface GigabitEthernet1/0/28

!         

interface Vlan1

 no ip address

!         

interface Vlan10

 description RECEPTION-GATEWAY

 ip address 192.168.10.1 255.255.255.0

 ip helper-address 10.0.100.2

!         

interface Vlan20

 description SALES-OPS-GATEWAY

 ip address 192.168.20.1 255.255.255.0

 ip helper-address 10.0.100.2

!         

interface Vlan30

 description IT-SERVERS-GATEWAY

 ip address 192.168.30.1 255.255.255.0

!         

interface Vlan99

 description MANAGEMENT-GATEWAY

 ip address 10.0.99.1 255.255.255.0

!         

router ospf 1

 router-id 3.3.3.3

 passive-interface default

 no passive-interface GigabitEthernet1/0/2

 no passive-interface GigabitEthernet1/0/3

 network 10.0.99.0 0.0.0.255 area 0

 network 10.0.100.0 0.0.0.3 area 0

 network 10.0.101.0 0.0.0.3 area 0

 network 192.168.10.0 0.0.0.255 area 0

 network 192.168.20.0 0.0.0.255 area 0

 network 192.168.30.0 0.0.0.255 area 0

!         

ip http server

ip http secure-server

!         

!         

!         

!         

!         

!         

!         

line con 0

line vty 0 4

 login local

 transport input ssh

line vty 5 15

 login local

 transport input ssh

!         

end