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

FastPaste(paste_me){
    saved := ClipboardAll()
    A_Clipboard := paste_me
    Sleep(35)
    Send("^v")
    Sleep(35)
    A_Clipboard := saved
    saved := ""
}

GamesClick(click_x, click_y){
    number_clicks := 1
    speed := 2
    MouseClick("Left", click_x, click_y, number_clicks, speed)
}

GamesClickRight(click_x, click_y){
    number_clicks := 1
    speed := 2
    MouseClick("Right", click_x, click_y, number_clicks, speed)
}

GamesClickModifier(click_x, click_y, modifier){
    number_clicks := 1
    speed := 2
    Send("{" modifier " down}")
    GamesClick(click_x, click_y)
    Send("{" modifier " up}")
}

GamesClickBack(click_x, click_y, key){
    state := GetKeyState("ScrollLock", "T")
    if (state) {
        MouseGetPos &x_pos, &y_pos
        GamesClick(click_x, click_y)
        MouseMove(x_pos, y_pos, 2)
    } else {
        Send(key)
    }
}
