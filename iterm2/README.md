# iTerm2 Configuration

## Author: `Himel Das`

## References

* [iTerm2 + Oh My Zsh + Solarized color scheme + Source Code Pro Powerline + Font Awesome + Powerlevel10k - (macOS)](https://gist.github.com/kevin-smets/8568070)
* [Source: How I set up the Terminal on my M1 Max MacBook Pro - Engineering with Utsav](https://youtu.be/0MiGnwPdNGE)
* [Spice up your MacOS Terminal](https://www.engineeringwithutsav.com/blog/spice-up-your-macos-terminal)

## Settings

### Install Software

* Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
  * Source: [brew.sh](https://brew.sh)
  * **Make sure to execute the commands to add Homebrew to the PATH.**
* Install iterm2: `brew install --cask iterm2`
  * Source: [brew.sh/cask/iterm2](https://formulae.brew.sh/cask/iterm2)
* Install git: `brew install git`
  * Source: [brew.sh/formula/git](https://formulae.brew.sh/formula/git)
* Install oh-my-zsh: `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
  * Source: [https://ohmyz.sh](https://ohmyz.sh/#install) | [creator: Robby Russell](https://github.com/robbyrussell)

### Install Theme

* Execute `git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k`
  * This command is cloning this repository into `/Users/<username>/.oh-my-zsh/custom/themes/powerlevel10k`
* Download `VS Code`, and open. Open the Command Palette with `⇧ + ⌘ + P` and type `> Shell Command: Install 'code'
command in PATH`.
* Go to the root directory, and run `code ~/.zshrc` to open the file.
  * Replace `ZSH_THEME="robbyrussell"` by `ZSH_THEME="powerlevel10k/powerlevel10k"` to set the theme.

### Install Font

* Download [Source Code Pro + Font Awesome](https://github.com/Falkor/dotfiles/blob/master/fonts/SourceCodePro%2BPowerline%2BAwesome%2BRegular.ttf)
* Double-click the file and install. It will be added in `Font Book / My Fonts`.
* Otherwise, you can open `Font Book / My Fonts` and drag and drop the `ttf` file.

### Download Color Scheme

* [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes)
* Download [Solarized Dark - Patched](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/schemes/Solarized%20Dark%20-%20Patched.itermcolors)

### Configure iTerm

* Go to preferences: `⌘ + ,`
* `Appearance`
  * `General`
    * `Theme`: `Minimal`
    * `Status bar location`: `Bottom`
  * `Windows`
    * `Hide scrollbars`: `True`
* Create a profile. Make it the default profile.
  * `Colors`
    * `Option 1 (Preferred)`
      * `Color Presets...: Tango Dark`
    * `Option 2`
      * `Color Presets... / Import...`: Select `Solarized Dark - Patched.itermcolors`. Now choose this color scheme.
    * `Basic Colors / Background`: `HSB with Brightness Slider / 2b2b2b`.
  * `Text`
    * `Cursor: Vertical bar | Blinking cursor: True`
    * `Font: SourceCode+PowerLine+AwesomeRegular | Regular | 14 | Use ligatures: True`.
    * The ligatures are used to make symbols like `-->` look pretty.
  * `Window`
    * `Window Appearances: Transparency: 20 | Keep background colors opaque: True | Blue: 20`
    * `Settings for New Windows: Columns: 100 | Rows: 25`
  * `Session`
    * `Status bar enabled: True`
    * `Configure Status Bar`
      * Add `CPU`, `RAM`, and `Custom Action`.
        * Select `Custom Action` and click on `Configure Component`.
          * Set `Configure Action` with `Action`: `New Window with Profile`, and `Profile`: `<selection-your-profile>`.
      * `Auto-Rainbow`: `Automatic`
      * `Advanced / Background Color`
        * Set the color as `HSB with Brightness Slider / 2b2b2b` that is same as the background color of the terminal.
        * If scroll bar exists:
          * With the `Pen (✎)` icon, choose the color of the background of the scroll bar in the terminal.
          * For dark mode the color is `HSB with Brightness Slider / 373737`.
          * After selecting the color, make sure to turn off the `Screen Recording` for `iTerm` in `System Settings /
          Privacy and Security`.

### Remove the ‘Last Login’ Prompt

* Go to the home directory, and run `touch .hushlogin`.
* [Source](https://medium.com/macoclock/how-to-remove-the-last-login-prompt-from-iterm-terminal-on-macos-8d70dea0f2e)

### Configure Power Level 10K

* Restart `iterm2`. Follow the prompts. The configurations are saved in `~/.zshrc` file.
* The backup of this file is saved in `$TMPDIR/.zshrc.*`.
* For more information, follow [this link](https://github.com/romkatv/powerlevel10k/blob/master/font.md).
* To restart prompt, use `p10k configure`.
* Make these settings from the iTerm terminal only. If you do the settings from the terminal of any IDE such as PyCharm,
the terminal will not be configured properly.

### IDE Settings

> If the font is not configured properly, the icons are not visible in the terminal of the IDE.

#### PyCharm

* `Preferences / Font`
* `Font: SourceCode+PowerLine+AwesomeRegular` | `Size: 14`.

#### VS Code

* `Preferences / Settings / Search settings`
* `terminal.integrated.fontFamily`: `'SourceCodePro+Powerline+Awesome Regular'`
* The single quotes are very important here. Otherwise, the font won't be applied.

### Plugins

#### Auto suggestions (for Oh My Zsh)

* [Source](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)
* Clone and store the plugin with `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`.
* Add the plugin in configuration file with `code ~/.zshrc`.

```
plugins=( 
    # existing plugins
    zsh-autosuggestions
)
```

#### Syntax highlighting

* Clone and store the plugin with `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`.
* Add the plugin in configuration file with `code ~/.zshrc`. After adding this plugin the section may look like:

```
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
)
```
