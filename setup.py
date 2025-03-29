from setuptools import setup
import os

APP = ['bethcheck.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'bethcheck.icns',
    'argv_emulation': True,
    'includes': ['sip', 'ctypes'],
    'packages': ['PyQt5'],
    'frameworks': [
        '/opt/homebrew/opt/libffi/lib/libffi.8.dylib'
    ],
    'plist': {
        'CFBundleName': 'BethCheck',
        'CFBundleDisplayName': 'BethCheck',
        'CFBundleIdentifier': 'com.mari.bethcheck',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
