**➜**  **~** ping 8.8.8.8

PING 8.8.8.8 (8.8.8.8): 56 data bytes

64 bytes from 8.8.8.8: icmp_seq=0 ttl=114 time=13.576 ms

64 bytes from 8.8.8.8: icmp_seq=1 ttl=114 time=11.441 ms

64 bytes from 8.8.8.8: icmp_seq=2 ttl=114 time=11.395 ms

64 bytes from 8.8.8.8: icmp_seq=3 ttl=114 time=11.537 ms

64 bytes from 8.8.8.8: icmp_seq=4 ttl=114 time=13.043 ms

64 bytes from 8.8.8.8: icmp_seq=5 ttl=114 time=12.498 ms

64 bytes from 8.8.8.8: icmp_seq=6 ttl=114 time=11.583 ms

^C

--- 8.8.8.8 ping statistics ---

7 packets transmitted, 7 packets received, 0.0% packet loss

round-trip min/avg/max/stddev = 11.395/12.153/13.576/0.821 ms

  

  

Router-A#sh ip nat statistics  

Total active translations: 83 (0 static, 83 dynamic; 83 extended)

Outside interfaces:

  GigabitEthernet0/0/1

Inside interfaces: 

  GigabitEthernet0/0/0

Hits: 62655  Misses: 434

Expired translations: 351

Dynamic mappings:

-- Inside Source

[Id: 1] access-list NAT-TRAFFIC interface GigabitEthernet0/0/1 refcount 83

nat-limit statistics:

 max entry: max allowed 0, used 0, missed 0

In-to-out drops: 0  Out-to-in drops: 0

Pool stats drop: 0  Mapping stats drop: 0

Port block alloc fail: 0

IP alias add fail: 0

Limit entry add fail: 0