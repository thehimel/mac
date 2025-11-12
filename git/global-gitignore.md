# Global Gitignore Setup for macOS

Guide to creating a global gitignore file that applies to all your Git repositories on macOS.

## Quick Setup

### Step 1: Create the Global Gitignore File

Create `~/.gitignore_global` as [.gitignore_global](.gitignore_global)

### Step 2: Configure Git

Run this command to tell Git to use your global gitignore:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

### Step 3: Verify

Check that it's configured:

```bash
git config --global core.excludesfile
```

It should output: `~/.gitignore_global`

## What This Covers

- **macOS system files** - .DS_Store and other macOS-specific files
- **IDEs** - Cursor, VS Code, and JetBrains settings
- **Python** - Cache files and virtual environments
- **Node.js** - Dependencies and debug logs
- **Common files** - Logs, temporary files, and cache directories

## Customization

You can edit `~/.gitignore_global` anytime to add or remove patterns. The changes will apply to all your Git repositories.

## Project-Specific Ignores

You can still use project-specific `.gitignore` files for additional patterns. The global gitignore works alongside local `.gitignore` files.

