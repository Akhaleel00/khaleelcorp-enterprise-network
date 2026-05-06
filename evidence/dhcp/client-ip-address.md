**➜**  **~** ifconfig

lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384

options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>

inet 127.0.0.1 netmask 0xff000000

inet6 ::1 prefixlen 128 

inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 

nd6 options=201<PERFORMNUD,DAD>

gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280

stf0: flags=0<> mtu 1280

anpi2: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=400<CHANNEL_IO>

ether ba:b2:b2:5c:02:e4

media: none

status: inactive

anpi1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=400<CHANNEL_IO>

ether ba:b2:b2:5c:02:e3

media: none

status: inactive

anpi0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=400<CHANNEL_IO>

ether ba:b2:b2:5c:02:e2

media: none

status: inactive

en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=400<CHANNEL_IO>

ether ba:b2:b2:5c:02:c2

nd6 options=201<PERFORMNUD,DAD>

media: none

status: inactive

en6: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=400<CHANNEL_IO>

ether ba:b2:b2:5c:02:c3

nd6 options=201<PERFORMNUD,DAD>

media: none

status: inactive

en7: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=400<CHANNEL_IO>

ether ba:b2:b2:5c:02:c4

nd6 options=201<PERFORMNUD,DAD>

media: none

status: inactive

en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500

options=460<TSO4,TSO6,CHANNEL_IO>

ether 36:21:0b:de:1b:c0

media: autoselect <full-duplex>

status: inactive

en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500

options=460<TSO4,TSO6,CHANNEL_IO>

ether 36:21:0b:de:1b:c4

media: autoselect <full-duplex>

status: inactive

en3: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500

options=460<TSO4,TSO6,CHANNEL_IO>

ether 36:21:0b:de:1b:c8

media: autoselect <full-duplex>

status: inactive

bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=63<RXCSUM,TXCSUM,TSO4,TSO6>

ether 36:21:0b:de:1b:c0

Configuration:

id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0

maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200

root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0

ipfilter disabled flags 0x0

member: en1 flags=3<LEARNING,DISCOVER>

        ifmaxaddr 0 port 10 priority 0 path cost 0

member: en2 flags=3<LEARNING,DISCOVER>

        ifmaxaddr 0 port 11 priority 0 path cost 0

member: en3 flags=3<LEARNING,DISCOVER>

        ifmaxaddr 0 port 12 priority 0 path cost 0

nd6 options=201<PERFORMNUD,DAD>

media: <unknown type>

status: inactive

utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1500

inet6 fe80::e671:e6f2:301:c9aa%utun0 prefixlen 64 scopeid 0x10 

nd6 options=201<PERFORMNUD,DAD>

ap1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>

ether 62:3b:df:3d:7f:7b

nd6 options=201<PERFORMNUD,DAD>

media: autoselect (none)

status: inactive

en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>

ether 7a:d6:27:5b:af:1f

inet6 fe80::e8:5986:fc02:279d%en0 prefixlen 64 secured scopeid 0xe 

inet 10.0.0.46 netmask 0xffffff00 broadcast 10.0.0.255

nd6 options=201<PERFORMNUD,DAD>

media: autoselect

status: active

awdl0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>

ether 72:7b:de:b0:aa:0e

inet6 fe80::707b:deff:feb0:aa0e%awdl0 prefixlen 64 scopeid 0x11 

nd6 options=201<PERFORMNUD,DAD>

media: autoselect

status: active

llw0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=400<CHANNEL_IO>

ether 72:7b:de:b0:aa:0e

inet6 fe80::707b:deff:feb0:aa0e%llw0 prefixlen 64 scopeid 0x12 

nd6 options=201<PERFORMNUD,DAD>

media: autoselect (none)

utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380

inet6 fe80::dd6d:91db:5923:d0b%utun1 prefixlen 64 scopeid 0x13 

nd6 options=201<PERFORMNUD,DAD>

utun2: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000

inet6 fe80::1515:32f8:6d5:88e5%utun2 prefixlen 64 scopeid 0x14 

nd6 options=201<PERFORMNUD,DAD>

utun3: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1000

inet6 fe80::ce81:b1c:bd2c:69e%utun3 prefixlen 64 scopeid 0x15 

nd6 options=201<PERFORMNUD,DAD>

utun4: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380

inet6 fe80::d3c5:f653:30f5:963c%utun4 prefixlen 64 scopeid 0x16 

nd6 options=201<PERFORMNUD,DAD>

utun5: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380

inet6 fe80::9f7e:e453:ff4a:326b%utun5 prefixlen 64 scopeid 0x17 

nd6 options=201<PERFORMNUD,DAD>

en8: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500

options=404<VLAN_MTU,CHANNEL_IO>

ether 6c:1f:f7:1b:6c:74

inet6 fe80::4f1:2d8d:18a6:6b77%en8 prefixlen 64 secured scopeid 0x18 

inet 192.168.10.11 netmask 0xffffff00 broadcast 192.168.10.255

nd6 options=201<PERFORMNUD,DAD>

media: autoselect (100baseTX <full-duplex>)

status: active