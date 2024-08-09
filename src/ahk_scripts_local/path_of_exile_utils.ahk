#SingleInstance Force
SendMode("Event")
#include utils.ahk
Thread "Interrupt", 0

#HotIf WinActive("ahk_exe PathOfExileSteam.exe")
    class KeyGroup {
        __New(keys, peroid){
            
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


    RunKeyW() {
        if (WinActive("ahk_exe PathOfExileSteam.exe")){
            Send("w")
        }
    }

    RunKeyE() {
        if (WinActive("ahk_exe PathOfExileSteam.exe")){
            Send("e")
        }
    }

    RunKeyQ() {
        if (WinActive("ahk_exe PathOfExileSteam.exe")){
            Send("q")
        }
    }

    SendFlask(flaskNumber) {
        if (WinActive("ahk_exe PathOfExileSteam.exe")){
            Send(flaskNumber)
        }
    }

    RunKey1() {
        SendFlask(1)
    }

    RunKey2() {
        SendFlask(2)
    }

    RunKey3() {
        SendFlask(3)
    }

    RunKey4() {
        SendFlask(4)
    }

    RunKey5() {
        SendFlask(5)
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
        SendFlask(lastFlaskA)
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
        SendFlask(lastFlaskB)
        lastFlaskB := lastFlaskB + 1
    }

#HotIf
