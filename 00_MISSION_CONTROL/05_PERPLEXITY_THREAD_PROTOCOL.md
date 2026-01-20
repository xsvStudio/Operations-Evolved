# 05_PERPLEXITY_THREAD_PROTOCOL.md

## 💭 PERPLEXITY THREAD RULES

This document specifies how to start and manage Perplexity threads for Operations-Evolved project work.

**Purpose:** Ensure Perplexity threads load required frameworks and stay on track.

---

## THE PROBLEM THIS SOLVES

**Without protocol:**
- Perplexity thread starts without context
- Frameworks not loaded/referenced
- AI doesn't know Phase 2 is locked
- AI doesn't know about xsvStudio org requirements
- Thread goes off-track with wrong information
- Work duplicated in different threads
- No continuity between sessions

**With protocol:**
- Every thread loads all required frameworks
- AI knows Phase 2 locked
- AI knows repository requirements
- AI knows feature spec
- Threads stay on track
- Clean context from start
- Continuity maintained

---

## THREAD INITIALIZATION CHECKLIST

**BEFORE STARTING any new Perplexity thread, use this checklist:**

### Step 1: Gather Required Files

- [ ] 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md (have available)
- [ ] 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md (have available)
- [ ] 03_MASTER_AI_GUIDANCE_FRAMEWORK.md (have available)
- [ ] 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md (have available)
- [ ] This file: 05_PERPLEXITY_THREAD_PROTOCOL.md (have available)

**Location:** All in `xsvStudio/Operations-Evolved/00_MISSION_CONTROL/`

### Step 2: Create New Perplexity Thread

Go to: https://www.perplexity.ai

- [ ] Create new thread ("New Chat" button)
- [ ] Title thread with task name: e.g., "Operations-Evolved: Phase 2 Setup Wizard Screen 1"
- [ ] Do NOT start any work yet

### Step 3: Attach Framework Documents

**Attach these files in order:**

1. [ ] Attach: 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
2. [ ] Attach: 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md
3. [ ] Attach: 03_MASTER_AI_GUIDANCE_FRAMEWORK.md
4. [ ] Attach: 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md
5. [ ] Attach: 05_PERPLEXITY_THREAD_PROTOCOL.md (this file)

**Tip:** Drag and drop files into Perplexity thread window

### Step 4: Send Thread Initialization Prompt

**Copy and paste this EXACTLY into the thread:**

```
I've attached 5 framework documents that are the source of truth for 
the Operations-Evolved project. Please confirm you've reviewed them.

Before we start any work, confirm you understand:

1. Phase 2 is LOCKED (setup wizard + folder structure + master files only)
2. All code goes to xsvStudio/Operations-Evolved on GitHub
3. Features must be in 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
4. You will reference these documents throughout our session
5. You will NOT make business or scope decisions (you will escalate)
6. If you're unsure about anything, ask before proceeding

Confirm understanding:
- [ ] Reviewed all 5 documents
- [ ] Phase 2 locked confirmed
- [ ] Code goes to xsvStudio org confirmed
- [ ] Features must match spec confirmed
- [ ] Will escalate decisions confirmed
- [ ] Ready to proceed
```

### Step 5: Wait for AI Confirmation

- [ ] Perplexity confirms it has read documents
- [ ] Perplexity confirms all 5 locked rules
- [ ] Perplexity confirms understanding
- [ ] If not clear: Re-state the rules
- [ ] Proceed only when fully confirmed

### Step 6: State Your Task

**NOW you can state your task:**

```
Build: [Feature Name]
Reference: 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md, [Workflow #], [Section]
Phase: 2 (LOCKED)
Repository: xsvStudio/Operations-Evolved
Branch: feature/phase-2-setup-wizard
Code location: src/components/[ComponentName]

Specific requirements:
[List requirements from spec]

Perplexity, before you write code:
1. Confirm this is Phase 2
2. Confirm this matches the spec
3. Confirm the correct branch and location
4. Proceed when confirmed
```

### Step 7: Thread During Session

**Keep thread focused:**

- [ ] Reference framework documents as needed
- [ ] AI checks spec before writing code
- [ ] AI confirms repository and branch
- [ ] AI confirms commit message format
- [ ] Ask clarifying questions
- [ ] Don't let scope creep

### Step 8: End of Thread

**Before finalizing:**

- [ ] Code matches spec (no more, no less)
- [ ] Repository and branch confirmed
- [ ] No sensitive data
- [ ] Commit message ready
- [ ] Ready for code review

**Save thread for reference:**
- [ ] Copy Perplexity URL
- [ ] Archive thread (in Perplexity)
- [ ] Note in project management where work is

---

## THREAD RULES (LOCKED)

### Rule 1: Only ONE Task Per Thread

**Good:**
- One thread for: "Setup Wizard Screen 1"
- One thread for: "Master Project Tracker template"
- One thread for: "RFI notification system"

**Bad:**
- One thread for: "Setup wizard + master files + dashboard" (TOO BROAD)
- One thread for: "Everything Phase 2" (TOO BROAD)

**Why:** Keeps context clean and focused. Easier to review and manage.

---

### Rule 2: Thread Title Must Include Phase

**Good thread titles:**
- "Operations-Evolved: [PHASE 2] Setup Wizard Screen 1 - Welcome"
- "Operations-Evolved: [PHASE 3] Dashboard Home Screen - Financials Widget"
- "Operations-Evolved: [BUG] RFI auto-numbering fix"

**Bad thread titles:**
- "Perplexity thread 1"
- "Build the app"
- "Work on features"

---

### Rule 3: All 5 Frameworks Must Be Attached

**REQUIRED attachments (in order):**
1. 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
2. 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md
3. 03_MASTER_AI_GUIDANCE_FRAMEWORK.md
4. 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md
5. 05_PERPLEXITY_THREAD_PROTOCOL.md

**If any missing:** Go back and attach it before continuing.

---

### Rule 4: No Phase 3+ Code in Phase 2 Threads

**Phase 2 thread asks for:**
- Setup wizard, folder structure, master files ONLY
- If AI suggests Phase 3: Stop and redirect
- Reference: 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md

**What to say if Phase 3 suggested:**
```
That's Phase 3 (Dashboard). We're in Phase 2 now.
Phase 2 is LOCKED to: Setup wizard + folder structure + master files.
Dashboard is Phase 3 (after January 21).
Let's stay focused on Phase 2.
```

---

### Rule 5: Reference Framework Continuously

**During thread:**
- "Reference 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md, Workflow 2, Screen 1"
- "Per 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md Rule #3, code goes in src/ folder"
- "Per 03_MASTER_AI_GUIDANCE_FRAMEWORK.md, commit format is: [type]: [description]"

**Why:** Keeps AI grounded in frameworks. Prevents scope drift.

---

### Rule 6: Confirm Before Committing

**Ask AI before commit:**

```
Before you write the commit message, confirm:
1. All code is in correct location (src/ folder)? 
2. All code matches spec (01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md)?
3. No sensitive data in code?
4. Branch is feature/phase-2-setup-wizard?
5. Commit message follows format: [type]: [description]?
```

**Wait for confirmation before AI commits.**

---

### Rule 7: Thread Archive & Continuity

**After thread is complete:**

- [ ] Save thread URL
- [ ] Archive thread (Perplexity UI)
- [ ] Note what was completed
- [ ] Reference in next thread if needed

**If continuing work in new thread:**
- [ ] Create new thread with same initialization
- [ ] Reference previous thread: "In [previous thread URL], we completed Screen 1. Now building Screen 2."
- [ ] Attach all 5 frameworks again
- [ ] State task clearly

---

### Rule #8: The "Secretary" Protocol

- **YOU (The AI)** are responsible for updating the project status files, task or issues in Github.

- **Requirement:** At the end of every successful build, you must update 06_TECHNICAL_STATE_SNAPSHOT.md and mark the specific feature as [x] Completed.  As well, locate any related issues or tasks in Github, and create a comment or update to issue.  **DO NOT** close the Github Issue, CEO will confirm comment and close.

**Goal:** Ian (CEO | Managing Principle) should never have to manually update a status file.  But verify complete prior to closing the related Roadmap, Phase or Stage task in the Github(Whether that be an, issue or item in Github Projects).

---

## COMMON MISTAKES TO AVOID

### Mistake 1: Not Attaching Frameworks

**Problem:** Start thread without attaching documents

**Result:** AI doesn't know Phase 2 locked, adds Phase 3 features, commits to wrong repo

**Fix:** STOP. Go back. Attach all 5 frameworks. Re-state rules. Restart.

---

### Mistake 2: Too Broad Task

**Problem:** "Build the entire setup wizard" in one thread

**Result:** Thread gets too complex, AI loses focus, quality suffers

**Fix:** Break into smaller threads:
- Thread 1: Setup Wizard Screen 1
- Thread 2: Setup Wizard Screen 2
- Thread 3: Setup Wizard Screen 3
- etc.

---

### Mistake 3: Not Confirming Frameworks

**Problem:** Start work without AI confirming it read documents

**Result:** AI doesn't know rules, violates them immediately

**Fix:** Use Step 4 initialization prompt. Wait for AI confirmation. Then proceed.

---

### Mistake 4: Allowing Phase Creep

**Problem:** AI suggests adding Phase 3 features

**Result:** Phase 2 gets bloated, date gets delayed

**Fix:** Reference 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md. Say "That's Phase 3. Phase 2 is locked. Let's focus."

---

### Mistake 5: Not Referencing Repository

**Problem:** AI doesn't mention repository or branch

**Result:** Could commit to wrong location

**Fix:** Explicitly state before code: "All code goes to xsvStudio/Operations-Evolved, branch feature/phase-2-setup-wizard, in src/ folder."

---

### Mistake 6: Forgetting Commit Format

**Problem:** AI writes commit: "update code"

**Result:** Commit messages are unclear, hard to track

**Fix:** Reference 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md Rule #4. Give example format.

---

## EXAMPLE THREAD FLOW

### Good Example:

**Step 1: Create thread**
- Title: "Operations-Evolved: [PHASE 2] Setup Wizard Screen 1 - Welcome"

**Step 2: Attach frameworks**
- Attach all 5 documents

**Step 3: Initialize**
```
I've attached 5 frameworks. Please confirm you understand:
1. Phase 2 locked (setup wizard + folders only)
2. Code to xsvStudio/Operations-Evolved
3. Features must be in spec
4. You will escalate decisions
5. You will reference frameworks
```

**Step 4: AI confirms**
```
Perplexity responds:
I've reviewed all 5 documents. I understand:
- Phase 2 is locked to setup wizard + folder structure
- All code goes to xsvStudio/Operations-Evolved
- Features must match spec
- I will escalate decisions
Ready to build Setup Wizard Screen 1.
```

**Step 5: Task definition**
```
Build: Setup Wizard Screen 1 (Welcome Screen)
Ref: 01_COMPLETE_FEATURES..., Workflow 2, Screen 1
Phase: 2 (LOCKED)
Repo: xsvStudio/Operations-Evolved
Branch: feature/phase-2-setup-wizard
Code: src/components/SetupWizard/Screen1_Welcome.js

Requirements:
1. Show app greeting
2. User selects industry (dropdown)
3. Show description of next steps
4. Have Continue button

Before code, confirm this matches spec and correct location.
```

**Step 6: AI confirms**
```
Perplexity responds:
Confirmed:
- This is Phase 2 (setup wizard - in spec)
- Code goes to src/components/SetupWizard/Screen1_Welcome.js
- Branch: feature/phase-2-setup-wizard
- Matches 01_COMPLETE_FEATURES..., Workflow 2, Screen 1

Ready to build. Writing code now.
```

**Step 7: AI writes code**
- Provides complete, working component
- Includes comments
- Suggests testing approach

**Step 8: Pre-commit confirmation**
```
Before commit, confirm:
1. Code matches spec? YES
2. No sensitive data? YES
3. Repository is xsvStudio org? YES
4. Branch is feature/phase-2-setup-wizard? YES
5. Commit message format: [type]: [description]? YES
```

**Step 9: AI writes commit**
```
Commit message:
feat: Phase 2 setup wizard screen 1 - welcome screen

Implements Workflow 2, Screen 1 from 01_COMPLETE_FEATURES...
- User selects industry from dropdown
- Shows description of next steps
- Continue button ready for next screen
```

**Step 10: Thread saved**
- Save URL
- Archive thread
- Note: "Setup Wizard Screen 1 complete"

---

## PERPLEXITY SPACES VS THREADS

### When to Use Threads

**Use threads for:**
- Single feature implementation
- Bug fixes
- Code review sessions
- Documentation writing
- One-off questions

**Example threads:**
- "Setup Wizard Screen 1"
- "Fix RFI auto-numbering bug"
- "Review code for security"
- "Update README documentation"

### When to Use Spaces (if available)

**Use Spaces for:**
- Long-running project work (if you have Spaces access)
- Multiple related threads under one project
- Shared workspace with team
- Continuous conversation

**If using Spaces:**
- Create Space: "Operations-Evolved Development"
- Start threads within Space
- All threads inherit framework context
- Team can see all threads

**For now:** Use Threads (more reliable, consistent)

---

## PERPLEXITY SPECIFIC LIMITATIONS

### What Perplexity Can Do

- ✅ Write code following specification
- ✅ Review code for issues
- ✅ Suggest improvements
- ✅ Reference documentation
- ✅ Answer questions about frameworks
- ✅ Create commit messages
- ✅ Explain architecture decisions

### What Perplexity CANNOT Do

- ❌ Directly push to GitHub (user does this)
- ❌ View actual GitHub repo (user shares changes)
- ❌ Make business decisions (escalates to user)
- ❌ Change locked rules (references frameworks)
- ❌ Prevent rogue decisions (user enforces)

**Important:** Always review AI output before committing to repo.

---

## ESCALATION FOR PERPLEXITY THREADS

**If Perplexity suggests:**

**Suggestion 1: "Add Phase 3 feature to Phase 2"**
→ Response: "No, Phase 2 is locked. Reference 01_COMPLETE_FEATURES list. This is Phase 3."

**Suggestion 2: "Commit to personal GitHub"**
→ Response: "No, all code goes to xsvStudio/Operations-Evolved. Reference Document 02 Rule #3."

**Suggestion 3: "Remove [required feature] to simplify"**
→ Response: "That feature is in the spec. Check 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md. We can't remove required features."

**Suggestion 4: "Use [different technology] instead"**
→ Response: "We're using [specified technology]. If you see a better approach, we escalate to leadership. For now, use [technology]."

**If Perplexity is confused:**
→ Refresh thread: "Let me re-state the core rules. Then we'll proceed."
→ Re-attach frameworks if needed
→ Restart initialization

---

## STORING THREAD REFERENCES

**After thread is complete, save:**

```
Project: Operations-Evolved
Feature: [Feature Name]
Phase: 2
Thread URL: [Perplexity URL]
Date: [Date]
Status: [Complete / In Progress / Blocked]
Notes: [Any important notes]
```

**Example:**
```
Project: Operations-Evolved
Feature: Setup Wizard Screen 1 - Welcome
Phase: 2
Thread URL: https://perplexity.ai/threads/abc123
Date: January 20, 2026
Status: Complete
Notes: Welcome screen with industry selection dropdown. Ready for PR review.
```

**Store in:** Project management tool or shared doc

---

## PERPLEXITY THREAD CHECKLIST (PRINT THIS)

```
┌────────────────────────────────────────────────┐
│  PERPLEXITY THREAD INITIALIZATION CHECKLIST               │
├────────────────────────────────────────────────┤
│                                                            │
│  Before starting Perplexity thread:                       │
│                                                            │
│  SETUP:                                                   │
│  □ Create new thread on Perplexity                         │
│  □ Title thread with Phase and feature name              │
│  □ Attach 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md    │
│  □ Attach 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md         │
│  □ Attach 03_MASTER_AI_GUIDANCE_FRAMEWORK.md             │
│  □ Attach 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md           │
│  □ Attach 05_PERPLEXITY_THREAD_PROTOCOL.md               │
│                                                            │
│  INITIALIZATION:                                          │
│  □ Send thread initialization prompt (copy-paste)          │
│  □ Wait for AI confirmation of frameworks                 │
│  □ Confirm Phase 2 locked                                 │
│  □ Confirm repo is xsvStudio/Operations-Evolved           │
│  □ Confirm feature in spec (01_COMPLETE_FEATURES)        │
│                                                            │
│  WORK:                                                    │
│  □ State task clearly                                      │
│  □ Confirm AI understands requirements                    │
│  □ Get code/output                                        │
│  □ Review before commit                                   │
│  □ Confirm all checksbox before proceeding               │
│                                                            │
│  END:                                                     │
│  □ Save thread URL                                        │
│  □ Archive thread                                         │
│  □ Note what was completed                                │
│                                                            │
└────────────────────────────────────────────────┘
```

---

**Status:** ✅ READY
**Location:** `xsvStudio/Operations-Evolved/00_MISSION_CONTROL/`
**Next Step:** Use this protocol when starting new Perplexity threads
