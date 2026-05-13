# Network Automation Dashboard

## Overview

Python-based network automation and monitoring system built for the KhaleelCorp Enterprise Network Lab.

The automation stack connects to Cisco IOS devices using SSH and Netmiko, collects operational network data, stores timestamped JSON snapshots, and visualizes collected network information through a Flask web dashboard.

---

## Features

### Network Automation

* SSH connectivity to Cisco devices
* Automated command execution
* Multi-device data collection
* Raw CLI output storage
* Timestamped JSON snapshot storage

### Monitoring Dashboard

* Interface monitoring
* OSPF neighbor visibility
* Routing table visibility
* VLAN visibility
* Trunk monitoring
* Historical network snapshots
* Snapshot browsing from dashboard interface

---

## Technologies Used

* Python 3.9+
* Netmiko
* Flask
* JSON
* Cisco IOS

---

## Project Structure

```text
automation/
├── app.py
├── collector.py
├── dashboard_collector.py
├── devices.py
├── requirements.txt
│
├── data/
│   ├── latest.json
│   └── snapshots/
│
├── outputs/
│
├── templates/
│   └── index.html
│
└── screenshots/
```

---

## Installation

### Clone Repository

```bash
git clone YOUR_REPO_LINK
cd khaleelcorp-enterprise-network
cd automation
```

---

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

## Configure Devices

Update device credentials and IP addresses in:

```text
devices.py
```

Example:

```python
devices = [
    {
        "name": "SW-DIST",
        "device_type": "cisco_ios",
        "host": "10.0.99.1",
        "username": "admin",
        "password": "YOUR_PASSWORD"
    }
]
```

---

## Run Automation Collector

Collect operational data from all network devices:

```bash
python3 dashboard_collector.py
```

This will:

* connect to Cisco devices
* execute monitoring commands
* generate JSON snapshots
* update latest dashboard state

---

## Run Raw CLI Collector

Generate raw CLI output backups:

```bash
python3 collector.py
```

This creates timestamped folders containing unmodified Cisco CLI command outputs.

---

## Run Flask Dashboard

Start the dashboard server:

```bash
python3 app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Example Workflow

1. Run automation collector:

```bash
python3 dashboard_collector.py
```

2. Generate timestamped JSON snapshots

3. Start Flask dashboard:

```bash
python3 app.py
```

4. Browse dashboard:

```text
http://127.0.0.1:5000
```

5. Review historical snapshots directly from the dashboard dropdown menu

---

## Example Commands Collected

* `show ip interface brief`
* `show ip route`
* `show ip ospf neighbor`
* `show vlan brief`
* `show interfaces trunk`

---

## Dashboard Screenshots
![alt text](<screenshots/Screenshot 2026-05-11 at 6.55.54 pm.png>)
![alt text](<screenshots/Screenshot 2026-05-11 at 6.56.09 pm.png>)
![alt text](<screenshots/Screenshot 2026-05-11 at 6.56.18 pm.png>)
![alt text](<screenshots/Screenshot 2026-05-11 at 6.54.20 pm.png>)
---

## Data Collection Architecture

The automation platform stores network data using two collection methods.

### 1. Raw CLI Output Storage

Operational command outputs are saved as raw text files for:

* troubleshooting
* validation evidence
* configuration review
* operational backups

Example:

```text
outputs/
└── 2026-05-11_17-15-30/
    ├── Router-A.txt
    ├── Router-B.txt
    └── SW-DIST.txt
```

These files contain unmodified Cisco CLI command outputs collected directly from devices.

Generate raw CLI outputs with:

```bash
python3 collector.py
```

---

### 2. Structured JSON Snapshot Storage

Operational network state is also stored as structured JSON snapshots for dashboard rendering and historical state tracking.

Example:

```text
data/
├── latest.json
└── snapshots/
    ├── 2026-05-11_17-15-30.json
    └── 2026-05-11_18-00-01.json
```

Each snapshot contains:

* interface information
* routing data
* OSPF neighbor state
* VLAN information
* trunk status
* collection timestamps

The Flask dashboard reads from:

```text
data/latest.json
```

while historical snapshots can be browsed directly from the dashboard interface.

---

### Benefits of This Design

* Human-readable operational evidence
* Historical state tracking
* Structured dashboard data
* Simplified future monitoring expansion
* Foundation for alerting and analytics

---

## Validation Tests

The automation platform successfully validated:

* SSH connectivity to Cisco IOS devices
* Multi-device operational data collection
* OSPF neighbor visibility
* Routing table visibility
* VLAN visibility
* Trunk interface visibility
* JSON snapshot generation
* Routing visibility through collected operational snapshots
* Historical snapshot browsing
* Flask dashboard rendering


---

## Future Improvements

* SNMP monitoring
* Live dashboard refresh
* Email alerting
* Interface utilization graphs
* Automated config backups
* Real-time status monitoring
* Database integration

---
