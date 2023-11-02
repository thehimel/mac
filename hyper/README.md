# Hyper Terminal

* This is a walkthrough to install and configure Hyper terminal in Mac.
* Inspired by the terminal used in [this video](https://youtu.be/oe21Nlq8GS4).

## ZSH

* We use ZSH as our shell in this configuration.
* Configure ZSH with the following [instructions](../zsh).

## Hyper

* Install Hyper with Homebrew from [here](https://formulae.brew.sh/cask/hyper).

### Customize

#### Cursor

```
module.exports = {
  config: {
    ...
      // `'BEAM'` for |, `'UNDERLINE'` for _, `'BLOCK'` for █
      cursorShape: 'BEAM',
      // set to `true` (without backticks and without quotes) for blinking cursor
      cursorBlink: true,
    ...
  }
}
```

### Plugins

#### hyperpower

* Install from [here](https://hyper.is/store/hyperpower)

#### hyperborder

* Open the configuration file with VS Code using `code ~/.hyper.js`.
* Add the plugin in this section `plugins: ["hyperborder"]`.
* Customize by setting border width and animating the border:
```
module.exports = {
  config: {
    ...
      hyperBorder: {
          borderWidth: '4px',
          animate: true,
      },
    ...
  }
}
```
* [Source](https://github.com/webmatze/hyperborder)
* [Tutorial - HyperTerm with hyperborder Plugin](https://youtu.be/SfDWJRaqdLA)

### Themes

> To allow `powerlevel10k` take impact properly, run `p10k configure` after installing the theme.

#### hyper-night-owl

* Install from [here](https://hyper.is/store/hyper-night-owl).
* Tutorial: [My NEW Favourite TERMINAL Configuration | Hyper Fig Night Owl](https://youtu.be/QsXbY33EX9w)

## Uninstall a Theme or Plugin

* `hyper uninstall <theme or plugin name>`. Example: `hyper uninstall hyper-material-theme`.
* [Reference](https://stackoverflow.com/questions/62668216/how-can-i-change-the-theme-of-my-hyper-terminal-downloaded-from-hyper-is)

## References

* [My NEW Favourite TERMINAL Configuration | Hyper Fig Night Owl](https://youtu.be/QsXbY33EX9w)
* [Hyper - A modern terminal emulator for Linux](https://youtu.be/u8_HwJjbKHA)
* [Setup for new machine | Hyper Teminal + zsh (with autosuggestions) + spaceship prompt](https://gist.github.com/xavianaxw/8e75ff37adc45bc9d3d62ada2e72ff3f)
