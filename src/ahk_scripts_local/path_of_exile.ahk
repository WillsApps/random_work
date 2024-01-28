#SingleInstance Force
;#NoTrayIcon
;#InstallKeybdHook
SendMode("Event")
#include utils.ahk
Thread "Interrupt", 0


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
global flasks_triggering := 0
    *WheelDown::{
        if(GetKeyState("Shift") || GetKeyState("Ctrl")){
            MouseClick()
        } else {
            Send("{WheelDown}")
        }
    }

    *WheelUp::{
        if(GetKeyState("Shift") || GetKeyState("Ctrl")){
            MouseClick()
        } else {
            Send("{WheelUp}")
        }
    }

    MButton::{
        Send("{Shift down}``{Shift up}")
    }

    *`::{
        Send("{Shift down}``{Shift up}")
    }

    *F11::{
        Send(1)
    }

    *F12::{
        Send(2)
    }

    *F13::{
        Send(3)
    }

    *F14::{
        Send(4)
    }

    *F15::{
        Send(5)
    }

    NumpadAdd::{

    }

    *F16::{
        Send("{Shift down}q{Shift up}")
    }

    NumpadSub::{

    }

    ;F8::{
    ;    global flasks_triggering := 0
    ;    X226, Y543
    ;}
;
    ; 6-link orbing
;Item Class: Body Armours
;Rarity: Unique
;Thousand Ribbons
;Simple Robe
;--------
;Evasion Rating: 32 (augmented)
;Energy Shield: 65 (augmented)
;--------
;Requirements:
;Intelligence: 17
;--------
;Sockets: G-B-B-G B B
;--------
;Item Level: 85
;--------
;Socketed Gems are Supported by Level 5 Elemental Proliferation
;Adds 4 to 8 Fire Damage to Spells and Attacks
;Adds 4 to 7 Cold Damage to Spells and Attacks
;Adds 1 to 8 Lightning Damage to Spells and Attacks
;+32 to Evasion Rating
;+49 to maximum Energy Shieldlue
;+28 to maximum Life
;+41 to maximum Mana
;+18% to Fire Resistance
;+18% to Cold Resistance
;+15% to Lightning Resistance
;--------
;The night of a thousand ribbons
;To remember the day of a thousand flames
;When Sarn burned
;And was born again

;    ^!+LButton::{
;        MouseGetPos &x_pos, &y_pos
;        GamesClick(x_pos, y_pos)
;        Sleep(35)
;        Send("{Ctrl down}c{Ctrl up}")
;        modifier_text := A_Clipboard
;        pattern := "[RBG]-[RBG]-[RBG]-[RBG]-[RBG]-[RBG]"
;        position := RegExMatch(modifier_text, pattern)
;        if (position != 0){
;            MsgBox("position: '" position "'")
;        }
;    }


    F9::{
        global flasks_triggering
        global last_flask := 2
        if (!IsSet(flasks_triggering)){
            flasks_triggering := 1
        }
        else if (flasks_triggering == 0){
            flasks_triggering := 1
        }
        else {
            flasks_triggering := 0
        }

        if (flasks_triggering == 1){
;            MostMeta()
;            PocketGopher()
;            RenHangingOut()
;            ColeHangingOut()
;            SpeedQueen()
;            SnakeBite()
        } else {
            SetTimer(RunFlask1, 0)
            SetTimer(RunFlask2, 0)
            SetTimer(RunFlask3, 0)
            SetTimer(RunFlask4, 0)
            SetTimer(RunFlask5, 0)
            SetTimer(RunFlasks, 0)
            SetTimer(SendW, 0)
        }

        RenHangingOut() {
            global character_name := "Aggy_AF_RenHangingOut"
            RunFlask1()
            RunFlask3()
            RunFlask4()
            RunFlask5()
            SetTimer(RunFlask1, 2300)
            SetTimer(RunFlask3, 9700)
        }

        PocketGopher() {
            RunFlasks()
            RunFlask4()
            SetTimer(RunFlasks, 6000)
            SetTimer(RunFlask4, 5000)
        }

        ColeHangingOut() {
            RunFlasks()
            RunFlask4()
            SetTimer(RunFlasks, 6000)
            SetTimer(RunFlask4, 5)
        }

        MostMeta() {
            RunFlask5()
            SetTimer(RunFlask5, 5300)
        }

        SpeedQueen() {
;            RunFlasks()
;            RunFlask1()
;            RunFlask2()
;            RunFlask3()
            RunFlask5()
;            SetTimer(RunFlask1, 10100)
;            SetTimer(RunFlask2, 7300)
;            SetTimer(RunFlask3, 10100)
            SetTimer(RunFlask5, 5300)
        }

        SnakeBite() {
            SendW()
            RunFlask1()
            RunFlask2()
            RunFlask3()
            RunFlask4()
            SetTimer(SendW, 12000)
            SetTimer(RunFlask4, 4000)
;            SetTimer(RunFlask3, 15000)
;            SetTimer(RunFlask4, 11400)
;            SetTimer(RunFlask5, 8000)
        }

        SendW() {
            if (WinActive("ahk_exe PathOfExileSteam.exe")){
                Send("w")
            }
        }

        SendFlask(flask_number) {
            if (WinActive("ahk_exe PathOfExileSteam.exe")){
                Send(flask_number)
            }
        }

        RunFlask1() {
            SendFlask(1)
        }

        RunFlask2() {
            SendFlask(2)
        }

        RunFlask3() {
            SendFlask(3)
        }

        RunFlask4() {
            SendFlask(4)
        }

        RunFlask5() {
            SendFlask(5)
        }

        RunFlasks() {
            global last_flask
            if (last_flask == 2){
                SendFlask(3)
                last_flask := 3
            } else {
                SendFlask(2)
                last_flask := 2
            }
        }
    }

;    *F10::{
;        ; craft flasks
;        MouseGetPos &x_pos, &y_pos
;        GamesClick(x_pos, y_pos)
;        Send("{Ctrl down}c{Ctrl up}")
;    }

    F10::{
        drag_start_x := 970
        drag_start_y := 1062
        drag_end_x := 836
        drag_end_y := 1066
        confirm_x := 814
        confirm_y := 987
        grab_x := 814
        grab_y := 665

        MouseGetPos &x_pos, &y_pos
        GamesClickModifier(x_pos, y_pos, "Ctrl")
        GamesClick(confirm_x, confirm_y)
        GamesClickModifier(grab_x, grab_y, "Ctrl")
        MouseMove(x_pos, y_pos, 2)
    }


    ;F8::{
    ;    global calls_this_item := 0
    ;    global mouse_start_x := 0
    ;    global mouse_start_y := 0
    ;}
;
;
    ;F9::{
    ;    textbox_x := 837
    ;    textbox_y := 1021
    ;    confirm_x := 830
    ;    confirm_y := 1148
;
    ;    global calls_this_item
    ;    static previous_price
    ;    global mouse_start_x
    ;    global mouse_start_y
;
    ;    if (calls_this_item == 0){
    ;        calls_this_item += 1
;
    ;        ; Get item position, click it
    ;        MouseGetPos &x_pos, &y_pos
    ;        mouse_start_x := x_pos
    ;        mouse_start_y := y_pos
    ;        GamesClick(x_pos, y_pos)
;
    ;        ; Click the textbox, grab value
    ;        GamesClick(textbox_x, textbox_y)
    ;        Send("{Ctrl down}a{Ctrl up}")
    ;        Send("{Ctrl down}c{Ctrl up}")
    ;        max_value := A_Clipboard
;
    ;        ; Half the value, send it
    ;        half_value := Ceil(max_value / 2)
    ;        previous_price := half_value
    ;        Send(half_value)
    ;        GamesClick(confirm_x, confirm_y)
    ;    }
    ;    else{
    ;        calls_this_item += 1
;
    ;        ; Click the textbox, grab value
    ;        GamesClick(textbox_x, textbox_y)
    ;        Send("{Ctrl down}a{Ctrl up}")
    ;        Send("{Ctrl down}c{Ctrl up}")
    ;        max_value := A_Clipboard
;
    ;        ; Find difference, add quarter of difference to previous, send it
    ;        difference := max_value - previous_price
    ;        quarter_value := Ceil(difference / 4)
    ;        send_value := previous_price + quarter_value + 1
    ;        previous_price := send_value
    ;        Send(send_value)
    ;        GamesClick(confirm_x, confirm_y)
    ;    }
    ;}

    ;F10::{
    ;    global calls_this_item
    ;    global mouse_start_x
    ;    global mouse_start_y
;
    ;    calls_this_item := 0
    ;    MouseMove(mouse_start_x, mouse_start_y, 2)
    ;}

    ;F9::{
    ;    MouseGetPos &x_pos, &y_pos
    ;    GamesClick(x_pos, y_pos)
    ;    wrap_paste("/destroy")
    ;}

    F17::{
        drag_start_x := 970
        drag_start_y := 1062
        drag_end_x := 836
        drag_end_y := 1066
        click_x := 830
        click_y := 1148

        MouseGetPos &x_pos, &y_pos
        GamesClick(x_pos, y_pos)
        MouseMove(drag_start_x, drag_start_y, 2)
        MouseClickDrag("left", drag_start_x, drag_start_y, drag_end_x, drag_end_y, 2)
        GamesClick(click_x, click_y)
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
        GamesClick(x_pos, y_pos)
        MouseMove(drag_start_x, drag_start_y, 2)
        MouseClickDrag("left", drag_start_x, drag_start_y, drag_end_x, drag_end_y, 2)
        GamesClick(click_x, click_y)
        MouseMove(x_pos, y_pos, 2)
    }

    F19::{
        reset_x := 1258
        reset_y := 1162
        MouseGetPos &x_pos, &y_pos
        GamesClick(reset_x, reset_y)
        MouseMove(x_pos, y_pos, 2)
    }

    wrap_paste(warped_paste_me){
        Send("{Enter}")
        Sleep(35)
        Send("^a")
        FastPaste(warped_paste_me)
        Send("{Enter}")
    }

    F2::{
        essence_x := 1867
        essence_y := 837

        MouseGetPos &x_pos, &y_pos

        Send("i")
        Sleep(15)
        GamesClickRight(essence_x, essence_y)
        MouseMove(x_pos, y_pos)
        Sleep(15)
        Send("i")
    }

    F3::{
        wrap_paste("/menagerie")
    }

    F4::{
        wrap_paste("Thank you!")
    }

    F5::{
        wrap_paste("/hideout")
    }

    F6::{
        wrap_paste("/invite @last")
    }

    F7::{
        wrap_paste("/leave")
    }

    ; F8::{
    ;     wrap_paste("/tradewith @last")
    ; }

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
