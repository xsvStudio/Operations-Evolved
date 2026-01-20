# 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md

## ⭐ THE GOLDEN RULE

**ALL CODE MUST GO TO: `xsvStudio/Operations-Evolved`**

**NEVER TO:** Personal GitHub account

---

## THE PROBLEM THIS SOLVES

**Before (Chaos):**
- Copilot commits code to personal account by mistake
- Feature branch gets pushed to wrong repo
- Sensitive API keys leak in public personal repo
- Team can't find the code
- Production breaks

**After (Controlled):**
- All code goes to xsvStudio organization repo
- Branch assignment is locked by feature
- Sensitive data blocked before commit
- Team always knows where code is
- Production stays safe

---

## 7 MANDATORY RULES FOR ALL AI ASSISTANTS

### RULE 1: Repository Location (NON-NEGOTIABLE)

**REQUIRED REPO:**
```
https://github.com/xsvStudio/Operations-Evolved
```

**FOLDER STRUCTURE:**
```
Operations-Evolved/
├── src/
│   ├── components/
│   ├── pages/
│   ├── styles/
│   ├── utils/
│   └── assets/
├── 00_MISSION_CONTROL/          (Documentation only)
│   ├── 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
│   ├── 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md
│   ├── 03_MASTER_AI_GUIDANCE_FRAMEWORK.md
│   ├── 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md
│   └── 05_PERPLEXITY_THREAD_PROTOCOL.md
├── docs/
├── tests/
├── README.md
└── .gitignore
```

**VERIFICATION BEFORE EVERY CLONE:**
- [ ] Clone URL is: `https://github.com/xsvStudio/Operations-Evolved`
- [ ] NOT: `https://github.com/[personal-account]/Operations-Evolved`
- [ ] NOT: `https://github.com/xsvStudio/[wrong-repo-name]`
- [ ] Organization is: `xsvStudio`
- [ ] Repository is: `Operations-Evolved`

---

### RULE 2: Branch Assignment (LOCKED)

**Branch Structure:**

**Main Branch:**
```
main
  ↓ (Production code, always deployable)
```

**Development Branch:**
```
develop
  ↓ (Staging code, tested before main)
```

**Phase 2 Branch:**
```
feature/phase-2-setup-wizard
  ↓ (Setup wizard + folder deployment)
```

**Phase 3 Branches:**
```
feature/phase-3-dashboard
feature/phase-3-reporting
feature/phase-3-alerts
feature/phase-3-team-management
```

**Bug Fix Branches:**
```
bugfix/[brief-description]
  ↓ (For urgent fixes to main)
```

**Documentation Branches:**
```
docs/[brief-description]
  ↓ (For documentation updates only)
```

**ASSIGNMENT RULES:**
- Phase 2 work → `feature/phase-2-setup-wizard` ONLY
- Phase 3 work → Corresponding `feature/phase-3-*` branch
- Bug fixes → `bugfix/*` branch
- Documentation → `docs/*` branch
- DO NOT push directly to `main` or `develop`
- DO NOT create branches off wrong branch

**VERIFICATION BEFORE EVERY PUSH:**
- [ ] Current branch is correct for the task
- [ ] Branch name matches assignment
- [ ] Branch is NOT `main` or `develop`
- [ ] Confirm branch with: `git branch` (shows * on current)

---

### RULE 3: File Destination (LOCKED)

**Code Files → `src/` folder**

```
src/
├── components/          (Reusable UI components)
├── pages/               (Page-level components)
├── styles/              (CSS, themes, design system)
├── utils/               (Helper functions, business logic)
├── assets/              (Images, icons, fonts)
├── config/              (Configuration files - NO SECRETS)
└── hooks/               (Custom React hooks)
```

**Documentation → `00_MISSION_CONTROL/` folder**

```
00_MISSION_CONTROL/
├── 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
├── 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md
├── 03_MASTER_AI_GUIDANCE_FRAMEWORK.md
├── 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md
└── 05_PERPLEXITY_THREAD_PROTOCOL.md
```

**Tests → `tests/` folder**

```
tests/
├── unit/
├── integration/
└── e2e/
```

**Configuration → Root folder**

```
.gitignore          (What NOT to commit)
.env.example        (Environment variables - NO REAL SECRETS)
package.json
pakage-lock.json
README.md
```

**CRITICAL: What NOT to push**
- `.env` (real environment file with secrets)
- `.env.local`
- API keys
- Database credentials
- Private keys
- Secrets

IF YOU SEE THESE, DO NOT COMMIT.

---

### RULE 4: Commit Message Format (STANDARDIZED)

**Format:**
```
[type]: [brief description]

[optional body explaining why]
```

**Type Options:**
- `feat:` - New feature (must reference Phase)
- `fix:` - Bug fix
- `docs:` - Documentation only
- `style:` - Code formatting, no logic change
- `refactor:` - Code restructuring
- `test:` - Test additions/updates
- `chore:` - Maintenance, dependency updates

**Examples (CORRECT):**
```
feat: Phase 2 setup wizard screen 1 - welcome screen

Adds welcome screen to setup wizard with industry selection.
User chooses: Construction, Agency, Tech, Restaurant, or Personal.
Aligns with 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md Workflow 2.

feat: Phase 3 dashboard home screen - financial widget

feat: Phase 2 universal folder structure - initial 7 core folders

fix: RFI tracker auto-numbering bug on new project

docs: Update 00_MISSION_CONTROL readme for clarity
```

**Examples (WRONG - DO NOT USE):**
```
update code
add dashboard
fixed stuff
wip
changes
```

**VERIFICATION BEFORE COMMITTING:**
- [ ] Message starts with `[type]:`
- [ ] Type is from approved list
- [ ] Description is brief and clear
- [ ] If phase-dependent, states phase
- [ ] No vague language

---

### RULE 5: Pull Request Guidelines

**When to Create PR:**
- Every feature branch → Pull request before merge
- Requires code review before merging
- Link to relevant GitHub issues

**PR Title Format:**
```
[PHASE] [Type]: Brief description
```

**Example PR Titles:**
```
[PHASE 2] feat: Setup wizard complete - all 5 screens
[PHASE 3] feat: Dashboard home screen with financial widget
[BUG] fix: RFI auto-numbering not incrementing
[DOCS] docs: Framework overview clarification
```

**PR Description Must Include:**
- [ ] What this PR does
- [ ] Which features/workflows it implements (reference 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md)
- [ ] Testing done
- [ ] Breaking changes (if any)
- [ ] Screenshots/demo (if UI change)
- [ ] Link to issue (if applicable)

**PR Must Pass:**
- [ ] No conflicts with base branch
- [ ] All tests passing
- [ ] No sensitive data in commits
- [ ] Code review approved
- [ ] Feature matches specification in 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md

---

### RULE 6: Sensitive Information Protection (ABSOLUTE)

**NEVER COMMIT:**
- API keys or tokens
- Database credentials
- Private keys
- .env files with real values
- Payment information
- Personal data (email, phone, address)
- Authentication tokens
- OAuth secrets
- Database connection strings with passwords
- SSL certificates
- SSH keys

**SAFE TO COMMIT:**
- `.env.example` (with placeholder values: `YOUR_API_KEY_HERE`)
- Configuration structure
- Public API documentation
- Settings and parameters (non-sensitive)

**IF SENSITIVE DATA IS IN A COMMIT:**
1. STOP immediately
2. DO NOT PUSH
3. Use: `git reset HEAD~1` (undo commit)
4. Remove sensitive data
5. Commit again without secrets
6. Escalate to leadership

**AUTOMATED CHECK:**
- Git hooks scan for common patterns:
  - API_KEY=
  - PASSWORD=
  - SECRET=
  - private_key
  - .pem
  - .pfx
  - DATABASE_URL with password

---

### RULE 7: Verification Checklist (BEFORE EVERY ACTION)

**Before Cloning:**
- [ ] URL is: `https://github.com/xsvStudio/Operations-Evolved`
- [ ] Organization: `xsvStudio`
- [ ] Repository: `Operations-Evolved`
- [ ] NOT cloning personal account

**Before Creating Branch:**
- [ ] Starting from correct base branch
- [ ] Branch name matches assignment
- [ ] Branch is NOT `main` or `develop`
- [ ] Branch follows naming convention

**Before Writing Code:**
- [ ] Feature is in 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
- [ ] Feature is Phase 2 (if Phase 2)
- [ ] Code goes to `src/` folder
- [ ] No sensitive data will be added

**Before Committing:**
- [ ] All changes are intentional
- [ ] No accidental files committed
- [ ] Message follows format
- [ ] No sensitive data in commit
- [ ] Commit message references feature

**Before Pushing:**
- [ ] Branch is correct
- [ ] Commits are on correct branch
- [ ] No force push to `main` or `develop`
- [ ] Ready for code review
- [ ] Feature matches spec in 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md

**After Pushing:**
- [ ] Create Pull Request
- [ ] Reference related issues
- [ ] Request code review
- [ ] Wait for approval before merge

---

## USING WITH DIFFERENT AI TOOLS

### GitHub Copilot (in VS Code)

**Before Starting:**
1. Open Operations-Evolved project
2. Confirm repository in VS Code terminal: `git remote -v`
3. Confirm correct branch: `git branch`
4. Verify no uncommitted changes: `git status`

**During Coding:**
- Reference the file location: "Store this in `src/components/SetupWizard.js`"
- Reference branch: "Work on `feature/phase-2-setup-wizard` branch"
- Reference spec: "Follow 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md Workflow 2"

**Before Pushing:**
- Review all file locations with Copilot
- Confirm no sensitive data with Copilot
- Have Copilot review commit message

### Claude / ChatGPT

**At Start of Session:**
1. Attach 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md (this file)
2. Attach 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
3. Ask to confirm repository: "xsvStudio/Operations-Evolved"
4. Ask to confirm branch before any code

**During Session:**
- Ask for file paths: "Should this go in `src/components/` or `src/pages/`?"
- Ask for verification: "Can you confirm this data doesn't contain secrets?"
- Ask before commit: "Does the commit message follow the format?"

### Cursor / Windsurf / Other IDEs

**Same as Copilot above** - verify repo, branch, and file locations before coding.

---

## EMERGENCY PROCEDURES

### Problem: Committed to Wrong Repo

**Solution:**
1. Stop immediately (DO NOT PUSH)
2. Run: `git reset HEAD~1` (undo last commit)
3. Check remote: `git remote -v`
4. If wrong remote:
   ```bash
   git remote remove origin
   git remote add origin https://github.com/xsvStudio/Operations-Evolved
   ```
5. Create correct branch on correct repo
6. Recommit with correct message
7. Push to correct repo
8. Escalate to leadership

### Problem: Committed Sensitive Data

**Solution:**
1. DO NOT PUSH
2. View what's in commit: `git show HEAD`
3. If sensitive data found:
   ```bash
   git reset HEAD~1
   ```
4. Remove sensitive data from files
5. Add to `.gitignore`
6. Commit again without secrets
7. Escalate to leadership immediately

### Problem: Pushed to Wrong Branch

**Solution:**
1. Create PR from wrong branch to correct branch
2. Review changes carefully
3. If safe: merge to correct branch
4. Delete wrong branch
5. Note the mistake for future prevention
6. If not safe: revert PR and redo on correct branch

### Problem: Merge Conflict

**Solution:**
1. DO NOT force merge
2. Contact team lead
3. Review conflicting changes
4. Resolve conflicts carefully
5. Test merged code
6. Create new PR after resolution

---

## GITHUB BRANCH PROTECTION SETUP

**Repository Admin should configure:**

**For `main` branch:**
- [ ] Require pull request reviews before merging
- [ ] Require status checks to pass
- [ ] Require branches to be up to date
- [ ] Require code owners review (if applicable)
- [ ] Dismiss stale PR approvals
- [ ] Require signed commits
- [ ] Include administrators in restrictions
- [ ] Allow force pushes: **DISABLED**

**For `develop` branch:**
- [ ] Require pull request reviews before merging
- [ ] Require status checks to pass
- [ ] Require branches to be up to date
- [ ] Allow force pushes: **DISABLED**

**For `feature/*` branches:**
- [ ] No special restrictions
- [ ] Allow deletion after merge
- [ ] Auto-delete head branches

---

## TESTING SCENARIOS

### Scenario 1: Copilot Suggests Wrong Repository

**Situation:**
Copilot suggests: "Let me push this to your personal GitHub..."

**Response:**
- [ ] STOP
- [ ] Say: "No, this must go to xsvStudio/Operations-Evolved"
- [ ] Verify repository URL before proceeding
- [ ] Confirm branch assignment

### Scenario 2: Phase 4 Feature Request in Phase 2

**Situation:**
User asks: "Add the analytics dashboard to Phase 2"
Phase 2 is LOCKED to setup wizard + folders only.

**Response:**
- [ ] Reference 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
- [ ] Show Phase 2 is locked to:
  - Setup wizard
  - Folder structure
  - Master files
- [ ] Explain analytics is Phase 3 (after Jan 21)
- [ ] Offer to add to Phase 3 instead

### Scenario 3: Accidental Commit of .env File

**Situation:**
```bash
$ git commit -m "feat: add environment setup"
# Accidentally included .env file with real API keys
```

**Response:**
- [ ] DO NOT PUSH
- [ ] Run: `git reset HEAD~1`
- [ ] Remove .env file
- [ ] Add .env to .gitignore
- [ ] Create .env.example (with placeholders)
- [ ] Commit again without secrets
- [ ] Alert leadership about near-miss

---

## SUCCESS METRICS (After 1 Week)

- ✅ Zero commits to personal accounts (target: 0)
- ✅ 100% of code in xsvStudio/Operations-Evolved
- ✅ 100% of code in `src/` folder
- ✅ Zero sensitive data leaked (target: 0)
- ✅ All commit messages follow format
- ✅ All branches follow naming convention
- ✅ 100% of PRs reference features
- ✅ Zero rogue Phase 4 code in Phase 2 branch

**IF ALL GREEN:** Framework is working! 🎉

---

## CUSTOMIZATION REQUIRED

**ADD YOUR GITHUB INFORMATION:**

```
Organization Name: xsvStudio
Repository Name: Operations-Evolved
Repository URL: https://github.com/xsvStudio/Operations-Evolved
Code Review Lead: [ADD NAME]
Leadership Contact: [ADD NAME/EMAIL]
```

---

**Status:** ✅ READY
**Location:** `xsvStudio/Operations-Evolved/00_MISSION_CONTROL/`
**Next Step:** Add your contact information above, then share with all AI assistants
