# STS Prepaid Metering & Legacy Key Management in SSA (SSA-STS-LEGACY-2026-001)
> **Formal Industry Correspondence Regarding STS Prepayment Standards and Legacy Fleet Key Management**

---

* **Date:** 18 May 2026
* **Reference:** SSA-STS-LEGACY-2026-001
* **Primary Addressees:**
  * The Executive Director, STS Association (STSA), Johannesburg, South Africa
  * The Chairman, IEC TC13 WG14 (IEC 62055 Series Working Group)
  * The Africa Regional Director, STS Association
* **For Information:**
  * All meter manufacturers in Annex A
  * Regional energy regulators — East, West, and Southern Africa
* **From:**
  * **Coalition of Mini-Grid Developers and System Integrators — Sub-Saharan Africa**
  * *Submitted on behalf of mini-grid operators, rural electrification programme developers, and off-grid energy system integrators operating across Sub-Saharan Africa (SSA), representing an estimated installed base exceeding **2.5 million STS-compliant prepayment meters** across Kenya, Tanzania, Uganda, Rwanda, Ethiopia, Ghana, Nigeria, Senegal, Zambia, Zimbabwe, Mozambique, and Madagascar.*

---

## ✉️ 1. Purpose and Background

This letter is submitted to the STS Association (STSA) and to the prepaid meter manufacturing community to:
1. **Formally validate** the specific operational context of mini-grid and off-grid deployments in Sub-Saharan Africa as distinct from utility-scale grid deployments.
2. **Formally enumerate** all STS encryption algorithm versions and key management parameters encountered in deployed legacy meter fleets across SSA, for the purposes of creating an authoritative reference for STS correspondence, technical compliance, and field operations.
3. **Request formal recognition** from the STSA and from meter OEMs of the right of mini-grid developers and operators with large legacy meter fleets to **self-manage and continue operating their existing meters indefinitely**, without being compelled to undertake full fleet replacement due to algorithm or TID lifecycle changes.

> [!IMPORTANT]
> This letter does not advocate circumventing the STS standard’s security model. It advocates for **structured legacy key management access** — specifically, formal permission for qualified mini-grid operators to retain and manage their vending keys and Security Modules for STS-compliant meters already in their fleet, for the operational life of those meters.

---

## 🌍 2. Sub-Saharan Africa — Validation of the Operating Context

### 2.1 Why SSA Mini-Grid Deployments Are Structurally Different
Mini-grid and off-grid deployments in Sub-Saharan Africa differ materially from the urban utility environments for which the STS standard was originally designed and administered.

| Parameter | Urban Utility Context | SSA Mini-Grid Context |
| :--- | :--- | :--- |
| **Grid Connectivity** | Permanent national grid | Off-grid; solar/diesel/hybrid generation |
| **Operator Type** | Licensed utility (e.g. KPLC, ZESCO, ECG) | Private IPP, NGO, cooperative, community enterprise |
| **Meter Fleet Size** | Hundreds of thousands | 200 – 20,000 per operator |
| **Revenue Model** | Government-subsidised tariffs | Commercial cost-reflective tariffs; survival-critical |
| **KMC Access** | Direct institutional STSA member access | Often via third-party vending partners; indirect |
| **Replacement CapEx** | Cost borne by national tariff base | Cost borne by project developer; existential risk |
| **Field Service Access** | Urban technician density | Remote; travel costs can exceed meter unit cost |
| **Connectivity** | Reliable GSM | GSM intermittent or absent; offline token mandatory |

### 2.2 The Mini-Grid Energy Access Imperative
Approximately **600 million people** in Sub-Saharan Africa lack access to electricity. Mini-grids powered by solar and hybrid generation are one of the most cost-effective pathways to energy access for populations beyond the reach of the national grid. The IEA and SE4All estimate that **&gt;35% of new electricity connections** needed to reach universal energy access in Africa by 2030 must come from mini-grids.

STS prepaid metering is uniquely suited to this environment because:
* It functions **entirely offline** — no internet or GSM required for token generation or meter operation.
* It is **vendor-interoperable** — utilities can procure from multiple manufacturers.
* It is **tamper-evident and fraud-resistant** — critical for remote revenue collection.
* It uses a **20-digit keypad interface** — accessible without smartphones or connectivity.

### 2.3 The Legacy Fleet Problem
Mini-grid projects in SSA typically have a **25-year project life**, financed by development loans. Meters are expected to last the full project term.

The installed legacy fleet across SSA includes meters manufactured between **2010 and 2022**, spanning multiple STS algorithm generations. The **TID (Token Identifier) Rollover event of 24 November 2024** exposed a systemic vulnerability: a significant subset of mini-grid operators discovered they lacked the authorized access to Security Modules or vending keys required to generate TID rollover tokens for their own fleets, because those keys were held by the meter OEM or the original vending platform provider.

Mini-grid developers must have **documented, authorized, and long-term access** to the cryptographic material and STSA-compliant processes needed to service the meters they have procured and deployed.

---

## 🛠️ 3. Enumeration of STS Algorithm Versions & Key Parameters

### 3.1 STS Encryption Algorithms (EA)
The STS standard defines Encryption Algorithms that are applied to tokens to secure token data in transit and prevent unauthorized token generation.

| Algorithm | Designation | Cipher | Key Length | Status | Deployed Era |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EA07** | Legacy Standard | DES (Data Encryption Standard) | 64-bit | Deprecated — still in widespread SSA field use | 1993 – 2018 (approx.) |
| **EA11** | Current Standard | MISTY1 | 128-bit | Current — mandatory for new STS certifications | 2015 onwards |

#### 3.1.1 EA07 — Legacy 64-bit DES
* **Cipher:** DES, 64-bit block cipher.
* **Key effective length:** 56 bits (8 parity bits discarded).
* **IEC 62055-41 reference:** Edition 1, Annex A.
* **Security status:** Cryptographically weak by modern standards. NIST formally deprecated DES in 2005. However, the STS token format provides additional security layers (Supply Group Code, PAN, Token Class) that partially compensate.
* **SSA field prevalence:** Estimated to represent **40–60%** of the current SSA installed base, concentrated in meter generations manufactured between 2005 and 2016.
* **Legacy management requirement:** Operators managing EA07 fleets must retain access to EA07-capable Security Modules and DKGA02-compliant vending key material. Transition to EA11 requires physical key-change tokens or meter replacement.

#### 3.1.2 EA11 — Current 128-bit MISTY1
* **Cipher:** MISTY1, 128-bit key, 64-bit payload.
* **IEC 62055-41 reference:** Edition 2.
* **Security status:** Current; recommended for all new deployments.
* **SSA field prevalence:** Predominant in meters manufactured from 2016 onwards; standard in new tenders.
* **Key management:** Requires DKGA04-compatible Security Modules and STSA KMC registration.

### 3.2 Decoder Key Generation Algorithms (DKGA)
The DKGA defines how the meter’s unique Decoder Key (DeKu) is derived from its credentials.

| DKGA | Description | Key Derivation Method | Compatible EA | Status |
| :--- | :--- | :--- | :--- | :--- |
| **DKGA01** | First-gen derivation | DES ECB | EA07 | Retired/deprecated |
| **DKGA02** | Standard legacy derivation | DES CBC | EA07 | Still in use for legacy fleet maintenance |
| **DKGA03** | Triple-DES derivation | 3DES | EA07/hybrid | Not recommended; superseded |
| **DKGA04** | Modern HMAC derivation | HMAC-SHA256 | EA11 | Current — required for all EA11 deployments |

> [!IMPORTANT]
> Mini-grid operators managing legacy EA07 fleets must retain operational access to **DKGA02-capable Security Modules** to continue servicing those meters. The STSA is requested to formally confirm that operators with existing DKGA02 Security Modules are entitled to continued use of those modules for existing meter fleet management, without mandatory upgrade timelines.

### 3.3 Token Identifier (TID) and Key Revision Number (KRN)

#### 3.3.1 TID — Token Identifier
The TID is a 24-bit field encoding elapsed time in minutes from the STS Epoch. It serves as an anti-replay mechanism.

| Parameter | Value |
| :--- | :--- |
| **Bit length** | 24 bits |
| **Counter unit** | Minutes |
| **Epoch (KRN=1)** | 1 January 1993, 00:00:00 UTC |
| **Epoch (KRN=2)** | 1 January 2014, 00:00:00 UTC |
| **TID Rollover Date (KRN=1)** | **24 November 2024** (counter exhaustion) |
| **TID Rollover Date (KRN=2)** | **Approximately 2045** |
| **Maximum TID value** | 16,777,215 minutes (~31.97 years) |

* **Rollover event (November 2024):** Meters operating with KRN=1 exhausted their 24-bit TID counter on 24 November 2024. Meters not updated via two-token Key Change process prior to this date began rejecting new credit tokens.

#### 3.3.2 KRN — Key Revision Number
The KRN indicates which TID epoch and associated vending keys a meter is operating under.

| KRN | TID Epoch | Status |
| :--- | :--- | :--- |
| **KRN 0** | N/A | Non-vending key (test/token lock mode) |
| **KRN 1** | 1993 Epoch | Deployed legacy fleet (requires TID change to KRN 2) |
| **KRN 2** | 2014 Epoch | Current standard (safe from rollover until ~2045) |
| **KRN 3–9** | Future Epochs | Reserved for future rollover lifecycles |

---

## 📢 4. The Self-Management Request

To protect massive investments in off-grid energy access and prevent premature asset abandonment, the Coalition requests the STSA and meter manufacturers to formally recognize the following principles:

1. **Cryptographic Self-Management Rights:** Qualified mini-grid developers with a registered installed base of &gt;1,000 meters shall have the right to request direct, secure, and independent custody of their associated Vending Keys and Security Modules from their vending providers and OEMs.
2. **Access to Legacy Security Modules:** The STSA and OEMs commit to maintaining the supply of EA07/DKGA02-capable hardware Security Modules (HSMs) or software Security Modules (virtual HSMs) for the operational life of existing meter fleets.
3. **Open-Access Key Migration:** OEMs shall provide standardized, non-proprietary procedures for migrating SGCs and active vending keys between vending platforms, preventing third-party software vendors from using proprietary lock-in to hold utility assets hostage.
4. **Graduated Compliance Pathways:** Establish a special "SME Utility" membership tier within the STSA, allowing smaller mini-grid operators to access the Key Management Centre (KMC) at cost-reflective, subsidized rates.

---

## 🏭 5. OEM Key Specifications & Compatibility Summary

Primary meter manufacturers deployed in SSA, their legacy key capabilities, and current status:

| Manufacturer | Headquarters | Legacy EA/DKGA Capability | Current EA11/DKGA04 Status | KMC SGC Availability |
| :--- | :--- | :--- | :--- | :--- |
| **Conlog** | Durban, South Africa | Fully supported (EA07, DKGA02) | Certified standard | Open migration supported |
| **Landis+Gyr** | Zug, Switzerland | Supported | Certified standard | Structured migration |
| **Itron (Actaris)**| Liberty Lake, USA | Supported | Certified standard | Structured migration |
| **Hexing Electrical**| Hangzhou, China | Supported (widespread in SSA) | Certified standard | OEM platform lock-in risk |
| **INHEMETER** | Shenzhen, China | Supported (IHM series) | Certified standard | OEM platform lock-in risk |
| **Sanxing** | Ningbo, China | Supported | Certified standard | OEM platform lock-in risk |
| **Chint Instrument**| Zhejiang, China | Supported | Certified standard | OEM platform lock-in risk |

---

## 📂 Annex A — Recipient & Manufacturer Addressees

* **Conlog (Pty) Ltd:** Durban, South Africa (support@conlog.com)
* **Landis+Gyr (Pty) Ltd:** Centurion, South Africa (info.za@landisgyr.com)
* **Itron Metering Solutions:** Cape Town, South Africa
* **Hexing Electrical Co., Ltd:** Hangzhou, China (market@hexing.com)
* **Shenzhen INHEMETER Co., Ltd:** Shenzhen, China (sales@inhemeter.com)
* **Ningbo Sanxing Smart Power Co., Ltd:** Ningbo, China
* **Zhejiang Chint Instrument & Meter Co., Ltd:** Wenzhou, China
* **Rural Electrification Agencies (REA):** Nigeria, Kenya (EPRA), Tanzania (EWURA), Uganda (ERA)

---

## 📖 6. Technical Glossary

* **STSA:** Standard Transfer Specification Association. The custodian of the STS prepaid metering standard.
* **TID:** Token Identifier. A 24-bit value representing minutes since the epoch, preventing token replay attacks.
* **PAN:** Primary Account Number. The unique 19-digit identifier of an STS prepayment meter.
* **SGC:** Supply Group Code. A 6-digit number identifying the utility or supply authority that owns the meter's vending keys.
* **DKGA:** Decoder Key Generation Algorithm. Cryptographic derivation function used to generate unique meter keys.
* **DeKu:** Decoder Key. The unique 128-bit key stored inside a meter to decrypt STS tokens.
* **KMC:** Key Management Centre. The STSA secure facility that manages the generation and distribution of master keys.
* **ROPS:** Roll-Over Protective Structure. High-strength structural framing designed to protect occupants during rollover events.

---

*This formal industry petition was synthesized and archived by **Antigravity** (Google DeepMind Advanced Agentic Coding team) on May 28, 2026, for the sattal-a27f2 archival project.*
