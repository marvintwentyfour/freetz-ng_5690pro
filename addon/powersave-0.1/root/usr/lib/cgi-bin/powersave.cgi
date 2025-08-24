#!/bin/sh

. /usr/lib/libmodcgi.sh

[ -r /etc/options.cfg ] && . /etc/options.cfg

sec_begin "$(lang de:"Starttyp" en:"Start type")"
cgi_print_radiogroup_service_starttype "enabled" "$POWERSAVE_ENABLED" "" "" 0
sec_end

sec_begin "$(lang de:"Energiesparen konfigurieren" en:"Configure energy saving")"
cgi_print_checkbox_br "governor_enabled" "$POWERSAVE_GOVERNOR_ENABLED" "$(lang de:"CPU Frequenz Strategie einstellen " en:"Set CPU frequency strategy ")"
for g in `cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors`; do
    echo $g
done
cgi_print_textline_p "governor" "$POWERSAVE_GOVERNOR" 20/20 "$(lang de:"CPU Frequenz Strategie " en:"CPU frequency strategy ")"
cgi_print_checkbox_br "eee_enabled" "$POWERSAVE_EEE_ENABLED" "$(lang de:"Energieeffizienzes Ethernet aktivieren " en:"Enable energy efficient ethernet ")"
cgi_print_textline_p "eee_ports" "$POWERSAVE_EEE_PORTS" 40/40 "$(lang de:"EEE auf folgenden Schittstellen aktivieren " en:"Enable EEE on the following interfaces ")"
cgi_print_checkbox_br "aspm_enabled" "$POWERSAVE_ASPM_ENABLED" "$(lang de:"Erzwingen von ASPM auf PCI Schnittstellen (experimentell) " en:"Enforce ASPM on PCI interfaces (experimental)")"
cgi_print_textline_p "aspm_devs" "$POWERSAVE_ASPM_DEVS" 80/255 "$(lang de:"ASPM auf folgenden Schittstellen aktivieren " en:"Enable ASPM on the following interfaces ")"
cgi_print_checkbox_br "fiber_disabled" "$POWERSAVE_FIBER_DISABLED" "$(lang de:"Glasfasermodem deaktivieren " en:"Deactivate fiber modem ")"
sec_end
