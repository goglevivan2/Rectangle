import sys
from PyQt5 import  QtCore,QtWidgets
from PyQt5.QtGui import QColor
import random

class TestRectItem(QtWidgets.QGraphicsRectItem,):
    def __init__(self, parent=None,HEIGHT=50.0,WIDTH = 100.0):
        QtWidgets.QGraphicsPixmapItem.__init__(self, parent)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.move_restrict_rect = QtCore.QRectF(-50, -50, WIDTH, HEIGHT)

        self.setRect(QtCore.QRectF( 300-WIDTH*0.25,300-HEIGHT*0.1, WIDTH*0.5,HEIGHT*0.2))
        self.setBrush(QColor(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))

    def mouseMoveEvent(self, event):
        # check of mouse moved within the restricted area for the item
        if self.move_restrict_rect.contains(event.scenePos()):
            QtWidgets.QGraphicsRectItem.mouseMoveEvent(self, event)

class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.isRectangleExist=False
        scene = QtWidgets.QGraphicsScene(-50, -50, 600, 600)
        scene.setBackgroundBrush(QColor("gray"))
        view = QtWidgets.QGraphicsView()
        view.setScene(scene)
        view.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.setCentralWidget(view)


    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_A and self.isRectangleExist == False:
            scene = QtWidgets.QGraphicsScene(-50, -50, 600, 600)

            TestRectItem.HEIGHT = scene.height()
            TestRectItem.WIDTH = scene.width()
            scene.setBackgroundBrush(QColor("gray"))
            rectItem = TestRectItem(HEIGHT=self.size().height(),WIDTH=self.size().width())
            scene.addItem(rectItem)
            view = QtWidgets.QGraphicsView()
            view.setScene(scene)
            view.setGeometry(QtCore.QRect(0, 0, 400, 200))
            self.setCentralWidget(view)
            self.isRectangleExist=True
        if e.key() == QtCore.Qt.Key_Q and self.isRectangleExist == True:
            scene = QtWidgets.QGraphicsScene(-50, -50, 600, 800)

            scene.setBackgroundBrush(QColor("gray"))
            rectItem = None
            scene.addItem(rectItem)
            view = QtWidgets.QGraphicsView()
            view.setScene(scene)
            view.setGeometry(QtCore.QRect(0, 0, 400, 200))
            self.setCentralWidget(view)
            self.isRectangleExist = False


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()