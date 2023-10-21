#SingleInstance Force
;#NoTrayIcon
;#InstallKeybdHook
SendMode("Event")
#include utils.ahk


maps_to_skip := [
    "core",
    "arsenal",
    "maze",
    "siege",
    "frozen cabin",
    "overgrown ruin",
]
okay_maps := [
    "jungle valley",
    "plaza",
    "terrace",
]
maps_i_like := [
    "underground river",
    "wharf",
]


#HotIf WinActive("ahk_exe PathOfExileSteam.exe")
global click_x := 830
global click_y := 1148
    *WheelDown::{
        MouseClick()
    }
    *WheelUp::{
        MouseClick()
    }
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

    F16::{
        Send("Q")
    }


    F8::{
        global calls_this_item := 0
        global mouse_start_x := 0
        global mouse_start_y := 0
    }


    F9::{
        textbox_x := 837
        textbox_y := 1021
        confirm_x := 830
        confirm_y := 1148

        global calls_this_item
        static previous_price
        global mouse_start_x
        global mouse_start_y

        if (calls_this_item == 0){
            calls_this_item += 1

            ; Get item position, click it
            MouseGetPos &x_pos, &y_pos
            mouse_start_x := x_pos
            mouse_start_y := y_pos
            games_click(x_pos, y_pos)

            ; Click the textbox, grab value
            games_click(textbox_x, textbox_y)
            Send("{Ctrl down}a{Ctrl up}")
            Send("{Ctrl down}c{Ctrl up}")
            max_value := A_Clipboard

            ; Half the value, send it
            half_value := Ceil(max_value / 2)
            previous_price := half_value
            Send(half_value)
            games_click(confirm_x, confirm_y)
        }
        else{
            calls_this_item += 1

            ; Click the textbox, grab value
            games_click(textbox_x, textbox_y)
            Send("{Ctrl down}a{Ctrl up}")
            Send("{Ctrl down}c{Ctrl up}")
            max_value := A_Clipboard

            ; Find difference, add quarter of difference to previous, send it
            difference := max_value - previous_price
            quarter_value := Ceil(difference / 4)
            send_value := previous_price + quarter_value + 1
            previous_price := send_value
            Send(send_value)
            games_click(confirm_x, confirm_y)
        }
    }

    F10::{
        global calls_this_item
        global mouse_start_x
        global mouse_start_y

        calls_this_item := 0
        MouseMove(mouse_start_x, mouse_start_y, 2)
    }

    F17::{
        drag_start_x := 970
        drag_start_y := 1062
        drag_end_x := 836
        drag_end_y := 1066
        click_x := 830
        click_y := 1148

        MouseGetPos &x_pos, &y_pos
        games_click(x_pos, y_pos)
        MouseMove(drag_start_x, drag_start_y, 2)
        MouseClickDrag("left", drag_start_x, drag_start_y, drag_end_x, drag_end_y, 2)
        games_click(click_x, click_y)
        MouseMove(x_pos, y_pos, 2)
    }

    F18::{
        drag_start_x := 970
        drag_start_y := 1062
        drag_end_x := 891
        drag_end_y := 1066
        click_x := 830
        click_y := 1148

        MouseGetPos &x_pos, &y_pos
        games_click(x_pos, y_pos)
        MouseMove(drag_start_x, drag_start_y, 2)
        MouseClickDrag("left", drag_start_x, drag_start_y, drag_end_x, drag_end_y, 2)
        games_click(click_x, click_y)
        MouseMove(x_pos, y_pos, 2)
    }

    F19::{
        reset_x := 1258
        reset_y := 1162
        MouseGetPos &x_pos, &y_pos
        games_click(reset_x, reset_y)
        MouseMove(x_pos, y_pos, 2)
    }

    F20::{
        MouseGetPos &x_pos, &y_pos
        MsgBox("Mouse position is X" x_pos " Y" y_pos ".")
    }

    wrap_paste(warped_paste_me){
        Send("{Enter}")
        Sleep(35)
        Send("^a")
        fast_paste(warped_paste_me)
        Send("{Enter}")
    }

    F3::{
        wrap_paste("F4-Thanks | F5-hideout | F6-Invite | F7-Leave")
    }

    F4::{
        wrap_paste("Thanks")
    }

    F5::{
        wrap_paste("/hideout")
    }

    F6::{
        wrap_paste("/invite @last")
    }

    F7::{
        wrap_paste("/kick Aggy_AN_BoomingGoodTime")
    }

    ScrollLock::{
        Send("{Space}")
    }

    ;F21::{
    ;    Loop
    ;    {
    ;        Send("^{Click}")
    ;        Sleep 125
    ;        if !GetKeyState("F21"){
    ;            break
    ;        }
    ;    }
    ;}
;}
