from sys import platform
from cx_Freeze import setup, Executable


base = None
if platform == 'win32':
    base = 'Win32Gui'

setup(
    name='indicador-dolar-futuro',
    version='1.0',
    description='Indicador dolar-futuro',
    options={
        'build_exe': {
            'includes': ['tkinter']
        }
    },
    executables=[
        Executable('app.py', base=base)
    ],
)