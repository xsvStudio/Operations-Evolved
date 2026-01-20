# 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md

## YOUR ACTIVATION PLAYBOOK

This document is your step-by-step guide to activate the complete framework.

---

## PHASE A: REVIEW & EDIT (30 minutes)

**Your responsibility:** Verify the framework makes sense for YOUR situation.

### A1: Read All Documents

- [ ] 00_READ_ME_FIRST.md (5 min)
- [ ] README_FRAMEWORK_OVERVIEW.md (10 min)
- [ ] 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md - **EDIT THIS** (60 min)
- [ ] NEXT_STEPS_FOR_YOU.md (10 min)
- [ ] 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md (15 min)
- [ ] 03_MASTER_AI_GUIDANCE_FRAMEWORK.md (20 min)
- [ ] 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md (this file) (10 min)
- [ ] 05_PERPLEXITY_THREAD_PROTOCOL.md (15 min)

**Total time:** ~2.5 hours

### A2: Edit Document 01 (DRAFT)

**Review 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md:**

- [ ] All features correct?
- [ ] All phases assigned correctly?
- [ ] Phase 2 truly locked? (setup wizard + folders + master files)
- [ ] Anything missing?
- [ ] Anything out of scope?
- [ ] User perspective language clear?
- [ ] All 5 workflows complete?

**Make edits:**
- [ ] Fix errors
- [ ] Add missing features
- [ ] Remove out-of-scope items
- [ ] Clarify unclear sections
- [ ] Mark items [EDITED]

### A3: Customize Documents 2 & 3

**Document 02:**
- [ ] Add your GitHub organization URLs
- [ ] Add code review lead contact
- [ ] Add leadership escalation contact

**Document 03:**
- [ ] Add leadership contact information
- [ ] Add escalation process
- [ ] Add code review lead contact

### A4: Verify 5 Locked Rules

- [ ] Phase 2 date locked: January 21, 2026
- [ ] Business model locked: $0-500/mo, 10-minute setup
- [ ] Repository locked: xsvStudio/Operations-Evolved
- [ ] Features locked: Must be in spec
- [ ] No rogue decisions: Must escalate

**All CONFIRMED?** ✅ Ready for Phase B

---

## PHASE B: PUSH TO GITHUB (10 minutes)

**Who:** You
**What:** All files are already in GitHub. They're ready.
**Status:** ✅ COMPLETE

---

## PHASE C: SHARE WITH TEAM (15 minutes)

### C1: Create Team Access

- [ ] GitHub organization members added
- [ ] Permissions set (read access to 00_MISSION_CONTROL)
- [ ] Team can clone Operations-Evolved repo
- [ ] Team can see framework documents

### C2: Share the Documents

**Send to team:**
- [ ] 00_READ_ME_FIRST.md (start here)
- [ ] README_FRAMEWORK_OVERVIEW.md (overview)
- [ ] 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md (features)
- [ ] 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md (repo rules)
- [ ] 03_MASTER_AI_GUIDANCE_FRAMEWORK.md (master guidance)
- [ ] 04_DEPLOYMENT_AND_USAGE_CHECKLIST.md (this file)
- [ ] 05_PERPLEXITY_THREAD_PROTOCOL.md (Perplexity rules)

**With message:**
```
Team,

We have a complete framework to guide our Operations-Evolved project.

START HERE: 00_READ_ME_FIRST.md

Key points:
- Phase 2 is LOCKED (setup wizard + folders)
- All code goes to xsvStudio/Operations-Evolved
- Features must be in 01_COMPLETE_FEATURES list
- When in doubt, reference these documents or escalate

Read 00_READ_ME_FIRST.md first, then the others.

Questions? Escalate to [LEADERSHIP]
```

### C3: Verify Team Understanding

- [ ] Team has access to repo
- [ ] Team can read all documents
- [ ] Team confirms 5 locked rules
- [ ] Team asks clarifying questions
- [ ] All questions answered before Phase D

---

## PHASE D: ACTIVATE & ENFORCE (Ongoing)

### D1: First AI Session

**Before starting:**
- [ ] Attach all 5 framework documents
- [ ] Confirm AI has read documents
- [ ] Confirm Phase 2 locked
- [ ] Confirm repo is xsvStudio/Operations-Evolved
- [ ] Confirm branch assignment
- [ ] Start coding with 03_MASTER_AI_GUIDANCE_FRAMEWORK.md as reference

### D2: Monitor During Work

**Weekly check-ins:**
- [ ] Are all commits going to xsvStudio org?
- [ ] Is any Phase 3 code creeping into Phase 2?
- [ ] Are sensitive data protections working?
- [ ] Are commit messages following format?
- [ ] Any rogue decisions happening?

### D3: Enforce Rules Immediately

**If you see violations:**
1. STOP work immediately
2. Reference the violated rule (Document 2 or 3)
3. Have AI fix it (undo commit, redo correctly)
4. Escalate to leadership if repeat issue
5. Update framework if clarification needed

**Examples of violations:**
- Commit to wrong repository
- Phase 3 features in Phase 2 work
- Sensitive data in commit
- Wrong commit message format
- Features not in spec

---

## PHASE E: ONGOING MAINTENANCE (Monthly)

### E1: Monthly Review

**First week of each month:**
- [ ] Review success metrics (below)
- [ ] Check for Phase 2 scope creep
- [ ] Review escalations
- [ ] Confirm all locked rules still locked
- [ ] Verify framework still makes sense

### E2: Update Framework

**Only if:**
- [ ] New information discovered
- [ ] Rules need clarification
- [ ] Processes proven ineffective
- [ ] Leadership approves changes

**NEVER update without leadership approval.**

### E3: Team Refresh

**Quarterly:**
- [ ] Share success metrics with team
- [ ] Celebrate wins
- [ ] Address persistent issues
- [ ] Refresh team on locked rules
- [ ] Onboard any new team members

---

## SUCCESS METRICS

**After 1 week of using framework, measure:**

| Metric | Target | Status |
|--------|--------|--------|
| Commits to personal accounts | 0 | [ ] Pass / [ ] Fail |
| Unauthorized Phase 3+ features | 0 | [ ] Pass / [ ] Fail |
| AI sessions starting with framework | 100% | [ ] Pass / [ ] Fail |
| Code in correct folders | 100% | [ ] Pass / [ ] Fail |
| Features matching Phase 2 spec | 100% | [ ] Pass / [ ] Fail |
| Commit messages formatted correctly | 100% | [ ] Pass / [ ] Fail |
| Sensitive data leaks | 0 | [ ] Pass / [ ] Fail |
| Team awareness of framework | 100% | [ ] Pass / [ ] Fail |

**IF ALL GREEN:** Framework is working! 🎉

**IF ANY RED:** Troubleshoot using section below.

---

## TROUBLESHOOTING

### Problem 1: Commits to Personal Account

**Symptom:** Commits showing in personal GitHub, not xsvStudio org

**Solution:**
1. Check remote URL: `git remote -v`
2. If wrong: `git remote remove origin` then `git remote add origin https://github.com/xsvStudio/Operations-Evolved`
3. Force push correct commits (after removing bad ones)
4. Share Document 02 again with AI
5. Escalate: How did this happen?

---

### Problem 2: Phase 3 Features in Phase 2 Branch

**Symptom:** Dashboard code appears in Phase 2 branch

**Solution:**
1. Reference 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
2. Show Phase 2 is LOCKED (setup wizard + folders only)
3. Have AI move code to correct Phase 3 branch
4. Reference 03_MASTER_AI_GUIDANCE_FRAMEWORK.md Rule #1
5. Escalate: How did scope creep happen?

---

### Problem 3: Sensitive Data in Commit

**Symptom:** API key, password, or credentials in commit

**Solution:**
1. DO NOT PUSH
2. Undo: `git reset HEAD~1`
3. Remove sensitive data
4. Add file to .gitignore
5. Create .env.example (with placeholders)
6. Commit again
7. Reference Document 02 Rule #6
8. Escalate immediately

---

### Problem 4: Wrong Branch Used

**Symptom:** Code committed to `main` instead of `feature/phase-2-*`

**Solution:**
1. DO NOT PUSH if it's local-only
2. Undo: `git reset HEAD~1`
3. Create correct branch: `git checkout -b feature/phase-2-setup-wizard`
4. Recommit: `git commit -m "..."`
5. If already pushed: Create PR to fix, or escalate
6. Reference Document 02 Rule #2

---

### Problem 5: Unclear Commit Message

**Symptom:** Commit message: "update code" or "fix stuff"

**Solution:**
1. Reference Document 02 Rule #4 (commit format)
2. Have AI rewrite: `[type]: [clear description]`
3. Example: `feat: Phase 2 setup wizard screen 1 - welcome screen`
4. Enforce on next commit

---

### Problem 6: Team Doesn't Understand Framework

**Symptom:** Questions about scope, phases, or procedures

**Solution:**
1. Share relevant document from the 5 frameworks
2. If still unclear: Hold team briefing
3. Reference 00_READ_ME_FIRST.md for orientation
4. For specific questions:
   - Feature questions → 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md
   - Repository questions → 02_AI_REPO_BRANCH_CONTROL_FRAMEWORK.md
   - Decision questions → 03_MASTER_AI_GUIDANCE_FRAMEWORK.md
5. If gaps in framework: Update and redistribute

---

## FAQ (Frequently Asked Questions)

### Q1: Can we add [feature] to Phase 2?
A: Check 01_COMPLETE_FEATURES_AND_WORKFLOWS_LIST.md. If not there and Phase 2: No. If Phase 3+: Defer. If not in list: Escalate to leadership.

### Q2: Can we push to personal GitHub to keep it private?
A: NO. Code MUST go to xsvStudio/Operations-Evolved. Use .gitignore for sensitive files. Reference Document 02 Rule #3.

### Q3: Can we change the January 21 date?
A: NO. Phase 2 is LOCKED. If urgent: Cut features, not date. Reference Document 03 Rule #1.

### Q4: What if we find a bug in Phase 2 code?
A: Fix it! Create bugfix branch, push to xsvStudio org, make PR, merge. Reference Document 02 for branch naming.

### Q5: Can AI commit directly to main?
A: NO. All code through feature branches and PRs. No direct commits to main/develop. Reference Document 02 Rule #2.

### Q6: What if someone asks us to deviate from the framework?
A: Reference the applicable document (02 or 03) and locked rules. If they still disagree: Escalate to leadership.

### Q7: How do we onboard new team members?
A: 1) Share 00_READ_ME_FIRST.md. 2) Have them read all 5 documents. 3) Verify understanding of 5 locked rules. 4) Assign first task with framework references.

### Q8: Can we use different AI assistants?
A: Yes. But each must confirm they've read all 5 framework documents first. Reference Document 03 sign-off section.

### Q9: What if the framework seems wrong?
A: Document the issue. Reference which document/rule seems wrong. Escalate to leadership for discussion. Don't deviate without approval.

### Q10: Who do we escalate to?
A: [ADD NAME/CONTACT FROM DOCUMENT 03]

### Q11: How often should we update the framework?
A: Monthly review. Updates only with leadership approval. Never without authority.

---

## FINAL DEPLOYMENT CHECKLIST

**Before going live:**

- [ ] Phase A complete (reviewed & edited)
- [ ] Phase B complete (in GitHub)
- [ ] Phase C complete (team has access)
- [ ] All 5 locked rules confirmed
- [ ] Team understands framework
- [ ] First AI session planned
- [ ] Leadership ready to enforce
- [ ] Escalation contacts confirmed
- [ ] Success metrics defined
- [ ] Troubleshooting guide reviewed

**READY TO LAUNCH:** ✅

---

## YOUR NEXT STEP

👉 **Go to: NEXT_STEPS_FOR_YOU.md**

It has your immediate action items and timeline.

---

**Status:** ✅ READY
**Location:** `xsvStudio/Operations-Evolved/00_MISSION_CONTROL/`
**Next Step:** Follow phases A through E above
