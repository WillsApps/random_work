#NoTrayIcon
#SingleInstance Force
SetNumLockState("AlwaysOn")
SetTitleMatchMode(2)

F22::{
    active_id := WinGetProcessName()
    MsgBox "The active window's ID is " active_id
}

fast_paste(paste_me){
    saved := ClipboardAll()
    A_Clipboard := paste_me
    Sleep(35)
    Send("^v")
    Sleep(35)
    A_Clipboard := saved
    saved := ""
}
