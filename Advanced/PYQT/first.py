from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as db

class Ui_Form(object):

    def insert_data(self):
        id_value = self.lineEdit.text()
        name_value = self.lineEdit_2.text()
        
        try:
            mydb = db.connect(host="localhost", user="root", password="", database="bitdb")
            cursor = mydb.cursor()
            query = "INSERT INTO pyqt (id, name) VALUES (%s, %s)"
            values = (id_value, name_value)
            cursor.execute(query, values)
            mydb.commit()
            cursor.close()
            mydb.close()
            QtWidgets.QMessageBox.information(None, "Success", "Data inserted successfully!")
        except db.Error as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Error inserting data: {e}")

        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(649, 609)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 140, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 200, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 390, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.insert_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Info"))
        self.label.setText(_translate("Form", "Application"))
        self.label_2.setText(_translate("Form", "ID"))
        self.label_3.setText(_translate("Form", "Name"))
        self.pushButton.setText(_translate("Form", "Insert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())