import sys
from PyQt5.QtWidgets import QApplication
import presenter

if __name__ == "__main__":
    app = QApplication(sys.argv)
    presenter = presenter.Presenter()
    app.exec_()
