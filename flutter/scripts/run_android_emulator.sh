# Launch the only available emulator in background without terminal output
emulator @$(emulator -list-avds | head -n 1) > /dev/null 2>&1 &
