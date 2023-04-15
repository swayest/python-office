# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '..\customizeWindowUIfile\widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os.path

from PyQt5 import QtCore, QtGui, QtWidgets
from pofile import mkdir

from office.api.ppt import ppt2pdf


class Ui_Widget(object):
    def on_convertButtonPPT2PDF_clicked(self):
        print('ppt to pdf convert button')
        input_path = self.pathPPT2PDF.text()
        _, output_path = mkdir(os.path.join(input_path, 'out'))
        ppt2pdf(input_path, output_path)
        print(f'已完成，输出文件夹：{output_path}')
        # QMessageBox.information(self, '提示框', 'ppt已经转换成pdf！')

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(667, 424)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resource/picture/office365.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Widget.setWindowIcon(icon)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 0)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(100, -1, 130, -1)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(Widget)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./resource/picture/office365.png"))
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(Widget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setPixmap(QtGui.QPixmap("./resource/picture/office365.png"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.tabWidget = QtWidgets.QTabWidget(Widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pathPPT2PDF = QtWidgets.QLineEdit(self.frame_2)
        self.pathPPT2PDF.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.pathPPT2PDF.setDragEnabled(True)
        self.pathPPT2PDF.setObjectName("pathPPT2PDF")
        self.horizontalLayout_2.addWidget(self.pathPPT2PDF)

        self.chooseButtonPPT2PDF = QtWidgets.QPushButton(self.frame_2)
        self.chooseButtonPPT2PDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./resource/picture/path.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chooseButtonPPT2PDF.setIcon(icon1)
        self.chooseButtonPPT2PDF.setObjectName("chooseButtonPPT2PDF")
        self.horizontalLayout_2.addWidget(self.chooseButtonPPT2PDF)

        self.convertButtonPPT2PDF = QtWidgets.QPushButton(self.frame_2)
        self.convertButtonPPT2PDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./resource/picture/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.convertButtonPPT2PDF.setIcon(icon2)
        self.convertButtonPPT2PDF.setObjectName("convertButtonPPT2PDF")
        self.convertButtonPPT2PDF.clicked.connect(self.on_convertButtonPPT2PDF_clicked)
        self.horizontalLayout_2.addWidget(self.convertButtonPPT2PDF)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pathPPT2JPG = QtWidgets.QLineEdit(self.frame_2)
        self.pathPPT2JPG.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.pathPPT2JPG.setDragEnabled(True)
        self.pathPPT2JPG.setObjectName("pathPPT2JPG")
        self.horizontalLayout_3.addWidget(self.pathPPT2JPG)
        self.chooseButtonPPT2JPG = QtWidgets.QPushButton(self.frame_2)
        self.chooseButtonPPT2JPG.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chooseButtonPPT2JPG.setIcon(icon1)
        self.chooseButtonPPT2JPG.setObjectName("chooseButtonPPT2JPG")
        self.horizontalLayout_3.addWidget(self.chooseButtonPPT2JPG)
        self.convertButtonPPT2JPG = QtWidgets.QPushButton(self.frame_2)
        self.convertButtonPPT2JPG.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertButtonPPT2JPG.setIcon(icon2)
        self.convertButtonPPT2JPG.setObjectName("convertButtonPPT2JPG")
        self.horizontalLayout_3.addWidget(self.convertButtonPPT2JPG)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.pathImageExtract = QtWidgets.QLineEdit(self.frame_2)
        self.pathImageExtract.setObjectName("pathImageExtract")
        self.horizontalLayout_7.addWidget(self.pathImageExtract)
        self.chooseButtonImageExtract = QtWidgets.QPushButton(self.frame_2)
        self.chooseButtonImageExtract.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chooseButtonImageExtract.setIcon(icon1)
        self.chooseButtonImageExtract.setObjectName("chooseButtonImageExtract")
        self.horizontalLayout_7.addWidget(self.chooseButtonImageExtract)
        self.ExtractButton = QtWidgets.QPushButton(self.frame_2)
        self.ExtractButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExtractButton.setIcon(icon2)
        self.ExtractButton.setObjectName("ExtractButton")
        self.horizontalLayout_7.addWidget(self.ExtractButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./resource/picture/powerpoint1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelWord2Pdf = QtWidgets.QLabel(self.frame)
        self.labelWord2Pdf.setObjectName("labelWord2Pdf")
        self.horizontalLayout_4.addWidget(self.labelWord2Pdf)
        self.pathWord2PDF = QtWidgets.QLineEdit(self.frame)
        self.pathWord2PDF.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.pathWord2PDF.setAcceptDrops(True)
        self.pathWord2PDF.setDragEnabled(True)
        self.pathWord2PDF.setObjectName("pathWord2PDF")
        self.horizontalLayout_4.addWidget(self.pathWord2PDF)
        self.chooseButtonWord2PDF = QtWidgets.QPushButton(self.frame)
        self.chooseButtonWord2PDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chooseButtonWord2PDF.setIcon(icon1)
        self.chooseButtonWord2PDF.setObjectName("chooseButtonWord2PDF")
        self.horizontalLayout_4.addWidget(self.chooseButtonWord2PDF)
        self.convertButtonWord2PDF = QtWidgets.QPushButton(self.frame)
        self.convertButtonWord2PDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertButtonWord2PDF.setIcon(icon2)
        self.convertButtonWord2PDF.setObjectName("convertButtonWord2PDF")
        self.horizontalLayout_4.addWidget(self.convertButtonWord2PDF)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.pathKeywordReplace = QtWidgets.QLineEdit(self.frame)
        self.pathKeywordReplace.setObjectName("pathKeywordReplace")
        self.horizontalLayout_15.addWidget(self.pathKeywordReplace)
        self.chooseButtonKeywordReplace = QtWidgets.QPushButton(self.frame)
        self.chooseButtonKeywordReplace.setIcon(icon1)
        self.chooseButtonKeywordReplace.setObjectName("chooseButtonKeywordReplace")
        self.horizontalLayout_15.addWidget(self.chooseButtonKeywordReplace)
        self.adjustButtonKeyword = QtWidgets.QPushButton(self.frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./resource/picture/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adjustButtonKeyword.setIcon(icon4)
        self.adjustButtonKeyword.setObjectName("adjustButtonKeyword")
        self.horizontalLayout_15.addWidget(self.adjustButtonKeyword)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.verticalLayout.addWidget(self.frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./resource/picture/word1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.pathAddWatermark = QtWidgets.QLineEdit(self.tab_4)
        self.pathAddWatermark.setObjectName("pathAddWatermark")
        self.horizontalLayout_5.addWidget(self.pathAddWatermark)
        self.choosePathAddWatermarkButton = QtWidgets.QPushButton(self.tab_4)
        self.choosePathAddWatermarkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choosePathAddWatermarkButton.setIcon(icon1)
        self.choosePathAddWatermarkButton.setObjectName("choosePathAddWatermarkButton")
        self.horizontalLayout_5.addWidget(self.choosePathAddWatermarkButton)
        self.addWatermarkButton = QtWidgets.QPushButton(self.tab_4)
        self.addWatermarkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addWatermarkButton.setIcon(icon4)
        self.addWatermarkButton.setObjectName("addWatermarkButton")
        self.horizontalLayout_5.addWidget(self.addWatermarkButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_13.addWidget(self.label_7)
        self.pathEncryption = QtWidgets.QLineEdit(self.tab_4)
        self.pathEncryption.setObjectName("pathEncryption")
        self.horizontalLayout_13.addWidget(self.pathEncryption)
        self.choosePathEncryption = QtWidgets.QPushButton(self.tab_4)
        self.choosePathEncryption.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choosePathEncryption.setIcon(icon1)
        self.choosePathEncryption.setObjectName("choosePathEncryption")
        self.horizontalLayout_13.addWidget(self.choosePathEncryption)
        self.encryptionButton = QtWidgets.QPushButton(self.tab_4)
        self.encryptionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.encryptionButton.setIcon(icon2)
        self.encryptionButton.setObjectName("encryptionButton")
        self.horizontalLayout_13.addWidget(self.encryptionButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.pathDecrypt = QtWidgets.QLineEdit(self.tab_4)
        self.pathDecrypt.setObjectName("pathDecrypt")
        self.horizontalLayout_14.addWidget(self.pathDecrypt)
        self.choosePathDecryption = QtWidgets.QPushButton(self.tab_4)
        self.choosePathDecryption.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choosePathDecryption.setIcon(icon1)
        self.choosePathDecryption.setObjectName("choosePathDecryption")
        self.horizontalLayout_14.addWidget(self.choosePathDecryption)
        self.DecryptionButton = QtWidgets.QPushButton(self.tab_4)
        self.DecryptionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DecryptionButton.setIcon(icon2)
        self.DecryptionButton.setObjectName("DecryptionButton")
        self.horizontalLayout_14.addWidget(self.DecryptionButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./resource/picture/pdf1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pathFileClassication = QtWidgets.QLineEdit(self.tab_3)
        self.pathFileClassication.setObjectName("pathFileClassication")
        self.horizontalLayout.addWidget(self.pathFileClassication)
        self.chooseButtonFileClassification = QtWidgets.QPushButton(self.tab_3)
        self.chooseButtonFileClassification.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("E:/图吧工具箱/skin/user/系统信息.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chooseButtonFileClassification.setIcon(icon7)
        self.chooseButtonFileClassification.setObjectName("chooseButtonFileClassification")
        self.horizontalLayout.addWidget(self.chooseButtonFileClassification)
        self.classificationButton = QtWidgets.QPushButton(self.tab_3)
        self.classificationButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.classificationButton.setIcon(icon2)
        self.classificationButton.setObjectName("classificationButton")
        self.horizontalLayout.addWidget(self.classificationButton)
        self.verticalLayout_14.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.pathDuplicateFile = QtWidgets.QLineEdit(self.tab_3)
        self.pathDuplicateFile.setObjectName("pathDuplicateFile")
        self.horizontalLayout_6.addWidget(self.pathDuplicateFile)
        self.chooseDuplicateFileButton = QtWidgets.QPushButton(self.tab_3)
        self.chooseDuplicateFileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chooseDuplicateFileButton.setIcon(icon1)
        self.chooseDuplicateFileButton.setObjectName("chooseDuplicateFileButton")
        self.horizontalLayout_6.addWidget(self.chooseDuplicateFileButton)
        self.duplicateFileButton = QtWidgets.QPushButton(self.tab_3)
        self.duplicateFileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.duplicateFileButton.setIcon(icon2)
        self.duplicateFileButton.setObjectName("duplicateFileButton")
        self.horizontalLayout_6.addWidget(self.duplicateFileButton)
        self.verticalLayout_14.addLayout(self.horizontalLayout_6)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./resource/picture/file1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon8, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        spacerItem = QtWidgets.QSpacerItem(531, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Widget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label_8.setText(_translate("Widget", "官网：www.python-office.com"))
        self.label_2.setText(_translate("Widget", "PPT转PDF:"))
        self.pathPPT2PDF.setText(_translate("Widget", r"D:\\download\\plugin\\test_file"))
        self.chooseButtonPPT2PDF.setText(_translate("Widget", " 选择路径"))
        self.convertButtonPPT2PDF.setText(_translate("Widget", "开始转换"))
        self.label_3.setText(_translate("Widget", "PPT转JPG:"))
        self.pathPPT2JPG.setText(_translate("Widget", r"D:\\download\\plugin\\test_file"))
        self.chooseButtonPPT2JPG.setText(_translate("Widget", "选择路径"))
        self.convertButtonPPT2JPG.setText(_translate("Widget", "开始转换"))
        self.label_6.setText(_translate("Widget", "提取图片:"))
        self.chooseButtonImageExtract.setText(_translate("Widget", "选择文件"))
        self.ExtractButton.setText(_translate("Widget", " 开始提取"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Widget", "PPT处理"))
        self.labelWord2Pdf.setText(_translate("Widget", "Word转PDF："))
        self.pathWord2PDF.setText(_translate("Widget", "D:\\Desktop\\功能测试\\word文件"))
        self.chooseButtonWord2PDF.setText(_translate("Widget", " 选择路径"))
        self.convertButtonWord2PDF.setText(_translate("Widget", "开始转换"))
        self.label_13.setText(_translate("Widget", "关键字替换:"))
        self.pathKeywordReplace.setText(_translate("Widget", "D:\\Desktop\\功能测试\\word文件\\替换关键字"))
        self.chooseButtonKeywordReplace.setText(_translate("Widget", "选择路径"))
        self.adjustButtonKeyword.setText(_translate("Widget", " 调整参数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Widget", "Word处理"))
        self.label_4.setText(_translate("Widget", "添加水印:"))
        self.pathAddWatermark.setText(_translate("Widget", "D:\\Desktop\\功能测试\\PDF文件"))
        self.choosePathAddWatermarkButton.setText(_translate("Widget", "选择路径"))
        self.addWatermarkButton.setText(_translate("Widget", " 参数设置"))
        self.label_7.setText(_translate("Widget", "批量加密:"))
        self.pathEncryption.setText(_translate("Widget", "D:\\Desktop\\功能测试\\PDF文件"))
        self.choosePathEncryption.setText(_translate("Widget", "选择路径"))
        self.encryptionButton.setText(_translate("Widget", "开始"))
        self.label_12.setText(_translate("Widget", "批量解密:"))
        self.pathDecrypt.setText(_translate("Widget", "D:\\Desktop\\功能测试\\PDF文件"))
        self.choosePathDecryption.setText(_translate("Widget", "选择路径"))
        self.DecryptionButton.setText(_translate("Widget", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Widget", "PDF 处理"))
        self.label.setText(_translate("Widget", "文件分类："))
        self.pathFileClassication.setText(_translate("Widget", "D:\\Desktop\\功能测试\\文件分类功能展示"))
        self.chooseButtonFileClassification.setText(_translate("Widget", "选择路径"))
        self.classificationButton.setText(_translate("Widget", "开始处理"))
        self.label_5.setText(_translate("Widget", "冗余文件处理："))
        self.pathDuplicateFile.setText(_translate("Widget", "D:\\Desktop\\功能测试\\检测重复文件功能展示"))
        self.chooseDuplicateFileButton.setText(_translate("Widget", "选择路径"))
        self.duplicateFileButton.setText(_translate("Widget", "开始处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Widget", " 文件处理"))
