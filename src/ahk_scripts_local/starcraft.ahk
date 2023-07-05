#SingleInstance Force
#NoTrayIcon
;#InstallKeybdHook
SendMode("Event")
#HotIf WinActive("ahk_exe SC2_x64.exe")
    ^F11::{
        Send("{Ctrl down}6{Ctrl up}")
    }
    ^F12::{
        Send("{Ctrl down}7{Ctrl up}")
    }
    ^F13::{
        Send("{Ctrl down}8{Ctrl up}")
    }
    ^F14::{
        Send("{Ctrl down}9{Ctrl up}")
    }
    ^F15::{
        Send("{Ctrl down}0{Ctrl up}")
    }
    F11::{
        Send("6")
    }
    F12::{
        Send("7")
    }
    F13::{
        Send("8")
    }
    F14::{
        Send("9")
    }
    F15::{
        Send("0")
    }

