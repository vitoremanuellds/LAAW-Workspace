# Dogfood the script against this workspace

**ID:** t037-2386-07232       **Status:** done



<!-- TOC -->
<details><summary>Table of Contents</summary>

  - [Description](#description)
  - [TL;DIR](#tldir)
  - [Steps](#steps)
  - [Validations](#validations)

</details>
## Description

Dogfood: run the new script against this repo's own project root
(source = the already-checked-out LAAW/) and confirm it reproduces
.ai/workflow/'s current content unchanged.

## TL;DIR
- Run sync-workflow.sh against this workspace
- Verify diff is clean
- Confirm mechanism works against real target

## Steps
1. Run script against this workspace
2. Diff output against current .ai/workflow/
3. Confirm clean

## Validations
- diff -r shows no differences
- Script runs successfully
