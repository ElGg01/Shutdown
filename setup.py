import os
import sys
from cx_Freeze import Executable, setup

files = ["assets"]

target = Executable(
    script="app.py",
    base="Win32GUI",
    icon="icon.ico"
    )

setup(
    name="Apagador",
    version="1.0",
    description="Aplication to turn off the PC",
    author="ElGg",
    options={"build_exe": {"include_files" : files}},
    executables=[target]
    )