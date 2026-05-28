# OpenAMI Technical Reference Design (EMG-TRD-005)
> **Interoperable Smart Metering, Wi-SUN Mesh Downlink, Satellite Backhaul, and NERC/Grid Code Audits**

---

## 🏢 1. INHEMETER Customization &amp; Physical Hardware Profile

### Adaptive Design Strategy vs. Consumer Electronics
Unlike consumer devices (e.g., standard smartphones), INHEMETER smart grid products do not utilize a fixed, single-variant design. Instead, they employ an **adaptive design strategy** customized dynamically for each regional project. 

Reusing older regional equipment (such as Nigerian legacy samples) is obsolete for modern integrations. Because smart grids introduce evolving security parameters, load profiles, and radio environments, newer hardware profiles (e.g., latest IHM-5000 and IHM-4000 concentrators) are critical to support current standard requirements.

### Physical Hardware Profile (Model IHM-4000 DCU)
Gleaned from industrial diagnostic audits, the Model IHM-4000 Data Concentrator Unit (DCU) features the following physical hardware specifications:

* **CPU:** Industrial high-performance ARMv7 Processor (revision 5, `armv7l`), running a 24MHz clocksource yielding a 41ns scheduler clock resolution.
* **Memory:** 256MB DDR RAM, providing approximately 215MB of free available memory after kernel reservation.
* **Operating System:** Customized Linux kernel `4.1.15 #27 SMP PREEMPT armv7l` compiled in August 2017.
* **Storage &amp; Partitioning:** 256MB Spansion SLC NAND Flash running the UBIFS (Unsorted Block Image File System) for high write endurance. MTD partitioning includes:
  * `ubi0:rootfs`: Mounted read-only (R/O) on `/` (size 58.7M) to prevent system partition corruption.
  * `ubi1_0:opt`: Mounted read-write (R/W) on `/opt` (size 134.7M) for local configurations and update packages.
* **Communication Interfaces:** Built-in `eth0` (Freescale FEC Ethernet operating at 100Mbps Full Duplex) and Realtek `RTL8188EU` USB Wi-Fi adapter (running the `8188eu` module).
* **Cellular Uplink:** Dual SIM high-reliability automatic switching with 4G/3G/2G automatic network drop adaptation.
* **System Initialization:** Booting is governed by `/home/startup` which duplicates binaries to RAM (`/tmp/work/`) and extracts the update bundle `update.tar.gz` to execute the multi-threaded daemon `./daemon` out of the temporary RAM disk, protecting NAND flash from excessive write wear.
* **Clock Sync:** PTP clock support is registered with PPS source `pps0` (disciplined by ptp0).

---

## 📶 2. Hybrid Network Topology: Mesh Downlink &amp; Backhaul Uplink

Off-grid mini-grid networks must bridge dense household clusters scattered across rural topographies.

```
[HES Servers] <--- (Satellite / 4G Uplink) ---> [IHM-4000 DCU] <--- (400m Wi-SUN Mesh) ---> [Meters B & A]
```

### Downlink (Meter-to-DCU)
The preferred downlink is a **Wi-SUN (Wireless Smart Utility Network)** RF mesh (IEEE 802.15.4g) operating in license-free sub-GHz bands:
* **Hop Limits:** Maximum direct point-to-point equipment-to-equipment communication distance is capped at **400 meters**.
* **Self-Healing Mesh Relaying:** Intermediate meters act as packet relays. If Smart Meter A is located 600m from the DCU, it automatically hops its packets through Smart Meter B (located 300m from the DCU and 300m from Meter A).

### Uplink (DCU-to-HES)
* **Satellite Backhaul:** The preferred uplink backhaul for remote, off-grid locations where terrestrial cellular networks are absent.
* **Cellular Backhaul:** Dynamically drops back to cellular (4G LTE / 3G / 2G APN networks) where stable cellular signal is present.

---

## 📋 3. The 7 Core AMI Use Cases &amp; Communication Flows

### Use Case I: Meter Automatic Registration
* **Trigger:** Meter installation or power restoration.
* **Flow:** Meter scans for DCU Wi-SUN beacons -> syncs network timing -> initiates connection request -> performs mutual cryptographic authentication (exchanging keys using DLMS Security Suite 0/1 PKI) -> DCU registers the meter serial and ID with the Head-End System (HES) database.

### Use Case II: On-Demand Reading of Energy &amp; Maximum Demand
* **Trigger:** Utility operator request via HES WebUI.
* **Flow:** HES issues pull command via MQTT -> DCU sends DLMS `GET-REQUEST` over Wi-SUN -> Meter responds -> DCU returns JSON payload back to HES.
* **Objects:** Cumulative active/reactive energy registers (kWh), instantaneous voltage (V), current (A), instantaneous power (kW), and maximum demand.

### Use Case III: On-Demand Reading of Meter Profiles
* **Trigger:** Scheduled audits or operator queries.
* **Flow:** HES queries date/time range -> DLMS `GET-BY-RANGE` sent to meter -> Meter extracts logged interval data from internal memory -> streams packet via Wi-SUN to HES.
* **Objects:** Interval **Load Profile** (30-60 min intervals), **Daily Billing Profile**, and **Monthly Billing Profile**.

### Use Case IV: Periodical Push of Data to HES
* **Trigger:** Pre-scheduled autonomous cron (e.g. daily at 00:00).
* **Flow:** Meter autonomously bundles cumulative load profiles -> pushes via Wi-SUN to DCU -> DCU collects and aggregates neighborhood data -> uploads compressed bundle to HES over Satellite/4G.

### Use Case V: Remote Prepaid Token Delivery
* **Trigger:** Consumer prepayment purchase.
* **Flow:** Payment gateway notifies HES -> HES generates encrypted credit token -> sends OTA via MQTT/Wi-SUN -> Meter decodes token, updates internal credit register, and validates transaction.
* **Objects:** STS (Standard Transfer Specification) 20-digit token or custom encrypted credit payload.

### Use Case VI: Clock Synchronization
* **Trigger:** Daily schedule or drift threshold crossing (> 2 seconds).
* **Flow:** DCU disciplines local clock via GPS/PTP -> HES matches network time -> DCU broadcasts time-sync command to Wi-SUN meters using DLMS clock object -> Meters correct internal RTC.

### Use Case VII: Remote Firmware Upgrade
* **Trigger:** Ad-hoc system upgrades.
* **Flow:** HES uploads binary image to DCU -> HES triggers broadcast upgrade -> DCU streams blocks via Wi-SUN multicast -> Meters write to backup flash partition -> perform checksum verify -> swap partition and boot.

---

## 📐 4. Architectural Alignment: 7-Layer OSI &amp; 5-Layer SGAM

In compliance with the **Group of Experts on Sustainable Energy UNECE (2025) Interoperability Guidelines**, the OpenAMI system aligns across the 7 Layers of the OSI Model and the 5 Layers of the Smart Grid Architecture Model (SGAM):

| OSI Layer | SGAM Layer | UNECE Interoperability Dimension | OpenAMI Technical Protocol / Mapping | Description &amp; Implementation Nuance |
| :--- | :--- | :--- | :--- | :--- |
| **7. Application** | Business / Function | Organizational / Informational | DLMS/COSEM, MQTT, JSON, HTTP | Defines business rules. OBIS codes represent variables as logical objects. HES exchanges JSON payloads via MQTT. |
| **6. Presentation** | Information | Informational (Semantics) | CIM (IEC 61970/61968), STS, A-XDR | Ensures uniform, semantic meaning. XDR encodes DLMS messages. STS tokens translate securely across vendors. |
| **5. Session** | Information / Function | Technical (Syntax) | COSEM-AS, TLS 1.3 | Establishes and secures sessions. Manages DLMS Security Suite 0/1 keys for active connection periods. |
| **4. Transport** | Communication | Technical (Syntax) | TCP / UDP | TCP for secure HES-to-DCU exchanges; UDP for low-overhead multicasts over local Wi-SUN mesh. |
| **3. Network** | Communication | Technical (Syntax) | IPv6, 6LoWPAN, IPv4 | Manages logical routing. <strong>6LoWPAN</strong> compresses IPv6 headers to enable packets to traverse sub-GHz mesh bands. |
| **2. Data Link** | Communication / Component | Technical (Basic Connectivity) | IEEE 802.15.4 MAC (Wi-SUN), 802.3 Ethernet | Controls channel access. Wi-SUN profile specifies frequency-hopping spread spectrum (FHSS) to bypass grid noise. |
| **1. Physical** | Component | Technical (Basic Connectivity) | IEEE 802.15.4g PHY, 100BASE-TX, 4G LTE | Transmission of raw bits. sub-GHz radio bands (915MHz/868MHz) for Wi-SUN mesh, and copper Ethernet on DCU. |

---

## 🛡️ 5. RFP Technical Specifications &amp; Life-Safety Protection

### Life-Safety Current Thresholds
Standard over-current protection is blind to hazardous earth leakage currents. High-penetration DER (solar PV/battery storage) networks introduce complex waveforms with pulsating DC components. OpenAMI mandates:
* **Detection Thresholds:** Continuous, autonomous detection of **6 mA smooth DC** and **30 mA AC** current leakages.
* **Type B Residual Current Monitors (RCM):** Mandated for all tenant circuits in DER networks. Standard Type A/AC RCDs are blind to smooth DC leakages, risking lethal shocks.
* **Rapid Isolation:** Per-tenant **Solid-State Relays (SSRs)** or contactors must isolate the circuit within **40 milliseconds** of crossing safety thresholds.
* **Secure Restoration:** Remote re-energization is supported but local internal microcontroller logic **must block restoration** if the leakage condition persists.

### Grid Code Compliance
* **IEEE 1547-2018 Compatibility:** Establishes criteria for dynamic interconnection, reactive power support, and frequency/voltage ride-through of DERs.
* **Kenya Electricity Grid Code Standards:**
  * **Frequency Ride-Through:** Equipment must remain in active service within the power frequency range of **45.0 Hz to 52.0 Hz**, unless directed by the System Operator for load shedding.
  * **Voltage Tolerances:** Steady-state voltages at the connection point must be maintained within **90% to 110% of nominal voltage**.
