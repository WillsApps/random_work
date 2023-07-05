#SingleInstance Force
#NoTrayIcon
SendMode("Event")
#HotIf WinActive("ahk_exe C:\Program Files (x86)\Steam\steamapps\common\Vampire Survivors\VampireSurvivors.exe")
    Q::{
        global run := "True"
        Loop {
            Send("{A down}")
            Sleep 10000
            Send("{A up}")
            Send("{S down}")
            Sleep 10000
            Send("{S up}")
        } Until run="False"
    }
    Pause::{
        global run := "False"
    }
