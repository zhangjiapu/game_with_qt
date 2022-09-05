import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
import CommonValues
import ChapterOneUI

if __name__ == '__main__':
    # 创建这个应用上下文
    app = QApplication(sys.argv)
    app.setApplicationName(CommonValues.APP_NAME)
    app.setWindowIcon(QIcon(QPixmap("resource/tropical_storm.png")))

    # 第一篇章
    chapterOneMainWindow = QMainWindow()
    chapterOneMainWindow.setWindowTitle(CommonValues.APP_NAME)
    mainUI = ChapterOneUI.ChapterOneMainUI()
    mainUI.setupUi(chapterOneMainWindow)

    chapterOneMainWindow.show()
    sys.exit(app.exec_())
