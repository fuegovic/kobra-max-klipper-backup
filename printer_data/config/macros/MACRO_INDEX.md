# Macro index (generated)

_Auto-generated list of macros found in the macros folder_

## calibration.cfg

- **CLEAR_BED_MESH** — Clear current bed mesh data from memory; **params:** none

- **CALIBRATE_PROBE** — Run Klipper's probe calibration routine and save result; **params:** none

- **PID_TUNE_HOTEND** — Run PID autotune for hotend at target temperature; **params:** TEMP=210

- **PID_TUNE_BED** — Run PID autotune for heated bed at target temperature; **params:** TEMP=60

- **MESH_QUICK_SAVE** — Run a full bed mesh calibration, COLD, and save result; **params:** none

- **MESH_HOT_LEVEL** — Heat, level gantry, probe mesh (flexible temps, no auto-save); **params:** BED_TEMP=60, NOZZLE_TEMP=150

- **MESH_SMART** — Smart mesh — full bed by default, or adaptive area mesh if bounds are given; **params:** AREA_END, AREA_START



## filament.cfg

- **LOAD_FILAMENT** — Heat nozzle and feed filament into hotend until primed; **params:** MAX_VELOCITY=1500, SPEED=1000, TEMP=220

- **UNLOAD_FILAMENT** — Heat nozzle and retract filament fully for removal; **params:** MAX_VELOCITY=1500, SPEED=1000, TEMP=220

- **FILAMENT_CHANGE** — Pause print and run a filament change workflow (heat, retract, park head); **params:** none



## print.cfg

- **START_PRINT** — Prepare printer, heat bed/nozzle, home, load mesh, purge line, and begin print; **params:** BED_TEMP=60, EXTRUDER_TEMP=190, PAUSE=False

- **END_PRINT** — Safely finish print — retract, lift nozzle, cool heaters, park, then power off; **params:** PAUSE_BEFORE_POWER_OFF

- **PAUSE** — Pause print and play alert beeps; **params:** none

- **CANCEL_PRINT** — Cancel print and play error beeps; **params:** none



## tuning.cfg

- **TEST_FANS** — Spin fans at various speeds for testing; use params SLOW/FAST (0-255); **params:** FAST=255, SLOW=100

- **TEST_SPEED** — no description; **params:** ACCEL=printer.configfile.settings.printer.max_accel, BOUND=20, ITERATIONS=5, SPEED=printer.configfile.settings.printer.max_velocity

- **PA_TUNING_TOWER** — Run a pressure advance tuning tower using Klipper's TUNING_TOWER; **params:** HEIGHT=40, START=0, STEP=0.005



## utils.cfg

- **HOME_ALL** — Home all axes cleanly (G28 wrapper); **params:** none

- **SAVE_CONFIG_AND_RESTART** — Save current config (including tuned values) and restart Klipper; **params:** none

- **LED_ON** — LED Fade In; **params:** none

- **LED_OFF** — LED Fade Out; **params:** none

- **POWER_OFF** — Safe shutdown and power off; **params:** none

- **QUICK_POWER_OFF** — Shutdown printer; **params:** none

- **M300** — no description; **params:** P=100, S=1000

- **BEEP_SHORT** — Single short beep; **params:** none

- **BEEP_LONG** — Single long beep; **params:** none

- **BEEP_DOUBLE** — Two quick beeps; **params:** none

- **BEEP_ALERT** — Repeating triple beep (attention grabber); **params:** none

- **PROBE_RESET** — Reset probe by toggling its reset pin (use when probe locks); **params:** none

- **SNAPSHOT_CAMERA** — Trigger a camera snapshot. Tries TAKE_PHOTO first; fallback to MJPG snapshot via ustreamer (port 8080); **params:** none

- **STATUS_REPORT** — Print a short status report (temperatures, bed mesh profile list); **params:** none



## Refile suggestions (automated hints)

- **CLEAR_BED_MESH** (currently in `calibration.cfg`) — suggested group: adaptive

- **PID_TUNE_HOTEND** (currently in `calibration.cfg`) — suggested group: tuning

- **PID_TUNE_BED** (currently in `calibration.cfg`) — suggested group: tuning

- **MESH_QUICK_SAVE** (currently in `calibration.cfg`) — suggested group: adaptive

- **MESH_HOT_LEVEL** (currently in `calibration.cfg`) — suggested group: adaptive

- **MESH_SMART** (currently in `calibration.cfg`) — suggested group: adaptive

- **LOAD_FILAMENT** (currently in `filament.cfg`) — suggested group: filament

- **UNLOAD_FILAMENT** (currently in `filament.cfg`) — suggested group: filament

- **FILAMENT_CHANGE** (currently in `filament.cfg`) — suggested group: filament

- **LED_ON** (currently in `utils.cfg`) — suggested group: lighting

- **LED_OFF** (currently in `utils.cfg`) — suggested group: lighting, power

- **POWER_OFF** (currently in `utils.cfg`) — suggested group: power

- **QUICK_POWER_OFF** (currently in `utils.cfg`) — suggested group: power


