import sys
import os

APP_NAME = "热带风暴"

def resource_path(filaeName):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filaeName)
    return os.path.join(filaeName)
