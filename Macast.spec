# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Macast.py'],
    pathex=[],
    binaries=[],
    datas=[('macast/.version', '.'), ('macast/xml/*', 'macast/xml'), ('i18n/zh_CN/LC_MESSAGES/*.mo', 'i18n/zh_CN/LC_MESSAGES'), ('macast/assets/*', 'macast/assets'), ('macast/assets/fonts/*', 'macast/assets/fonts')],
    hiddenimports=[],
    hookspath=['.'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter'],
    noarchive=False,
)

# Do not bundle the GLib/GIO stack: PyInstaller's collected copies come from
# the build image and conflict with the system GIO modules / dbusmenu on newer
# distributions (e.g. "undefined symbol: g_once_init_leave_pointer").  The
# runtime loads the system libraries instead.
_glib_libs = ('libglib-2.0', 'libgobject-2.0', 'libgio-2.0', 'libgmodule-2.0',
              'libgthread-2.0', 'libgirepository', 'libdbusmenu',
              'libmount', 'libblkid', 'libuuid', 'libselinux', 'libseccomp',
              'libpcre2-8')
a.binaries = [b for b in a.binaries
              if not any(lib in b[0] for lib in _glib_libs)]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Macast',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
