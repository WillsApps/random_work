#NoTrayIcon
#SingleInstance Force
InstallKeybdHook
SetNumLockState("AlwaysOn")
SetTitleMatchMode(2)


F20::{
    MouseGetPos &xPos, &yPos
    MsgBox("Mouse position is X" xPos " Y" yPos ".")
}

F21::{
   KeyHistory
}

F22::{
    ;active_id := WinGetProcessName("A")
    ;MsgBox "active_id: '" active_id "'"
    processPath := WinGetProcessPath("A")
    processName := WinGetProcessName("A")
    class := WinGetClass("A")
    MsgBox "processPath: '" processPath "'`nprocessName: '" processName "'`nclass: '" class "'"
    A_Clipboard := processPath
}

FastPaste(pasteMe){
    saved := ClipboardAll()
    A_Clipboard := pasteMe
    Sleep(35)
    Send("^v")
    Sleep(35)
    A_Clipboard := saved
    saved := ""
}

GamesClick(clickX, clickY){
    numberClicks := 1
    speed := 2
    MouseClick("Left", clickX, clickY, numberClicks, speed)
}

GamesClickSpeed(clickX, clickY, speed){
    numberClicks := 1
    MouseClick("Left", clickX, clickY, numberClicks, speed)
}

GamesClickRight(clickX, clickY){
    numberClicks := 1
    speed := 2
    MouseClick("Right", clickX, clickY, numberClicks, speed)
}

GamesClickModifier(clickX, clickY, modifier){
    numberClicks := 1
    speed := 2
    Send("{" modifier " down}")
    GamesClick(clickX, clickY)
    Send("{" modifier " up}")
}

GamesClickBack(clickX, clickY, key){
    state := GetKeyState("ScrollLock", "T")
    if (state) {
        MouseGetPos &xPos, &yPos
        GamesClick(clickX, clickY)
        MouseMove(xPos, yPos, 2)
    } else {
        Send(key)
    }
}

WarpPaste(warpedPasteMe){
    Send("{Enter}")
    Sleep(35)
    Send("^a")
    FastPaste(warpedPasteMe)
    Send("{Enter}")
}
