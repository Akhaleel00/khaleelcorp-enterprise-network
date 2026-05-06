SW-ACCESS#sh running-config               

Building configuration...

  

Current configuration : 7685 bytes

!

version 15.0

no service pad

service timestamps debug datetime msec

service timestamps log datetime msec

no service password-encryption

!

hostname SW-ACCESS

!

boot-start-marker

boot-end-marker

!

!

username admin privilege 15 secret 5 $1$Rf92$Aud7VN/DODsTCa/SbkeMa1

no aaa new-model

system mtu routing 1500

!

!

ip domain-name khaleel.local

!

!

crypto pki trustpoint TP-self-signed-209227648

 enrollment selfsigned

 subject-name cn=IOS-Self-Signed-Certificate-209227648

 revocation-check none

 rsakeypair TP-self-signed-209227648

!         

!

crypto pki certificate chain TP-self-signed-209227648

 certificate self-signed 01

  3082024D 308201B6 A0030201 02020101 300D0609 2A864886 F70D0101 04050030 

  30312E30 2C060355 04031325 494F532D 53656C66 2D536967 6E65642D 43657274 

  69666963 6174652D 32303932 32373634 38301E17 0D393330 33303130 30303035 

  325A170D 32303031 30313030 30303030 5A303031 2E302C06 03550403 1325494F 

  532D5365 6C662D53 69676E65 642D4365 72746966 69636174 652D3230 39323237 

  36343830 819F300D 06092A86 4886F70D 01010105 0003818D 00308189 02818100 

  C88C193A BA3B38AE 0F902CD4 AA1B3FAD 1304CCA1 063F2D81 53911BB0 00593F57 

  9F316568 1B70A18E 102C2C6D 4ED2C2A4 5CEC5EDF 72838DA6 69340CCF FBB481C3 

  E7FF3195 F5553A6E 979DF60E 5B7F49B1 5058BD69 56D2F90E 4A3CDE29 1880FC40 

  3D9BEC8C 08E14875 53D6E5C4 D7BCBA83 80E24472 F883F541 2CA07DD2 9C2EDB61 

  02030100 01A37730 75300F06 03551D13 0101FF04 05300301 01FF3022 0603551D 

  11041B30 19821753 572D4143 43455353 2E6B6861 6C65656C 2E6C6F63 616C301F 

  0603551D 23041830 16801465 A7AC764C F55C825C 44BFF69C AE158374 F7105830 

  1D060355 1D0E0416 041465A7 AC764CF5 5C825C44 BFF69CAE 158374F7 1058300D 

  06092A86 4886F70D 01010405 00038181 00B547A3 F251D46A FB7D0A30 01A1C19C 

  8D301007 DF38A86E 6A97803D 0E3F1358 3A5AE4C3 7B8C560A A707062B 60DEF6F3 

  C7536EC5 6B469875 0FC62059 DA6C749B 93D1BBE0 41EF6D09 EAE33F37 8686A255 

  26DE4317 7D516472 A07B393A D59377E8 7EEE0FC4 2295DCEC D13F0B59 3D7497B5 

  C17652AB 5CB3DD91 D701FBD5 EED5A8CC AB

        quit

!         

!

!         

!

spanning-tree mode pvst

spanning-tree extend system-id

spanning-tree vlan 10,20,99 priority 8192

!

vlan internal allocation policy ascending

!

ip ssh version 2

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

!

interface FastEthernet0/2

 switchport access vlan 10

 switchport mode access

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!         

interface FastEthernet0/3

 switchport access vlan 10

 switchport mode access

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/4

 switchport access vlan 10

 switchport mode access

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!         

interface FastEthernet0/5

 switchport access vlan 10

 switchport mode access

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/6

 switchport access vlan 10

 switchport mode access

 switchport port-security

switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!         

interface FastEthernet0/7

 switchport access vlan 10

 switchport mode access

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/8

 switchport access vlan 10

 switchport mode access

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

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

!

interface FastEthernet0/10

 switchport access vlan 20

 switchport mode access

 switchport port-security maximum 2

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/11

 switchport access vlan 20

 switchport mode access

 switchport port-security maximum 2

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/12

 switchport access vlan 20

 switchport mode access

 switchport port-security maximum 2

switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/13

 switchport access vlan 20

 switchport mode access

 switchport port-security maximum 2

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/14

 switchport access vlan 20

 switchport mode access

 switchport port-security maximum 2

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/15

 switchport access vlan 20

 switchport mode access

 switchport port-security maximum 2

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/16

 switchport access vlan 20

 switchport mode access

 switchport port-security maximum 2

 switchport port-security

 switchport port-security violation restrict

 switchport port-security mac-address sticky

 spanning-tree portfast

 spanning-tree bpduguard enable

!

interface FastEthernet0/17

 switchport access vlan 99

 switchport mode access

 shutdown

!         

interface FastEthernet0/18

 switchport access vlan 99

 switchport mode access

 shutdown 

!

interface FastEthernet0/19

 switchport access vlan 99

 switchport mode access

 shutdown

!         

interface FastEthernet0/20

 switchport access vlan 99

 switchport mode access

 shutdown 

!

interface FastEthernet0/21

 switchport access vlan 99

 switchport mode access

 shutdown

!         

interface FastEthernet0/22

 switchport access vlan 99

 switchport mode access

 shutdown 

!

interface FastEthernet0/23

 switchport access vlan 99

 switchport mode access

 shutdown

!         

interface FastEthernet0/24

 switchport access vlan 99

 switchport mode access

 shutdown 

!

interface GigabitEthernet0/1

 switchport trunk allowed vlan 10,20,30,99

 switchport mode trunk

!

interface GigabitEthernet0/2

!

interface Vlan1

 no ip address

 shutdown 

!

ip http server

ip http secure-server

logging esm config

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