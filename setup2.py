from setuptools import setup

APP = ['bethcheck.py']
DATA_FILES = ['Logo.png']  # Assicurati che il logo sia il solo file da includere
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5', 'streamlit'],
    # Assicurati che il logo sia solo incluso una volta, niente directory
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)


