# IEEE Smart Village & OpenAMI Collaborative Repository
> **Centralized Knowledge Archive of Open-Source Smart Grid Specs, Policy Frameworks, and Rural Electrification Blueprints**

This repository serves as the centralized, version-controlled repository hosting the migrated legacy knowledgebase of the **IEEE Smart Village (ISV)** committee (`wiki.smartvillage.ieee.org`) and the **OpenAMI (Advanced Metering Infrastructure)** technical specifications. 

Rather than serving as a static, unmonitored repository, this archive represents an active collaborative engineering environment. Here, strategic reports, regulatory tariff tools, vehicle suspension audits, and cryptographic metering standards are maintained under git version control and served continuously over **Firebase Hosting** using an automated, preview-gated CI/CD pipeline.

---

## 🌐 The Converted DokuWiki Knowledgebase

The legacy DokuWiki knowledgebase has been fully compiled into a GFM markdown archive and publication-grade static HTML pages. It is structured into distinct, navigable technical directories that document over a decade of rural electrification engineering:

```
wiki/
├── home/                    # Core Wiki Portals
│   ├── openami.html         # OpenAMI smart metering overview & standards
│   ├── projects.html        # Interactive remote monitoring mapping portal
│   ├── standards.html       # IEEE 1547 (DER) & IEEE 802.15.4 specifications
│   ├── technologies.html    # Core technology stacks and power generation indices
│   └── wash.html            # Water, Sanitation, and Hygiene (WASH) resources
├── wg/                      # Working Group Directories
│   ├── tech.html            # ISV Technology Committee agendas and charters
│   ├── pdc.html             # Project Development Committee intake processes
│   ├── standards.html       # Earth-leakage, earthing, and lightning protection
│   └── education.html       # Academic curriculum integration & field guides
├── playground/              # Prototyping & Template Sandboxes
│   ├── techspec.html        # Smart Village site engineering specifications
│   └── experiment1.html     # Hydro, telecom, Starlink, and monitoring audits
└── wiki/                    # Platform & Documentation Rules
    └── syntax.html          # DokuWiki-to-Markdown syntax translation guide
```

* **Regional Working Groups:** Integrates meeting cadences and coordinator details across **North America (NAWG)**, **Latin America (LAWG)**, **Africa (AWG)**, and **South Asia (SAWG)**.
* **Technology Commitee (`wg/tech`):** Details the active hardware evaluations, remote terminal unit (RTU) standards, and telemetry formats utilized across active ISV pilots.
* **Site Engineering Sandboxes:** Contains detailed templates for sizing off-grid PV arrays, standardizing micro-hydro generation, and setting up off-grid satellite backhaul (e.g., Starlink integration).

---

## 📂 The Technical & Strategic Reports Catalog

This repository archives **18 active, publication-grade technical reference specifications, regulatory policy frameworks, engineering audits, and strategic capitalization prospectuses** that support OpenAMI and IEEE Smart Village operations across South Asia and Sub-Saharan Africa (SSA). All reports are maintained under git version control and deployed as interactive, responsive, multi-tabbed dashboards.

### 📋 Registry of Active Reports (EMG Suite)

| Document ID | Category | Title | Live Portal URL (Firebase) |
| :--- | :--- | :--- | :--- |
| **EMG-TECH-018** | Technical Spec | Filtered AI Architecture & OPAI Use-Case Matrix | [minigrid-opai-software-audit](https://sattal.cottonspace.com/reports/minigrid-opai-software-audit) |
| **EMG-TECH-017** | Technical Spec | Power Quality (PQ) Management in Decentralized Mini-Grids | [minigrid-power-quality](https://sattal.cottonspace.com/reports/minigrid-power-quality) |
| **EMG-TECH-016** | Technical Spec | Mini-Grid Dynamic Capacity & AI-Driven Optimization | [minigrid-dynamic-capacity-ai](https://sattal.cottonspace.com/reports/minigrid-dynamic-capacity-ai) |
| **EMG-TECH-015** | Technical Spec | EPRI Smart Grid Open-Source Stacks: Hardening Spec | [epri-dev-software-audit](https://sattal.cottonspace.com/reports/epri-dev-software-audit) |
| **EMG-TECH-014** | Technical Spec | Combined Cooling & Heating Heat Pump (CCHHP) for Agro-Processing | [cchhp-milk-chilling-drying](https://sattal.cottonspace.com/reports/cchhp-milk-chilling-drying) |
| **EMG-TECH-013** | Technical Spec | SSA Mini-Grid Downtime: Cloud Lock-In & Edge Topology | [ssa-minigrid-downtime](https://sattal.cottonspace.com/reports/ssa-minigrid-downtime) |
| **EMG-TRD-011** | Technical Spec | Open-Source DCU Edge Architecture & Wi-SUN Mesh | [open-source-dcu-mesh-hes](https://sattal.cottonspace.com/reports/open-source-dcu-mesh-hes) |
| **EMG-TRD-005** | Technical Spec | OpenAMI Technical Reference Design & Grid Code Audits | [openami-smart-metering-spec](https://sattal.cottonspace.com/reports/openami-smart-metering-spec) |
| **SSA-STS-LEGACY** | Technical Spec | Prepaid Metering & STS Legacy Key Management in SSA | [STS-SubSaharanAfrica_Industry_Letter](https://sattal.cottonspace.com/reports/STS-SubSaharanAfrica_Industry_Letter) |
| **EMG-REG-008** | Regulatory/Policy | OpenAMI Nigeria Expansion Blueprint & NERC 2023 Rules | [openami-strategic-report](https://sattal.cottonspace.com/reports/openami-strategic-report) |
| **EMG-REG-006** | Regulatory/Policy | UN ECE Energy Interoperability & Digitalization Guidelines | [unece-interoperability-guidelines](https://sattal.cottonspace.com/reports/unece-interoperability-guidelines) |
| **EMG-REG-003** | Regulatory/Policy | Prepaid Metering & NERC Regulations: Equity & Grid Arrival | [nerc-afur-minigrid-tariffs](https://sattal.cottonspace.com/reports/nerc-afur-minigrid-tariffs) |
| **EMG-NEX-004** | Regulatory/Policy | The Decentralized Energy Nexus: Solar-Biomass-eATV Loop | [cse-minigrid-biofuels-synthesis](https://sattal.cottonspace.com/reports/cse-minigrid-biofuels-synthesis) |
| **EMG-CRIT-012** | Critique/Audit | MicroPowerManager: Architectural & Regulatory Critique | [micropowermanager-critique](https://sattal.cottonspace.com/reports/micropowermanager-critique) |
| **TXE-CR-001** | Critique/Audit | Motrike TrikeXplor E-Truck Design & Upgrade Roadmap | [trikexplor-etruck-critique](https://sattal.cottonspace.com/reports/trikexplor-etruck-critique) |
| **EMG-PITCH-007**| Capital Strategy | OpenAMI & IEEE Smart Village: Pan-African Pitch Blueprint | [openami-funding-pitch](https://sattal.cottonspace.com/reports/openami-funding-pitch) |
| **EMG-PITCH-002**| Capital Strategy | eATV MiniGrid Nexus: SSA + South Asia Expansion Pitch | [eatv-minigrid-pitch](https://sattal.cottonspace.com/reports/eatv-minigrid-pitch) |
| **EMG-SSA-V001**| Capital Strategy | Electric Cargo Vehicles as Productive-Use Anchors for SSA | [eATV-minigrid-ssa-vehicles](https://sattal.cottonspace.com/reports/eATV-minigrid-ssa-vehicles) |

---

### 🔑 Key Deep-Dive Technical Highlights

#### 🔌 [EPRI Smart Grid Open-Source Stacks Audit & Hardening (EMG-TECH-015)](https://sattal.cottonspace.com/reports/epri-dev-software-audit)
* **Code Audit & Gap Mapping:** Audits `epri-dev/DLMS-COSEM` C++ library files, exposing missing Interface Classes (Class 7 Profiles, Class 70 Disconnects, Class 18 OTA) and High-Level Security (HLS) deficiencies needed for Calin/Hexing edge meters.
* **DCU Hardware Architecture:** Specifies production board modifications including TPM 2.0/HSM secure enclave storage, local SQLite WAL cache transactional storage, Wi-SUN FAN RF drivers, priority queue thread pools, and A/B partition OTA bootloaders.
* **DER Compliance Loops:** Formulates IEEE 1547-2018 Volt-Var, Volt-Watt, and Freq-Watt loops for high-penetration solar PV grids.

#### ⚡ [Power Quality (PQ) Management in Decentralized Mini-Grids (EMG-TECH-017)](https://sattal.cottonspace.com/reports/minigrid-power-quality)
* **OpenDSS Dynamic Optimization:** Integrates active OpenDSS Python modules calculating Voltage Unbalance Factor (VUF) and executing a greedy heuristic phase-swapping rebalancing routine.
* **Edge Inverter Modulation:** Configures 3-Phase 4-Wire (3P4W) hybrid inverters under LF Energy Fledge/OpenFMB to inject asymmetric reactive power ($Q$) to rebalance phase voltage vectors.
* **Harmonic Traps:** Outlines primary Delta-Wye (\Delta-Y) winding configurations to trap and dissipate zero-sequence triplen harmonics harmlessly as heat.

#### 🧠 [Filtered OPAI Asset & Use-Case Matrix (EMG-TECH-018)](https://sattal.cottonspace.com/reports/minigrid-opai-software-audit)
* **Consortium Asset Filtering:** Audits 20 AI models/datasets in the LF Energy / EPRI OPAI repository, filtering out wholesale or nuclear models to focus on 9 critical rural grid tools (SolarNet, Quartz, PowerNet, powerFormer).
* **Multi-Model Architectures:** Details three high-value production systems: Solar Nowcasting Lead-Acid Shield (Quartz + SolarNet), MARL Phase Balancing (PowerNet), and PUE Demand Coordination (DMP-PCFC + GridLearn).
* **Data Fusion Stack:** Outlines a three-tier meteorological data pipeline (coarse NASA POWER data -> high-res Solargis/Meteostat satellite -> on-site PWS edge calibration loops).

#### 🥛 [Combined Cooling & Heating Heat Pump for Agro-Processing (EMG-TECH-014)](https://sattal.cottonspace.com/reports/cchhp-milk-chilling-drying)
* **Radial Scroll Compliance:** Audits Copeland Scroll radial and axial compliance under liquid floodback, mapping a combined heating/cooling $COP_{\text{total}}$ of $5.5 - 6.5$.
* **PCM Thermal Decoupling:** Integrates latent-heat water-ice Phase Change Material vaults ($334\text{ kJ/kg}$) to shift bulk milk chilling (2x500L BMC) loads to peak midday solar production.
* **Agricultural Waste Heat:** Recovers high-grade superheated condenser waste gas (55°C–65°C) to run deep drying chambers for regional cereals, spices, and vegetables.
* **TCO & Financial Models:** Side-by-side 10-year cash flows contrasting CCHHP + PCM against conventional diesel configurations, modeling a 21–22 month capital payback.

#### 🔌 [OpenAMI Smart Metering & Grid Code Reference Design (EMG-TRD-005)](https://sattal.cottonspace.com/reports/openami-smart-metering-spec)
* **IHM-4000 Board Design:** Standardizes hardware interfaces, Wi-SUN sub-GHz mesh RF transceiver specifications, and physical optical Eye Mode E communication.
* **Life-Safety Limits:** Details double-throw automated remote isolation ELCBs calibrated with strict limits (**6mA DC** for solar backfeed and **30mA AC** for human contact thresholds).
* **OSI & SGAM Mappings:** Outlines complete 7-layer OSI communication layers and 5-layer SGAM mappings to ensure multi-vendor meter interoperability.

---

## 🛠️ Infrastructure & CD Pipeline Configuration

```mermaid
graph LR
  A[Developer Commit] -->|Git Push| B[GitHub Repo]
  B -->|GitHub Actions CI/CD| C[Firebase Hosting]
  C -->|Clean URLs / Static Assets| D[Global Edge CDN]
```

### Git Actions Workflows (`.github/workflows/`)
This repository contains two fully automated continuous deployment workflows:
1. **`firebase-hosting-pull-request.yml`:** Triggers on all incoming PRs. Packages the static assets and compiles them onto a temporary **Firebase Preview Channel**, outputting the staging URL directly into the PR comments for peer review.
2. **`firebase-hosting-merge.yml`:** Triggers on successful merges to the `main` branch. Deploys the production bundle directly to the live environment, clearing the CDN cache and applying updated routing.

### Firebase Hosting Configuration (`firebase.json`)
The serving architecture implements:
* **Clean URLs (`cleanUrls: true`):** Automatically maps incoming requests like `/wiki/wg/tech` to the static `/wiki/wg/tech.html` file in the background, eliminating ugly trailing `.html` extensions and maintaining modern, SEO-compliant routes.
* **Cache Headers:** Implements optimized cache-control headers for static media attachments (e.g. `/media/*` assets and PDFs cached at the edge CDN for maximum delivery speed).

---

*This collaborative framework was engineered by **Antigravity** (Google DeepMind Advanced Agentic Coding team) on May 28, 2026.*
