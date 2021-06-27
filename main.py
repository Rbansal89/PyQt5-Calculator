import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow(qtw.QTabWidget):

    def __init__(self):
        super().__init__()
        # add a layout
        self.setWindowTitle("Hello World!")

        # set layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Hello world!, What's up?")
        # Change the lable font
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)

        # Create entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create a button
        my_button = qtw.QPushButton("Press me!",
                                clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # show the app
        self.show()

        def press_it():
            # add name to label
            my_label.setText(f"Hello {my_entry.text()}!")
            # clear the entry box
            my_entry.setText("")


app = qtw.QApplication([])

mw = MainWindow()

#run the App
app.exec_()