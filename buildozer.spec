[app]
# (str) Title of your application
title = BizFix-Security

# (str) Package name
package.name = bizfixsec

# (str) Package domain (needed for android/ios packaging)
package.domain = org.bizfix

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# We need certifi for secure connections to threat databases
requirements = python3,kivy==2.3.0,certifi

# (str) Supported orientations
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific
# -----------------------------------------------------------------------------

# (list) Permissions - Critical for BizFix-Security to scan your phone
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) Target Android API (34 is standard for 2025/2026)
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True
