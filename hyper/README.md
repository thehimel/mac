# Hyper Terminal

This is a walkthrough to install and configure Hyper terminal in Mac.

## ZSH

* We use ZSH as our shell in this configuration.
* Configure ZSH with the following [instructions](../zsh).

## Hyper

* Install Hyper with Homebrew from [here](https://formulae.brew.sh/cask/hyper).

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

## References

* [My NEW Favourite TERMINAL Configuration | Hyper Fig Night Owl](https://youtu.be/QsXbY33EX9w)
* [Hyper - A modern terminal emulator for Linux](https://youtu.be/u8_HwJjbKHA)
* [Setup for new machine | Hyper Teminal + zsh (with autosuggestions) + spaceship prompt](https://gist.github.com/xavianaxw/8e75ff37adc45bc9d3d62ada2e72ff3f)
