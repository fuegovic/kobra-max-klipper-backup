# Macro index (generated)

_Auto-generated list of macros found in the macros folder_

## 00_helpers.cfg

- **_CG28** — Conditional home - only home if axes not already homed; **params:** none



## 10_print.cfg

- **HOME** — Home all axes cleanly (G28 wrapper); **params:** none

- **START_PRINT** — Prepare printer, heat bed/nozzle, home, load mesh, purge line, and begin print; **params:** BED_TEMP=60, EXTRUDER_TEMP=190, PAUSE=False

- **END_PRINT** — Safely finish print — retract, lift nozzle, cool heaters, park, then power off; **params:** PAUSE_BEFORE_POWER_OFF

- **PAUSE** — Pause print and play alert beeps; **params:** none

- **RESUME** — Resume print with audio and visual feedback; **params:** none

- **CANCEL_PRINT** — Cancel print and play error beeps; **params:** none



## 11_filament.cfg

- **LOAD_FILAMENT** — Heat nozzle and feed filament into hotend until primed; **params:** MAX_VELOCITY=1500, SPEED=1000, TEMP=220

- **UNLOAD_FILAMENT** — Heat nozzle and retract filament fully for removal; **params:** MAX_VELOCITY=1500, SPEED=1000, TEMP=220

- **FILAMENT_CHANGE** — Pause print and run a filament change workflow (heat, retract, park head); **params:** none

- **M600** — Filament change (standard M600); **params:** none

- **HEAT_PLA** — Preheat for PLA (bed 60°C, nozzle 200°C); **params:** none

- **HEAT_PETG** — Preheat for PETG (bed 80°C, nozzle 235°C); **params:** none

- **HEAT_ABS** — Preheat for ABS (bed 100°C, nozzle 245°C); **params:** none

- **HEAT_TPU** — Preheat for TPU (bed 50°C, nozzle 220°C); **params:** none

- **COOLDOWN** — Active cooldown - run fans until temps are safe; **params:** none



## 20_calibration.cfg

- **CLEAR_BED_MESH** — Clear current bed mesh data from memory; **params:** none

- **CALIBRATE_PROBE** — Run Klipper's probe calibration routine and save result; **params:** none

- **MESH_CALIBRATE_KAMP** — Run a full bed mesh calibration (KAMP), and save result; **params:** none

- **MESH_CALIBRATE_LEGACY** — Run a full bed mesh calibration (legacy), and save result; **params:** none

- **FIRST_LAYER_CAL** — Print a first layer calibration pattern; **params:** none

- **MESH_SAVE** — Save current mesh with a profile name; **params:** NAME='default'

- **MESH_LOAD** — Load a saved mesh profile; **params:** NAME='default'

- **MESH_CLEAR** — Clear the current bed mesh; **params:** none

- **MESH_LIST** — List all saved mesh profiles; **params:** none

- **PREFLIGHT_CHECK** — Verify printer readiness before starting a print; **params:** none

- **TEST_EXTRUSION** — Extrude 100mm to verify extruder calibration; **params:** none

- **HEAT_SOAK** — Heat bed and wait for thermal equilibrium; **params:** BED_TEMP=60, DURATION=10



## 30_tuning.cfg

- **Z_OFFSET_UP** — Increase Z offset by 0.01mm (nozzle moves closer to bed); **params:** none

- **Z_OFFSET_DOWN** — Decrease Z offset by 0.01mm (nozzle moves away from bed); **params:** none

- **Z_OFFSET_RESET** — Reset Z offset to 0; **params:** none

- **PID_TUNE_HOTEND** — Run PID autotune for hotend at target temperature; **params:** TEMP=210

- **PID_TUNE_BED** — Run PID autotune for heated bed at target temperature; **params:** TEMP=60

- **TEST_FANS** — Spin fans at various speeds for testing; use params SLOW/FAST (0-255); **params:** FAST=255, SLOW=100

- **TEST_SPEED** — no description; **params:** ACCEL=printer.configfile.settings.printer.max_accel, BOUND=20, ITERATIONS=5, SPEED=printer.configfile.settings.printer.max_velocity

- **PA_TUNING_TOWER** — Run a pressure advance tuning tower using Klipper's TUNING_TOWER; **params:** HEIGHT=40, START=0, STEP=0.005

- **SET_PA_PLA** — Set pressure advance value for PLA; **params:** none

- **SET_PA_PETG** — Set pressure advance value for PETG; **params:** none

- **SET_PA_ABS** — Set pressure advance value for ABS; **params:** none

- **SET_PA_TPU** — Set pressure advance value for TPU; **params:** none



## 40_utils.cfg

- **SAVE_AND_RESTART** — Save current config (including tuned values) and restart Klipper; **params:** none

- **PROBE_RESET** — Reset probe by toggling its reset pin (use when probe locks); **params:** none

- **STATUS_REPORT** — Print a short status report (temperatures, active mesh); **params:** none

- **PRINT_STATS** — Display current print statistics; **params:** none

- **HEATERS_OFF** — Emergency heater shutdown - turn off all heaters immediately; **params:** none

- **PARK_FRONT** — Park toolhead at front-center for easy access; **params:** none

- **PARK_CENTER** — Park toolhead at center of bed; **params:** none

- **PARK_REAR** — Park toolhead at rear for maintenance access; **params:** none

- **MOTORS_OFF** — Disable all stepper motors; **params:** none

- **MOTORS_ON** — Enable all stepper motors; **params:** none

- **EMERGENCY_STOP** — Emergency stop with alarm sound; **params:** none

- **NOZZLE_PURGE** — Purge nozzle at front-left corner for maintenance; **params:** none



## 50_io.cfg

- **LED_ON** — LED Fade In; **params:** none

- **LED_OFF** — LED Fade Out; **params:** none

- **M300** — Single short beep; **params:** P=100, S=1000

- **BEEP_SHORT** — Single short beep; **params:** none

- **BEEP_LONG** — Single long beep; **params:** none

- **BEEP_DOUBLE** — Two quick beeps; **params:** none

- **BEEP_ALERT** — Repeating triple beep (attention grabber); **params:** none

- **BEEP_ERROR** — Error beep pattern (three long beeps); **params:** none



## 60_power.cfg

- **POWER_OFF** — Safe shutdown and power off; **params:** none

- **SHUTDOWN** — Safe shutdown - verify no print running before powering off; **params:** none



## Refile suggestions (automated hints)

- **LOAD_FILAMENT** (currently in `11_filament.cfg`) — suggested group: filament

- **UNLOAD_FILAMENT** (currently in `11_filament.cfg`) — suggested group: filament

- **FILAMENT_CHANGE** (currently in `11_filament.cfg`) — suggested group: filament

- **CLEAR_BED_MESH** (currently in `20_calibration.cfg`) — suggested group: adaptive

- **MESH_CALIBRATE_KAMP** (currently in `20_calibration.cfg`) — suggested group: adaptive

- **MESH_CALIBRATE_LEGACY** (currently in `20_calibration.cfg`) — suggested group: adaptive

- **MESH_SAVE** (currently in `20_calibration.cfg`) — suggested group: adaptive

- **MESH_LOAD** (currently in `20_calibration.cfg`) — suggested group: adaptive, filament

- **MESH_CLEAR** (currently in `20_calibration.cfg`) — suggested group: adaptive

- **MESH_LIST** (currently in `20_calibration.cfg`) — suggested group: adaptive

- **PREFLIGHT_CHECK** (currently in `20_calibration.cfg`) — suggested group: lighting

- **Z_OFFSET_UP** (currently in `30_tuning.cfg`) — suggested group: power

- **Z_OFFSET_DOWN** (currently in `30_tuning.cfg`) — suggested group: power

- **Z_OFFSET_RESET** (currently in `30_tuning.cfg`) — suggested group: power

- **PID_TUNE_HOTEND** (currently in `30_tuning.cfg`) — suggested group: tuning

- **PID_TUNE_BED** (currently in `30_tuning.cfg`) — suggested group: tuning

- **HEATERS_OFF** (currently in `40_utils.cfg`) — suggested group: power

- **MOTORS_OFF** (currently in `40_utils.cfg`) — suggested group: power

- **NOZZLE_PURGE** (currently in `40_utils.cfg`) — suggested group: purge

- **LED_ON** (currently in `50_io.cfg`) — suggested group: lighting

- **LED_OFF** (currently in `50_io.cfg`) — suggested group: lighting, power

- **POWER_OFF** (currently in `60_power.cfg`) — suggested group: power

- **SHUTDOWN** (currently in `60_power.cfg`) — suggested group: power


