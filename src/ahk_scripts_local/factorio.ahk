#SingleInstance Force
#NoTrayIcon
;#InstallKeybdHook
#HotIf WinActive("ahk_exe Factorio.exe")
;    F11::
;        MouseGetPos, xpos, ypos
;        MsgBox, The cursor is at X%xpos% Y%ypos%.
;    return

   #F11::{
        MouseGetPos(&xpos, &ypos)
        Click(496, 36)
        MouseMove(xpos, ypos)
    }
#HotIf
