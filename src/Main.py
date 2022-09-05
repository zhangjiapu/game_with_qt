import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap

import ChapterTwoUI
import CommonValues
import ChapterOneUI

if __name__ == '__main__':
    # 创建这个应用上下文
    app = QApplication(sys.argv)
    app.setApplicationName(CommonValues.APP_NAME)
    app.setWindowIcon(QIcon(QPixmap("resource/tropical_storm.png")))

    # 第二篇章
    chapterTwoMainWindow = QMainWindow()
    chapterTwoMainWindow.setWindowTitle(CommonValues.APP_NAME)
    chapterTwoMainUI = ChapterTwoUI.ChapterTwoMainUI()
    chapterTwoMainUI.setupUi(chapterTwoMainWindow)


    # 第一篇章
    chapterOneMainWindow = QMainWindow()
    chapterOneMainWindow.setWindowTitle(CommonValues.APP_NAME)
    chapterOneMainUI = ChapterOneUI.ChapterOneMainUI()
    chapterOneMainUI.setupUi(chapterOneMainWindow,chapterTwoMainWindow)

    chapterOneMainWindow.show()
    sys.exit(app.exec_())
