import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QSpinBox, QWidget, QLineEdit, QPlainTextEdit, QPushButton

class TextBomb():
    def __init__(self):
        self.number = None
        self.text = None
        self.repeat = 1
    
    def setNumber(self, number):
        self.number = number

    def setText(self, text):
        self.text = text

    def setRepeat(self, repeat):
        self.repeat = repeat

    def send(self):
        for i in range(self.repeat):
            for word in self.text.split():
                os.system('osascript /Library/TextBomb/1.0.0/sendMessage.scpt ' + self.number + ' ' + word)

def window():
    textbomb = TextBomb()
    app = QApplication([])
    w = QWidget()
    w.resize(386, 292)

    # title
    label = QLabel("Text Bomber", w)
    font = label.font()      
    font.setPointSize(18)              
    label.setFont(font)  
    label.move(150, 20)
    label.show()

    # repeat 
    label = QLabel("Repeat", w)
    label.show()
    label.move(20, 250)
    repeatNumber = QSpinBox(w)
    repeatNumber.setValue(1)
    repeatNumber.show()
    repeatNumber.move(70, 250)
    repeatNumber.valueChanged.connect(textbomb.setRepeat)
    label = QLabel("time(s)", w)
    label.show()
    label.move(120, 250)

    # phone number input
    label = QLabel("Recipient #", w)
    label.show()
    label.move(20, 50)
    numberBox = QLineEdit(w)
    numberBox.setFixedWidth(261)
    numberBox.move(100, 50)
    numberBox.textChanged.connect(textbomb.setNumber)

    # raw text input
    label = QLabel("Content", w)
    label.show()
    label.move(40, 80)
    textBox = QPlainTextEdit(w) 
    textBox.setFixedSize(261, 151)
    textBox.move(100, 80)
    textBox.textChanged.connect(
        lambda: textbomb.setText(textBox.document().toPlainText()))

    # button to send text bomb
    button = QPushButton("Send", w)
    button.setFixedWidth(113)
    button.move(250, 250)
    button.clicked.connect(
        lambda: textbomb.send()
    )

    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()