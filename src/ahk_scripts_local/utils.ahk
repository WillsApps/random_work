#NoTrayIcon
#SingleInstance Force
InstallKeybdHook
SetNumLockState("AlwaysOn")
SetTitleMatchMode(2)


F20::{
    MouseGetPos &x_pos, &y_pos
    MsgBox("Mouse position is X" x_pos " Y" y_pos ".")
}

F21::{
   KeyHistory
}

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

games_click_modifier(click_x, click_y, modifier){
    number_clicks := 1
    speed := 2
    Send("{" modifier " down}")
    games_click(click_x, click_y)
    Send("{" modifier " up}")
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
