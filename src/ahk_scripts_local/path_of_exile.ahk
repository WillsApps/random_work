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
        Send("``")
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

    NumpadAdd::{

    }

    NumpadSub::{

    }

    *F15::{
        Send(5)
    }

    *F16::{
        Send("{Shift down}q{Shift up}")
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
;Sockets: G-B B G B-B
;--------
;Item Level: 85
;--------
;{ Unique Modifier — Defences, Energy Shield }
;+49(30-60) to maximum Energy Shield
;{ Unique Modifier — Defences, Evasion }
;+32(30-60) to Evasion Rating
;{ Unique Modifier — Gem }
;Socketed Gems are Supported by Level 5 Elemental Proliferation — Unscalable Value
;{ Unique Modifier — Life }
;+28(25-50) to maximum Life
;{ Unique Modifier — Mana }
;+41(25-50) to maximum Mana
;{ Unique Modifier — Damage, Elemental, Fire, Attack, Caster }
;Adds 4(2-4) to 8(5-9) Fire Damage to Spells and Attacks
;{ Unique Modifier — Damage, Elemental, Lightning, Attack, Caster }
;Adds 1 to 8(4-12) Lightning Damage to Spells and Attacks
;{ Unique Modifier — Damage, Elemental, Cold, Attack, Caster }
;Adds 4(2-4) to 7(5-9) Cold Damage to Spells and Attacks
;{ Unique Modifier — Elemental, Fire, Resistance }
;+18(15-30)% to Fire Resistance
;{ Unique Modifier — Elemental, Cold, Resistance }
;+18(15-30)% to Cold Resistance
;{ Unique Modifier — Elemental, Lightning, Resistance }
;+15(15-30)% to Lightning Resistance
;--------
;The night of a thousand ribbons
;To remember the day of a thousand flames
;When Sarn burned
;And was born again


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
;            run_flasks()
;            SetTimer(run_flasks, 6000)
;            SetTimer(run_flask_1, 2300)
;            run_flask_1()
            run_flask_2()
;            run_flask_3()
;            SetTimer(run_flask_1, 4900)
            SetTimer(run_flask_2, 8500)
;            SetTimer(run_flask_3, 8500)
        } else {
;            SetTimer(run_flasks, 0)
;            SetTimer(run_flask_1, 0)
;            SetTimer(run_flask_1, 0)
            SetTimer(run_flask_2, 0)
;            SetTimer(run_flask_3, 0)
        }

        send_flask(flask_number) {
            if (WinActive("ahk_exe PathOfExileSteam.exe")){
                Send(flask_number)
            }
        }

        run_flask_1() {
            send_flask(1)
        }

        run_flask_2() {
            send_flask(2)
        }

        run_flask_3() {
            send_flask(3)
        }

        run_flask_4() {
            send_flask(4)
        }

        run_flask_5() {
            send_flask(5)
        }

        run_flasks() {
            global last_flask
            if (last_flask == 2){
                send_flask(3)
                last_flask := 3
            } else {
                send_flask(2)
                last_flask := 2
            }
        }
    }

;    *F10::{
;        ; craft flasks
;        MouseGetPos &x_pos, &y_pos
;        games_click(x_pos, y_pos)
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
        games_click_modifier(x_pos, y_pos, "Ctrl")
        games_click(confirm_x, confirm_y)
        games_click_modifier(grab_x, grab_y, "Ctrl")
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
    ;        games_click(x_pos, y_pos)
;
    ;        ; Click the textbox, grab value
    ;        games_click(textbox_x, textbox_y)
    ;        Send("{Ctrl down}a{Ctrl up}")
    ;        Send("{Ctrl down}c{Ctrl up}")
    ;        max_value := A_Clipboard
;
    ;        ; Half the value, send it
    ;        half_value := Ceil(max_value / 2)
    ;        previous_price := half_value
    ;        Send(half_value)
    ;        games_click(confirm_x, confirm_y)
    ;    }
    ;    else{
    ;        calls_this_item += 1
;
    ;        ; Click the textbox, grab value
    ;        games_click(textbox_x, textbox_y)
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
    ;        games_click(confirm_x, confirm_y)
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
    ;    games_click(x_pos, y_pos)
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
        wrap_paste("Thank you!")
    }

    F5::{
        wrap_paste("/hideout")
    }

    F6::{
        wrap_paste("/invite @last")
    }

    F7::{
        wrap_paste("/kick Aggy_AF_FlyFlyAway")
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
