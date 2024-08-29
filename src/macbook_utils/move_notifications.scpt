#!/usr/bin/osascript
repeat while true
  tell application "System Events"
    repeat with theWindow in windows of application process "NotificationCenter"
      set displaySize to size of theWindow
      set notifSize to size of first UI element of first scroll area of first group of theWindow
      set position of theWindow to {1100-((first item of displaySize)-(first item of notifSize))/2,((second item of displaySize)-(second item of notifSize)-200)}
    end repeat
  end tell
  delay 1
end repeat
