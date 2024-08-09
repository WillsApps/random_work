#SingleInstance Force
#NoTrayIcon
InstallKeybdHook
SendMode("Event")
#include utils.ahk
Thread "Interrupt", 0
SetTitleMatchMode("RegEx")

winName := "Grim Dawn.exe"
#HotIf WinActive("ahk_exe .*Dawn.exe")

    global grimDawnGlobals := Map()
    grimDawnGlobals["keysTriggering"] := 0
    grimDawnGlobals["activeRunKeyFuncs"] := Map()
    grimDawnGlobals["cooldowns"] := Map()
;    grimDawnGlobals["cooldowns"][1] := 1000
;    grimDawnGlobals["cooldowns"][2] := 10000
;    grimDawnGlobals["cooldowns"][3] := 59000


    RunKeyGrimDawn(key) {
        if (WinActive("Grim Dawn")){
            Send("{Blind}" key)
        }
    }

    ScheduleKeyGrimDawn(key){
        global grimDawnGlobals
        cooldowns := grimDawnGlobals["cooldowns"]
        activeRunKeyFuncs := grimDawnGlobals["activeRunKeyFuncs"]
        ; Run the flask
        RunKeyGrimDawn(key)

        ; If the flask has a schedule, reset timer
        if(cooldowns.Has(key)){
            if(activeRunKeyFuncs.Has(key)){
                runKeyTimer := activeRunKeyFuncs[key]
                SetTimer(runKeyTimer, 0)
            } else {
                runKeyTimer := RunKeyGrimDawn.bind(key)
                activeRunKeyFuncs[key] := runKeyTimer
            }
            SetTimer(runKeyTimer, cooldowns[key])
        }
    }

    *1::{
        RunKeyGrimDawn(1)
    }

    *2::{
        RunKeyGrimDawn(2)
    }

    *3::{
        RunKeyGrimDawn(3)
    }

    *4::{
        RunKeyGrimDawn(4)
    }

    *5::{
        RunKeyGrimDawn(5)
    }

    *6::{
        RunKeyGrimDawn(6)
    }

    *7::{
        RunKeyGrimDawn(7)
    }

    *8::{
        RunKeyGrimDawn(8)
    }

    *9::{
        RunKeyGrimDawn(9)
    }

    *0::{
        RunKeyGrimDawn(0)
    }

    *F11::{
        RunKeyGrimDawn(1)
    }

    *F12::{
        RunKeyGrimDawn(2)
    }

    *F13::{
        RunKeyGrimDawn(3)
    }

    *F14::{
        RunKeyGrimDawn(4)
    }

    *F15::{
        RunKeyGrimDawn(5)
    }

    *F16::{
        RunKeyGrimDawn(6)
    }

    *F17::{
        RunKeyGrimDawn(7)
    }

    *F18::{
        RunKeyGrimDawn(8)
    }

    ScrollLock::{
        Send("{Space}")
    }
;#HotIf
#HotIf
