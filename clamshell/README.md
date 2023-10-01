# Mac

## Clamshell Mode

* `macOS -> Ventura 13.0`
* `Displays -> Advanced -> Battery & Energy -> Prevent automatic sleeping on power adapter when the display is off -> On`
* `Lock Screen -> Require password after screen saver begins or display is turned off -> Immediately`
* `Lock Screen -> Start Screen Saver when inactive -> Never`

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
