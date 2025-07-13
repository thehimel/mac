# GitHub Template Update Integration Guide

When you use a GitHub template to create a new repository, it creates a completely independent copy with no connection to the original template. This means you won't automatically get updates from the template. Here are several strategies to handle template updates:

## Option 1: Manual Integration (Most Common)

**Process:**
1. Monitor the original template repository for updates (watch it or check releases)
2. When updates are available, manually compare and copy relevant changes
3. Use GitHub's compare feature: `https://github.com/original-template/compare/old-commit...new-commit`
4. Cherry-pick the changes you want to integrate

**Pros:** Full control over what gets updated  
**Cons:** Manual work required for each update

## Option 2: Set Up a Remote to the Template

### Initial setup after creating from template:
```bash
# Add the template as a remote
git remote add template https://github.com/pdsuwwz/nextjs-nextra-starter.git

# Fetch template updates
git fetch template

# View available updates
git log HEAD..template/main --oneline
```

### When updates are available:
```bash
# Fetch latest changes
git fetch template

# Merge template changes (may require conflict resolution)
git merge template/main

# Or cherry-pick specific commits
git cherry-pick <commit-hash>
```

## Option 3: Use GitHub Actions for Update Notifications

Create a workflow that checks for template updates:

```yaml
# .github/workflows/check-template-updates.yml
name: Check Template Updates
on:
  schedule:
    - cron: '0 9 * * 1' # Weekly on Monday
  workflow_dispatch:

jobs:
  check-updates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check for template updates
        run: |
          git remote add template https://github.com/pdsuwwz/nextjs-nextra-starter.git
          git fetch template
          # Create issue if updates are available
```

## Option 4: Fork Instead of Template (Alternative Approach)

If you expect frequent updates:
1. Fork the template repository instead of using "Use this template"
2. You can then sync your fork with the upstream repository
3. Use GitHub's "Sync fork" button or:

```bash
git remote add upstream https://github.com/pdsuwwz/nextjs-nextra-starter.git
git fetch upstream
git merge upstream/main
```

## Best Practices

1. **Document your customizations** - Keep track of what you've changed from the original template
2. **Use branches** - Create a branch for template updates to test before merging
3. **Review changes carefully** - Template updates might conflict with your customizations
4. **Semantic versioning** - If the template uses releases/tags, track which version you're based on
5. **Backup before major updates** - Always commit your current state before integrating template changes

## Recommended Workflow

1. Use the template to create your project
2. Add the template as a remote (Option 2)
3. Watch the template repository for updates
4. When updates are available, create a new branch and carefully integrate changes
5. Test thoroughly before merging to main

## Key Points to Remember

- Template updates are never automatic - you always have full control over what gets integrated into your project
- Each approach has trade-offs between convenience and control
- Always test template updates in a separate branch before merging to main
- Keep documentation of your customizations to avoid conflicts during updates
