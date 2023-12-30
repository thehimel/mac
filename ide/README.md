# IDE

## Common in PyCharm, Goland, and IntelliJ IDEA

### Restore Defaults

```File -> Manage IDE Settings -> Restore IDE Settings```

### Enable or Disable Sync

```Settings -> Settings Sync```

### Customizations

#### Settings

- Appearance & Behavior
  - Appearance
    - ☑ Use custom font: `Fira Code` | Size: `14`
  - New UI
    - ☑ Enable new UI
    - ☑ Compact mode
  - Editor
    - Font
      - Font: `Fira Code`
      - Size: `14`
      - Line height: `1.2`
      - ☑ Enable ligatures
    - Color Scheme
      - Color Scheme Font
        - □ Use color scheme font instead of the default
      - Console Font
        - □ Use console font instead of the default
- Tools
  - Terminal
    - Cursor shape: `Vertical`
  - Actions on Save
    - ☑ Reformat code
    - ☑ Optimize imports
    - ☑ Rearrange code
    - ☑ Run code cleanup

#### Plugins

- [Atom Material Icons - Atom Material Themes & Plugins](https://plugins.jetbrains.com/plugin/10044-atom-material-icons)
- [Material Theme UI - Atom Material Themes & Plugins](https://plugins.jetbrains.com/plugin/8006-material-theme-ui)

#### Theme

- Material Oceanic

## IntelliJ IDEA

### Customizations

#### Settings

- Build
  - Compiler
    - ☑ Build project automatically 
  - Advanced Settings
    - ☑ Allow auto-make to start even if developed application is currently running

#### Load Maven Modules

* Clone the repository and open it with IDE and wait for sometime for the IDE to detect Maven modules.

![img.png](images/img.png)

* Click on `LOAD` to load all the projects.
* You can also load the projects manually.
  * Navigate to `Project Structure | Modules | + | Add | Import Module`
  * Select the project directory and load.

## WebStorm

### Customizations

#### Settings

- Editor
  - Code Style
    - HTML
      - Tab size: `2`
      - Indent: `2`
      - Continuation indent: `2`
    - JavaScript
      - Tab size: `2`
      - Indent: `2`
      - Continuation indent:`2`
    - Style Sheets
      - CSS
        - Tab size: `2`
        - Indent: `2`
        - Continuation indent: `2`
    - TypeScript
      - Tab size: `2`
      - Indent: `2`
      - Continuation indent: `2`
- Languages & Frameworks
  - Node.js
    - ☑ Coding assistance for Node.js

#### Load JavaScript Project

* Clode the repository and copy to the project to a directory.
* Select project directory and select `Mark Directory as | Resource Root`.

![resource-root.png](images/resource-root.png)
