# Mac
Mac configurations

## Update Software

* `brew update -d`. Here `-d` is to see what is happening behind.

## Useful Commands

* Change creation date all files and directories recursively: `find /Users/username/Documents -exec SetFile -d "$(date +"%m/%d/%Y %H:%M:%S")" {} +`
* Change creation date all files and directories recursively in current directory: `find . -exec SetFile -d "$(date +"%m/%d/%Y %H:%M:%S")" {} +`
* Generate a 32-byte random value encoded in Base64 format: `openssl rand -base64 32`
* Remove password protection from a PDF file: `qpdf --password=yourpassword --decrypt input.pdf output.pdf`

## Install Software

### Install Python with brew:

* Install: `brew install python`
* Link: `brew link python3`
* Test: `which python3` and `where python3`
* Open `~/.zshrc` with `code ~/.zshrc`
* Add the following configurations to the `~/.zshrc` file:

```shell
# Aliases
alias ts="ts-node"
alias python="python3"
alias pip="pip3"

# Ensure Python is in the PATH for the scripts to work correctly
export PATH="/usr/local/bin:$PATH"
```

* To apply the changes without restarting your terminal, run:

* References
  * https://opensource.com/article/19/5/python-3-default-mac
* Notes:
  * Previous location of python3: `/usr/bin/python3`
  * Homebrew location of python3: `/opt/homebrew/bin/python3`

### Install Python Libraries

```shell
pip install jupyter
pip install numpy
pip install pandas
pip install matplotlib
```

#### Jupyter Notebook

* `pip install jupyter`
* Update `~/.zshrc`
  * `code ~/.zshrc`
  * Add `export JUPYTER_PLATFORM_DIRS=1` at the bottom and save the file.

##### Support PDF Convert with Jupyter Notebook

```shell
brew install pandoc
brew install --cask mactex-no-gui  # This is to install xelatex
xelatex --version
```

> Restart PyCharm. Start the Jupyter Notebook web server. Export to PDF.

* If there is any issue with path for `xelatex`, update `~/.zshrc`:
  * `code ~/.zshrc`
  * Add `export PATH="/usr/local/texlive/2023/bin/universal-darwin:$PATH"` at the bottom and save the file.

### Maven

#### With Homebrew

```shell
# Install
brew install maven

# Test
mvn -help

# Uninstall
brew uninstall maven
```

> Having Maven caused error starting Spring Boot project. Therefore, do not install Maven.

### With IntelliJ

#### Install

* Install IntelliJ with Toolbox.
* Open a project in the IDE and navigate to a Java file.
* Download and add SDK. Use Corretto variation.
* The installation files are saved in the following directory:
  * `/Users/admin/Library/Java/JavaVirtualMachines/corretto-17.0.9`

#### Test

```shell
java -version
```

#### Uninstall

```shell
cd /Users/admin/Library/Java/JavaVirtualMachines/
sudo rm -rf corretto-17.0.9
```

* Tutorial: [Amazon Corretto 17 Installation Instructions for macOS 11 or later](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/macos-install.html)

### With Homebrew

> Not recommended because IntelliJ IDEA Integration has some issues.

#### Install

* Install: `brew install openjdk@17` # Install a specific version
* Link: `brew link openjdk@17`
* Optional:
  * Create alias: `code ~/.zshrc` and add `alias java=/opt/homebrew/Cellar/openjdk@17/17.0.9/bin/java`
  * Or, Add to PATH with:
  ```sh
  echo 'export PATH="/opt/homebrew/opt/openjdk@17/bin:$PATH"' >> ~/.zshrc
  ```
#### Test

```sh
java -version                                                                             ✔ 
openjdk version "17.0.9" 2023-10-17
OpenJDK Runtime Environment Homebrew (build 17.0.9+0)
OpenJDK 64-Bit Server VM Homebrew (build 17.0.9+0, mixed mode, sharing)
```

#### Uninstall

```sh
brew unlink openjdk@17
brew uninstall openjdk@17
```

* Configure IntelliJ IDEA
  * Path to JDK: `/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home`
  * Tutorial: [IntelliJ IDEA: How to add JDK installed by Brew on Mac](https://medium.com/@life-is-short-so-enjoy-it/intellij-idea-how-to-add-jdk-installed-by-brew-on-mac-d3e790d6a7aa)

## Remove Deleted Apps From Background Login Items

* Remove the app-related files from the following locations (wherever they exist):
   * `~/Library/LaunchAgents`
   * `/Library/LaunchAgents`
   * `/Library/LaunchDaemons`
* Reference: [Remove Deleted Apps From Background Login Items In Ventura](https://droidwin.com/remove-deleted-apps-from-background-login-items-in-ventura/)

### Node

```shell
# Uninstall if you have already have any installed version
brew list
brew uninstall --force node
rm -rf ~/.npm

# Install latest version
brew install node

# Install a specific or LTS version
# Install
brew install node@22

# Link the newly installed version: After installing, you might need to link node@22 to make it the default version.
brew link --overwrite --force node@22

# Test
node -v
npm -v

# If you do not get any resutl with `node -v`, you need to have node@22 first in your PATH, run:
echo 'export PATH="/opt/homebrew/opt/node@22/bin:$PATH"' >> ~/.zshrc

# Optional: For compilers to find node@22 you may need to set:
export LDFLAGS="-L/opt/homebrew/opt/node@22/lib"
export CPPFLAGS="-I/opt/homebrew/opt/node@22/include"
```

#### Delete `node_modules` and Reinstall Dependencies

```shell
rm -rf node_modules
rm -f package-lock.json
rm -f yarn.lock

npm cache clean --force

npm install
```

### TypeScript

```shell
npm install -g typescript
```
#### Generate Configuration File

```shell
tsc --init
```

#### Important Configuration for `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "es2016",
    "module": "commonjs",
    
    "rootDir": "./src",
    "sourceMap": true,
    "outDir": "./dist",
    
    "removeComments": true,
    "noEmitOnError": true,
    
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true
  }
}
```

#### Compile and Run

```shell
# Compile
tsc

# Run
node fileName.js
```

##### ts-node

* This package is used to run TypeScript files directly.

```shell
npm install -g ts-node
```

###### Create Alias

* `code ~/.zshrc`
* Add at the bottom of the file:

```shell
# Aliases
alias ts="ts-node"
```

###### Test

```shell
ts -v
```

###### Run

```shell
ts fileName.ts
```

### Create React Project with Vite

* Syntax: `npm init vite@latest <projectName> --template react`
* `npm init vite@latest core --template react`
  * `Select a framework: › React` 
  * `Select a variant: › TypeScript + SWC`
* Install dependencies: `npm install`.
* Run server: `npm run dev`.

#### Install Redux with Redux-Toolkit

* `npm install react-redux @reduxjs/toolkit`

> Redux core is included in `@reduxjs/toolkit`.

### Bootstrap in React

> Go to https://getbootstrap.com/ and grab the installation command with latest version.

```shell
npm i bootstrap@5.3.2
```

#### Configure Bootstrap in React Project

* Remove css code from the project file like `index.css` and `App.css`.
* Go to main.tsx and add the following lines above `import './index.css'`.
* Clean up `App.tsx`.

```typescript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import './index.css'
```

### Install and Login to GitHub

* `brew install gh`
* [Generate personal access token](https://github.com/settings/tokens)
* `gh auth login`

