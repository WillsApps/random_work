#NoTrayIcon
#SingleInstance Force

SetTitleMatchMode 2
#SingleInstance Force
#NoTrayIcon
SendMode("Event")
#HotIf WinActive("ahk_exe C:\Program Files\JetBrains\JetBrains Rider 2023.1\bin\rider64.exe")
    F11::{
        Send("{Shift down}{F6}{Shift up}")
    }
#HotIf
