# IDE

## VS Code

### Extensions

- [Typos spell checker](https://open-vsx.org/extension/tekumara/typos-vscode)
- [MDX](https://open-vsx.org/extension/unifiedjs/vscode-mdx)
- [vscode-pdf](https://open-vsx.org/extension/tomoki1207/pdf)
- [LaTeX Workshop](https://open-vsx.org/extension/James-Yu/latex-workshop)

### Theme

- [One Dark Pro Flat](https://open-vsx.org/extension/zhuangtongfa/material-theme)
- [Atom Material Icons](https://marketplace.visualstudio.com/items?itemName=AtomMaterial.a-file-icon-vscode)

## Common in PyCharm, Goland, and IntelliJ IDEA

### Restore Defaults

```File -> Manage IDE Settings -> Restore IDE Settings```

### Enable or Disable Sync

```Settings -> Settings Sync```

### Customizations

#### Settings

- Appearance & Behavior
  - Appearance
    - Theme: `Material Oceanic`
    - Editor color scheme: `Material Oceanic Theme default`
    - ☑ Use custom font: `Fira Code` | Size: `14`
  - New UI
    - ☑ Enable new UI
    - ☑ Compact mode
- Editor
  - General
    - ☑ Change font size with Command+Mouse Wheel in:
      - All editors
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
- Version Control
  - Git
    - Push
      - Protected branches
        - Remove `master;main` if exists to enable `Force Push` for all branches
- Tools
  - Terminal
    - Terminal engine: `Classic` (For unified colors)
    - Font Settings
      - Font: `MesloLGS NF` | Fallback: `Fira Code`
      - Size: `14.0` | Line height: `1.0` | Column width: `1.0`
    - Cursor shape: `Vertical`
  - Actions on Save
    - ☑ Reformat code
    - ☑ Optimize imports
    - ☑ Rearrange code
    - ☑ Run code cleanup
- Advanced Settings 
  - ☑ Use Safe Force Push (Use '--force-with-lease' when calling force push from IDE instead of just '--force')

#### Plugins

- [Atom Material Icons - Atom Material Themes & Plugins](https://plugins.jetbrains.com/plugin/10044-atom-material-icons)
- [Material Theme UI - Atom Material Themes & Plugins](https://plugins.jetbrains.com/plugin/8006-material-theme-ui)
- [Rainbow Brackets](https://plugins.jetbrains.com/plugin/10080-rainbow-brackets)
- [.​env files support](https://plugins.jetbrains.com/plugin/9525--env-files-support)
- [TeXiFy-IDEA](https://plugins.jetbrains.com/plugin/9473-texify-idea)
- [PDF Viewer](https://plugins.jetbrains.com/plugin/14494-pdf-viewer)
- [StarFactory - For MDC Files](https://plugins.jetbrains.com/plugin/28096-starfactory)

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
      - Tabs and Indents
        - Tab size: `2`
        - Indent: `2`
        - Continuation indent: `2`
      - Wrapping and Braces
        - Function declaration parameters
          - □ Align when multiline
- Languages & Frameworks
  - Node.js
    - ☑ Coding assistance for Node.js

### Debugging TypeScript

* Enable `sourceMap` and set the distribution output directory with `outDir` in the TS config file.
* Compile the code with tsc command.
* Select your breakpoints in the TS file.
* Select the corresponding JS file in the distribution output directory.
* Launch debug session by clicking on the 🐞 icon from the top right corner.
* It will start the debug session with TS file.

#### tsconfig.json

```json
{
  "compilerOptions": {
    "target": "es2016",
    "module": "commonjs",
    "rootDir": "./src",
    "sourceMap": true,
    "outDir": "./dist",
    "removeComments": true,
    "noEmitOnError": true
  }
}
```

#### Load JavaScript Project

* Clode the repository and copy to the project to a directory.
* Select project directory and select `Mark Directory as | Resource Root`.

![resource-root.png](images/resource-root.png)
