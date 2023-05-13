#SingleInstance Force
;#NoTrayIcon
;#InstallKeybdHook

#include utils.ahk


if WinActive("ahk_exe PathOfExileSteam.exe"){
    drag_start_x := 970
    drag_start_y := 1062
    drag_end_x := 891
    drag_end_y := 1066
    click_x := 830
    click_y := 1148
    reset_x := 1258
    reset_y := 1162

    F11::{
        Send(1)
    }

    F12::{
        Send(2)
    }

    F13::{
        Send(3)
    }

    F14::{
        Send(4)
    }

    F15::{
        Send(5)
    }

    F17::{
        MouseGetPos &x_pos, &y_pos
        Click click_x, click_y
        MouseMove x_pos, y_pos
    }

    F20::{
        MouseGetPos &x_pos, &y_pos
        MsgBox("Mouse position is X" x_pos "Y" y_pos ".")
    }

    F18::{
        MouseGetPos &x_pos, &y_pos
        Click(x_pos, y_pos)
        MouseMove(drag_start_x, drag_start_y)
        MouseClickDrag("left", drag_start_x, drag_start_y, drag_end_x, drag_end_y, 5)
        Click(click_x, click_y)
        MouseMove(x_pos, y_pos)
    }

    F19::{
        MouseGetPos &x_pos, &y_pos
        Click(reset_x, reset_y)
        MouseMove(x_pos, y_pos)
    }

    wrap_paste(paste_me){
        Send("{Enter}")
        Send("^a")
        fast_paste(paste_me)
        Send("{Enter}")
    }

    F4::{
        wrap_paste("F5-hideout | F6-Invite | F7-Leave")
    }

    F5::{
        wrap_paste("/hideout")
    }

    F6::{
        wrap_paste("/invite @last")
    }

    F7::{
        wrap_paste("/kick Agathos_CR_WandGoesBurr")
    }

    ScrollLock::{
        Send("{Space}")
    }

    F21::{
        Loop
        {
            Send("^{Click}")
            Sleep 125
            if !GetKeyState("F21"){
                break
            }
        }
    }
}
