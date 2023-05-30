#NoTrayIcon
#SingleInstance Force
SetNumLockState("AlwaysOn")
SetTitleMatchMode(2)

F22::{
    ;active_id := WinGetProcessName("A")
    ;MsgBox "active_id: '" active_id "'"
    process_path := WinGetProcessPath("A")
    MsgBox "process_path: '" process_path "'"
    A_Clipboard := process_path
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

games_click(click_x, y_pos){
    number_clicks := 1
    speed := 2
    MouseClick("Left", click_x, y_pos, number_clicks, speed)
}
