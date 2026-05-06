# Network Handoff Document

**Project:** Khaleel Corp Enterprise Network Lab  
**Author:** Amin Khaleel  
**Date:** 2026-05

---

# 1. Overview

This network was designed to simulate a small enterprise environment with segmented VLANs, dynamic routing using OSPF, and internet access via NAT. Redundancy is implemented using dual routers, providing internal routing failover.

The goal of this network is to demonstrate practical routing, switching, troubleshooting, and automation skills in a realistic topology.

---

# 2. Network Architecture

### Core Layer

- **SW-DIST (Layer 3 Switch)**
    
    - Performs inter-VLAN routing (SVIs)
        
    - Acts as default gateway for all VLANs
        

### Access Layer

- **SW-ACCESS (Layer 2 Switch)**
    
    - Connects end devices
        
    - Enforces port security and BPDU Guard
        

### Edge Layer

- **Router-A (Primary)**
    
    - WAN connectivity (DHCP)
        
    - NAT (PAT overload)
        
    - Injects default route into OSPF
        
- **Router-B (Secondary)**
    
    - Provides backup routing via OSPF
        
    - No WAN/NAT configured
        

---

# 3. Network Diagram

Refer to:  
`khaleelcorp-network-diagram`

---

# 4. IP Addressing Scheme

### VLANs

|VLAN|Name|Subnet|Gateway|
|---|---|---|---|
|10|Reception|192.168.10.0/24|192.168.10.1|
|20|Sales|192.168.20.0/24|192.168.20.1|
|30|IT|192.168.30.0/24|192.168.30.1|
|99|Management|10.0.99.0/24|10.0.99.1|

### Router Links

|Link|Subnet|
|---|---|
|SW-DIST ↔ Router-A|10.0.100.0/30|
|SW-DIST ↔ Router-B|10.0.101.0/30|

---

# 5. Routing Design (OSPF)

- OSPF Area 0 is used across all devices
    
- SW-DIST advertises VLAN networks
    
- Router-A injects default route (`0.0.0.0/0`)
    
- Router-B acts as backup path
    

### Behavior:

- Under normal operation → traffic exits via Router-A
    
- On failure → routes reconverge via Router-B
    

---

# 6. Internet & NAT Configuration

- Router-A WAN interface (`G0/0/1`) receives IP via DHCP
    
- NAT Overload (PAT) is configured:
    
    - Inside: `G0/0/0`
        
    - Outside: `G0/0/1`
        

### Result:

- Internal clients can access external networks using a single public IP
    

---

# 7. Switching Configuration

### VLANs

- VLANs 10, 20, 30, 99 created on both switches
    

### Trunking

- 802.1Q trunk between SW-DIST and SW-ACCESS
    
- Allowed VLANs: 10, 20, 30, 99
    

### Inter-VLAN Routing

- Performed on SW-DIST using SVIs
    

---

# 8. Security Features

### Port Security

- Enabled on access ports
    
- Sticky MAC addresses
    
- Violation mode: restrict
    

### BPDU Guard

- Enabled on edge ports (PortFast)
    

### Segmentation

- VLANs isolate departments
    

---

# 9. Testing & Validation

The following tests were successfully completed:

### DHCP

- Clients receive correct IP addresses
    
- Verified using:
    

```bash
show ip dhcp binding
```

### OSPF

- Neighbors reach FULL state
    
- Verified using:
    

```bash
show ip ospf neighbor
```

### Routing

- VLAN networks reachable across topology
    
- Verified using:
    

```bash
show ip route
```

### NAT

- Translations observed
    
- Verified using:
    

```bash
show ip nat translations
show ip nat statistics
```

### Internet Connectivity

- Clients can ping external IP (8.8.8.8)
    

### Failover (Internal)

- Router-A link shutdown simulated
    
- OSPF reconverged
    
- Connectivity restored via Router-B
    

---

# 10. Failover Behavior

### When Router-A fails:

- OSPF adjacency drops
    
- Default route removed
    
- Traffic reroutes via Router-B
    
- Internal connectivity remains functional
    

### Limitation:

- Internet access is lost (Router-B has no WAN/NAT)
    

---

# 11. Troubleshooting Guide

### NAT Issues

```bash
show ip nat translations
show ip nat statistics
```

### OSPF Issues

```bash
show ip ospf neighbor
show ip route
```

### DHCP Issues

```bash
show ip dhcp binding
```

### VLAN Issues

```bash
show vlan brief
show interfaces trunk
```

---

# 14. Repository Structure

```text
configs/        → device configurations  
evidence/       → test screenshots and outputs      
```

---

# 15. Known Limitations

- No internet failover (Router-B lacks WAN)
    
- No firewall implementation
    
- No centralized monitoring (SNMP/NetFlow)
    
- Dashboard is basic
    

---

# 16. Future Improvements

- Add WAN/NAT to Router-B for full failover
    
- Implement firewall (ACLs or ASA)
    
- Add SNMP monitoring
    
- Add automation
    
- Add a dashboard to visualize data collected from automation
    

---

# 17. Conclusion

This network demonstrates:

- Enterprise network design principles
    
- Routing and switching fundamentals
    
- Fault tolerance via OSPF
    
- Real-world troubleshooting

    

The environment is fully functional and can be extended for more advanced networking scenarios.

---
