# wifi_map
dev wifi list | grep sanoken

sudo iwlist wlan0 scan | grep -e ESSID -e Quality | sed '1~2{h;d};G'
