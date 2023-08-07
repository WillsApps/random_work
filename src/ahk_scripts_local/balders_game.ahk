#SingleInstance Force
#NoTrayIcon
;#InstallKeybdHook
SendMode("Event")
#include utils.ahk
;MyGui := Gui()
;MyGui.Opt("+AlwaysOnTop")
;MyGui.Opt("+Disabled")
;;MyGui.Opt("-Border")
;MyGui.Opt("+MaxSize20")
;;MyGui.Opt("+MaxSizey200")
#HotIf WinActive("ahk_exe C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\bin\bg3_dx11.exe")
    F11::{
        click_x := 1313
        click_y := 561
        MouseGetPos &x_pos, &y_pos
        games_click(click_x, click_y)
        MouseMove(x_pos, y_pos, 2)
    }

    F12::{
        click_x := 1280
        click_y := 1090
        MouseGetPos &x_pos, &y_pos
        games_click(click_x, click_y)
        MouseMove(x_pos, y_pos, 2)
    }

    F20::{
        MouseGetPos &x_pos, &y_pos
        MsgBox "x_pos: '" x_pos "' y_pos: '" y_pos "'"
    }

   ;ScrollLock::{
   ;    Send("{ScrollLock}")
   ;    state := GetKeyState("ScrollLock", "T")
;
   ;    if (state) {
   ;        ;MyGui.AddText("x888 y1162", "1")
   ;        MyGui.Show()
   ;    } else {
   ;         MyGui.Hide()
   ;    }
;
   ;}

; START_GEN_HERE

    1::{
        games_click_back(888, 1164, "1")
    }


    2::{
        games_click_back(947, 1164, "2")
    }


    3::{
        games_click_back(1006, 1164, "3")
    }


    4::{
        games_click_back(1065, 1164, "4")
    }


    5::{
        games_click_back(1124, 1164, "5")
    }


    6::{
        games_click_back(1183, 1164, "6")
    }


    7::{
        games_click_back(1242, 1164, "7")
    }


    8::{
        games_click_back(1301, 1164, "8")
    }


    9::{
        games_click_back(1360, 1164, "9")
    }


    0::{
        games_click_back(1419, 1164, "0")
    }


    -::{
        games_click_back(1478, 1164, "-")
    }


    =::{
        games_click_back(1537, 1164, "=")
    }


    +1::{
        games_click_back(888, 1223, "{Shift}1")
    }


    +2::{
        games_click_back(947, 1223, "{Shift}2")
    }


    +3::{
        games_click_back(1006, 1223, "{Shift}3")
    }


    +4::{
        games_click_back(1065, 1223, "{Shift}4")
    }


    +5::{
        games_click_back(1124, 1223, "{Shift}5")
    }


    +6::{
        games_click_back(1183, 1223, "{Shift}6")
    }


    +7::{
        games_click_back(1242, 1223, "{Shift}7")
    }


    +8::{
        games_click_back(1301, 1223, "{Shift}8")
    }


    +9::{
        games_click_back(1360, 1223, "{Shift}9")
    }


    +0::{
        games_click_back(1419, 1223, "{Shift}0")
    }


    +-::{
        games_click_back(1478, 1223, "{Shift}-")
    }


    +=::{
        games_click_back(1537, 1223, "{Shift}=")
    }


    ^1::{
        games_click_back(888, 1282, "{Ctrl}1")
    }


    ^2::{
        games_click_back(947, 1282, "{Ctrl}2")
    }


    ^3::{
        games_click_back(1006, 1282, "{Ctrl}3")
    }


    ^4::{
        games_click_back(1065, 1282, "{Ctrl}4")
    }


    ^5::{
        games_click_back(1124, 1282, "{Ctrl}5")
    }


    ^6::{
        games_click_back(1183, 1282, "{Ctrl}6")
    }


    ^7::{
        games_click_back(1242, 1282, "{Ctrl}7")
    }


    ^8::{
        games_click_back(1301, 1282, "{Ctrl}8")
    }


    ^9::{
        games_click_back(1360, 1282, "{Ctrl}9")
    }


    ^0::{
        games_click_back(1419, 1282, "{Ctrl}0")
    }


    ^-::{
        games_click_back(1478, 1282, "{Ctrl}-")
    }


    ^=::{
        games_click_back(1537, 1282, "{Ctrl}=")
    }


    !1::{
        games_click_back(888, 1341, "{Alt}1")
    }


    !2::{
        games_click_back(947, 1341, "{Alt}2")
    }


    !3::{
        games_click_back(1006, 1341, "{Alt}3")
    }


    !4::{
        games_click_back(1065, 1341, "{Alt}4")
    }


    !5::{
        games_click_back(1124, 1341, "{Alt}5")
    }


    !6::{
        games_click_back(1183, 1341, "{Alt}6")
    }


    !7::{
        games_click_back(1242, 1341, "{Alt}7")
    }


    !8::{
        games_click_back(1301, 1341, "{Alt}8")
    }


    !9::{
        games_click_back(1360, 1341, "{Alt}9")
    }


    !0::{
        games_click_back(1419, 1341, "{Alt}0")
    }


    !-::{
        games_click_back(1478, 1341, "{Alt}-")
    }


    !=::{
        games_click_back(1537, 1341, "{Alt}=")
    }
