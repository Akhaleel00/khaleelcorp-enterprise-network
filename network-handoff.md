# Network Handoff Document

**Project:** KhaleelCorp Enterprise Network Lab
**Author:** Amin Khaleel
**Date:** 2026-05

---

# 1. Overview

This network was designed to simulate a small enterprise environment using physical Cisco hardware.

The environment implements VLAN segmentation, inter-VLAN routing, OSPF dynamic routing, dual-WAN resiliency, NAT services, Python-based network automation, and a Flask monitoring dashboard.

The goal of the project is to demonstrate practical infrastructure engineering skills including routing, switching, failover validation, troubleshooting, automation, and operational monitoring.

---

# 2. Network Architecture

## Core Layer

### SW-DIST (Layer 3 Switch)

* Performs inter-VLAN routing using SVIs
* Acts as default gateway for all VLANs
* Maintains OSPF adjacencies with edge routers
* Uses floating static routes for WAN path preference

---

## Access Layer

### SW-ACCESS (Layer 2 Switch)

* Connects end devices
* Enforces PortFast and BPDU Guard
* Provides VLAN access segmentation

---

## Edge Layer

### Router-A (Primary WAN Router)

* Primary internet edge router
* WAN connectivity via DHCP
* NAT overload (PAT)
* OSPF default route advertisement

### Router-B (Backup WAN Router)

* Secondary internet edge router
* Backup WAN connectivity via DHCP
* Backup NAT overload (PAT)
* Provides WAN failover path during Router-A failure

---

# 3. Network Diagram

Refer to:

`khaleelcorp-network-diagram`

---

# 4. IP Addressing Scheme

## VLANs

| VLAN | Name       | Subnet          | Gateway      |
| ---- | ---------- | --------------- | ------------ |
| 10   | Reception  | 192.168.10.0/24 | 192.168.10.1 |
| 20   | Sales      | 192.168.20.0/24 | 192.168.20.1 |
| 30   | IT         | 192.168.30.0/24 | 192.168.30.1 |
| 99   | Management | 10.0.99.0/24    | 10.0.99.1    |

---

## Router Links

| Link               | Subnet        |
| ------------------ | ------------- |
| SW-DIST ↔ Router-A | 10.0.100.0/30 |
| SW-DIST ↔ Router-B | 10.0.101.0/30 |

---

# 5. Routing Design (OSPF)

* OSPF Area 0 is deployed across all routing devices
* SW-DIST advertises VLAN networks
* Router-A advertises a default route into OSPF
* Router-B provides backup WAN routing capability

---

## Routing Behavior

### Normal Operation

Traffic exits through:

SW-DIST → Router-A → ISP

---

### Failover Operation

During Router-A failure:

* OSPF adjacency drops
* SW-DIST transitions to backup route
* Traffic reroutes through Router-B
* Internet connectivity is restored through Router-B NAT

---

# 6. Internet & NAT Configuration

## Router-A

* WAN interface: `GigabitEthernet0/0/1`
* Receives public IP via DHCP
* Performs NAT overload (PAT)

### NAT Configuration

* Inside interface: `G0/0/0`
* Outside interface: `G0/0/1`

---

## Router-B

* Backup WAN interface: `GigabitEthernet0/0/1`
* Receives IP via DHCP
* Performs backup NAT overload (PAT)

### NAT Configuration

* Inside interface: `G0/0/0`
* Outside interface: `G0/0/1`

---

# 7. Switching Configuration

## VLANs

* VLANs 10, 20, 30, and 99 configured across switching infrastructure

---

## Trunking

* 802.1Q trunk between SW-DIST and SW-ACCESS
* Allowed VLANs:

  * 10
  * 20
  * 30
  * 99

---

## Inter-VLAN Routing

* Performed using SVIs on SW-DIST

---

# 8. Security Features

## SSHv2 Remote Management

* Secure remote administrative access enabled

---

## Port Security

* Sticky MAC addressing enabled
* Violation mode set to restrict

---

## BPDU Guard

* Enabled on access ports using PortFast

---

## VLAN Segmentation

* Departmental traffic isolation implemented using VLANs

---

# 9. Automation & Monitoring

Python automation scripts were developed using:

* Python
* Netmiko
* Flask
* JSON snapshot storage

---

## Automation Functions

* SSH connectivity to Cisco devices
* Automated operational data collection
* Timestamped JSON snapshot generation
* Historical snapshot storage
* Dashboard rendering of collected operational data

---

## Dashboard Features

* Interface visibility
* OSPF neighbor visibility
* VLAN visibility
* Routing table visibility
* Historical snapshot browsing

---

# 10. Testing & Validation

The following scenarios were successfully validated:

## DHCP

Verified using:

```bash
show ip dhcp binding
```

---

## OSPF Neighbor Adjacency

Verified using:

```bash
show ip ospf neighbor
```

---

## Routing Visibility

Verified using:

```bash
show ip route
```

---

## NAT Functionality

Verified using:

```bash
show ip nat translations
show ip nat statistics
```

---

## Internet Connectivity

Validated using:

```bash
ping 8.8.8.8 source vlan10
```

---

## WAN Failover

Validated by:

* simulating Router-A failure
* observing OSPF convergence
* verifying backup route activation
* validating Router-B NAT translations
* confirming internet recovery

---

# 11. Failover Behavior

## Router-A Failure Scenario

When Router-A internal uplink fails:

* OSPF adjacency is lost
* SW-DIST removes the primary route
* Backup route through Router-B becomes active
* Internet connectivity restores through Router-B

---

## Validation Evidence

Evidence stored under:

```text
evidence/wan-failover/
```

Includes:

* primary route validation
* backup route activation
* Router-B NAT translations
* ping recovery testing
* failback restoration

---

# 12. Troubleshooting Guide

## NAT Troubleshooting

```bash
show ip nat translations
show ip nat statistics
```

---

## OSPF Troubleshooting

```bash
show ip ospf neighbor
show ip route
```

---

## DHCP Troubleshooting

```bash
show ip dhcp binding
```

---

## VLAN Troubleshooting

```bash
show vlan brief
show interfaces trunk
```

---

## WAN Failover Troubleshooting

```bash
show ip route
show ip nat translations
show ip ospf neighbor
```

---

# 13. Repository Structure

```text
configs/           → device configurations
evidence/          → operational validation evidence
automation/        → Python automation and dashboard
troubleshooting/   → troubleshooting notes
```

---

# 14. Known Limitations

* WAN failover currently validates router failure scenarios rather than upstream ISP-only failure detection
* No IP SLA or route tracking implemented
* No firewall appliance implementation
* Dashboard uses snapshot-based monitoring rather than real-time telemetry

---

# 15. Future Improvements

* Implement IP SLA + route tracking
* Add SNMP monitoring
* Add Grafana/LibreNMS monitoring stack
* Add automated configuration backups
* Add real-time dashboard updates
* Add centralized logging/syslog
* Expand automation capabilities

---

# 16. Conclusion

This environment demonstrates:

* enterprise routing and switching concepts
* OSPF dynamic routing
* VLAN segmentation
* dual-WAN resiliency
* NAT services
* routing convergence testing
* infrastructure troubleshooting
* network automation
* operational monitoring

The environment is fully operational and can be extended into more advanced infrastructure engineering scenarios.

---
