from setuptools import setup

APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["rumps", "cairosvg", "objc", "requests"],
    "iconfile": "AppIcons",
    "plist": {
        "CFBundleIdentifier": "com.yourcompany.OpenAIUsage",
        "CFBundleName": "OpenAIUsage",
        "CFBundleDisplayName": "OpenAI Usage",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0",
        "LSUIElement": True,
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
