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
#HotIf WinActive("ahk_exe bg3_dx11.exe")
    F11::{
        clickX := 1313
        clickY := 561
        MouseGetPos &xPos, &yPos
        GamesClick(clickX, clickY)
        MouseMove(xPos, yPos, 2)
    }

    F12::{
        clickX := 1280
        clickY := 1090
        MouseGetPos &xPos, &yPos
        GamesClick(clickX, clickY)
        MouseMove(xPos, yPos, 2)
    }

    F20::{
        MouseGetPos &xPos, &yPos
        MsgBox "xPos: '" xPos "' yPos: '" yPos "'"
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
        GamesClickBack(888, 1164, "1")
    }


    2::{
        GamesClickBack(947, 1164, "2")
    }


    3::{
        GamesClickBack(1006, 1164, "3")
    }


    4::{
        GamesClickBack(1065, 1164, "4")
    }


    5::{
        GamesClickBack(1124, 1164, "5")
    }


    6::{
        GamesClickBack(1183, 1164, "6")
    }


    7::{
        GamesClickBack(1242, 1164, "7")
    }


    8::{
        GamesClickBack(1301, 1164, "8")
    }


    9::{
        GamesClickBack(1360, 1164, "9")
    }


    0::{
        GamesClickBack(1419, 1164, "0")
    }


    -::{
        GamesClickBack(1478, 1164, "-")
    }


    =::{
        GamesClickBack(1537, 1164, "=")
    }


    +1::{
        GamesClickBack(888, 1223, "{Shift}1")
    }


    +2::{
        GamesClickBack(947, 1223, "{Shift}2")
    }


    +3::{
        GamesClickBack(1006, 1223, "{Shift}3")
    }


    +4::{
        GamesClickBack(1065, 1223, "{Shift}4")
    }


    +5::{
        GamesClickBack(1124, 1223, "{Shift}5")
    }


    +6::{
        GamesClickBack(1183, 1223, "{Shift}6")
    }


    +7::{
        GamesClickBack(1242, 1223, "{Shift}7")
    }


    +8::{
        GamesClickBack(1301, 1223, "{Shift}8")
    }


    +9::{
        GamesClickBack(1360, 1223, "{Shift}9")
    }


    +0::{
        GamesClickBack(1419, 1223, "{Shift}0")
    }


    +-::{
        GamesClickBack(1478, 1223, "{Shift}-")
    }


    +=::{
        GamesClickBack(1537, 1223, "{Shift}=")
    }


    ^1::{
        GamesClickBack(888, 1282, "{Ctrl}1")
    }


    ^2::{
        GamesClickBack(947, 1282, "{Ctrl}2")
    }


    ^3::{
        GamesClickBack(1006, 1282, "{Ctrl}3")
    }


    ^4::{
        GamesClickBack(1065, 1282, "{Ctrl}4")
    }


    ^5::{
        GamesClickBack(1124, 1282, "{Ctrl}5")
    }


    ^6::{
        GamesClickBack(1183, 1282, "{Ctrl}6")
    }


    ^7::{
        GamesClickBack(1242, 1282, "{Ctrl}7")
    }


    ^8::{
        GamesClickBack(1301, 1282, "{Ctrl}8")
    }


    ^9::{
        GamesClickBack(1360, 1282, "{Ctrl}9")
    }


    ^0::{
        GamesClickBack(1419, 1282, "{Ctrl}0")
    }


    ^-::{
        GamesClickBack(1478, 1282, "{Ctrl}-")
    }


    ^=::{
        GamesClickBack(1537, 1282, "{Ctrl}=")
    }


    !1::{
        GamesClickBack(888, 1341, "{Alt}1")
    }


    !2::{
        GamesClickBack(947, 1341, "{Alt}2")
    }


    !3::{
        GamesClickBack(1006, 1341, "{Alt}3")
    }


    !4::{
        GamesClickBack(1065, 1341, "{Alt}4")
    }


    !5::{
        GamesClickBack(1124, 1341, "{Alt}5")
    }


    !6::{
        GamesClickBack(1183, 1341, "{Alt}6")
    }


    !7::{
        GamesClickBack(1242, 1341, "{Alt}7")
    }


    !8::{
        GamesClickBack(1301, 1341, "{Alt}8")
    }


    !9::{
        GamesClickBack(1360, 1341, "{Alt}9")
    }


    !0::{
        GamesClickBack(1419, 1341, "{Alt}0")
    }


    !-::{
        GamesClickBack(1478, 1341, "{Alt}-")
    }


    !=::{
        GamesClickBack(1537, 1341, "{Alt}=")
    }
#HotIf
