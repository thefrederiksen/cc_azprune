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
    ['run_app.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        # Include customtkinter assets (themes, etc.)
        (str(ctk_path), 'customtkinter'),
        # Include the source package
        ('src/cc_azprune', 'cc_azprune'),
    ],
    hiddenimports=[
        # Our own modules
        'cc_azprune',
        'cc_azprune.app',
        'cc_azprune.logging_config',
        'cc_azprune.scanner',
        'cc_azprune.portal_links',
        'cc_azprune.exporter',
        'cc_azprune.resource_info',
        'cc_azprune.costs',
        'cc_azprune.detectors',
        'cc_azprune.detectors.disk',
        'cc_azprune.detectors.nic',
        'cc_azprune.detectors.public_ip',
        'cc_azprune.detectors.vm',
        'cc_azprune.detectors.app_gateway',
        'cc_azprune.detectors.vnet_gateway',
        'cc_azprune.detectors.nat_gateway',
        'cc_azprune.detectors.ddos_plan',
        'cc_azprune.detectors.traffic_manager',
        'cc_azprune.detectors.frontdoor_waf',
        'cc_azprune.detectors.nsg',
        'cc_azprune.detectors.route_table',
        'cc_azprune.detectors.availability_set',
        'cc_azprune.detectors.ip_group',
        'cc_azprune.detectors.private_dns',
        'cc_azprune.detectors.private_endpoint',
        'cc_azprune.detectors.resource_group',
        'cc_azprune.detectors.api_connection',
        'cc_azprune.detectors.certificate',
        'cc_azprune.detectors.load_balancer',
        'cc_azprune.detectors.app_service_plan',
        'cc_azprune.detectors.sql_elastic_pool',
        # Azure SDK modules
        'azure',
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
)
