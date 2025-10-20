# Android

> Install [JDK](jdk) (I.e. Corretto) before proceeding.

## Android Studio

* Install via Jetbrains Toolbox.

### Environment Setup

After installing Android Studio via JetBrains Toolbox, you need to configure the Android SDK paths in your shell profile.

#### Add to `~/.zshrc`:

```bash
# Android Configuration
export ANDROID_HOME="$HOME/Library/Android/sdk"
export ANDROID_SDK_ROOT="$HOME/Library/Android/sdk"
export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/build-tools:$PATH"
export ANDROID_STUDIO_PATH="$HOME/Applications/Android Studio.app"
```

#### Verify Setup:

```bash
# Reload shell configuration
source ~/.zshrc

# Check environment variables
echo $ANDROID_HOME
echo $ANDROID_SDK_ROOT

# Test Android tools
adb version
which adb
which emulator
```

### Initialization

![sdk_setup_location.png](images/sdk_setup_location.png)
![downloaded_sdk_components.png](images/downloaded_sdk_components.png)
![license_agreement.png](images/license_agreement.png)

### Pair Devices Using Wi-Fi

#### Mac

* System Settings -> Privacy & Security -> Local Network -> Android Studio ☑

> This will allow Android Studio to search for devices in your network.

#### Android

* Developer options -> Wireless debugging -> Pair device with pairing code

> You will receive a code to use in Android Studio for connecting your device. If needed, you can remove the paired device later.

> Once the connection is established, you can run your app directly from the IDE onto the device.

> If you turn off wireless debugging and enable it again, you will be able to seamlessly run the app on your device once more.

#### Android Studio

Pair Devices Using Wi-Fi -> Pair using pairing code -> PAIR

> The connection may take anywhere from 2 to 4 minutes. Make sure to keep the screens active on both the IDE and your device during this time.
