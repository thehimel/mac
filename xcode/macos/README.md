# macOS Swift Project Initialization Guide

Complete guide to creating a new macOS application project using Swift and SwiftUI.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Creating a New Project](#creating-a-new-project)
3. [Project Configuration](#project-configuration)
4. [Project Structure](#project-structure)
5. [Using Cursor for Code Editing](#using-cursor-for-code-editing)
6. [Building and Running](#building-and-running)
7. [Next Steps](#next-steps)

## Prerequisites

### Required Tools

- **Xcode 15+** (latest version recommended)
- **macOS 13+** (for SwiftUI and modern APIs)
- **Swift 5.9+**
- Basic knowledge of Swift and SwiftUI

### Verify Installation

```bash
# Check if Xcode is installed
xcode-select --version

# Check Swift version
swift --version

# If not installed, download Xcode from Mac App Store or Apple Developer
```

## Creating a New Project

### Step 1: Launch Xcode

1. Open **Xcode** from Applications or Spotlight
2. If this is your first time, complete the setup wizard

### Step 2: Create New Project

1. In Xcode, go to **File → New → Project**
2. Select **macOS** platform tab
3. Choose **App** template
4. Click **Next**

### Step 3: Choose Template Options

Select the following options:

- **Interface**: `SwiftUI` (recommended) or `Storyboard`
- **Language**: `Swift`
- Click **Next**

## Project Configuration

### Required Fields

Configure your project with these values:

| Field                       | Description                 | Example             | Notes                                                        |
|-----------------------------|-----------------------------|---------------------|--------------------------------------------------------------|
| **Product Name**            | Display name users will see | `MyApp`             | This appears in Finder and Dock                              |
| **Team**                    | Apple Developer account     | `Add account...`    | Optional for development; required for distribution          |
| **Organization Identifier** | Reverse domain format       | `com.example`       | Used to generate Bundle Identifier                           |
| **Bundle Identifier**       | Unique app identifier       | `com.example.MyApp` | Auto-generated from Product Name and Organization Identifier |
| **Interface**               | UI framework                | `SwiftUI`           | Modern declarative framework                                 |
| **Language**                | Programming language        | `Swift`             | Only option for Swift projects                               |
| **Testing System**          | Unit testing framework      | `None` or `XCTest`  | Can add tests later                                          |
| **Storage**                 | Data persistence            | `None`              | Use UserDefaults/FileManager/Core Data as needed             |
| **Host in CloudKit**        | iCloud integration          | ☐ Unchecked         | Enable only if using CloudKit                                |

### Important Notes

- **Product Name**: This is what users see in Finder, Dock, and system menus
- **Bundle Identifier**: Must be unique. Format: `com.organization.productname`
- **Team**: Optional for local development. Required for:
  - Code signing
  - App Store distribution
  - Notarization
  - TestFlight
- **Testing System**: Choose `XCTest` if you plan to write unit tests
- **Storage**: Set to `None` if you'll handle persistence manually (UserDefaults, FileManager, etc.)

### Step 4: Save Project

1. Choose a location to save your project
2. Optionally create a Git repository (recommended)
3. Click **Create**

## Project Structure

### Default Structure

Xcode creates this structure:

```
YourApp/
├── YourApp/
│   ├── YourAppApp.swift          # App entry point (@main)
│   ├── ContentView.swift         # Main view
│   └── Assets.xcassets/          # Images, colors, icons
├── YourAppTests/                 # Unit tests (if enabled)
├── YourAppUITests/               # UI tests (if enabled)
└── YourApp.xcodeproj/            # Project file
```

### Recommended Structure

For a better organization, consider this structure:

```
YourApp/
├── YourApp/
│   ├── App/
│   │   ├── YourAppApp.swift      # App entry point
│   │   ├── AppDelegate.swift     # App lifecycle (if needed)
│   │   ├── Views/
│   │   │   ├── ContentView.swift     # Main view
│   │   │   └── Components/           # Application-specific UI components
│   │   ├── Models/
│   │   │   └── YourModel.swift       # Application-specific data models
│   │   ├── Services/
│   │   │   └── YourService.swift     # Application-specific business logic
│   │   └── Utils/
│   │       └── Extensions.swift      # Application-specific helper extensions
│   ├── Core/
│   │   ├── Utils/
│   │   │   └── CoreUtility.swift     # Reusable utilities
│   │   └── Views/
│   │       └── CoreComponent.swift  # Reusable UI components
│   └── Assets.xcassets/              # Resources
├── YourAppTests/
└── YourApp.xcodeproj/
```

This structure follows the Core/App separation principle:

- **App/** - All application-specific code (App entry, Views, Models, Services, Utils)
- **Core/** - Reusable/foundational code (utilities, views, and components that can be extracted)

## Using Cursor for Code Editing

### Overview

**Yes, you can use Cursor (or any editor) to edit Swift code!** After initializing the project in Xcode, you can use
Cursor for all your code editing needs.

### Setup

1. **Open the project folder in Cursor**:
   ```bash
   cd /path/to/YourApp
   cursor .
   ```

2. **What you can edit in Cursor**:
  - ✅ All `.swift` source files
  - ✅ Configuration files (Info.plist, etc.)
  - ✅ README and documentation files
  - ✅ Markdown files
  - ✅ JSON, YAML, and other config files
  - ⚠️ `.xcodeproj` files (best edited in Xcode)

### Recommended Workflow

**Use Xcode for:**

- Initial project setup and configuration
- Adding new files to the project (File → New → File)
- Building and running the app
- Managing project settings and targets
- Debugging with breakpoints
- Interface Builder (if using Storyboards)
- SwiftUI previews
- Code signing and capabilities

**Use Cursor for:**

- Writing and editing Swift code
- Code navigation and search across files
- Git operations and version control
- General code editing and refactoring
- Documentation writing
- Working with multiple files simultaneously
- AI-assisted coding with Cursor's features

### Tips for Using Cursor

1. **Swift Language Support**:
  - Cursor has excellent Swift language support
  - Syntax highlighting works out of the box
  - Auto-completion and IntelliSense are available

2. **File Management**:
  - When adding new files, add them in Xcode first
  - Then edit the file content in Cursor
  - The `.xcodeproj` file tracks which files are part of the project

3. **Building from Terminal**:
   ```bash
   # Build from command line
   xcodebuild -project YourApp.xcodeproj -scheme "YourApp" build
   
   # Build and run
   xcodebuild -project YourApp.xcodeproj -scheme "YourApp" \
     -configuration Debug -destination 'platform=macOS' run
   ```

4. **File Watching**:
  - Xcode automatically detects changes made in Cursor
  - No need to manually refresh or reload
  - Just switch back to Xcode and build/run

5. **Best Practices**:
  - Keep Xcode open for building and debugging
  - Use Cursor for the actual code writing
  - Use Xcode's preview feature to see SwiftUI changes in real-time
  - Commit changes frequently with Git (Cursor has excellent Git integration)

### Cursor-Specific Features

- **AI-Assisted Coding**: Use Cursor's AI features for Swift code generation and refactoring
- **Multi-file Editing**: Easily work with multiple Swift files simultaneously
- **Search and Replace**: Powerful search across the entire project
- **Git Integration**: Built-in Git support for version control
- **Extensions**: Install Swift language extensions for enhanced features

### Common Workflow Example

1. **Initial Setup** (Xcode):
  - Create new project
  - Add new Swift file: File → New → File → Swift File
  - Configure project settings

2. **Code Editing** (Cursor):
  - Open project folder in Cursor
  - Write and edit Swift code
  - Use AI features for assistance
  - Commit changes to Git

3. **Testing** (Xcode):
  - Switch back to Xcode
  - Build and run (`Cmd + R`)
  - Debug if needed
  - Use SwiftUI previews to see UI changes

4. **Iterate**:
  - Continue editing in Cursor
  - Test in Xcode
  - Repeat as needed

## Building and Running

### Option 1: Xcode (Recommended)

1. Open the project:
   ```bash
   open YourApp.xcodeproj
   ```

2. Build and run:
  - Press `Cmd + R` or click the Play button
  - Xcode will build and launch the app

**Benefits:**

- Integrated debugging
- Breakpoints
- SwiftUI previews
- Error highlighting
- Auto-completion

### Option 2: Command Line

```bash
# Build
xcodebuild -project YourApp.xcodeproj -scheme YourApp -configuration Debug build

# Run the built app
open ~/Library/Developer/Xcode/DerivedData/YourApp-*/Build/Products/Debug/YourApp.app
```

### Option 3: Archive for Distribution

1. In Xcode: **Product → Archive**
2. Wait for build to complete
3. Organizer window opens
4. Click **Distribute App** for distribution options

## Next Steps

### Configure App Capabilities

1. Select your target in Xcode
2. Go to **Signing & Capabilities** tab
3. Configure as needed:
  - **App Sandbox**: Enable/disable based on file system access needs
  - **Hardened Runtime**: Enable for distribution
  - **Code Signing**: Configure team and certificates

### Add Dependencies

**Swift Package Manager:**

1. File → Add Package Dependencies
2. Enter package URL
3. Select version
4. Add to target

**CocoaPods or SPM:**

- Follow respective documentation

### Set Minimum Deployment Target

1. Select project in navigator
2. Select target
3. **General** tab → **Minimum Deployments**
4. Choose macOS version (e.g., macOS 13.0)

### Configure Info.plist

1. Select project → Target → **Info** tab
2. Add keys as needed:
  - `NSHumanReadableCopyright`
  - `NSHighResolutionCapable`
  - Custom URL schemes
  - App permissions

## Common Configuration Options

### App Sandbox

**When to disable:**

- Need full file system access
- Running shell commands
- Accessing system directories

**When to enable:**

- App Store distribution (required)
- Better security
- Sandboxed environment

### Interface Options

**SwiftUI** (Recommended):

- Modern declarative UI
- Cross-platform code
- Live previews
- Easier state management

**Storyboard**:

- Visual interface builder
- Traditional macOS development
- More control over layout

### Testing

**XCTest**:

- Unit tests
- UI tests
- Performance tests
- Integration tests

## Resources

- [Swift Documentation](https://swift.org/documentation/)
- [SwiftUI Tutorials](https://developer.apple.com/tutorials/swiftui)
- [AppKit Documentation](https://developer.apple.com/documentation/appkit)
- [macOS Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/macos)
- [Xcode Documentation](https://developer.apple.com/documentation/xcode)

## Troubleshooting

### Build Errors

- Clean build folder: **Product → Clean Build Folder** (`Cmd + Shift + K`)
- Delete DerivedData: `~/Library/Developer/Xcode/DerivedData`
- Restart Xcode

### Code Signing Issues

- Add Apple Developer account in Xcode preferences
- Select team in Signing & Capabilities
- For development, use automatic signing

### Swift Version Issues

- Check project's Swift version: Project → Build Settings → Swift Language Version
- Update Xcode to latest version

### Cursor Not Detecting Swift

- Ensure Swift extension is installed in Cursor
- Check file associations in Cursor settings
- Verify `.swift` files are recognized (should show Swift icon)

