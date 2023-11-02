# ZSH

* Presently, ZSH is the default shell in Mac.
* Therefore, we do not need to install this.

## Beautify

### Remove the ‘Last Login’ prompt from iTerm/Terminal

* `cd ~ && touch .hushlogin`
* [Source](https://medium.com/macoclock/how-to-remove-the-last-login-prompt-from-iterm-terminal-on-macos-8d70dea0f2e)

### Use Current Working Directory as the Tab Title in Termnial

* Open the configuration file with VS Code using `code ~/.zshrc`.
* Uncomment `DISABLE_AUTO_TITLE="true"`.
* Add the following lines:

```
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

* [Install with Homebrew](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#homebrew)
* To edit the configuration file with vscode, you can use: `code ~/.zshrc`.

#### zsh-syntax-highlighting

* [Install with Homebrew](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md#using-packages)
* To edit the configuration file with vscode, you can use: `code ~/.zshrc`.

### Fonts

* The [nerd-fonts](https://github.com/ryanoasis/nerd-fonts) is the recommended font according to the documentation mentioned [here](https://github.com/romkatv/powerlevel10k#fonts).
* [Install with Homebrew](https://github.com/ryanoasis/nerd-fonts#option-4-homebrew-fonts)

#### Configure ZSH

* Open Terminal.app
* Go to Settings.
* Select `Heck Nerd Font Regular` in `Profiles/Basic/Fonts`.

#### Configure Hyper

* Open the configuration file located in `~/.hyper.js`.
* Update the fontFamily as `fontFamily: '"Hack Nerd Font", "DejaVu Sans Mono", Consolas, "Lucida Console", monospace',`

### Themes

#### powerlevel10k

* [Install with Homebrew](https://formulae.brew.sh/formula/powerlevel10k)
* Add the following line at the end of the `~/.zshrc` file: `source $(brew --prefix)/share/powerlevel10k/powerlevel10k.zsh-theme`

## Fig

* Fig allows powerfull autocompletion in the terminal.
* Install fig from [here](https://fig.io/).
* [Tutorial](https://youtu.be/QsXbY33EX9w?t=243)
> Presently, Fig is not allowing new Signups.

## References

* [Install zsh autosuggestion on your terminal on your Mac for autocompletion of command you type](https://youtu.be/Gj5BuFwGK6o)

