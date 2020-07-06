# -*- mode: python ; coding: utf-8 -*-

import sys
sys.modules['FixTk'] = None

import os
VERSION = os.getenv('VERSION', '0.0.0')

block_cipher = None

analysis = Analysis(
    ['../Tautulli.py'],
    pathex=['lib'],
    datas=[
        ('../data', 'data'),
        ('../CHANGELOG.md', '.'),
        ('../LICENSE', '.'),
        ('../version.txt', '.'),
        ('../lib/ipwhois/data', 'data')
    ],
    excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
    hiddenimports=['Foundation', 'AppKit'],
    cipher=block_cipher
)
pyz = PYZ(
    analysis.pure,
    analysis.zipped_data,
    cipher=block_cipher
)
exe = EXE(
    pyz,
    analysis.scripts,
    exclude_binaries=True,
    name='Tautulli',
    console=False,
    icon='../data/interfaces/default/images/logo-circle.icns'
)
coll = COLLECT(
    exe,
    analysis.binaries,
    analysis.zipfiles,
    analysis.datas,
    name='Tautulli'
)
app = BUNDLE(
    coll,
    name='Tautulli.app',
    icon='../data/interfaces/default/images/logo-circle.icns',
    bundle_identifier='com.Tautulli.Tautulli',
    version=VERSION
)
