# Uninstall Android Studio and Related Android Files

## Remove the App

* Uninstall Android Studio via JetBrains ToolBox.
* Or Remove Manually:
    * Open Finder → Applications.
    * Find Android Studio and drag it to the Trash.
    * Empty the Trash.

## Remove Related Files

### Delete Configuration and Cache Files

Run the following command in Terminal to remove Android Studio’s preferences, caches, and settings:

```bash
rm -rf ~/Library/Application\ Support/Google/AndroidStudio*
rm -rf ~/Library/Preferences/com.google.android.studio.plist
rm -rf ~/Library/Caches/Google/AndroidStudio*
rm -rf ~/Library/Logs/Google/AndroidStudio*
rm -rf ~/.android
```

### Remove SDK and Emulator Files (if not needed)

If you also want to delete the Android SDK and AVD (emulator) files, run:

```shell
rm -rf ~/Library/Android
rm -rf ~/.android
rm -rf ~/Library/Caches/com.google.android.*
```

Check if the SDK exists in another location:

```shell
echo $ANDROID_HOME
echo $ANDROID_SDK_ROOT
```

If they point to another directory, delete them as well:

```shell
rm -rf /path/to/your/android/sdk
```

##  Remove Environment Variables (if set)

If you manually set environment variables for Android SDK, remove them from ~/.zshrc or ~/.bash_profile:

* Open Terminal and edit the file:

```shell
code ~/.zshrc
```

* Look for lines like:

```shell
export ANDROID_HOME=...
export ANDROID_SDK_ROOT=...
export PATH=$ANDROID_HOME/tools:$PATH
```

* Delete them and save the file.

* Reload the shell: `source ~/.zshrc`

## Remove Gradle Cache (Optional)

If you want to clear all Gradle caches:

```shell
rm -rf ~/.gradle
```

## Restart Your Mac

Restart your Mac to ensure all changes take effect.
