[app]

# App title shown on the device
title = Happy Face

# Package name (must be unique, lowercase, no spaces)
package.name = happyface

# Package domain (reverse domain style)
package.domain = org.example

# Source directory (where main.py lives)
source.dir = .

# Entry point
source.include_exts = py,png,jpg,kv,atlas

# App version
version = 1.0

# Requirements: kivy and its dependencies
requirements = python3,kivy

# Orientation
orientation = portrait

# Android permissions (none needed for this app)
# android.permissions = INTERNET

# Minimum Android API level
android.minapi = 21

# Target Android API level
android.api = 33

# Android NDK version
android.ndk = 25b

# Fullscreen (hides status bar)
fullscreen = 1

# Icon (optional — place a 512x512 icon.png in the same folder to use it)
# icon.filename = %(source.dir)s/icon.png

[buildozer]

# Log level: 0=error, 1=info, 2=debug
log_level = 2

# Warn before building for the first time (downloads ~1GB of tools)
warn_on_root = 1
