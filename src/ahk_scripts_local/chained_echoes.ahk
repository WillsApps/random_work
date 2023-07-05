#SingleInstance Force
#NoTrayIcon
SendMode("Event")
#HotIf WinActive("ahk_exe C:\Program Files (x86)\Steam\steamapps\common\Chained Echoes\Chained Echoes.exe")
    Up::{
        Send("W")
    }
    Left::{
        Send("A")
    }
    Right::{
        Send("D")
    }
    Down::{
        Send("S")
    }

