#SingleInstance Force
;#NoTrayIcon
;#InstallKeybdHook
SendMode("Event")
#include utils.ahk
Thread "Interrupt", 0

#HotIf WinActive("ahk_exe terrorhedron.exe")
    Q::{
        Send("I")
    }

    W::{
        Send("O")
    }

    E::{
        Send("P")
    }

    A::{
        Send("J")
    }

    S::{
        Send("K")
    }

    D::{
        Send("L")
    }

    Z::{
        Send("B")
    }

    X::{
        Send("N")
    }

    C::{
        Send("M")
    }


    R::{
        Send("U")
    }


    F::{
        Send("X")
    }

