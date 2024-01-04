# Mac
Mac configurations

## Update Software

* `brew update -d`. Here `-d` is to see what is happening behind.

## Install Software

### Install Python with brew:

* Install: `brew install python`
* Link: `brew link python3`
* Test: `which python3` and `where python3`
* Create alias: `alias python=/opt/homebrew/bin/python3`
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

### Java

> Make sure to install Maven first.

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
# Install
brew install node

# Uninstall
brew uninstall node
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
