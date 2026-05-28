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

This repository archives the 9 core technical reference specifications, regulatory tariff reviews, vehicle engineering critiques, and strategic capitalization prospectuses that define the OpenAMI and IEEE Smart Village initiatives.

### 📐 Technical Reference Designs & Vehicle Audits

```
markdown-archive/
├── openami-smart-metering-spec.md  # OpenAMI Smart Metering Specification
└── trikexplor-etruck-critique.md    # Motrike TrikeXplor E-Truck Audit
```

#### 🔌 [OpenAMI Smart Metering Reference Design (EMG-TRD-005)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/openami-smart-metering-spec.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/openami-smart-metering-spec) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/openami-smart-metering-spec.md)
* **Core Technical Contents:**
  * **Hardware Architecture:** Specifies the core components of the **IHM-4000 Data Concentrator Unit (DCU)** and edge Smart Meters, mapping their communication pipelines.
  * **RF Downlink Mesh Topology:** Defines the **Wi-SUN sub-GHz mesh RF networking downlink** operating at 868/915 MHz, detailing automatic routing and link-quality parameters for high-attenuation environments.
  * **Life-Safety Earth-Leakage Protection:** Standardizes built-in life-safety earth-leakage circuit breakers (ELCB) with strict thresholds of **6mA DC** (to detect solar DC backfeed) and **30mA AC** (for human safety limits) with automated remote disconnect.
  * **SGAM & OSI Mapping:** Formulates a complete 5-layer Smart Grid Architecture Model (SGAM) and 7-layer OSI communication model mapping, standardizing data payloads over DLMS/COSEM and MQTT protocols.

#### 🛺 [Motrike TrikeXplor E-Truck Engineering Critique (TXE-CR-001)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/trikexplor-etruck-critique.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/trikexplor-etruck-critique) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/trikexplor-etruck-critique.md)
* **Core Technical Contents:**
  * **Structural Vulnerabilities:** Documents physical failures under the stock 150 kg payload rating. Identifies thin-wall butted roll cage tubing buckling modes and light-weight rear axle traction slip under loaded grades.
  * **Chassis & Suspension Engineering:** Critiques the stock bicycle air-fork and outlines the transition to a robust **A-arm double wishbone suspension geometry** utilizing high-travel Gabriel India/Uno Minda coilovers.
  * **Brake & Powertrain Integration:** Computes master cylinder stroke volume and caliper piston displacement requirements. Formulates Kelly controller throttle mappings, 3-level regenerative braking curves, and standardizes **DOM steel tubing** specs for roll cage rebuilding.
  * **Bill of Materials (BOM):** Includes a complete engineering sourcing catalog mapping stock components to motorsport-grade and locally-available Indian OEM alternatives.

---

### 🌍 Regulatory, Tariff, & Decarbonization Policy Frameworks

```
markdown-archive/
├── unece-interoperability-guidelines.md  # UNECE Digitalization Policy
├── nerc-afur-minigrid-tariffs.md         # NERC isolated tariff systems
└── cse-minigrid-biofuels-synthesis.md    # Circular Solar-Biomass Nexus
```

#### ⚖️ [UNECE Energy Interoperability & Digitalization Guidelines (EMG-REG-006)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/unece-interoperability-guidelines.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/unece-interoperability-guidelines) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/unece-interoperability-guidelines.md)
* **Core Technical Contents:**
  * **Interoperability Dimensions:** Mapped directly to the GridWise Architecture Council (GWAC) stack, detailing the semantic, syntactic, and organizational interoperability layers.
  * **OpenPAYGO Tokenization:** Defines standard token encryption rules, standardizing the integration of OpenPAYGO key generation with decentralized billing architectures.
  * **Moldova NRPC Place of Consumption (PoC):** Details Moldovan National Energy Regulatory Agency standards, implementing an alphanumeric, checksummed registry schema for distributed energy resources (DERs).
  * **Secure Hybrid Database Architecture:** Outlines the design of a hybrid database system combining local offline PostgreSQL caching with encrypted Google Cloud SQL sync.

#### 📊 [Prepaid Metering & NERC Mini-Grid Regulations (EMG-REG-003)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/nerc-afur-minigrid-tariffs.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/nerc-afur-minigrid-tariffs) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/nerc-afur-minigrid-tariffs.md)
* **Core Technical Contents:**
  * **NERC 2023 Regulation Mapping:** Codifies mini-grid classifications (under 100kW isolated vs. 100kW–1MW interconnected), streamlining portfolio licensing and the "Deemed Consent" grid arrival rules.
  * **MYTO Tariff Revenue Model:** Formalizes the Multi-Year Tariff Order (MYTO) math, applying a Grant "Haircut" (Net Regulatory Asset Base adjustment) to eliminate double-compensation on DFI capital grants.
  * **Loss Caps & Encroachment Buyouts:** Enforces maximum allowable mini-grid losses (**4% technical / 3% commercial**) and details the legal exit buyout formulas (Depreciated Asset Value + 12-Month Historical Revenue) upon grid encroachment.

#### 🌱 [Solar Mini-Grids & Circular Bioenergy Policy (EMG-NEX-004)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/cse-minigrid-biofuels-synthesis.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/cse-minigrid-biofuels-synthesis) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/cse-minigrid-biofuels-synthesis.md)
* **Core Technical Contents:**
  * **CapEx-OpEx CBG Metrics:** Audits Compressed Bio-Gas (CBG) plant business models, documenting the critical **30:70 CapEx-to-OpEx ratio** driven by feedstock supply chain volatility.
  * **State Bioenergy Performance Ratings:** Ranks 13 Indian states on policy execution, recognizing Gujarat's high-efficiency feed-in tariff structure and Jharkhand's regulatory hurdles.
  * **Jharkhand (JREDA) Electrification Audit:** Evaluates post-concession degradation across **859 solar-electrified villages**, documenting technical battery decay and institutional handover failures.
  * **Agro-Energy Circular Loop:** Synthesizes a closed-loop rural economy linking solar mini-grids (powering local CBG anaerobic digesters), bio-CNG generation, organic fertilizer distribution, and local electric agricultural vehicle (eATV) fleets.

---

### 💰 Strategic Capital, Mobility, & Cryptographic Correspondence

```
markdown-archive/
├── openami-funding-pitch.md              # Smart Village Fundraising Prospectus
├── eatv-minigrid-pitch.md                 # eATV Mobility Scaling Roadmap
├── eatv-minigrid-ssa-vehicles.md          # 7-Vehicle Productive-Use Scoring
└── sts-subsaharan-africa-industry-letter.md # STS Association Security Letter
```

#### 💸 [IEEE Smart Village & OpenAMI Fundraising Prospectus (EMG-PITCH-007)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/openami-funding-pitch.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/openami-funding-pitch) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/openami-funding-pitch.md)
* **Core Technical Contents:**
  * **Moody's Fundraising Laws:** Translates Fielding Graduate University's H.R. Moody principles into non-profit smart grid marketing and brand equity strategies.
  * **DFI Gated Capitalization:** Establishes a **4-stage capitalization roadmap** (Seed, Pilot, Expansion, Reserve) targeting a **$5M total fundraise** with strict technical milestone gates.
  * **Donor Objection Mitigation:** Synthesizes an active Objections Log targeting Development Finance Institution (DFI) concerns regarding local developer default risks, technical scalability, and battery disposal environmental profiles.

#### 🚛 [eATV Mini-Grid Logistics & Rural Mobility Pitch (EMG-PITCH-002)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/eatv-minigrid-pitch.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/eatv-minigrid-pitch) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/eatv-minigrid-pitch.md)
* **Core Technical Contents:**
  * **Off-Grid Mobility Deficits:** Documents Sub-Saharan African last-mile transport logistics costs and outlines solutions for expanded South Asian markets (India, Nepal, Bangladesh, Sri Lanka).
  * **PAYG Mobile Money Fleet Model:** Pairs mobile money PAYG micro-leasing with electric ATV fleet charging terminals integrated into off-grid solar mini-grid nodes.
  * **DFI Scale-Up Roadmap:** Details a 5-year mature capitalization path scaling up to **$40M CAPEX** to deploy 2,500 active productive-use vehicles.

#### 🔋 [Electric Vehicles as Productive-Use Anchors (EMG-SSA-V001)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/eatv-minigrid-ssa-vehicles.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/eATV-minigrid-ssa-vehicles) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/eatv-minigrid-ssa-vehicles.md)
* **Core Technical Contents:**
  * **7-Vehicle Evaluation Matrix:** Scores vehicles (Tachyon, Hamba, OGIRIDE, generic Chinese imports, Powerland Epic, etc.) across 5 core dimensions: payload capacity, off-grid range, acquisition cost, spare parts logistics, and mini-grid grid integration.
  * **Sizing and Role Division:** Defines a **3-tier operational fleet profile** (Supervisor light-weight, Daily light cargo, Heavy agricultural hauling).
  * **Procurement Engineering Checklist:** Standardizes mandatory hardware specifications, including minimum **IP65 ingress protection**, integrated cell monitoring BMS, agricultural tire treads, and dual-speed transfer cases.

#### 🔑 [STS Prepaid Metering Key Management in SSA (SSA-STS-LEGACY-2026-001)](file:///C:/Users/rhlbh/.gemini/antigravity/scratch/sattal-pitch/markdown-archive/sts-subsaharan-africa-industry-letter.md)
* **Status:** 🌐 [Live HTML View (Firebase)](https://smartvillage-openami.web.app/reports/STS-SubSaharanAfrica_Industry_Letter) | 📝 [Raw GFM Markdown (GitHub)](./markdown-archive/sts-subsaharan-africa-industry-letter.md)
* **Core Technical Contents:**
  * **STS Encryption Cryptography:** Critiques legacy Standard Transfer Specification (STS) key management inside off-grid local IPP grids, contrasting **EA07 (DES-based)** vs. **EA11 (MISTY1-based)** encryption standards.
  * **TID Rollover Rollout:** Outlines the critical **2024/2025 Token Identifier (TID) rollover** vulnerability (truncating tokens based on the 1993 base epoch) and details the Decoder Key Generation (DKGA01-04) migration paths.
  * **IPP Security Autonomy:** Details the coalition's formal request to the STS Association for operator self-management of Supply Group Codes (SGC) and custom Key Management Centre (KMC) access.

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
