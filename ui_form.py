# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 140, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(parent=Widget)
        self.checkBox.setGeometry(QtCore.QRect(310, 310, 61, 18))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(parent=Widget)
        self.pushButton.setGeometry(QtCore.QRect(170, 180, 80, 18))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 290, 80, 18))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.checkBox.setText(_translate("Widget", "CheckBox"))
        self.pushButton.setText(_translate("Widget", "PushButton"))
        self.pushButton_2.setText(_translate("Widget", "PushButton"))
