#SingleInstance Force
#NoTrayIcon
SendMode("Event")
#HotIf WinActive("ahk_exe C:\Program Files (x86)\Steam\steamapps\common\Vampire Survivors\VampireSurvivors.exe")
    Q::{
        Send("WA")
    }
