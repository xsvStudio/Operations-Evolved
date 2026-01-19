# ENGINEERING ROADMAP V2: THE "LAUNCHER" BUILD
**Tech Stack:** Electron | React | Python (Headless) | Local-First

## 1. ARCHITECTURE OVERVIEW
We are building a **Modular Monolith Desktop App**.

* **Frontend (The Face):** Electron + React + Tailwind CSS.
    * *Directive:* Must look premium. Custom title bar. Glassmorphism details.
* **Backend (The Muscle):** Python (bundled binary).
    * *Directive:* Runs "Headless" (CLI mode). No UI code in Python.
* **Data Layer:** The User's File System (JSON/Excel).
    * *Directive:* NO SQL Database. NO Cloud Backend.

## 2. PHASE 2 DELIVERABLES (Due Jan 21)

### Component A: The Headless Engine (Python)
Refactor existing `create_folders.py` to accept CLI arguments:
`./engine.exe --mode="install" --template="construction" --path="C:/Users/Ian/OneDrive"`
* **Must Do:** Write `.xsv-config.json` hidden file in the root directory.
* **Must Do:** Deploy `MASTER_ESTIMATE.xlsx` and templates.

### Component B: The "Visual Hook" UI (Electron)
Build the "Lobby" Screen.
* **Screen 1:** "Welcome to Business Essentials." (Visual: Slick, Dark Mode).
* **Screen 2:** "Where do you work?" (Grid selection: Construction, Agency, Personal).
* **Screen 3:** "Deploying..." (Progress bar with high-end animation).
* **Screen 4:** "Success." (Button: Open Folder).

**Crucial Engineering Note:**
Do not build the full Dashboard graphs yet. Just build the **Installer Flow** but make it look like the Dashboard is "sleeping" or waiting to be unlocked.

## 3. PHASE 4 PREVIEW (The Dashboard)
*Starting Jan 27, we activate the "Read" capabilities.*
* **SheetJS Integration:** To read the `MASTER_ESTIMATE.xlsx` totals.
* **Chokidar Integration:** To watch folders for new files.
* **Audit Engine:** To scan for missing compliance docs.

## 4. REPO STRUCTURE
```text
/xsv-root-architecture
  /engine (Python Code)
    /templates (JSONs)
    /scripts (Headless Logic)
  /interface (Electron Code)
    /src (React)
    /public (Assets)
  /docs (Strategy)