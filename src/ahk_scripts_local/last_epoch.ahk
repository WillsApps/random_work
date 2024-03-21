#SingleInstance Force
;#NoTrayIcon
;#InstallKeybdHook
SendMode("Event")
#include utils.ahk
Thread "Interrupt", 0

#HotIf WinActive("ahk_exe LastEpoch.exe")

    *F11::{
        Send(1)
    }

    *F12::{
        Send(2)
    }

    *F13::{
        Send(3)
    }

    *F14::{
        Send(4)
    }

    *F15::{
        Send(5)
    }
#HotIf
