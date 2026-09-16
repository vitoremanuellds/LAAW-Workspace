# Draft the copy/re-sync script

**ID:** t037-2386-55024       **Status:** done

## Description

Draft the script in LAAW/ checkout: given source and target paths,
copy workflow.md, skills/, templates/, reference/, README.md,
sync-skills.sh into <target>/.ai/workflow/, then write version stamp.

## TL;DR
- Draft LAAW/sync-workflow.sh
- Support two optional positional arguments
- Write version stamp on every run

## Steps
1. Draft sync-workflow.sh script
2. Support [source-dir] [target-root] arguments
3. Write version stamp file

## Validations
- Script exists and is executable
- Copies correct files
- Writes version stamp
