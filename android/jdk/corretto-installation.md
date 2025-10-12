# Amazon Corretto Installation Guide

This guide shows how to install Amazon Corretto JDK by downloading from the official website.

## Step-by-Step Installation

### 1. Download Corretto

1. **Visit the official website**: https://aws.amazon.com/corretto/
2. **Click "Download Corretto"**
3. **Select your platform**:
   - **Operating System**: macOS
   - **Architecture**: x64
   - **Version**: Choose your preferred version (8, 11, 17, or 21)
4. **Download the package**: `.pkg` file (e.g., `amazon-corretto-21-macos-x64.pkg`)

### 2. Install the Package

1. **Locate the downloaded file** in your Downloads folder
2. **Double-click** the `.pkg` file
3. **Follow the installer**

### 3. Verify Installation

Open Terminal and run:
```bash
java -version
```

You should see output similar to:
```
openjdk version "21.0.4" 2024-07-16 LTS
OpenJDK Runtime Environment Corretto-21.0.4.7.1 (build 21.0.4+7-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.4.7.1 (build 21.0.4+7-LTS, mixed mode, sharing)
```

### 4. Set JAVA_HOME (Optional)

If you need to set JAVA_HOME environment variable:

1. **Open Terminal**
2. **Edit your shell profile**:
   ```bash
   # For zsh (default on macOS)
   nano ~/.zshrc
   
   # For bash
   nano ~/.bash_profile
   ```

3. **Add the following lines**:
   ```bash
   # For Corretto 21
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/Contents/Home
   export PATH=$JAVA_HOME/bin:$PATH
   ```

4. **Reload your profile**:
   ```bash
   # For zsh
   source ~/.zshrc
   
   # For bash
   source ~/.bash_profile
   ```

## Installation Locations

Corretto installs to the following locations:

| Version     | Installation Path                                           |
|-------------|-------------------------------------------------------------|
| Corretto 8  | `/Library/Java/JavaVirtualMachines/amazon-corretto-8.jdk/`  |
| Corretto 11 | `/Library/Java/JavaVirtualMachines/amazon-corretto-11.jdk/` |
| Corretto 17 | `/Library/Java/JavaVirtualMachines/amazon-corretto-17.jdk/` |
| Corretto 21 | `/Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/` |

## What You Get

After installation, you'll have:

- ✅ **Complete JDK installation**
- ✅ **All Java development tools** (javac, jar, jdb, etc.)
- ✅ **System-wide availability**
- ✅ **Automatic PATH setup**
- ✅ **JAVA_HOME environment variable**

## Troubleshooting

### Java Not Found
If `java -version` doesn't work:

1. **Check installation path**:
   ```bash
   ls /Library/Java/JavaVirtualMachines/
   ```

2. **Verify PATH**:
   ```bash
   echo $PATH
   ```

3. **Reinstall** if necessary

### Multiple Java Versions
If you have multiple Java versions:

1. **List all versions**:
   ```bash
   /usr/libexec/java_home -V
   ```

2. **Switch to specific version**:
   ```bash
   export JAVA_HOME=$(/usr/libexec/java_home -v 21)
   ```

## Uninstallation

To remove Amazon Corretto:

1. **Delete the installation directory**:
   ```bash
   sudo rm -rf /Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/
   ```

2. **Remove from PATH** (if manually added):
   - Edit `~/.zshrc` or `~/.bash_profile`
   - Remove Corretto-related lines
   - Reload profile

## Next Steps

After installing Corretto:

1. **Verify installation** with `java -version`
2. **Set up Android Studio** (if needed)
3. **Configure development environment**

## Resources

- **Official Website**: https://aws.amazon.com/corretto/
- **Documentation**: https://docs.aws.amazon.com/corretto/
- **GitHub**: https://github.com/corretto/corretto-jdk
