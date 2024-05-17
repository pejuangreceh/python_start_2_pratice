import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Dialogue for opening files (and folders)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)


from PyQt5.QtCore import Qt # needs a Qt.KeepAspectRatio constant to resize while maintaining proportions
from PyQt5.QtGui import QPixmap # screen-optimised


from PIL import Image


app = QApplication([])
win = QWidget()       
win.resize(700, 500) 
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Image")
btn_dir = QPushButton("Folder")
lw_files = QListWidget()


btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_bw = QPushButton("B/W")


row = QHBoxLayout()          # Main line
col1 = QVBoxLayout()         # divided into two columns
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      # in the first - directory selection button
col1.addWidget(lw_files)     # and file list
col2.addWidget(lb_image, 95) # in the second - image
row_tools = QHBoxLayout()    # and button bar
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)


row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)


win.show()


workdir = ''


def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result


def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
   print("ini direktorinya - ",workdir)

   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)


btn_dir.clicked.connect(showFilenamesList)


class ImageProcessor():
    # property biasa
   def __init__(self):
       self.image = None
       self.dir = None
       self.filename = None
       self.save_dir = "Modified/"

    # method untuk mengambil image berdasarkan direktori dan nama file
   def loadImage(self, dir, filename):
       '''When loading, remember the path and file name'''
       self.dir = dir #D:\algoritmics\projects\ps\assets\ice.png
       self.filename = filename #ice.png
       image_path = os.path.join(dir, filename)
       self.image = Image.open(image_path)

    # method untuk menampilkan file berdasarkan path yang sudah dipilih melalui loadImage 
   def showImage(self, path):
       lb_image.hide()
       pixmapimage = QPixmap(path)
       w, h = lb_image.width(), lb_image.height()
       pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
       lb_image.setPixmap(pixmapimage)
       lb_image.show()

# membuat object baru dari class ImageProcessor
workimage = ImageProcessor()


# fungsi diluar class untuk dipanggil ketika memilih gambar
def showChosenImage():
   if lw_files.currentRow() >= 0:
       print("ini adalah cur Row = ",lw_files.currentRow())
       filename = lw_files.currentItem().text()
       print("ini adalah filename = ",filename)
       workimage.loadImage(workdir, filename)
       image_path = os.path.join(workimage.dir, workimage.filename)
       workimage.showImage(image_path)


lw_files.currentRowChanged.connect(showChosenImage)
app.exec()
