#SingleInstance Force
#NoTrayIcon
^SPACE::{
    title := WinGetTitle("A")
    WinSetAlwaysOnTop(-1, title)
}
return
