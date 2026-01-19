# 🏛️ THE PRIME DIRECTIVE: xsvStudio & Allstar Command

**STATUS:** IMMUTABLE LAW
**OWNER:** Ian Martin

## 1. THE ORIGIN STORY (CONTEXT)
This project started as a simple file structure for **xsvStudio**.
During the process, an epiphany occurred: The chaos of unorganized files is a universal problem.
We realized this solution has three distinct destinies:
1.  **The Product:** A tool we can sell to the world ("Business Essentials").
2.  **The Life System:** The permanent operating system for **xsvStudio** (Ian's Consulting & Life).
3.  **The Job System:** The day-to-day survival tool for **Allstar Construction** (Ian's Executive Role).

## 2. THE DUAL PRIORITY
This software serves two masters equally. Do not prioritize one over the other.

### A. xsvStudio (The Permanent Home)
* **Role:** Ian's personal consulting firm and life management.
* **Requirement:** If Allstar disappears tomorrow, this system must remain as the backbone of Ian's professional life.
* **Key Features:** Client Intake, Invoicing, "Life Admin" (Taxes/Assets), Consultant Deliverables.

### B. Allstar Construction (The Current Mission)
* **Role:** High-stakes Commercial Construction Management.
* **Requirement:** Needs strict "Owner's Rep" level compliance.
* **Key Features:** RFI Logs, Submittals, Financial Profit/Loss Tracking, Risk Mitigation.

## 3. THE "LOCAL-FIRST" PHILOSOPHY
We do not build SaaS. We do not trust the cloud with our data sovereignty.
* **The Data:** Lives in the User's File System (OneDrive / Google Drive).
* **The App:** Is merely a "Lens" that reads and visualizes that data.
* **The Benefit:** If the internet dies, we can still work.

## 4. THE VICTORY CONDITION
Success is achieved when:
1.  Ian can open the Dashboard and see his Allstar Profit Margins instantly.
2.  Ian can switch profiles and see his xsvStudio Client Pipeline instantly.
3.  A random user in Kansas downloads the "Free Tier," organizes their messy business, and thinks "Wow."


ENGINEERING MASTER DIRECTIVE (Technical Strategy)
What we're building:

text
One App, Three Tiers:
├─ Tier 1: Business Essentials (Free) - Folder structure + templates
├─ Tier 2: Shadow Ops (Light) - Dashboard + basic tracking
└─ Tier 3: Allstar Command (Deep) - Full dashboard + AI insights
Why three tiers?

Entry point is free (no friction)

Easy upgrade path (same codebase)

Captures customers at different budgets

Revenue per tier: $0 → $200/mo → $500/mo

Timeline to production:

text
Jan 21 → Phase 2: Folder structure + templates (SHIP THIS WEEK)
Jan 27 → Phase 4: Dashboard development begins (LIVE WITH ALLSTAR)
Feb 1  → Dashboard v0.1 functional (DEMO READY)
Feb 15 → Production-ready (REVENUE)
Technology Stack:

Frontend: Electron + React (desktop app)

Backend: Python + file watching

Data: Local-first (user's OneDrive/Google Drive)

No cloud backend needed (90% cost advantage)