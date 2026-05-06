# khaleelcorp-enterprise-network
Enterprise Network

## Project Overview
A fully functional small business network built on physical Cisco hardware,
simulating a real enterprise branch office deployment. Covers switching,
routing, redundancy, NAT, DHCP, and security hardening end-to-end.

## Hardware Used
- 2× Cisco ISR4331/K9 (IOS XE) — primary and failover routers
- Cisco WS-C3750G-24TS-S1U — distribution/Layer 3 switch
- Cisco WS-C2960-24TT-L — access layer switch

## Technologies Implemented
- 802.1Q trunking, inter-VLAN routing via SVIs, STP root bridge election
- OSPFv2 area 0, default route redistribution
- HSRP with preempt and interface tracking
- NAT overload (PAT), DHCP server + relay (ip helper-address)
- Named extended ACLs — guest isolation, Sales-to-IT policy
- SSH v2 hardening, port security, DHCP snooping

## Network Diagram
[embed topology.png here]

## How to Navigate This Repo
- /configs — full running configs for all 4 devices
- /evidence — show command output proving each feature works
- network-handoff.md — handoff doc written for IT ops team


<img width="510" height="661" alt="khaleelcorp drawio (1)" src="https://github.com/user-attachments/assets/f342e91c-26b9-4cdb-b868-6961c961a498" />
