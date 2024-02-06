# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Project\KnowledgeMap\PDF_Process\Process_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Table = QtWidgets.QTabWidget(self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(20, 10, 691, 511))
        self.Table.setObjectName("Table")
        self.ProcessMenu = QtWidgets.QWidget()
        self.ProcessMenu.setObjectName("ProcessMenu")
        self.Process = QtWidgets.QPushButton(self.ProcessMenu)
        self.Process.setGeometry(QtCore.QRect(540, 390, 93, 28))
        self.Process.setObjectName("Process")
        self.TargetFolder = QtWidgets.QTextBrowser(self.ProcessMenu)
        self.TargetFolder.setGeometry(QtCore.QRect(310, 230, 300, 30))
        self.TargetFolder.setObjectName("TargetFolder")
        self.TargetButton = QtWidgets.QPushButton(self.ProcessMenu)
        self.TargetButton.setGeometry(QtCore.QRect(140, 230, 120, 30))
        self.TargetButton.setObjectName("TargetButton")
        self.SourceButton = QtWidgets.QPushButton(self.ProcessMenu)
        self.SourceButton.setGeometry(QtCore.QRect(140, 130, 120, 30))
        self.SourceButton.setObjectName("SourceButton")
        self.SourceFolder = QtWidgets.QTextBrowser(self.ProcessMenu)
        self.SourceFolder.setGeometry(QtCore.QRect(310, 130, 300, 30))
        self.SourceFolder.setObjectName("SourceFolder")
        self.ProcessText = QtWidgets.QTextBrowser(self.ProcessMenu)
        self.ProcessText.setGeometry(QtCore.QRect(540, 440, 93, 28))
        self.ProcessText.setObjectName("ProcessText")
        self.Table.addTab(self.ProcessMenu, "")
        self.TableMenu = QtWidgets.QWidget()
        self.TableMenu.setObjectName("TableMenu")
        self.Folder = QtWidgets.QListWidget(self.TableMenu)
        self.Folder.setGeometry(QtCore.QRect(90, 50, 531, 351))
        self.Folder.setObjectName("Folder")
        self.Show = QtWidgets.QPushButton(self.TableMenu)
        self.Show.setGeometry(QtCore.QRect(520, 430, 93, 28))
        self.Show.setObjectName("Show")
        self.Table.addTab(self.TableMenu, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Table.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Process.setText(_translate("MainWindow", "运行"))
        self.TargetButton.setText(_translate("MainWindow", "选择目标文件夹"))
        self.SourceButton.setText(_translate("MainWindow", "选择源文件夹"))
        self.Table.setTabText(self.Table.indexOf(self.ProcessMenu), _translate("MainWindow", "TabProcess"))
        self.Show.setText(_translate("MainWindow", "Read"))
        self.Table.setTabText(self.Table.indexOf(self.TableMenu), _translate("MainWindow", "TabContent"))
