# Operations Evolved - System Architecture

## Overview

Operations Evolved is a Python-based folder structure generator with a Tkinter GUI. It creates standardized business infrastructure for project management, client work, and internal operations.

---

## Core Components

### 1. LAUNCH.py
**Role:** Entry point and environment validator

**Functions:**
- Checks Python version (3.x required)
- Verifies Tkinter installation
- Locates gui_installer.py dynamically
- Launches GUI with proper error handling

### 2. gui_installer.py
**Role:** Main user interface

**Key Features:**
- **Design System:** "Void Neon" dark theme
- **Input Collection:** Organization name, install path, service selection
- **Real-time Logging:** Console window with color-coded messages
- **Progress Tracking:** Animated progress bar
- **Threading:** Non-blocking execution

**UI Components:**
- `ModernScrollbar`: Custom canvas-based scrollbar
- `ModernToggle`: iOS-style toggle switches
- `ModernButton`: Styled clickable labels

**Tab Structure:**
- **INSTALLER:** Main configuration and deployment
- **NAMING RULES:** (Reserved for future features)
- **FEEDBACK:** User feedback submission

### 3. init_company_structure.py
**Role:** Backend folder generator

**Data Structures:**
- `COMPANY_STRUCTURE`: HR, Accounting, Marketing, Operations, Branding, Corporate Docs
- `PROJECT_STRUCTURE`: Internal Labs, External Clients, Proposals, Templates, Completed, Archive
- `SERVICE_TEMPLATES`: 8 service-specific templates (WEB/IT/CM/MFG/TECH/LEGAL/MS/MULTI)
- `EXAMPLE_CLIENT`: Sample client folder with proper structure

**Core Methods:**
- `create_structure()`: Recursive folder/file creation
- `create_folder()`: Makes directories
- `create_file()`: Writes files with content
- `build_complete_structure()`: Orchestrates full build
- `create_master_docs()`: Generates tracking files

---

## Data Flow

```
[User] --> LAUNCH.py
            ↓
       Validates Environment
            ↓
    gui_installer.py (GUI Opens)
            ↓
  User Inputs: Name, Path, Services
            ↓
   Click "INITIALIZE SYSTEMS"
            ↓
 Threading: execute_logic() in background
            ↓
   CompanyStructureBuilder instantiated
            ↓
Build Company Structure --> Create folders
            ↓
Build Project Structure --> Create folders
            ↓
Build Service Templates --> Filter by selection
            ↓
   Create Example Client --> Demo structure
            ↓
Create Master Docs --> Tracking files
            ↓
   Log completion --> Console output
            ↓
[User sees "DEPLOYMENT SUCCESSFUL"]
```

---

## Service Template Architecture

All service templates follow a standardized 5-phase workflow:

1. **01-Contract-Financials**
   - Invoicing
   - Contract-Documents
   - Change-Orders (if applicable)
   - Cost-Control (for complex projects)

2. **02-Design-Planning**
   - Service-specific planning artifacts
   - Requirements gathering
   - Design mockups/diagrams

3. **03-Execution-Deliverables**
   - Active work products
   - Testing/validation
   - Progress tracking

4. **04-Client-Communications**
   - Meeting-Minutes
   - Email-Threads
   - Weekly-Reports

5. **05-Closeout**
   - Final deliverables
   - Documentation handoff
   - Project archiving

---

## Safety Features

### Overwrite Protection
1. **Pre-check:** Before creating structure, checks if target directory exists
2. **User Confirmation:** Modal dialog requires explicit "Yes" to proceed
3. **Logging:** All skipped folders logged as warnings (yellow text)
4. **mkdir exists_ok:** Uses `Path.mkdir(exist_ok=True)` to prevent errors

### Error Handling
- Try/except blocks around all I/O operations
- User-friendly error messages in console
- No silent failures - everything logged

---

## Threading Model

**Main Thread (GUI):**
- Handles all UI updates
- Processes user input
- Updates console and progress bar

**Worker Thread (Builder):**
- Runs `execute_logic()` method
- Calls `CompanyStructureBuilder`
- Cannot directly update GUI (uses logging callback)

**Communication:**
- `self.log(message, color)` method used by worker
- Main thread updates console via `after()` calls
- Progress bar animated independently

---

## File Types Generated

### README Files (.md)
- Purpose: Explain folder contents
- Format: Markdown
- Location: Root of most major folders

### Placeholder Files
- Excel templates (.xlsx): Billing, Tracking, Schedules
- Word templates (.docx): Meeting notes, Letters
- PDF placeholders (.pdf): Contracts, Certificates
- Empty files with `path.touch()` for structure only

### Master Documentation
- PROPOSAL-TRACKER.md: CSV-format proposal log
- SERVICE-CODES.md: Markdown table of service definitions

---

## Customization Points

### Adding New Services
1. Add entry to `SERVICE_TEMPLATES` dict in `init_company_structure.py`
2. Follow 5-phase structure (01-05 folders)
3. Add toggle to `self.services` dict in `gui_installer.py`
4. Service automatically appears in GUI grid

### Modifying Folder Structure
1. Edit `COMPANY_STRUCTURE` or `PROJECT_STRUCTURE` dicts
2. Use nested dicts for folders: `'FolderName': {}`
3. Use string values for files: `'filename.txt': 'content here'`

### UI Customization
1. Color constants at top of `gui_installer.py`
2. Font constants: `FONT_HERO`, `FONT_NAV`, etc.
3. Modify `setup_ui()` method for layout changes

---

## Dependencies

### Built-in Libraries (No install needed)
- `tkinter`: GUI framework
- `pathlib`: Modern path handling
- `threading`: Background tasks
- `datetime`: Timestamps
- `argparse`: CLI argument parsing

### Optional
- `webbrowser`: Opens URLs (for upgrade links)
- `json`: Config file parsing (future feature)

---

## Performance

**Typical Build Time:**
- Small structure (1 service): 2-5 seconds
- Full structure (8 services): 8-12 seconds
- 150+ folders/files average

**Bottlenecks:**
- Disk I/O (SSD recommended)
- GUI update frequency (throttled to 20ms)
- Folder traversal in recursive creation

---

## Future Enhancements

### Planned Features
1. **Config Export/Import:** Save selections as JSON
2. **Git Integration:** Auto-initialize repos
3. **Google Drive Sync:** Cloud deployment option
4. **Custom Branding:** Logo, colors, tagline injection
5. **Template Editor:** GUI for modifying templates

### Technical Improvements
1. **Unit Tests:** pytest coverage for builder
2. **Type Hints:** Full mypy compatibility
3. **Logging Module:** Replace print() with proper logging
4. **Config Class:** Replace dicts with dataclasses

---

## Testing Strategy

### Manual Testing
1. **Happy Path:** Full build with all services
2. **Selective Build:** Individual services only
3. **Overwrite Protection:** Existing folder scenarios
4. **Error Cases:** Invalid paths, permissions issues

### Automated Testing (Future)
```python
def test_builder():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        builder = CompanyStructureBuilder(tmpdir, local_mode=True)
        builder.build_complete_structure()
        assert (Path(tmpdir) / 'HR').exists()
        assert (Path(tmpdir) / '04-TEMPLATES' / 'WEB-TEMPLATE').exists()
```

---

## Deployment

### Standard Distribution
```bash
git clone https://github.com/xsvStudio/Operations-Evolved.git
cd Operations-Evolved
python LAUNCH.py
```

### Executable Build (Future)
```bash
pyinstaller --onefile --windowed --icon=icon.ico LAUNCH.py
```

---

**Last Updated:** January 19, 2026  
**Version:** 1.0.0
