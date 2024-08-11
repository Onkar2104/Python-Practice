from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as db

class Ui_Application(object):

    def Submit(self):
        id = self.id.text()
        name = self.name.text()
        birth = self.date.text()
        place = self.place.text()
        gender = self.gender.currentText()
        aadhar = self.aadhar.text()
        phone = self.phone.text()
        email = self.email.text()

        if(name=="" or birth=="" or place=="" or gender=="" or aadhar=="" or phone=="" or email==""):
            QtWidgets.QMessageBox.information(None, "Alert", "Please fill all information.!")
        else:
            con = db.connect(host="localhost", user="root", password="", database="bitdb")
            cursor = con.cursor()
            query = "INSERT INTO application values('"+id+"', '"+name+"', '"+birth+"', '"+place+"', '"+gender+"', '"+aadhar+"', '"+phone+"', '"+email+"')"
            cursor.execute(query)
            cursor.execute("commit")
            QtWidgets.QMessageBox.information(None, "Success", "Data inserted successfully!")


    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(846, 606)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Application.setPalette(palette)
        Application.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(Application)
        self.label.setGeometry(QtCore.QRect(310, 20, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Application)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Application)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Application)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Application)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Application)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Application)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Application)
        self.label_8.setGeometry(QtCore.QRect(30, 340, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Application)
        self.label_9.setGeometry(QtCore.QRect(30, 380, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.id = QtWidgets.QLineEdit(Application)
        self.id.setGeometry(QtCore.QRect(210, 100, 231, 22))
        self.id.setObjectName("id")
        self.name = QtWidgets.QLineEdit(Application)
        self.name.setGeometry(QtCore.QRect(210, 140, 231, 22))
        self.name.setObjectName("name")
        self.date = QtWidgets.QDateEdit(Application)
        self.date.setGeometry(QtCore.QRect(210, 180, 151, 22))
        self.date.setObjectName("date")
        self.place = QtWidgets.QLineEdit(Application)
        self.place.setGeometry(QtCore.QRect(210, 220, 231, 22))
        self.place.setObjectName("place")
        self.gender = QtWidgets.QComboBox(Application)
        self.gender.setGeometry(QtCore.QRect(210, 260, 73, 22))
        self.gender.setToolTipDuration(4)
        self.gender.setEditable(True)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.aadhar = QtWidgets.QLineEdit(Application)
        self.aadhar.setGeometry(QtCore.QRect(210, 300, 231, 22))
        self.aadhar.setObjectName("aadhar")
        self.phone = QtWidgets.QLineEdit(Application)
        self.phone.setGeometry(QtCore.QRect(210, 340, 231, 22))
        self.phone.setObjectName("phone")
        self.email = QtWidgets.QLineEdit(Application)
        self.email.setGeometry(QtCore.QRect(210, 380, 231, 22))
        self.email.setObjectName("email")
        self.submit = QtWidgets.QPushButton(Application)
        self.submit.setGeometry(QtCore.QRect(370, 490, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")

        self.retranslateUi(Application)
        self.gender.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Application)
        self.submit.clicked.connect(self.Submit)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "Application Form"))
        self.label.setText(_translate("Application", "Application Form"))
        self.label_2.setText(_translate("Application", "Application No."))
        self.label_3.setText(_translate("Application", "Name"))
        self.label_4.setText(_translate("Application", "Birth Date"))
        self.label_5.setText(_translate("Application", "Birth Place"))
        self.label_6.setText(_translate("Application", "Gender"))
        self.label_7.setText(_translate("Application", "Aadhar No."))
        self.label_8.setText(_translate("Application", "Phone No."))
        self.label_9.setText(_translate("Application", "Email Id"))
        self.gender.setCurrentText(_translate("Application", "Select"))
        self.gender.setItemText(0, _translate("Application", "Select"))
        self.gender.setItemText(1, _translate("Application", "Male"))
        self.gender.setItemText(2, _translate("Application", "Female"))
        self.gender.setItemText(3, _translate("Application", "Other"))
        self.submit.setText(_translate("Application", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QWidget()
    ui = Ui_Application()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())