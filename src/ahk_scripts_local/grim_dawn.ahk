#SingleInstance Force
#NoTrayIcon
InstallKeybdHook
SendMode("Event")
#include utils.ahk
Thread "Interrupt", 0
SetTitleMatchMode("RegEx")

#HotIf WinActive("Grim Dawn.exe")

    global grimDawnGlobals := Map()
    grimDawnGlobals["keysTriggering"] := 0
    grimDawnGlobals["activeRunKeyFuncs"] := Map()
    grimDawnGlobals["cooldowns"] := Map()
    grimDawnGlobals["cooldowns"][1] := 1000
    grimDawnGlobals["cooldowns"][2] := 10000
    grimDawnGlobals["cooldowns"][3] := 59000


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

    1::{
        ScheduleKeyGrimDawn(1)
    }

    2::{
        ScheduleKeyGrimDawn(2)
    }

    3::{
        ScheduleKeyGrimDawn(3)
    }

    4::{
        ScheduleKeyGrimDawn(4)
    }

    5::{
        ScheduleKeyGrimDawn(5)
    }

    6::{
        ScheduleKeyGrimDawn(5)
    }

    7::{
        ScheduleKeyGrimDawn(5)
    }

    8::{
        ScheduleKeyGrimDawn(5)
    }

    9::{
        ScheduleKeyGrimDawn(5)
    }

    0::{
        ScheduleKeyGrimDawn(5)
    }

    F11::{
        ScheduleKeyGrimDawn(1)
    }

    F12::{
        ScheduleKeyGrimDawn(2)
    }

    F13::{
        ScheduleKeyGrimDawn(3)
    }

    F14::{
        ScheduleKeyGrimDawn(4)
    }

    F15::{
        ScheduleKeyGrimDawn(5)
    }

    F16::{
        ScheduleKeyGrimDawn(6)
    }

    F17::{
        ScheduleKeyGrimDawn(7)
    }

    F18::{
        ScheduleKeyGrimDawn(8)
    }

    ScrollLock::{
        Send("{Space}")
    }
;#HotIf
