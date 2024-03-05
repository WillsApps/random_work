#SingleInstance Force
#NoTrayIcon
SendMode("Event")
#HotIf WinActive("ahk_exe C:\Program Files (x86)\Steam\steamapps\common\Vampire Survivors\VampireSurvivors.exe")
    Q::{
        global runHorizontal
        runHorizontal := "True"
        Loop {
            Send("{A down}")
            Sleep 10000
            Send("{A up}")
            Send("{D down}")
            Sleep 10000
            Send("{D up}")
        } Until runHorizontal="False"
    }
    E::{
        global runSquare
        runSquare := "True"
        Loop {
            Send("{A down}")
            Sleep 1000
            Send("{A up}")
            Send("{S down}")
            Sleep 1000
            Send("{S up}")
            Send("{D down}")
            Sleep 1000
            Send("{D up}")
            Send("{W down}")
            Sleep 1000
            Send("{W up}")
        } Until runSquare="False"
    }
    Pause::{
        global runHorizontal := "False"
        global runSquare := "False"
    }
#HotIf
