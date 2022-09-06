import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap

import ChapterTwoUI
import CommonUtil
import ChapterOneUI
import ChapterThreeUI

if __name__ == '__main__':
    # 创建这个应用上下文
    app = QApplication(sys.argv)
    app.setApplicationName(CommonUtil.APP_NAME)
    app.setWindowIcon(QIcon(QPixmap(CommonUtil.resource_path("resource/image/tropical_storm.png"))))

    # 第三篇章
    chapterThreeMainWindow = QMainWindow()
    chapterThreeMainWindow.setWindowTitle(CommonUtil.APP_NAME)
    chapterThreeMainUI = ChapterThreeUI.Ui_MainWindow()
    chapterThreeMainUI.setupUi(chapterThreeMainWindow)

    # 第二篇章
    chapterTwoMainWindow = QMainWindow()
    chapterTwoMainWindow.setWindowTitle(CommonUtil.APP_NAME)
    chapterTwoMainUI = ChapterTwoUI.ChapterTwoMainUI()
    chapterTwoMainUI.setupUi(chapterTwoMainWindow,chapterThreeMainWindow)

    # 第一篇章
    chapterOneMainWindow = QMainWindow()
    chapterOneMainWindow.setWindowTitle(CommonUtil.APP_NAME)
    chapterOneMainUI = ChapterOneUI.ChapterOneMainUI()
    chapterOneMainUI.setupUi(chapterOneMainWindow, chapterTwoMainWindow)

    chapterOneMainWindow.show()
    sys.exit(app.exec_())
