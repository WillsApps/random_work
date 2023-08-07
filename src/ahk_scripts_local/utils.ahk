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

games_click(click_x, click_y){
    number_clicks := 1
    speed := 2
    MouseClick("Left", click_x, click_y, number_clicks, speed)
}

games_click_back(click_x, click_y, key){
    state := GetKeyState("ScrollLock", "T")
    if (state) {
        MouseGetPos &x_pos, &y_pos
        games_click(click_x, click_y)
        MouseMove(x_pos, y_pos, 2)
    } else {
        Send(key)
    }
}
