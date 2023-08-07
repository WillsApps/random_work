#NoTrayIcon
#SingleInstance Force

SetTitleMatchMode 2
#SingleInstance Force
#NoTrayIcon
SendMode("Event")
#HotIf WinActive("ahk_exe C:\Program Files\Unity\Hub\Editor\2022.3.5f1\Editor\Unity.exe")
    getProperties() {
        Send("{Alt down}p{Alt up}")
    }

    F11::{
        Send("{Shift down}{F6}{Shift up}")
        Send("{Shift down}{F7}{Shift up}")
    }

    F12::{
        Send("{Alt down}p{Alt up}")
    }
