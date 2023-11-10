# Mac
Mac configurations

## Update Software

* `brew update -d`. Here `-d` is to see what is happening behind.

## Install Software

* Install Python with brew:
  * Install: `brew install python`
  * Link: `brew link python3`
  * Test: `which python3` and `where python3`
  * Create alias: `alias python=/opt/homebrew/bin/python3`
  * References
    * https://opensource.com/article/19/5/python-3-default-mac
  * Notes:
    * Previous location of python3: `/usr/bin/python3`
    * Homebrew location of python3: `/opt/homebrew/bin/python3`

## Remove Deleted Apps From Background Login Items

* Remove the app-related files from the following locations (wherever they exist):
   * `~/Library/LaunchAgents`
   * `/Library/LaunchAgents`
   * `/Library/LaunchDaemons`
* Reference: [Remove Deleted Apps From Background Login Items In Ventura](https://droidwin.com/remove-deleted-apps-from-background-login-items-in-ventura/)
