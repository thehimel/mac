# Upgrade Amazon Corretto from 21 to 25

This guide shows how to replace Amazon Corretto 21 with Corretto 25 on macOS.

## Prerequisites

- Amazon Corretto 21 currently installed
- Administrator privileges
- Internet connection

## Step-by-Step Upgrade Process

### 1. Download Corretto 25

1. **Visit the official website**: https://aws.amazon.com/corretto/
2. **Click "Download Corretto"**
3. **Select your platform**:
   - **Operating System**: macOS
   - **Architecture**: x64
   - **Version**: 25 (latest)
4. **Download the package**: `amazon-corretto-25-macos-x64.pkg`

### 2. Install Corretto 25

1. **Locate the downloaded file** in your Downloads folder
2. **Double-click** the `.pkg` file
3. **Follow the installer**:
   - Click "Continue"
   - Review the license agreement
   - Click "Agree" if you accept the terms
   - Click "Install"
   - Enter your administrator password when prompted
   - Wait for installation to complete
   - Click "Close"

### 3. Verify Corretto 25 Installation

Open Terminal and run:
```bash
java -version
```

You should see output similar to:
```
openjdk version "25.0.1" 2024-10-15 LTS
OpenJDK Runtime Environment Corretto-25.0.1.7.1 (build 25.0.1+7-LTS)
OpenJDK 64-Bit Server VM Corretto-25.0.1.7.1 (build 25.0.1+7-LTS, mixed mode, sharing)
```

### 4. Remove Corretto 21

**⚠️ Warning**: This will permanently delete Corretto 21. Make sure Corretto 25 is working first.

```bash
sudo rm -rf /Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/
```

### 5. Update JAVA_HOME (If Set)

If you previously set JAVA_HOME, update it to point to Corretto 25:

1. **Open Terminal**
2. **Edit your shell profile**:
   ```bash
   # For zsh (default on macOS)
   nano ~/.zshrc
   
   # For bash
   nano ~/.bash_profile
   ```

3. **Update JAVA_HOME**:
   ```bash
   # Remove old JAVA_HOME lines and add:
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-25.jdk/Contents/Home
   export PATH=$JAVA_HOME/bin:$PATH
   ```

4. **Reload your profile**:
   ```bash
   # For zsh
   source ~/.zshrc
   
   # For bash
   source ~/.bash_profile
   ```

### 6. Final Verification

Run the following commands to confirm everything is working:

```bash
# Check Java version
java -version

# Check JAVA_HOME (if set)
echo $JAVA_HOME

# Check Java compiler
javac -version
```

## Expected Results

### Before Upgrade
```bash
$ java -version
openjdk version "21.0.4" 2024-07-16 LTS
OpenJDK Runtime Environment Corretto-21.0.4.7.1 (build 21.0.4+7-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.4.7.1 (build 21.0.4+7-LTS, mixed mode, sharing)
```

### After Upgrade
```bash
$ java -version
openjdk version "25.0.1" 2024-10-15 LTS
OpenJDK Runtime Environment Corretto-25.0.1.7.1 (build 25.0.1+7-LTS)
OpenJDK 64-Bit Server VM Corretto-25.0.1.7.1 (build 25.0.1+7-LTS, mixed mode, sharing)
```

## Installation Locations

| Version | Installation Path |
|---------|-------------------|
| ~~Corretto 21~~ | ~~`/Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/`~~ (removed) |
| Corretto 25 | `/Library/Java/JavaVirtualMachines/amazon-corretto-25.jdk/` |

## What You Get

After the upgrade:

- ✅ **Latest Java 25** with newest features
- ✅ **Better performance** and security
- ✅ **Future-proof** for new development tools
- ✅ **Clean system** with only one Java version
- ✅ **Compatible** with Android Studio and other tools

## Troubleshooting

### Java Version Still Shows 21

If `java -version` still shows 21:

1. **Check if Corretto 21 was actually removed**:
   ```bash
   ls /Library/Java/JavaVirtualMachines/
   ```

2. **Verify Corretto 25 installation**:
   ```bash
   ls /Library/Java/JavaVirtualMachines/amazon-corretto-25.jdk/
   ```

3. **Check PATH**:
   ```bash
   echo $PATH
   ```

4. **Restart Terminal** and try again

### JAVA_HOME Issues

If JAVA_HOME is not set correctly:

1. **Check current JAVA_HOME**:
   ```bash
   echo $JAVA_HOME
   ```

2. **Set JAVA_HOME manually**:
   ```bash
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-25.jdk/Contents/Home
   ```

3. **Add to shell profile** for persistence

### Multiple Java Versions

If you see multiple Java versions:

1. **List all versions**:
   ```bash
   /usr/libexec/java_home -V
   ```

2. **Set specific version**:
   ```bash
   export JAVA_HOME=$(/usr/libexec/java_home -v 25)
   ```

## Rollback (If Needed)

If you need to rollback to Corretto 21:

1. **Download Corretto 21** from the website
2. **Install it** using the same process
3. **Remove Corretto 25**:
   ```bash
   sudo rm -rf /Library/Java/JavaVirtualMachines/amazon-corretto-25.jdk/
   ```

## Next Steps

After successful upgrade:

1. **Test with your development tools** (Android Studio, etc.)
2. **Update any project configurations** if needed
3. **Enjoy the latest Java features** and performance improvements

## Resources

- **Official Website**: https://aws.amazon.com/corretto/
- **Release Notes**: https://github.com/corretto/corretto-jdk/releases
- **Documentation**: https://docs.aws.amazon.com/corretto/
