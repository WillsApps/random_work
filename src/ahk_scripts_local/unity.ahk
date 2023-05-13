#NoTrayIcon
#SingleInstance Force

SetTitleMatchMode 2

if WinActive("ahk_exe TowerDefense.exe"){
    getProperties() {
        Send("{Alt down}p{Alt up}")
    }


    #NumpadEnd::{
        getProperties()
    }

    #NumpadClear::{
        Send("{F6}")
        Send("{F7}")
    }
}
