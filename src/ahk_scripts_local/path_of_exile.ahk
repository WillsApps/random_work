#SingleInstance Force
SendMode("Event")
#include utils.ahk
#include path_of_exile_utils.ahk
Thread "Interrupt", 0

#HotIf WinActive("ahk_exe PathOfExileSteam.exe")
global currentCharacter := "Boo"

global clickX := 830
global clickY := 1148
global flasksTriggering := 0
global RunKeyFuncs := Map()

global activeRunKeyFuncs := Map()

RunKeyFuncs[1] := RunKey1
RunKeyFuncs[2] := RunKey2
RunKeyFuncs[3] := RunKey3
RunKeyFuncs[4] := RunKey4
RunKeyFuncs[5] := RunKey5
RunKeyFuncs["W"] := RunKeyW

global characters := Map()

characters["MostMeta"] := Map()
characters["MostMeta"][5] := 6900

characters["PocketGopher"] := Map()

characters["RenHangingOut"] := Map()
characters["RenHangingOut"][1] := 2300
characters["RenHangingOut"][3] := 9700

characters["ColeHangingOut"] := Map()
characters["ColeHangingOut"][4] := 5000
characters["SpeedQueen"] := Map()
characters["SpeedQueen"][5] := Map()
characters["SnakeBite"] := Map()

    RunKey(key) {
        if (WinActive("ahk_exe PathOfExileSteam.exe")){
            Send("{Blind}" key)
        }
    }

    *f::{
        StopFlasks()
        RunKey("f")
    }

    *p::{
        StopFlasks()
        RunKey("p")
    }


    *F9::{
        global flasksTriggering
        global keyCooldowns
        if (!IsSet(flasksTriggering)){
            flasksTriggering := 1
        }
        else if (flasksTriggering == 0){
            flasksTriggering := 1
        }
        else {
            flasksTriggering := 0
        }

        if (flasksTriggering == 1){
;            WheresTheBodies()
            CantRemember()
;            BombaBamBo()
;            StinkyBoy()
;            ColeAndRen()
        } else {
            StopFlasks()
        }
    }

    StopFlasks() {
        global flasksTriggering
        flasksTriggering := 0
        SetTimer(RunKey1, 0)
        SetTimer(RunKey2, 0)
        SetTimer(RunKey3, 0)
        SetTimer(RunKey4, 0)
        SetTimer(RunKey5, 0)
        SetTimer(RunKeysA, 0)
        SetTimer(RunKeysB, 0)
        SetTimer(RunKeyW, 0)
        SetTimer(RunKeyE, 0)
        SetTimer(RunKeyQ, 0)
    }

    CantRemember() {
;        global lastFlaskA
;        global lastFlaskB
;        global minFlaskA := 2
;        global maxFlaskA := 3
;        global minFlaskB := 4
;        global maxFlaskB := 5
;        if (!IsSet(lastFlaskA)){
;            lastFlaskA := minFlaskA
;            lastFlaskB := minFlaskB
;        }
;        RunKeysA()
;        RunKeysB()
;        SetTimer(RunKeysA, 7100)
;        SetTimer(RunKeysB, 7100)
        RunKey1()
        SetTimer(RunKey1, 6500)
    }

    WheresTheBodies() {
;        RunKey3()
;        RunKey4()
;        RunKey5()
        RunKeysA()
;        RunKeyE()
;        RunKeyQ()
        SetTimer(RunKeysA, 7100)
;        SetTimer(RunKey4, 7100)
;        SetTimer(RunKey5, 7100)
;        SetTimer(RunKeyE, 8500)
;        SetTimer(RunKeyQ, 16000)
;        global lastFlaskA
;        global lastFlaskB
;        if (!IsSet(lastFlaskA)){
;            lastFlaskA := 2
;            lastFlaskB := 4
;        }
;        global minFlaskA := 2
;        global maxFlaskA := 3
;        global minFlaskB := 4
;        global maxFlaskB := 5
    }

    BombaBamBo() {
        global minFlaskA := 2
        global maxFlaskA := 4
        RunKeysA()
        SetTimer(RunKeysA, 6000)
    }

    StinkyBoy() {
        RunKeysA()
        SetTimer(RunKeysA, 7200)
    }

    ColeAndRen() {
        RunKeysA()
        SetTimer(RunKeysA, 7200)
    }


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

    *1::{
        ScheduleKey(1)
    }

    *2::{
        ScheduleKey(2)
    }

    *3::{
        ScheduleKey(3)
    }

    *4::{
        ScheduleKey(4)
    }

    *5::{
        ScheduleKey(5)
    }

;    *W::{
;        ScheduleKey("W")
;    }


    *F11::{
        ScheduleKey(1)
    }

    *F12::{
        ScheduleKey(2)
    }

    *F13::{
        ScheduleKey(3)
    }

    *F14::{
        ScheduleKey(4)
    }

    *F15::{
        ScheduleKey(5)
    }

    *NumpadAdd::{

    }

    *NumpadSub::{

    }

    *F16::{
        Send("{Shift down}q{Shift up}")
    }


;    *F10::{
;        ; craft flasks
;        MouseGetPos &posX, &posY
;        GamesClick(posX, posY)
;        Send("{Ctrl down}c{Ctrl up}")
;    }

    F10::{
        dragStartX := 970
        dragStartY := 1062
        dragEndX := 836
        dragEndY := 1066
        confirmX := 814
        confirmY := 987
        grabX := 814
        grabY := 665

        MouseGetPos &posX, &posY
        GamesClickModifier(posX, posY, "Ctrl")
        GamesClick(confirmX, confirmY)
        GamesClickModifier(grabX, grabY, "Ctrl")
        MouseMove(posX, posY, 2)
    }


    ;F8::{
    ;    global callsThisItem := 0
    ;    global mouseStartX := 0
    ;    global mouseStartY := 0
    ;}
;
;
    ;F9::{
    ;    textboxX := 837
    ;    textboxY := 1021
    ;    confirmX := 830
    ;    confirmY := 1148
;
    ;    global callsThisItem
    ;    static previousPrice
    ;    global mouseStartX
    ;    global mouseStartY
;
    ;    if (callsThisItem == 0){
    ;        callsThisItem += 1
;
    ;        ; Get item position, click it
    ;        MouseGetPos &posX, &posY
    ;        mouseStartX := posX
    ;        mouseStartY := posY
    ;        GamesClick(posX, posY)
;
    ;        ; Click the textbox, grab value
    ;        GamesClick(textboxX, textboxY)
    ;        Send("{Ctrl down}a{Ctrl up}")
    ;        Send("{Ctrl down}c{Ctrl up}")
    ;        maxValue := A_Clipboard
;
    ;        ; Half the value, send it
    ;        halfValue := Ceil(maxValue / 2)
    ;        previousPrice := halfValue
    ;        Send(halfValue)
    ;        GamesClick(confirmX, confirmY)
    ;    }
    ;    else{
    ;        callsThisItem += 1
;
    ;        ; Click the textbox, grab value
    ;        GamesClick(textboxX, textboxY)
    ;        Send("{Ctrl down}a{Ctrl up}")
    ;        Send("{Ctrl down}c{Ctrl up}")
    ;        maxValue := A_Clipboard
;
    ;        ; Find difference, add quarter of difference to previous, send it
    ;        difference := maxValue - previousPrice
    ;        quarterValue := Ceil(difference / 4)
    ;        sendValue := previousPrice + quarterValue + 1
    ;        previousPrice := sendValue
    ;        Send(sendValue)
    ;        GamesClick(confirmX, confirmY)
    ;    }
    ;}

    ;F10::{
    ;    global callsThisItem
    ;    global mouseStartX
    ;    global mouseStartY
;
    ;    callsThisItem := 0
    ;    MouseMove(mouseStartX, mouseStartY, 2)
    ;}

    ;F9::{
    ;    MouseGetPos &posX, &posY
    ;    GamesClick(posX, posY)
    ;    WarpPaste("/destroy")
    ;}

    F17::{
        doExpedition := 1

        if (doExpedition == 0){
            Send("{Shift down}w{Shift up}")
        }
        else {
            dragStartX := 970
            dragStartY := 1062
            dragEndX := 836
            dragEndY := 1066
            clickX := 830
            clickY := 1148

            MouseGetPos &posX, &posY
            GamesClick(posX, posY)
            MouseMove(dragStartX, dragStartY, 2)
            MouseClickDrag("left", dragStartX, dragStartY, dragEndX, dragEndY, 2)
            GamesClick(clickX, clickY)
            MouseMove(posX, posY, 2)
        }
    }

    F18::{
        dragStartX := 970
        dragStartY := 1062
        dragEndX := 891
        dragEndY := 1066
        clickX := 830
        clickY := 1148

        MouseGetPos &posX, &posY
        GamesClick(posX, posY)
        MouseMove(dragStartX, dragStartY, 2)
        MouseClickDrag("left", dragStartX, dragStartY, dragEndX, dragEndY, 2)
        GamesClick(clickX, clickY)
        MouseMove(posX, posY, 2)
    }

    F19::{
        resetX := 1258
        resetY := 1162
        MouseGetPos &posX, &posY
        GamesClick(resetX, resetY)
        MouseMove(posX, posY, 2)
    }

    F2::{
        essenceX := 1867
        essenceY := 837

        MouseGetPos &posX, &posY

        Send("i")
        Sleep(15)
        GamesClickRight(essenceX, essenceY)
        MouseMove(posX, posY)
        Sleep(15)
        Send("i")
    }

    F3::{
        StopFlasks()
        WarpPaste("/menagerie")
    }

    F4::{
        WarpPaste("Thank you!")
    }

    F5::{
        StopFlasks()
        WarpPaste("/hideout")
    }

    F6::{
        WarpPaste("/invite @last")
    }

    F7::{
        StopFlasks()
        WarpPaste("/leave")
    }

;     F8::{
;         WarpPaste("/exit")
;     }

    ScrollLock::{
        Send("{Space}")
    }


    RenHangingOut() {
        RunKey1()
        RunKey3()
        RunKey4()
        RunKey5()
        SetTimer(RunKey1, 2300)
        SetTimer(RunKey3, 9700)
    }

    PocketGopher() {
        RunKeysA()
        RunKey4()
        SetTimer(RunKeysA, 6000)
        SetTimer(RunKey4, 5000)
    }

    ColeHangingOut() {
        RunKeysA()
        RunKey4()
        SetTimer(RunKeysA, 6000)
        SetTimer(RunKey4, 5000)
    }

    MostMeta() {
        RunKey5()
        SetTimer(RunKey5, 4300)
    }

    SpeedQueen() {
;            RunKeysA()
;            RunKey1()
;            RunKey2()
;            RunKey3()
        RunKey5()
;            SetTimer(RunKey1, 10100)
;            SetTimer(RunKey2, 7300)
;            SetTimer(RunKey3, 10100)
        SetTimer(RunKey5, 5300)
    }

    SnakeBite() {
        RunKeyW()
        RunKey1()
        RunKey2()
        RunKey3()
        RunKey4()
        SetTimer(RunKeyW, 12000)
        SetTimer(RunKey4, 4000)
;            SetTimer(RunKey3, 15000)
;            SetTimer(RunKey4, 11400)
;            SetTimer(RunKey5, 8000)
    }
#HotIf
