# 03_MASTER_AI_GUIDANCE_FRAMEWORK.md

## ⭐ ONE SOURCE OF TRUTH

This document is the master guidance for EVERY AI task related to Operations-Evolved.

**If you have a question about what to do, find it here first.**

---

## THE PROBLEM THIS SOLVES

**Without framework:**
- AI asks: "Should I add Phase 3 features?"
- Different sources give different answers
- Scope creep explodes
- Phases don't stay locked
- Team confused about what's actually being built

**With framework:**
- This document IS the answer
- No ambiguity
- Phases are LOCKED
- Everyone aligned
- Features guaranteed to match spec

---

## 5 MOST IMPORTANT RULES (LOCKED - CANNOT CHANGE)

### LOCKED RULE #1: Phase 2 IMMOVABLE

**Date:** January 21, 2026

**What's Included:**
- Setup wizard (5 screens)
- Universal folder structure (7 core folders)
- Industry templates (5 types)
- Master files (6 templates)
- App installation & launch

**What's NOT Included:**
- ❌ Dashboard
- ❌ Alerts & warnings
- ❌ Financial reports
- ❌ Analytics
- ❌ Premium features
- ❌ Integrations
- ❌ Mobile apps
- ❌ Team management UI
- ❌ RFI tracking
- ❌ Change order tracking

**If pressure to add more:**
→ **CUT FEATURES, NOT DATE**

---

### LOCKED RULE #2: Business Model FIRST

**Goal:** Organize construction files in 10 minutes

**Pricing:** $0-500/mo per customer

**Design:** Must be beautiful (justifies premium tier)

**Principle:** If technical complexity grows → simplify it

**Decision Test:**
If something is too complex for 10-minute setup → REMOVE IT or REDESIGN IT

---

### LOCKED RULE #3: Code Goes to xsvStudio Org

**Repository:** `https://github.com/xsvStudio/Operations-Evolved`

**NEVER:** Personal GitHub account

**NEVER:** Wrong organization

**NEVER:** Different repository

**Branch:** `feature/phase-2-setup-wizard` (for Phase 2 work)

**Verification before every clone:** Repository URL is xsvStudio/Operations-Evolved

---

### LOCKED RULE #4: Features Must Match 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md

**Before building ANY feature:**
1. Check if it's in 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
2. Check what Phase it's assigned to
3. If Phase 2: APPROVED
4. If Phase 3+: Defer to Phase 3 branch
5. If NOT in list: Escalate to leadership

**DO NOT build features that aren't in the spec.**

---

### LOCKED RULE #5: No Rogue Decisions

**What AI can decide:** Implementation details (how to code it)

**What AI CANNOT decide:**
- Which features to include
- Which Phase features go in
- When dates can change
- Scope changes
- Business model changes
- Repository changes

**If asked to decide these: ESCALATE TO LEADERSHIP**

---

### LOCKED RULE #6: "Director-Level" Code Commenting
**Goal:** Allow Ian (CEO) and team to scan code files in seconds without reading syntax.

**Requirement:** You MUST use the "Better Comments" syntax for all non-obvious logic.
- `// ! CRITICAL: [Critical path logic or potential failure point]` (Red)
- `// ? QUESTION: [Decision needed from Ian/Leadership]` (Blue)
- `// TODO: [Future feature / Phase 3 item]` (Orange)
- `// * NOTE: [Important context for other developers]` (Green)

**Example:**
// ! CRITICAL: If this API call fails, the entire dashboard crashes.
// ? QUESTION: Should we limit this to 5 uploads for the free tier?
// TODO: Move this to the backend in Phase 3.

---

### LOCKED RULE #7: The "Additive-Only" Mandate

- **NEVER** rewrite or "refactor" existing, working files unless explicitly instructed.

- **ONLY** add new files or append code to specific sections.

- **RISK**: AI often breaks hidden dependencies when "cleaning up" code.

- **Protocol**: If you believe existing code needs changing, you must ask: "I need to modify App.js to support this new feature. May I overwrite it?"

## HOW TO START AN AI SESSION (STEP-BY-STEP)

### Step 1: Load All Required Documents

**Attach or reference:**
- [ ] 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
- [ ] 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md
- [ ] This file (03_MASTER_AI_GUIDANCE_FRAMEWORK.md)
- [ ] 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md
- [ ] 05_PERPLEXITY_THREAD_PROTOCOL.md (if using Perplexity)

**In prompt, say:**
```
I'm attaching 5 framework documents. These are the source of truth.
Before we start, please confirm you've read them and understand:

1. Phase 2 is LOCKED (setup wizard + folders only)
2. All code goes to xsvStudio/Operations-Evolved
3. Features must be in 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
4. You will NOT make business/scope decisions
5. If you're unsure, ask me
```

### Step 2: State Your Task Clearly

**Example Good Prompts:**
```
Build Workflow 2: Setup Wizard Screen 1 (Welcome Screen)
- Reference: 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md, Workflow 2, Screen 1
- Phase: 2 (LOCKED)
- Branch: feature/phase-2-setup-wizard
- Code location: src/components/SetupWizard/Screen1_Welcome.js

Implement the welcome screen that:
1. Shows app greeting
2. User selects industry (Construction / Agency / Tech / Restaurant / Personal)
3. Shows brief description of next steps
4. Has Continue button
```

### Step 3: Confirm Understanding

Before AI writes code, ask:

```
Before you write code, confirm:
1. This feature is Phase 2? (yes/no)
2. This matches 01_COMPLETE_FEATURES list? (yes/no)
3. Code goes to src/ folder? (yes/no)
4. Branch is feature/phase-2-setup-wizard? (yes/no)
5. No sensitive data will be added? (yes/no)
```

### Step 4: Get Code

AI writes code. During this:
- AI references spec in 01_COMPLETE_FEATURES
- AI follows file structure in 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK
- AI includes helpful comments
- AI suggests testing approach

### Step 5: Code Review

Before committing, use checklist below.

### Step 6: Commit & Push

AI writes commit message following format:
```
feat: Phase 2 setup wizard screen 1 - welcome screen

Implements Workflow 2, Screen 1 from 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
- User selects industry
- Shows brief description
- Continue button ready
```

**Requirement:** The "Director's Validation" Checklist Before marking a task complete, you must provide a plain-English checklist for Ian to verify the feature visually:
   - "Click 'Start'. Expect button to turn green."
   - "Type 'test@test.com'. Expect checkmark icon."
   - "Click 'Next'. Expect to see 'Screen 2'."
   - **IF** visual output does not match this exactly, the code is considered FAILED.

### Step 7: Create PR

AI creates PR with:
- Title: `[PHASE 2] feat: Setup wizard screen 1 - welcome`
- Reference to features list
- Testing notes
- Screenshots if UI change

---

## QUICK REFERENCE (Q&A)

| Question | Answer | Reference |
|----------|--------|----------|
| What should we build? | What's in Phase 2 of 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md | Document 1 |
| Can we add [feature] to Phase 2? | NO - Phase 2 is LOCKED | Rule #1 |
| Where does code go? | xsvStudio/Operations-Evolved in src/ folder | Document 2 |
| Which branch? | feature/phase-2-setup-wizard (for Phase 2 work) | Document 2 |
| Can we push to personal GitHub? | NO - NEVER | Document 2, Rule #1 |
| What's the commit message format? | `[type]: [description]` | Document 2, Rule #4 |
| Can we change the Phase 2 date? | NO - January 21 is LOCKED | Rule #1 |
| Should we build [specific feature]? | Check 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md. If yes & Phase 2: yes. If Phase 3+: defer. If not in list: escalate. | Document 1 |
| Can we change the business model? | NO - $0-500/mo per customer is locked | Rule #2 |
| Should setup take <10 minutes? | YES - non-negotiable | Rule #2 |
| What if I'm unsure about scope? | Don't decide. Escalate to leadership. | Rule #5 |
| What if [framework document] conflicts with something I read? | This is the source of truth. The framework wins. | All |

---

## 6 COMMON SCENARIOS WITH RESPONSES

### Scenario 1: "Can we add analytics to Phase 2?"

**Your Response:**
- Check 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
- Analytics is Phase 3 (row: Dashboard Home Screen)
- Phase 2 is LOCKED (Rule #1)
- Offer: "Analytics will be Phase 3, after January 21. Should I add it to the Phase 3 plan?"

### Scenario 2: "This feature needs to be more complex"

**Your Response:**
- Check business model: Goal is "10-minute setup"
- If more complex breaks this: "That violates Rule #2. We need to simplify it or remove it."
- If complexity serves 10-minute goal: "OK, as long as it still supports 10-minute setup"

### Scenario 3: "Should I commit this to my personal GitHub to keep it private?"

**Your Response:**
- NO - Rule #3 is absolute
- Code MUST go to xsvStudio/Operations-Evolved
- If sensitive: Use .gitignore and .env.example
- Reference 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md Rule #6 (Sensitive Data)

### Scenario 4: "This feature isn't in the spec. Should I build it anyway?"

**Your Response:**
- Check 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
- If not there: "No. Don't build features outside the spec."
- If urgent: "Escalate to leadership for approval before building."

### Scenario 5: "We need to push back the January 21 date"

**Your Response:**
- Phase 2 date is LOCKED (Rule #1)
- Instead: "What can we remove to make January 21?"
- Cut features if necessary, not date

### Scenario 6: "AI committed to the wrong branch/repo"

**Your Response:**
- STOP immediately (don't push)
- Follow emergency procedures in 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md
- Undo commit: `git reset HEAD~1`
- Create correct branch/repo
- Recommit
- Escalate to leadership

---

## 3 OPERATIONAL CHECKLISTS

### CHECKLIST A: Starting a Feature Task

**Before AI starts coding:**

- [ ] Feature is in 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md (if not, escalate)
- [ ] Feature is Phase 2 (if Phase 3+, defer or escalate)
- [ ] Repository confirmed: xsvStudio/Operations-Evolved
- [ ] Branch assigned: feature/phase-2-setup-wizard (or appropriate branch)
- [ ] Code location confirmed: src/ folder with correct structure
- [ ] No sensitive data will be added
- [ ] Commit message format understood
- [ ] AI has read all 5 framework documents
- [ ] All 5 LOCKED RULES confirmed
- [ ] User understands this is Phase 2 (cannot add Phase 3 features)

---

### CHECKLIST B: Reviewing AI Code

**Before committing:**

- [ ] Code implements feature from 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md correctly
- [ ] Code is in correct location (src/ folder structure)
- [ ] Code is on correct branch (not main/develop)
- [ ] No sensitive data in code or commit
- [ ] Comments explain logic
- [ ] Follows project naming conventions
- [ ] Ready for code review
- [ ] Tests written (if applicable)
- [ ] Feature matches spec (not under/over-delivering)
- [ ] Commit message follows format: `[type]: [description]`

---

### CHECKLIST C: Approving a PR

**Before merging PR:**

- [ ] PR references feature in 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
- [ ] PR title follows format: `[PHASE] [type]: description`
- [ ] Feature matches spec (no scope creep)
- [ ] Code review passed
- [ ] Tests passing
- [ ] No conflicts with base branch
- [ ] No sensitive data in commits
- [ ] If Phase 2: confirm this is Phase 2 feature (not Phase 3 creeping in)
- [ ] Ready to merge
- [ ] Delete branch after merge

---

## ESCALATION PROCEDURES

**When to escalate to leadership:**

1. **Scope Question:** "Should we build [feature not in spec]?"
   - Escalate to leadership
   - Do NOT decide yourself
   - Reference 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md

2. **Phase Question:** "Can Phase 3 features go in Phase 2?"
   - Answer: NO - Phase 2 is locked
   - If pressure to change: Escalate to leadership
   - Reference Rule #1

3. **Business Model Question:** "Can we change the $0-500/mo pricing?"
   - Answer: NO - locked
   - Escalate if someone wants to change it
   - Reference Rule #2

4. **Repository Question:** "Should code go to personal GitHub?"
   - Answer: NO - xsvStudio org only
   - Escalate if someone insists
   - Reference Rule #3 and Document 2

5. **Security Issue:** "Sensitive data in commit"
   - STOP immediately
   - Don't push
   - Follow emergency procedures in Document 2
   - Escalate to leadership
   - Run: `git reset HEAD~1` and redo without secrets

6. **Conflicting Instructions:** "Document A says X, but you said Y"
   - This framework IS the source of truth
   - If conflict exists: Escalate to leadership
   - Don't guess - ask

---

## CUSTOMIZATION REQUIRED

**ADD YOUR CONTACT INFORMATION:**

```
Leadership Contact: [NAME]
Email: [EMAIL]
Phone: [PHONE]

Code Review Lead: [NAME]
Email: [EMAIL]

Escalation Process: [BRIEF DESCRIPTION]
```

---

## QUICK REFERENCE CARD (Print This)

```
┌─────────────────────────────────────────────────────────┐
│    OPERATIONS-EVOLVED AI GUIDANCE - QUICK REFERENCE    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  5 LOCKED RULES:                                        │
│  1. Phase 2 locked (setup wizard + folders only)       │
│  2. Business model locked ($0-500/mo, 10-min setup)    │
│  3. Code to xsvStudio/Operations-Evolved (NOT personal) │
│  4. Features must match 01_COMPLETE_FEATURES list      │
│  5. No rogue decisions (escalate if unsure)            │
│                                                         │
│  BEFORE STARTING:                                       │
│  □ Attach all 5 framework documents                     │
│  □ Confirm Phase 2 locked                              │
│  □ Confirm repo is xsvStudio org                        │
│  □ Confirm branch: feature/phase-2-setup-wizard        │
│  □ Confirm feature in 01_COMPLETE_FEATURES list        │
│                                                         │
│  BEFORE COMMITTING:                                     │
│  □ Code in src/ folder                                  │
│  □ No sensitive data                                    │
│  □ Branch is feature/phase-2-* (not main/develop)      │
│  □ Commit message: [type]: [description]               │
│  □ Feature matches spec (no scope creep)               │
│                                                         │
│  WHEN UNSURE:                                           │
│  → Check 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md    │
│  → If still unsure: ESCALATE, don't guess              │
│                                                         │
│  EMERGENCY:                                             │
│  Committed to wrong repo? Run: git reset HEAD~1        │
│  Sensitive data leaked? Run: git reset HEAD~1          │
│  Always escalate to leadership after emergency fix      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## SIGN-OFF CONFIRMATION

**When starting a new AI session, confirm:**

```
I confirm I have read and understand:

✓ Document 01: Features & Workflows List
✓ Document 02: AI Repo & Branch Control Framework  
✓ Document 03: Master AI Guidance (this file)
✓ Document 04: Deployment & Usage Checklist
✓ Document 05: Perplexity Thread Protocol (if applicable)

I understand and agree to:

✓ Phase 2 is LOCKED (setup wizard + folders only)
✓ All code goes to xsvStudio/Operations-Evolved
✓ Features must be in the spec (Document 01)
✓ I will not make business/scope decisions
✓ I will escalate if unsure

I am ready to start.
```

---

## DOCUMENT MAINTENANCE SCHEDULE

**This framework should be updated:**

- **Weekly:** Check for Phase 2 feature creep
- **Weekly:** Review escalation items
- **Monthly:** Review success metrics
- **As needed:** If rules or scope changes (escalate to leadership first)

**DO NOT update without leadership approval.**

---

**Status:** ✅ READY
**Location:** `xsvStudio/Operations-Evolved/00_MISSION_CONTROL/`
**Next Step:** Add your contact info above, then share with all AI assistants before starting work
