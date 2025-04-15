# 🧨 DDoS Attack Simulation with Snort Detection
---
## 👤 Author
- Nguyen Duy Thanh - B2108121
- Vo Tan Tai - B2111948
- Tran Van Sang - B2112002
---
## 🛠️ Project Description

This project simulates a **UDP Flood DDoS attack** using a Python script (`ddos.py`) and detects it in real-time with **Snort IDS**. Custom Snort rules are written to alert based on packet thresholds for ICMP, UDP, and TCP traffic.

---

## 🚀 How to Run `ddos.py`

> ⚠️ **Note**: Run in a controlled, isolated virtual environment. Do **not** execute on public or production networks.

### 1. Prerequisites
- Python 3 installed
- Linux-based OS (e.g., Lubuntu)
- Target machine (can be a VM) with Snort configured and running
- Snort should listen on the correct interface (`enp0s3`, `lo`, etc.)

### 2. Usage

Open terminal and run the script:

```bash
python3 ddos.py
