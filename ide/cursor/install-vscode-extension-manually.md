# How to Install VS Code Extensions Manually

## Problem

Sometimes, VS Code extensions (or Cursor extensions) may not be available when searching in the Extensions marketplace. This can happen for various reasons:
- The extension hasn't been indexed yet in Cursor's marketplace
- Marketplace sync issues
- Extension compatibility issues

## Solution

You can manually download and install extensions by downloading the `.vsix` file from the VS Code marketplace and installing it via the command line.

## Prerequisites

- VS Code or Cursor installed
- Command line access
- `curl` or `wget` installed (usually pre-installed on macOS/Linux)

## Step-by-Step Guide

### Step 1: Find the Extension ID

From the VS Code marketplace URL, extract the publisher and extension name:
- URL format: `https://marketplace.visualstudio.com/items?itemName=PublisherName.extension-name`
- Example: `https://marketplace.visualstudio.com/items?itemName=AtomMaterial.a-file-icon-vscode`
  - Publisher: `AtomMaterial`
  - Extension name: `a-file-icon-vscode`

### Step 2: Download the Extension

Use the VS Code marketplace API to download the `.vsix` file. **Important:** The file will be gzip-compressed even though it doesn't have a `.gz` extension, so we need to decompress it.

```bash
# Download the extension (it will be gzip-compressed)
curl -L -H "Accept: application/zip" -o extension-name.vsix \
  "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/PublisherName/vsextensions/extension-name/latest/vspackage"

# Verify the file type (should show as gzip-compressed)
file extension-name.vsix

# Rename to .gz and decompress
mv extension-name.vsix extension-name.vsix.gz
gunzip -f extension-name.vsix.gz

# Verify it's now a valid zip file
file extension-name.vsix
# Should show: "Zip archive data, at least v2.0 to extract"
```

**Note:** The marketplace API returns gzip-compressed files without the `.gz` extension, which is why we need to rename it before decompressing.

### Step 3: Install the Extension

**For VS Code:**
```bash
code --install-extension extension-name.vsix
```

**For Cursor:**
```bash
cursor --install-extension extension-name.vsix
```

### Step 4: Verify Installation

After installation, you should see a success message. Then:
1. Reload the window: Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "Reload Window" and press Enter
3. The extension should now be active

### Step 5: Clean Up (Optional)

After successful installation, you can remove the downloaded `.vsix` file:
```bash
rm extension-name.vsix
```

## Complete Example: Atom Material Icons

Here's the exact working example for installing the Atom Material Icons extension (tested and verified):

```bash
# Step 1: Download the extension (it will be gzip-compressed)
curl -L -H "Accept: application/zip" -o atom-material-icons.vsix \
  "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/AtomMaterial/vsextensions/a-file-icon-vscode/latest/vspackage"

# Step 2: Verify the file type (it should show as gzip-compressed)
file atom-material-icons.vsix

# Step 3: The file is gzip-compressed, so rename it and decompress
mv atom-material-icons.vsix atom-material-icons.vsix.gz
gunzip -f atom-material-icons.vsix.gz

# Step 4: Verify it's now a valid zip file
file atom-material-icons.vsix
# Should show: "Zip archive data, at least v2.0 to extract"

# Step 5: Install in Cursor
cursor --install-extension atom-material-icons.vsix

# Or install in VS Code
# code --install-extension atom-material-icons.vsix

# Step 6: Clean up after successful installation
rm atom-material-icons.vsix
```

**Expected Output:**
```
Installing extensions...
Extension 'atom-material-icons.vsix' was successfully installed.
```

**Note:** The marketplace API returns the file as gzip-compressed even though it doesn't have a `.gz` extension. That's why we need to rename it before decompressing.

## Alternative: Using VSIXHub

If the direct marketplace API doesn't work, you can also download from VSIXHub:

1. Visit: `https://www.vsixhub.com/vsix/[extension-id]/`
2. Click "Download Latest VSIX File"
3. Install using: `cursor --install-extension /path/to/downloaded-file.vsix`

## Troubleshooting

### Error: "End of central directory record signature not found"

This means the file is still gzip-compressed. The marketplace API returns gzip-compressed files without the `.gz` extension.

**Solution:**
```bash
# Check if file is gzip-compressed
file extension-name.vsix
# Should show: "gzip compressed data"

# Rename to .gz and decompress
mv extension-name.vsix extension-name.vsix.gz
gunzip -f extension-name.vsix.gz

# Verify it's now a valid zip file
file extension-name.vsix
# Should show: "Zip archive data, at least v2.0 to extract"

# Now try installing again
cursor --install-extension extension-name.vsix
```

### Error: "Extension not found"

- Double-check the publisher name and extension name in the URL
- Ensure the extension exists in the VS Code marketplace
- Try the VSIXHub alternative method

### Extension installed but not working

1. Reload the window (`Cmd+Shift+P` → "Reload Window")
2. Check if the extension requires additional configuration
3. Verify the extension is enabled in the Extensions view

## Safety Considerations

- **Always download to your project directory or a safe location** (not `/tmp/` which can be cleared)
- **Verify the file integrity** before installing
- **Check the extension source** - only download from official VS Code marketplace or trusted sources
- **Review extension permissions** before installing

## Notes

- Extensions installed this way are the same as marketplace-installed extensions
- The extension will appear in your Extensions view after installation
- You can uninstall it normally through the Extensions UI or command line
- This method works for both VS Code and Cursor (since Cursor is based on VS Code)

## References

- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/)
- [VS Code CLI Documentation](https://code.visualstudio.com/docs/editor/command-line)
- [VSIXHub](https://www.vsixhub.com/) - Alternative download source

