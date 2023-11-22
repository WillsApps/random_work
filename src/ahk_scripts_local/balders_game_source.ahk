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
        games_click_back(888, 1162, 1)
    }

    2::{
        games_click_back(947, 1164, 2)
    }

    3::{
        games_click_back(1005, 1164, 3)
    }
