# LaTeX Setup Guide

## Installation Instructions for macOS

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step 1: Install LaTeX Distribution](#step-1-install-latex-distribution)
4. [Step 2: Install LaTeX Workshop Extension in Cursor](#step-2-install-latex-workshop-extension-in-cursor)
5. [Step 2B: Install TeXiFy-IDEA in PyCharm](#step-2b-install-texify-idea-in-pycharm)
6. [Step 3: Configure Cursor Settings](#step-3-configure-cursor-settings)
7. [Step 4: Test Your Setup](#step-4-test-your-setup)
8. [Troubleshooting](#troubleshooting)
9. [Required Tools Summary](#required-tools-summary)
10. [Quick Reference Commands](#quick-reference-commands)
11. [Next Steps](#next-steps)
12. [Additional Resources](#additional-resources)

---

## Overview

This guide will help you install all necessary tools and plugins to run LaTeX successfully on your macOS system, specifically for editing and compiling documents in Cursor (VS Code-based editor).

---

## Prerequisites

- macOS (any recent version)
- Homebrew package manager (optional but recommended)
- Cursor editor installed
- Internet connection for downloading packages

---

## Step 1: Install LaTeX Distribution

### Option A: Install MacTeX (Full Distribution - Recommended)

MacTeX is the complete LaTeX distribution for macOS. It includes everything you need.

#### Using Homebrew (Fastest Method)

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install MacTeX
brew install --cask mactex
```

**Note:** This will download approximately 4GB. Installation takes 15-30 minutes.

#### Manual Installation

1. Visit: https://www.tug.org/mactex/
2. Download the MacTeX.pkg installer (latest version)
3. Open the downloaded .pkg file
4. Follow the installation wizard
5. Accept the default installation location

### Option B: Install BasicTeX (Minimal Distribution)

If you prefer a smaller installation (about 100MB), you can install BasicTeX and add packages as needed.

```bash
# Install BasicTeX
brew install --cask basictex

# Update PATH (add to ~/.zshrc or ~/.bash_profile)
echo 'export PATH="/Library/TeX/texbin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Install commonly needed packages
sudo tlmgr update --self
sudo tlmgr install collection-latexextra
sudo tlmgr install collection-fontsrecommended
```

### Verify LaTeX Installation

After installation, verify that pdflatex is available:

```bash
pdflatex --version
xelatex --version
```

You should see version information. If you get "command not found", you may need to add LaTeX to your PATH:

```bash
export PATH="/Library/TeX/texbin:$PATH"
```

---

## Step 2: Install LaTeX Workshop Extension in Cursor

### Method 1: Via Extension Marketplace (Recommended)

1. Open Cursor editor
2. Press `Cmd+Shift+X` (or click the Extensions icon in the sidebar)
3. Search for **"LaTeX Workshop"**
4. Look for the extension by **James Yu**
5. Click **"Install"**
6. Wait for installation to complete
7. Reload Cursor if prompted (or press `Cmd+Shift+P` and type "Reload Window")

### Method 2: Via Command Palette

1. Press `Cmd+Shift+P` to open command palette
2. Type "Extensions: Install Extensions"
3. Search for "LaTeX Workshop"
4. Install the extension

### Verify Extension Installation

1. Open any `.tex` file
2. You should see LaTeX commands highlighted
3. Check the Extensions sidebar - "LaTeX Workshop" should show as installed

---

## Step 2B: Install TeXiFy-IDEA in PyCharm

TeXiFy-IDEA is a LaTeX plugin for JetBrains IDEs (PyCharm, IntelliJ IDEA, etc.) that provides LaTeX editing and compilation support.

### Verify Plugin Installation

1. Open any `.tex` file in PyCharm
2. You should see LaTeX syntax highlighting
3. Check **Settings → Plugins** - TeXiFy-IDEA should show as installed and enabled
4. Right-click on a `.tex` file - you should see LaTeX-related options in the context menu

### Features

TeXiFy-IDEA provides:
- Syntax highlighting for LaTeX files
- Auto-completion for LaTeX commands
- Integrated PDF viewer
- BibTeX support
- Error highlighting and navigation
- Structure view for documents

---

## Step 3: Configure Cursor Settings

The workspace should already be configured, but here's how to verify or customize:

### Access Settings

1. Press `Cmd+,` to open Settings
2. Or go to Cursor → Settings → Settings

### Key Settings to Verify

- **LaTeX Workshop: Auto Build**: Set to "onSave"
- **LaTeX Workshop: Viewer**: Set to "tab" (for inline PDF viewer)
- **LaTeX Workshop: Recipe**: Set to "pdflatex"

### Workspace Settings

The project includes a `.vscode/` folder with pre-configured settings that enable all the Overleaf-like features. **These files are essential** - even if you've installed LaTeX Workshop manually, you need these configuration files for auto-compilation and PDF preview to work properly.

#### Configuration Files

1. **`.vscode/settings.json`** - [View file](.vscode/settings.json)
   - Configures LaTeX Workshop auto-compilation on save
   - Sets PDF viewer to open in a tab (like Overleaf)
   - Enables SyncTeX (double-click PDF to jump to source)
   - Configures auto-clean of build artifacts
   - Sets editor font size and styling to match Overleaf
   - **This file is REQUIRED** for auto-compilation to work

2. **`.vscode/extensions.json`** - [View file](.vscode/extensions.json)
   - Recommends the LaTeX Workshop extension
   - Cursor will prompt you to install if not already installed
   - Optional but helpful for team collaboration

#### Why These Files Are Needed

Without `.vscode/settings.json`, LaTeX Workshop won't:
- Auto-compile when you save
- Show PDF in a tab viewer
- Enable SyncTeX navigation
- Clean build artifacts automatically

These settings are automatically applied when you open the workspace in Cursor. You don't need to manually configure anything - just ensure the `.vscode/` folder is present in your project root.

---

## Step 4: Test Your Setup

### Test Compilation

1. Open `file.tex` in Cursor
2. Make a small change (e.g., edit your name)
3. Save the file (`Cmd+S`)
4. The PDF should automatically compile
5. Check the bottom panel for any errors

### Manual Compilation Test

If auto-compilation doesn't work, test manually:

```bash
cd <directory-containing-tex-file>
pdflatex file.tex
```

You should see a `file.pdf` file created.

---

## Troubleshooting

### Problem: "pdflatex: command not found"

**Solution:**

```bash
# Add to PATH
export PATH="/Library/TeX/texbin:$PATH"

# Make permanent (add to ~/.zshrc)
echo 'export PATH="/Library/TeX/texbin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Problem: Extension not working

**Solutions:**

- Reload Cursor window: `Cmd+Shift+P` → "Reload Window"
- Check if LaTeX is in PATH: `which pdflatex`
- Verify extension is enabled in Extensions panel
- Check Cursor Output panel for LaTeX Workshop errors

### Problem: PDF not showing

**Solutions:**

- Check if PDF was generated: Look for `.pdf` file in the same directory
- Open PDF manually: Right-click on PDF file → Open With
- Check LaTeX Workshop Output panel for errors
- Try compiling manually first to see error messages

### Problem: Missing LaTeX packages

**Solution:** Install missing packages using tlmgr:

```bash
sudo tlmgr install <package-name>
```

Or install common packages:

```bash
sudo tlmgr install collection-latexextra
sudo tlmgr install collection-fontsrecommended
```

---

## Required Tools Summary

### Core Tools

- **pdflatex**: PDF compiler (included in MacTeX/BasicTeX)
- **xelatex**: Alternative compiler with better font support
- **bibtex**: Bibliography processor (included)
- **tlmgr**: TeX Live package manager (included)

### Extensions

- **LaTeX Workshop**: Primary extension for LaTeX support in Cursor/VS Code
- **TeXiFy-IDEA**: LaTeX plugin for PyCharm and other JetBrains IDEs

### Optional but Recommended

- **Homebrew**: Package manager for easy installation
- **Git**: Version control (likely already installed)

---

## Quick Reference Commands

### LaTeX Commands

```bash
# Compile LaTeX document
pdflatex filename.tex

# Compile with bibliography
pdflatex filename.tex
bibtex filename
pdflatex filename.tex
pdflatex filename.tex

# Clean build artifacts
rm *.aux *.log *.out *.toc
```

### Cursor Shortcuts

- `Cmd+S` - Save and auto-compile (if enabled)
- `Cmd+Shift+P` - Command palette
- `Cmd+Shift+X` - Extensions panel
- `Cmd+,` - Settings
- `Cmd+J` - Toggle terminal panel

---

## Next Steps

After completing installation:

1. Open `file.tex`
2. Customize with your information
3. Save to see real-time PDF preview
4. Use SyncTeX: Double-click in PDF to jump to source

---

## Additional Resources

- **LaTeX Documentation**: https://www.latex-project.org/help/documentation/
- **LaTeX Workshop Extension**: https://github.com/James-Yu/LaTeX-Workshop
- **MacTeX Website**: https://www.tug.org/mactex/
- **Overleaf Documentation**: https://www.overleaf.com/learn

---
