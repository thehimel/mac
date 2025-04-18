# ZSH

* Presently, ZSH is the default shell in Mac.
* Therefore, we do not need to install this.

## Beautify

### Remove the ‘Last Login’ prompt from iTerm/Terminal

* `cd ~ && touch .hushlogin`
* [Source](https://medium.com/macoclock/how-to-remove-the-last-login-prompt-from-iterm-terminal-on-macos-8d70dea0f2e)

### Remove Terminal Title

* Open the configuration file with VS Code using `code ~/.zshrc`.
* Uncomment `DISABLE_AUTO_TITLE="true"`.

> Install Oh My ZSH first before editing this file.

### Use Current Working Directory as the Tab Title in Termnial

* Open the configuration file with VS Code using `code ~/.zshrc`.
* Uncomment `DISABLE_AUTO_TITLE="true"`.
* Add the following lines:

```bash
# The zsh precmd function to set terminal tab title to the current working directory.
precmd () {
    tab_title="\\033]0;${PWD##*/}\\007"
    echo -ne "$tab_title"
}
```

#### Reference

* [Elegant Development Experience With Zsh and Hyper Terminal](https://robertcooper.me/post/elegant-development-experience-with-zsh-and-hyper-terminal)

## Oh My ZSH

* `Oh My Zsh is an open source, community-driven framework for managing your Zsh configuration.` - [ohmyz.sh](https://ohmyz.sh/).
* Install Oh My ZSH from [ohmyz.sh](https://ohmyz.sh/)

### Plugins

#### zsh-autosuggestions

* Install: `brew install zsh-autosuggestions`
* Activate by adding this to `~/.zshrc`: `source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh`
* Source: [Install with Homebrew](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#homebrew)

#### zsh-syntax-highlighting

* Install: `brew install zsh-syntax-highlighting`
* Activate by adding this to `~/.zshrc`: `source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh`
* Source: [Install with Homebrew](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md#using-packages)

### Fonts

* Install `MesloLGS NF` fonts by downloading the files from [here](https://github.com/romkatv/powerlevel10k#manual-font-installation) and installing them individually.

#### Configure ZSH

* Open Terminal.app
* Go to Settings.
* Select `MesloLGS NF Font Regular` in `Profiles/Basic/Fonts`. Keep the font size 12.

#### Configure Hyper

* Open the configuration file located in `~/.hyper.js`.
* Update the following fields:

```
fontSize: 12,
fontFamily: 'MesloLGS NF',
```

#### Configure VS Code

* Add the following configuration in settings.json

```
{
    ...
    "terminal.integrated.fontFamily": "MesloLGS NF",
    "terminal.integrated.fontSize": 14,
    "terminal.integrated.cursorStyle": "line",
    "terminal.integrated.cursorBlinking": true,
    "terminal.integrated.enablePersistentSessions": false,
    "editor.fontFamily": "Fira Code",
    "editor.fontSize": 14,
    "editor.unicodeHighlight.nonBasicASCII": false,
    ...
}
```

##### References

* [How to disable session restore message in vscode terminal](https://stackoverflow.com/questions/70285159/how-to-disable-session-restore-message-in-vscode-terminal)

### Themes

#### powerlevel10k

* Install: `brew install powerlevel10k`
* Activate by adding this to `~/.zshrc`: `source $(brew --prefix)/share/powerlevel10k/powerlevel10k.zsh-theme`
* Source: [Install with Homebrew](https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#homebrew)

##### Customizations

###### Remove OS Icon from Prompt

* Open `~/.p10k.zsh`.
* Comment the `os_icon` as follows:

```
# The list of segments shown on the left. Fill it with the most important segments.
typeset -g POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(
    # os_icon                 # os identifier
    dir                     # current directory
    vcs                     # git status
    # prompt_char           # prompt symbol
)
```

## Fig

* Fig allows powerful autocompletion in the terminal.
* Install fig from [here](https://fig.io/).
* [Tutorial](https://youtu.be/QsXbY33EX9w?t=243)
> Presently, Fig is not allowing new Signups.

## References

* [Install zsh autosuggestion on your terminal on your Mac for autocompletion of command you type](https://youtu.be/Gj5BuFwGK6o)
