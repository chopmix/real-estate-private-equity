# Test plan

## Automated

Run from the repository root. The tools sit outside the plugin folder.

| Check | Command | Passes when |
|-------|---------|-------------|
| Plugin rules | `python3 tools/tests/lint_repo.py` | No errors against the directory's pre-submission rules |
| Plugin format | `claude plugin validate ./plugin` | Validation passed |
| Reference quick screen | `python3 tools/tests/test_engine.py` | Example deals build, recalculate and match the independent check |
| Reference auditor | `python3 tools/tests/test_audit.py` | Clean workbook passes. Corrupted copies are caught |

## By hand, before each release

1. Load the plugin in Claude and ask which skills it has.
2. Set up a buy box from `skills/repe-core/references/buy-box-template.md`.
3. Run one deal of each engine from offering memorandum to IC memo: screen, rent roll and T-12, market, model, waterfall, checklist, memo. Run the model once in a firm template and once built to standard.
4. Open each workbook in Excel. Confirm the master check reads OK, change three inputs, and confirm every sheet updates.
5. Compare each output with the same request run without the plugin.

## Real-deal testing

Run past deals with known answers privately. Compare the model's NOI, loan size, returns and waterfall with the closed model. Record differences and fix the cause. Never commit real deal files.

## Sector review

Each playbook needs a named reviewer with direct experience in that property type before it is marked reviewed.

| Playbook group | Reviewer | Status |
|----------------|----------|--------|
| Multifamily, student, single-family rental | | |
| Office, net lease, medical office | | |
| Industrial, retail | | |
| Hotels | | |
| Seniors housing | | |
| Data centers, life science | | |
| Development, for-sale | | |
| Affordable, program overlays | | |
