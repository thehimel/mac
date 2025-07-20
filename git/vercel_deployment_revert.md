# Reverting to a Specific Vercel Deployment

## Overview
When a deployment breaks your application, you can revert to a previous working commit to restore functionality.

## Steps

### 1. Find the target commit
```bash
git log --oneline
```

### 2. Reset to the working commit
```bash
git reset --hard abc123f
```

### 3. Force push to trigger redeployment
```bash
git push --force-with-lease origin main
```

## Example

```bash
$ git log --oneline
def456g Fix auth redirect (broken)
abc123f Add flashcard feature (working) ← target
789xyz0 Initial setup

$ git reset --hard abc123f
HEAD is now at abc123f Add flashcard feature

$ git push --force-with-lease origin main
+ def456g...abc123f main -> main (forced update)
```

Vercel automatically redeploys from the reverted commit.

## Safety Tips

**Create a backup branch first:**
```bash
git branch backup-broken-auth def456g
```

**Alternative (safer for teams):**
```bash
git revert HEAD~n  # revert last n commits
git push origin main
```

## Important Notes
- `--force-with-lease` prevents overwriting others' changes
- This permanently removes commits after the target
- Consider team coordination before force pushing
- Vercel will automatically trigger a new deployment
