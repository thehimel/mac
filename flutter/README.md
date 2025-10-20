# Flutter Installation Guide for macOS

Complete setup guide for Flutter development on macOS with iOS and Android support.

## Prerequisites

- macOS (works on Intel and Apple Silicon M1/M2/M3)
- Homebrew package manager installed
- Xcode installed from Mac App Store
- At least 10GB of free disk space

## Environment

This guide works for:
- **Device:** MacBook (Intel or Apple Silicon)
- **OS:** macOS Monterey 12.0 or later
- **Package Manager:** Homebrew
- **Target Platforms:** iOS and Android

---

## Installation Steps

### Install Flutter

```bash
brew install --cask flutter
```

```terminaloutput
==> Downloading https://storage.googleapis.com/flutter_infra_release/releases/stable/macos/flutter_macos_arm64_3.35.
############################################################################################################# 100.0%
==> Installing Cask flutter
==> Moving App Suite 'flutter' to '/opt/homebrew/share/flutter'
==> Linking Binary 'dart' to '/opt/homebrew/bin/dart'
==> Linking Binary 'flutter' to '/opt/homebrew/bin/flutter'
🍺  flutter was successfully installed!
```

## Install IDE Plugins

* [JetBrains Flutter Plugin](https://plugins.jetbrains.com/plugin/9212-flutter)

### Initial Health Check

```bash
flutter doctor
```

This command will show you what components are missing. Follow the steps below to fix everything.

### Configure Android

#### Install Android Studio

* Follow [Android Installation Guide](../android/README.md)
> Make sure you have set the environment variables in `~/.zshrc`.

#### Setup Android Command-line Tools

**Option A: Via Android Studio GUI (Recommended)**

1. Open Android Studio
2. Navigate to **Tools → SDK Manager**
3. Go to **SDK Tools** tab
4. Check **Android SDK Command-line Tools**
5. Click **Apply** or **OK**

**Option B: Via Command Line**

```bash
# Replace with your actual Android SDK path
~/Library/Android/sdk/cmdline-tools/latest/bin/sdkmanager --install "cmdline-tools;latest"
```

#### Android Emulator

1. Open Android Studio
2. Go to **Tools → Device Manager**
3. Click **Create Device**
4. Select a device definition (e.g., Pixel 6)
5. Select a system image (download if needed)
6. Click **Finish**

#### Accept Android Licenses

```bash
flutter doctor --android-licenses
```

Type `y` to accept all licenses when prompted.

#### Configure Android SDK Path

> Skip this step as you have already set up Android Studio and the SDK path should be auto-detected.

```bash
flutter config --android-sdk ~/Library/Android/sdk
```

### Configure iOS

#### Install Xcode

Make sure Xcode is installed from the App Store, then run:

```bash
# Switch to Xcode developer tools
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer

# Run first launch setup
sudo xcodebuild -runFirstLaunch

# Download iOS platform tools
xcodebuild -downloadPlatform iOS

# Open iOS Simulator
open -a Simulator
```

#### iOS Simulator

```bash
# Open iOS Simulator
open -a Simulator
```

Or open through Xcode: **Xcode → Open Developer Tool → Simulator**

#### Install CocoaPods

CocoaPods is required for iOS dependencies:

```bash
brew install cocoapods
```

### 3. Install Rosetta (Apple Silicon Macs Only)

If you have an M1/M2/M3 Mac, install Rosetta for compatibility:

```bash
sudo softwareupdate --install-rosetta --agree-to-license
```

### 10. Final Verification

```bash
flutter doctor -v
```

You should see checkmarks (✓) for:
- Flutter
- Android toolchain
- Xcode
- Android Studio
- Connected device (simulators/emulators)

```terminaloutput
flutter doctor                                                                                                                                                                                                                                              ✔ 
Doctor summary (to see all details, run flutter doctor -v):
[✓] Flutter (Channel stable, 3.35.6, on macOS 15.6 24G84 darwin-arm64, locale en-DE)
[✓] Android toolchain - develop for Android devices (Android SDK version 36.1.0)
[✓] Xcode - develop for iOS and macOS (Xcode 26.0.1)
[✓] Chrome - develop for the web
[✓] Android Studio (version 2025.1)
[✓] IntelliJ IDEA Ultimate Edition (version 2025.2.3)
[✓] VS Code (version 1.105.1)
[✓] Connected device (3 available)
[✓] Network resources

• No issues found!
```

## Testing Your Installation

### Create a Test Project

```bash
# Create a new Flutter project
flutter create my_first_app

# Navigate into the project
cd my_first_app
```

### Run on iOS Simulator

```bash
flutter run -d ios
```

### Run on Android Emulator

Make sure an Android emulator is running, then:

```bash
flutter run -d android
```

### List Available Devices

```bash
flutter devices
```

## Troubleshooting

### "cmdline-tools component is missing" Error

- Use **Option A** in Step 7 (Android Studio GUI method)
- Make sure you've installed the Android SDK Command-line Tools

### Xcode Issues

- Ensure Xcode is fully installed from the Mac App Store
- Open Xcode at least once and complete the initial setup
- Accept the Xcode license agreement

### Android License Issues

- Run `flutter doctor --android-licenses` and accept all
- Make sure Android Studio setup wizard has completed

### PATH Issues

If Flutter commands aren't found, add to your shell profile (`~/.zshrc` or `~/.bash_profile`):

```bash
export PATH="$PATH:`brew --prefix`/Caskroom/flutter/bin"
```

Then reload:

```bash
source ~/.zshrc  # or source ~/.bash_profile
```

---

## Useful Commands

```bash
# Check Flutter version
flutter --version

# Update Flutter
flutter upgrade

# List installed devices
flutter devices

# Clean build cache
flutter clean

# Get detailed doctor output
flutter doctor -v

# Run app in debug mode
flutter run

# Build for release (iOS)
flutter build ios --release

# Build for release (Android)
flutter build apk --release
```

## Additional Resources

- [How to install Flutter on a MacBook - YuriDevAT](https://dev.to/yuridevat/how-to-install-flutter-on-a-macbook-1mad)
- [Flutter Setup & Notes - Traversy Media](https://gist.github.com/bradtraversy/f1af78251962bb210c2ebe5b4f9a5c35)
- [Official Flutter Documentation](https://docs.flutter.dev/)
- [Flutter Installation Guide](https://docs.flutter.dev/get-started/install/macos)
- [Flutter DevTools](https://docs.flutter.dev/development/tools/devtools/overview)
