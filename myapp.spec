# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\code-pywebview\\t7\\\\main.py'],
    pathex=[],
    binaries=[('D:\\code-pywebview\\t7\\\\web_dist', 'web_dist')],
    datas=[('D:\\code-pywebview\\t7\\\\web_dist', 'web_dist')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='myapp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\code-pywebview\\t7\\web_dist\\favicon.ico'],
)
