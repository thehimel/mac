# Terraform

* [TFSwitch](https://tfswitch.warrensbox.com/) is used to easily switch between TF versions.
* You do not need to install Terraform separately if you install TFSwitch.
* Install with: `brew install warrensbox/tap/tfswitch`
* Installation guide: https://tfswitch.warrensbox.com/Installation/
* Once installed, you need to run `tfswitch` in the terminal at least once to install a TF version.
* You can switch between versions in the same way.
* You can verify with `terraform version`.

If you receive the following warning:

```bash
12:45:13.539 WARN Falling back to install to "/Users/<username>/bin" directory  
12:45:13.541 WARN Run `export PATH="$PATH:/Users/<username>/bin"` to append "/Users/<username>/bin/terraform" to $PATH 
```

This means:

* Your terminal doesn’t currently look in `/Users/<username>/bin` for programs.
* So, you should add it to your `$PATH` environment variable.
* That way, when you type terraform, the shell knows where to find it.

Add it permanently by editing your shell config file:

```bash
echo '# Add user-local bin directory to PATH for Terraform and other tools' >> ~/.zshrc
echo 'export PATH="$PATH:$HOME/bin"' >> ~/.zshrc
source ~/.zshrc
```

This will add the following to your `~/.zshrc` file:

```bash
# Add user-local bin directory to PATH for Terraform and other tools
export PATH="$PATH:$HOME/bin"
```

Verify with: `which terraform` or `terraform version`

## Set Alias

Add this line to your `~/.zshrc` file:

```bash
alias tf="terraform"
```

Then reload your shell configuration:

```bash
source ~/.zshrc
```

Or restart your terminal. Now you can use `tf` instead of `terraform` for all commands.

