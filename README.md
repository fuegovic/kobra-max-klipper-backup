# 🐍 Kobra Max - Klipper Setup & Backup Notes
> This backup is provided by [Klipper-Backup](https://github.com/Staubgeborener/klipper-backup)

This document describes how this Klipper installation was created, configured, and backed up.  
It serves both as a reproducible setup guide and a reference for restoring from backup.

---

## 🧱 Hardware

**Printer:** Anycubic Kobra Max  
**Mainboard:** Trigorilla Pro A v1.0.4  

**Firmware Note:**  
This board requires a resistor mod for Klipper compatibility — move the 0 Ω resistor from **R65 → R66** (or remove R65 and short R66).  
If you’re not comfortable performing the hardware mod, use **Catboat** firmware instead:  
👉 [https://github.com/printers-for-people/catboat](https://github.com/printers-for-people/catboat)

**Host:** Raspberry Pi 3 (any Pi ≥ 3 or Zero 2 W also works)

---

## 🪜 Base System

**OS:** Raspberry Pi OS Lite (32-bit)  
**Install method:** Fresh image from [raspberrypi.com/software](https://www.raspberrypi.com/software/)  
**Network:** SSH enabled, hostname and wifi set before first boot

---

## ⚙️ KIAUH Installation

**Reference:** [https://github.com/dw-0/kiauh](https://github.com/dw-0/kiauh)

```bash
cd ~
git clone https://github.com/dw-0/kiauh.git
./kiauh/kiauh.sh
````

### Installed Components

| Category        | Components                                                                                           | Notes                               |
| --------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------- |
| Firmware & API  | Klipper, Moonraker                                                                                   | Core firmware + API layer           |
| Web Interface   | Mainsail, Fluidd                                                                                     | Both installed (use one as default) |
| Client Config   | Mainsail config                                                                                      | Imported via KIAUH                  |
| Webcam Streamer | Crowsnest                                                                                            | Recommended over MJPG-streamer      |
| Extensions      | G-Code Shell Command, PrettyGCode, Mainsail Theme Installer (optional), Klipper-Backup (recommended) |                                     |

### Updates

Use KIAUH’s update menu as needed. On a fresh system, only **System Update** typically runs.

---

## 🔧 Firmware Build

Run via KIAUH or manually:

```bash
cd ~/klipper
make clean
make menuconfig
```

### Configuration

| Option              | Value        |
| ------------------- | ------------ |
| MCU Architecture    | HC32F460     |
| Serial Interface    | PA3 & PA2    |
| Application Address | 0x008000     |
| Clock Speed         | 200 MHz      |
| Low-Level Options   | All disabled |

### Build

```bash
make
ls -lh out/klipper.bin
```

### Flash SD Card

```bash
sudo mount /dev/sdx1 /mnt/printer_sd || sudo mount /dev/mmcblk0p1 /mnt/printer_sd
sudo cp ~/klipper/out/klipper.bin /mnt/printer_sd/firmware.bin
sudo cp ~/klipper/out/klipper.bin /mnt/printer_sd/klipper.bin
sync
sudo umount /mnt/printer_sd
```

### Install Procedure

1. Insert SD card into printer
2. Power **off** printer
3. Power **on** printer (no USB connected)
4. Wait ~5 minutes for auto-flash
5. Reconnect via USB and verify serial link

---

## 💾 Klipper Backup

Installed via KIAUH → `Advanced → Klipper-Backup`.

**GitHub token:**
Generate at [https://github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens)
Token requires: `repo`, `workflow`, `read:packages`, `write:packages`.

**Initial setup:**

```bash
~/kiauh/scripts/backup/backup.sh --configure
```

Backups are automatic (via cron) or manual via:

```bash
~/kiauh/scripts/backup/backup.sh
```

---

## 🧩 Installed Plugins & Extensions

### 🟣 Klipper Adaptive Meshing & Purging (KAMP)

**Repo:** [https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging](https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging)

**Installation:**

```bash
cd ~
git clone https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging.git
ln -s ~/Klipper-Adaptive-Meshing-Purging/Configuration ~/printer_data/config/KAMP
cp ~/Klipper-Adaptive-Meshing-Purging/Configuration/KAMP_Settings.cfg ~/printer_data/config/KAMP_Settings.cfg
```

Make sure it is enabled in your `printer.cfg`:

```ini
[include KAMP/KAMP_Settings.cfg]
```

---

## 🔄 Updating Klipper & Components

Use KIAUH or manual Git update:

```bash
# Klipper
cd ~/klipper
git pull
make clean
make

# Moonraker
cd ~/moonraker
git pull

# Mainsail
cd ~/mainsail
git pull
```

Then restart services:

```bash
sudo service klipper restart
sudo service moonraker restart
sudo service crowsnest restart
```

---

## 📦 Optional Tools & Notes

| Tool                         | Purpose                           | Install   |
| ---------------------------- | --------------------------------- | --------- |
| **Mainsail Theme Installer** | Customize Mainsail UI             | via KIAUH |
| **PrettyGCode**              | 3D G-code preview                 | via KIAUH |
| **G-Code Shell Command**     | Execute shell scripts from macros | via KIAUH |
| **Fluidd**                   | Alternate Klipper web UI          | via KIAUH |

---
