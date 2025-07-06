# Devices
Getting devices:
```shell
cat /proc/bus/input/devices | more
```

## Desktop devices:
- Logitech Gaming Mouse G600
  - Bus=0003 Vendor=046d Product=c24a Version=0111
  - Logitech_Gaming_Mouse_G600
- Corsair CORSAIR K70 RGB PRO Mechanical Gaming Keyboard
  - Bus=0003 Vendor=1b1c Product=1bb3 Version=0100
  - Corsair_CORSAIR_K70_RGB_PRO_Mechanical_Gaming_Keyboard
  
# udev rules
```shell
# sudo vim /etc/udev/rules.d/71-logitech-mouse-uaccess.rules
# Access to read from "Logitech Gaming Mouse G600"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="046d", ATTRS{idProduct}=="c24a", TAG+="uaccess"

# Access for python-evdev to create a new device
KERNEL=="uinput", SUBSYSTEM=="misc", OPTIONS+="static_node=uinput", TAG+="uaccess", MODE="0660"
```


```shell
# sudo vim /etc/udev/rules.d/71-corsair-keyboard-uaccess.rules
# Access to read from "Corsair CORSAIR K70 RGB PRO Mechanical Gaming Keyboard"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="1b1c", ATTRS{idProduct}=="1bb3", TAG+="uaccess"

# Access for python-evdev to create a new device
KERNEL=="uinput", SUBSYSTEM=="misc", OPTIONS+="static_node=uinput", TAG+="uaccess", MODE="0660"
```

# Restart udev
```shell
sudo udevadm control --reload-rules && sudo udevadm trigger
```