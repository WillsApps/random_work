#SingleInstance Force
SendMode("Event")
#include utils.ahk
Thread "Interrupt", 0

#HotIf WinActive("ahk_exe PathOfExileSteam.exe")

    CapsLockOn() {
        return (GetKeyState("CapsLock", "T") == 1)
    }

    StartFlasks() {
        global flasksTriggering
        if (CapsLockOn() == false) {
            return
        }
        if (!IsSet(flasksTriggering)){
            flasksTriggering := 1
            CharacterFunctions()
        } else if (flasksTriggering == 0){
            flasksTriggering := 1
            CharacterFunctions()
        }
    }

    SendKey(flaskNumber) {
        if (WinActive("ahk_exe PathOfExileSteam.exe")){
            if (CapsLockOn()) {
                Send(flaskNumber)
            } else {
                Send("{blind}" flaskNumber)
            }
        }
    }

    BacktickMove() {
;        Send("{Shift down}``{Shift up}")
        Send("``")
        StartFlasks()
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

    class KeyGroup {
        __New(keys, peroid){

        }
    }

    RunKey(key) {
        if (WinActive("ahk_exe PathOfExileSteam.exe")){
            Send("{Blind}" key)
        }
    }

    ScheduleKey(key){
        global characters
        global activeRunKeyFuncs
        global currentCharacter
        ; Run the flask
        RunKey(key)

        if(characters.Has(currentCharacter)){
            keyCooldowns := characters[currentCharacter]

            ; If the flask has a schedule, reset timer
            if(keyCooldowns.Has(key)){
                if(activeRunKeyFuncs.Has(key)){
                    runKeyTimer := activeRunKeyFuncs[key]
                    SetTimer(runKeyTimer, 0)
                } else {
                    runKeyTimer := RunKey.bind(key)
                    activeRunKeyFuncs[key] := runKeyTimer
                }
                SetTimer(runKeyTimer, keyCooldowns[key])
            }
        }
    }

    RunKeyE() {
        SendKey("e")
    }

    RunKeyW() {
        SendKey("w")
    }

    RunKeyQ() {
        SendKey("q")
    }

    RunKey1() {
        SendKey(1)
    }

    RunKey2() {
        SendKey(2)
    }

    RunKey3() {
        SendKey(3)
    }

    RunKey4() {
        SendKey(4)
    }

    RunKey5() {
        SendKey(5)
    }

    RunKeysA() {
        global lastFlaskA
        global minFlaskA
        global maxFlaskA
        if (!IsSet(minFlaskA) || !IsSet(maxFlaskA)){
            minFlaskA := 0
            maxFlaskA := 0
        }
        if (lastFlaskA > maxFlaskA) {
            lastFlaskA := minFlaskA
        }
        SendKey(lastFlaskA)
        lastFlaskA := lastFlaskA + 1
    }

    RunKeysB() {
        global lastFlaskB
        global minFlaskB
        global maxFlaskB
        if (!IsSet(minFlaskB) || !IsSet(maxFlaskB)){
            minFlaskB := 0
            maxFlaskB := 0
        }
        if (lastFlaskB > maxFlaskB) {
            lastFlaskB := minFlaskB
        }
        SendKey(lastFlaskB)
        lastFlaskB := lastFlaskB + 1
    }


    ; Settlers
    SendScarabShips(){
        select_port_buttons := [
            {x: 542, y: 336},
            {x: 542, y: 671},
            {x: 542, y: 1008}
        ]
        prepare_shipment_buttons := [
            {x: 542, y: 116},
            {x: 542, y: 446},
            {x: 542, y: 778},
        ]
        ports := Map(
            "Riben_Fell",
            {x: 1534, y: 543},
            "Ngakanu",
            {x: 1580, y: 645},
            "Te_Onui",
            {x: 966, y: 1214},
            "Pondium",
            {x: 1991, y: 272},
            "Kalguur",
            {x: 1930, y: 1144}
        )
        products := Map(
            "crimson",
            {x: 1022, y: 501},
            "orichalcum",
            {x: 1022, y: 537},
            "petrified_amber",
            {x: 1022, y: 573},
            "bismuth",
            {x: 1022, y: 606},
            "verisium",
            {x: 1022, y: 640},
            "wheat",
            {x: 1022, y: 678},
            "corn",
            {x: 1022, y: 716},
            "pumpkin",
            {x: 1022, y: 750},
            "orgond",
            {x: 1022, y: 789},
            "blue_zanthiumum",
            {x: 1022, y: 823},
            "thaumaturic_dust",
            {x: 1022, y: 854}
        )
        accept_product_button := {x: 961, y:898}

        Loop 3 {
            cord := select_port_buttons[A_Index]
            GamesClickSpeed(cord.x, cord.y, 3)
            cord := ports["Riben_Fell"]
            GamesClickSpeed(cord.x, cord.y, 3)
            cord := prepare_shipment_buttons[A_Index]
            GamesClickSpeed(cord.x, cord.y, 3)
            cord := products["verisium"]
            GamesClickSpeed(cord.x, cord.y, 3)
            Send("5")
;            cord := products["thaumaturic_dust"]
;            GamesClickSpeed(cord.x, cord.y, 3)
;            Send("5")
            cord := accept_product_button
            GamesClickSpeed(cord.x, cord.y, 3)
            cord := select_port_buttons[A_Index]
            GamesClickSpeed(cord.x, cord.y, 3)
        }
    }
#HotIf
