# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec file for cc_azprune."""

import os
import sys
from pathlib import Path

# Get the customtkinter package path
import customtkinter
ctk_path = Path(customtkinter.__file__).parent

block_cipher = None

a = Analysis(
    ['src/cc_azprune/app.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Include customtkinter assets (themes, etc.)
        (str(ctk_path), 'customtkinter'),
    ],
    hiddenimports=[
        # Azure SDK modules
        'azure.identity',
        'azure.identity._credentials',
        'azure.identity._credentials.azure_cli',
        'azure.identity._credentials.chained',
        'azure.identity._credentials.default',
        'azure.identity._credentials.environment',
        'azure.identity._credentials.managed_identity',
        'azure.identity._internal',
        'azure.identity._internal.msal_credentials',
        'azure.mgmt.resourcegraph',
        'azure.mgmt.resourcegraph.models',
        'azure.mgmt.resourcegraph.operations',
        'azure.mgmt.subscription',
        'azure.mgmt.subscription.models',
        'azure.mgmt.subscription.operations',
        'azure.core',
        'azure.core.pipeline',
        'azure.core.pipeline.policies',
        'azure.core.pipeline.transport',
        'azure.core.credentials',
        'azure.core.exceptions',
        # MSAL dependencies
        'msal',
        'msal_extensions',
        # Other dependencies
        'openpyxl',
        'openpyxl.workbook',
        'openpyxl.worksheet',
        'openpyxl.styles',
        'openpyxl.utils',
        'cffi',
        'cryptography',
        # Tkinter/customtkinter
        'tkinter',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'customtkinter',
        # Standard library that might be needed
        'json',
        'logging',
        'threading',
        'webbrowser',
        'subprocess',
        'datetime',
        'pathlib',
        'traceback',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='cc_azprune',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Windowed mode - no console
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='assets/icon.ico',  # Uncomment if you add an icon
)
