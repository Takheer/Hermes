from cx_Freeze import setup, Executable
build_exe_options = {
"includes": ['pandas', 'smtplib', 'tkinter'],
"packages": [],
'excludes' : ['boto.compat.sys',
              'boto.compat._sre',
              'boto.compat._json',
              'boto.compat._locale',
              'boto.compat._struct',
              'boto.compat.array'],
"include_files": []}

setup(
    name = "Hermes",
    version = "0.1",
    description = "",
    author = "SAS_tech",
    options = {"build_exe": build_exe_options},
    executables = [Executable("ui.py")]
)
