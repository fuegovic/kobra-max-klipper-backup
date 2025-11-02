# 🐍 Kobra Max - Klipper Configuration

> **Backup provided by:** [Klipper-Backup](https://github.com/Staubgeborener/klipper-backup)

Complete setup guide and configuration reference for Anycubic Kobra Max running Klipper firmware.

---

## 📋 Table of Contents

- [Hardware Specifications](#-hardware-specifications)
- [Quick Start](#-quick-start)
- [Initial Setup](#%EF%B8%8F-initial-setup)
- [Custom Macros](#-custom-macros)
- [Installed Plugins](#-installed-plugins)
- [Maintenance](#-maintenance)
- [Optional Tools](#-optional-tools)

---

## 🔧 Hardware Specifications

| Component  | Details                     |
| ---------- | --------------------------- |
| Printer    | Anycubic Kobra Max          |
| Mainboard  | Trigorilla Pro A v1.0.4     |
| Host       | Raspberry Pi 3+             |
| OS         | Raspberry Pi OS Lite (32bit) |

### ⚠️ Important Hardware Requirement

> **Resistor Mod Required:** This board needs a hardware modification for Klipper compatibility.
> 
> **Options:**
> - **Hardware mod:** Move 0Ω resistor from R65 → R66 (or remove R65 and short R66)
> - **Alternative:** Use [Catboat firmware](https://github.com/printers-for-people/catboat) instead (no mod needed)

---

## 🚀 Quick Start

<details>
<summary><b>New Installation</b></summary>

1. Flash Raspberry Pi OS Lite and enable SSH
2. Install KIAUH and components → [See Initial Setup](#-initial-setup)
3. Build and flash Klipper firmware → [See Firmware Build](#-firmware-build)
4. Configure printer and macros
5. Set up automatic backups → [See Klipper Backup](#-klipper-backup)

</details>

<details>
<summary><b>Restore from Backup</b></summary>

1. Install KIAUH and base components
2. Clone this repository to `~/printer_data/config/`
3. Flash firmware (if needed)
4. Restart Klipper service

</details>

---

## 🛠️ Initial Setup

### 1. Base System Preparation

**Requirements:**
- Raspberry Pi 3 or newer (Zero 2 W also supported)
- Raspberry Pi OS Lite (32-bit) fresh install
- SSH enabled, network configured

### 2. Install KIAUH

[KIAUH](https://github.com/dw-0/kiauh) is the Klipper Installation And Update Helper.

```bash
# Clone and launch KIAUH
cd ~
git clone https://github.com/dw-0/kiauh.git
./kiauh/kiauh.sh
```

### 3. Install Core Components

Use KIAUH's menu to install the following:

#### Core Services
- **Klipper** - Firmware
- **Moonraker** - API layer

#### Web Interfaces
- **Mainsail** (primary) or **Fluidd** (both can coexist)
- **Mainsail Config** - Default configuration

#### Utilities
- **Crowsnest** - Webcam streaming (modern, recommended)

#### Extensions
- **G-Code Shell Command** - Execute shell scripts from G-code
- **PrettyGCode** - 3D visualization
- **Klipper-Backup** - Automatic GitHub backups
- **Mainsail Theme Installer** *(optional)* - UI customization

---

## 🔨 Firmware Build

### Build Configuration

Launch the Klipper build menu:

```bash
cd ~/klipper
make clean
make menuconfig
```

**Settings:**

| Option              | Value        |
| ------------------- | ------------ |
| MCU Architecture    | HC32F460     |
| Serial Interface    | PA3 & PA2    |
| Application Address | 0x008000     |
| Clock Speed         | 200 MHz      |
| Low-Level Options   | All disabled |

### Compile Firmware

```bash
make
ls -lh out/klipper.bin  # Verify output
```

### Flash to Printer

#### Prepare SD Card

```bash
# Mount SD card (adjust device path as needed)
sudo mount /dev/sdx1 /mnt/printer_sd

# Copy firmware with both filenames (compatibility)
sudo cp ~/klipper/out/klipper.bin /mnt/printer_sd/firmware.bin
sudo cp ~/klipper/out/klipper.bin /mnt/printer_sd/klipper.bin

# Safely unmount
sync
sudo umount /mnt/printer_sd
```

#### Flash Procedure

1. Insert SD card into printer
2. **Power OFF** printer completely
3. **Power ON** printer (USB disconnected)
4. Wait ~5 minutes for auto-flash
5. Remove SD card
6. Connect USB and verify serial communication

---

## 📝 Custom Macros

Custom macros are organized in macros by category:

| File                 | Purpose                              |
| -------------------- | ------------------------------------ |
| `00_helpers.cfg`     | Helper functions and utilities       |
| `10_print.cfg`       | Print start/end sequences            |
| `11_filament.cfg`    | Filament load/unload/change          |
| `20_calibration.cfg` | Calibration routines                 |
| `30_tuning.cfg`      | Performance tuning macros            |
| `40_utils.cfg`       | General utilities                    |
| `50_io.cfg`          | Input/output controls                |
| `60_power.cfg`       | Power management (requires HA setup) |

**📖 Full Documentation:** [Macro Index](/printer_data/config/macros/MACRO_INDEX.md)

---

## 🧩 Installed Plugins

### KAMP (Klipper Adaptive Meshing & Purging)

Intelligent mesh leveling and purge lines that adapt to your print area.

**Repository:** [kyleisah/Klipper-Adaptive-Meshing-Purging](https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging)

<details>
<summary><b>Installation Steps</b></summary>

```bash
# Clone repository
cd ~
git clone https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging.git

# Create symlink and copy config
ln -s ~/Klipper-Adaptive-Meshing-Purging/Configuration ~/printer_data/config/KAMP
cp ~/Klipper-Adaptive-Meshing-Purging/Configuration/KAMP_Settings.cfg ~/printer_data/config/
```

**Enable in `printer.cfg`:**
```ini
[include KAMP_Settings.cfg]
```

</details>

### Smart Power Control (Home Assistant)

Automated power management via smart switch integration.

**Features:**
- Auto power-off after print completion
- Remote power control
- Scheduled shutdowns

<details>
<summary><b>Requirements & Setup</b></summary>

**Prerequisites:**
- Home Assistant instance
- Smart switch/plug controlling printer power
- Moonraker-Home Assistant integration configured

**Configuration:**
- Smart switch entity configured in Home Assistant
- Power device referenced in macros (`60_power.cfg`)

> ⚠️ **Note:** Without this setup, `POWER_OFF` and `SHUTDOWN` macros will fail. You can disable or modify them in 60_power.cfg.

</details>

---

## 💾 Klipper Backup

Automatic backup to GitHub via cron job.

### Initial Configuration

Installed via: `KIAUH → Advanced → Klipper-Backup`

**GitHub Token Setup:**

1. Generate at [github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens)
2. Required permissions: `repo`, `workflow`, `read:packages`, `write:packages`

**Configure backup:**

```bash
~/kiauh/scripts/backup/backup.sh --configure
```

### Manual Backup

```bash
~/kiauh/scripts/backup/backup.sh
```

Backups run automatically via cron.

---

## 🔄 Maintenance

### Updating Components

**Using KIAUH (Recommended):**

Launch KIAUH and use the update menu to update all components.

**Manual Updates:**

<details>
<summary><b>Update via Git</b></summary>

```bash
# Update Klipper
cd ~/klipper
git pull
make clean
make
# Re-flash firmware if needed

# Update Moonraker
cd ~/moonraker
git pull

# Update Mainsail
cd ~/mainsail
git pull
```

**Restart services:**
```bash
sudo service klipper restart
sudo service moonraker restart
sudo service crowsnest restart
```

</details>

---

## 📦 Optional Tools

| Tool                         | Purpose                           | Installation |
| ---------------------------- | --------------------------------- | ------------ |
| **Mainsail Theme Installer** | Customize Mainsail UI colors      | via KIAUH    |
| **PrettyGCode**              | 3D G-code preview in browser      | via KIAUH    |
| **G-Code Shell Command**     | Execute shell scripts from macros | via KIAUH    |
| **Fluidd**                   | Alternative web UI to Mainsail    | via KIAUH    |

---

## 🆘 Troubleshooting

<details>
<summary><b>Firmware won't flash</b></summary>

- Verify SD card is formatted FAT32
- Ensure both `firmware.bin` and `klipper.bin` are copied
- Try power cycling printer 2-3 times
- Check that resistor mod is completed correctly

</details>

<details>
<summary><b>Serial connection fails</b></summary>

- Verify USB cable is data-capable (not charge-only)
- Check `/dev/serial/by-id/` for device
- Ensure firmware flashed successfully
- Verify serial pins in menuconfig (PA3 & PA2)

</details>

<details>
<summary><b>Power macros fail</b></summary>

- Verify Home Assistant integration is configured
- Check smart switch entity name in macros
- Test manual control via Home Assistant first
- See Smart Power Control section

</details>

---
