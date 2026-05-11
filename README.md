# KhaleelCorp Enterprise Network + Automation Dashboard

## Project Overview
A fully functional enterprise-style network built on physical Cisco hardware,
simulating a real enterprise branch office deployment. 

Project implements NAT, DHCP services, OSPF failover testing, Python automation, and a Flask monitoring dashboard.

Operational data is collected from Cisco devices via SSH using Python and visualized through a web dashboard.

## Hardware Used
- 2× Cisco ISR4331/K9 (IOS XE) — primary and failover routers
- Cisco WS-C3750G-24TS-S1U — distribution/Layer 3 switch
- Cisco WS-C2960-24TT-L — access layer switch

## Technologies Implemented

### Networking
VLAN segmentation
802.1Q trunking
Inter-VLAN routing using SVIs
OSPFv2 Area 0
Default route advertisement
NAT overload (PAT)
DHCP services
Static + dynamic routing validation

### Security
SSHv2 remote management
Port security (sticky MAC)
BPDU Guard
VLAN isolation

### High Availability
OSPF-based internal failover testing
Primary/backup router topology

### Automation & Monitoring
Python automation using Netmiko
SSH data collection
JSON snapshot storage
Flask monitoring dashboard
Historical snapshot browsing

### Validation Tests

The following features were successfully tested and validated:

DHCP lease assignment
NAT translations
OSPF neighbor adjacency
Inter-VLAN routing
Internet connectivity
Internal failover routing
SSH automation connectivity
Dashboard functionality

## Network Diagram
<img width="510" height="661" alt="khaleelcorp drawio (1)" src="https://github.com/user-attachments/assets/f342e91c-26b9-4cdb-b868-6961c961a498" />


## Dashboard Screenshots
![alt text](<automation/screenshots/Screenshot 2026-05-11 at 6.55.54 pm.png>)

## Repository Structure
- /configs — full running configs for all 4 devices
- /evidence — show command output proving each feature works
- /automation - Python automation + dashboard code
- /troubleshooting - troubleshooting notes and fixes
- network-handoff.md — handoff doc written for IT ops team




