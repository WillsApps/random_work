#NoTrayIcon
#SingleInstance Force
SetNumLockState("AlwaysOn")
SetTitleMatchMode(2)

F22::{
    active_id := WinGetProcessName()
    MsgBox "The active window's ID is " active_id
;    state:=GetKeyState("F21")
;    MsgBox, %state%
}

fast_paste(paste_me){
    saved := ClipboardAll()
    A_Clipboard := paste_me
    Send("^v")
    A_Clipboard := saved
    saved := ""
}
