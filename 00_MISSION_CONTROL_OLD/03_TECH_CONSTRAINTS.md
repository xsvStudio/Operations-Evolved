# ⚙️ TECHNICAL CONSTRAINTS & BANNED TECH

## ❌ BANNED (DO NOT USE)
* **Tkinter / PySimpleGUI:** These look amateur. They are banned.
* **Cloud Databases (SQL/Firebase):** Banned. Local files only.
* **Web Portals:** We are not building a website. We are building a Desktop App.

## ✅ REQUIRED STACK
* **Frontend:** Electron + React + Tailwind CSS.
* **Backend:** Python (Running in "Headless" CLI mode).
* **Communication:** Electron spawns Python process -> Python prints JSON/Text -> Electron displays it.
* **Build System:** `electron-builder` (to create the .exe).

## ⚡ THE "GRANDMA-PROOF" RULE
The user must never see a terminal window.
The user must never have to install Python manually.
The Python environment must be bundled into the executable.