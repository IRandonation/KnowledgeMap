import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from Ui_Process_GUI import *
import PDF_Copy
import os
import sys
import subprocess

    
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        # 初始化路径变量
        self.sourceFolderPath = ''
        self.targetFolderPath = ''

        # 设置按钮的点击事件
        self.SourceButton.clicked.connect(self.updateSourceFolder)
        self.TargetButton.clicked.connect(self.updateTargetFolder)
        self.Process.clicked.connect(self.Process_Copy)
        self.Show.clicked.connect(self.ShowList)
        self.Folder.itemClicked.connect(self.open_pdf)
    
    def openFolderDialog(self):
        # 打开文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        return folder_path

    def updateSourceFolder(self):
        folder_path = self.openFolderDialog()  # 使用 QFileDialog 获取文件夹路径
        if folder_path:  # 检查路径是否非空
            self.SourceFolder.append(folder_path)  # 将路径添加到文本框或列表中
            self.sourceFolderPath = folder_path  # 保存路径
        else: 
            self.SourceFolder.setText("请选择文件夹")  # 如果路径为空，提示用户选择文件夹
    
    def updateTargetFolder(self):
        folder_path = self.openFolderDialog()  # 使用 QFileDialog 获取文件夹路径
        if folder_path:  # 检查路径是否非空
            self.TargetFolder.append(folder_path)  # 将路径添加到文本框或列表中
            self.targetFolderPath = folder_path  # 保存路径
    
    def Process_Copy(self):
        # 使用之前保存的路径
        if self.sourceFolderPath and self.targetFolderPath:
            PDF_Copy.copy_pdfs(self.sourceFolderPath, self.targetFolderPath)
            self.ProcessText.setText("Finish")
        else:
            self.ProcessText.setText("Fail")

    #打开pdf文件
    def open_pdf(self, item):
        pdf_filename = item.text()  # 获取被点击项的文本，即文件名
        pdf_path = os.path.join(self.targetFolderPath, pdf_filename)
        print(pdf_path)
        self.open_pdf_with_adobe(pdf_path)  
    
    #使用adobe打开pdf
    def open_pdf_with_adobe(self,pdf_path):
        adobe_path = "D:\\Software\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
        if os.path.exists(adobe_path) and os.path.isfile(pdf_path):
            subprocess.Popen([adobe_path, pdf_path])
        else:
            print("Adobe Reader 路径不存在或 PDF 文件不存在。")

  

    def ShowList(self):
        self.Folder.clear()  # 清空当前列表
        print(self.targetFolderPath)
        for file in os.listdir(self.targetFolderPath):
            if file.endswith('.pdf'):
                self.Folder.addItem(file)
        self.Folder.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())