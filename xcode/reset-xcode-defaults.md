# Reset Xcode to Defaults

This guide explains how to reset Xcode preferences and settings to their default values. This is useful when Xcode behavior is unexpected or when you want to restore default settings.

## Quick Reset (Preferences Only)

This resets Xcode preferences to defaults while keeping your projects and derived data intact.

### Steps

1. **Close Xcode completely**
   ```bash
   killall Xcode
   ```

2. **Delete Xcode preferences**
   ```bash
   defaults delete com.apple.dt.Xcode
   ```

3. **Restart Xcode**
   - Xcode will recreate default preferences on launch
   - You may need to re-enter some settings like code signing preferences

> **Note**: Resetting preferences only (without clearing caches) was sufficient to fix the issue where Xcode was automatically replacing apps without asking when building. After resetting preferences and restarting Xcode, it will ask what to do with existing apps (Replace, Add, or Keep Both).

## Complete Reset (Preferences + Caches)

For a more thorough reset that also clears caches and derived data:

1. **Close Xcode completely**
   ```bash
   killall Xcode
   ```

2. **Delete Xcode preferences**
   ```bash
   defaults delete com.apple.dt.Xcode
   ```

3. **Clear derived data (build artifacts)**
   ```bash
   rm -rf ~/Library/Developer/Xcode/DerivedData
   ```

4. **Clear Xcode caches**
   ```bash
   rm -rf ~/Library/Caches/com.apple.dt.Xcode
   ```

5. **Clear module cache (optional)**
   ```bash
   rm -rf ~/Library/Developer/Xcode/DerivedData/ModuleCache.noindex
   ```

6. **Restart Xcode**
