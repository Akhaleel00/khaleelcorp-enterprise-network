SW-DIST#ping 8.8.8.8 source vlan 10
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
Packet sent with a source address of 192.168.10.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 8/13/17 ms


Router-A#sh ip nat translations
Pro  Inside global         Inside local          Outside local         Outside global
udp  10.0.0.249:5146       192.168.10.11:54258   17.248.228.19:443     17.248.228.19:443
tcp  10.0.0.249:5063       192.168.10.11:55460   18.239.6.36:443       18.239.6.36:443
tcp  10.0.0.249:5068       192.168.10.11:55444   172.64.148.235:443    172.64.148.235:443
udp  10.0.0.249:512        192.168.10.11:123     17.253.20.45:123      17.253.20.45:123
tcp  10.0.0.249:5075       192.168.10.11:55464   142.250.69.69:443     142.250.69.69:443
udp  10.0.0.249:5120       192.168.10.11:58385   34.117.201.170:443    34.117.201.170:443
udp  10.0.0.249:5147       192.168.10.11:57594   17.248.228.19:443     17.248.228.19:443
tcp  10.0.0.249:5072       192.168.10.11:55457   140.82.114.25:443     140.82.114.25:443
udp  10.0.0.249:5121       192.168.10.11:50182   8.8.4.4:443           8.8.4.4:443
udp  10.0.0.249:5130       192.168.10.11:55331   8.8.4.4:443           8.8.4.4:443
udp  10.0.0.249:5124       192.168.10.11:37218   8.8.8.8:53            8.8.8.8:53
          
Router-A#sh ip nat statistics
Total active translations: 77 (0 static, 77 dynamic; 77 extended)
Outside interfaces:
  GigabitEthernet0/0/1
Inside interfaces: 
  GigabitEthernet0/0/0
Hits: 378553  Misses: 1017
Expired translations: 940
Dynamic mappings:
-- Inside Source
[Id: 1] access-list NAT-TRAFFIC interface GigabitEthernet0/0/1 refcount 77
nat-limit statistics:
 max entry: max allowed 0, used 0, missed 0
In-to-out drops: 0  Out-to-in drops: 0
Pool stats drop: 0  Mapping stats drop: 0
Port block alloc fail: 0
IP alias add fail: 0
Limit entry add fail: 0
Router-A#
