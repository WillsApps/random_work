#SingleInstance Force
SendMode("Event")
#include utils.ahk
Thread "Interrupt", 0

#HotIf WinActive("ahk_exe Sketchup.exe")
    *Left::{
        if(GetKeyState("ScrollLock")){
            Send("{Shift down}")
            MouseClick()
            Send("{Shift up}")
        }
        else {
            MouseClick()
        }
    }

#HotIf

