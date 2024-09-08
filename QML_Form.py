from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import os, sys

APP_ROOT = os.path.dirname(__file__)

class Myform:
    def __init__(self) -> None:
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.load(os.path.join(APP_ROOT, "form.qml"))

        if not self.engine.rootObjects(): # kilép, ha nem jó a qml
            sys.exit(-1)
        
        sys.exit(self.app.exec()) # így marad nyitva az ablak


if __name__ == "__main__":
    Myform()