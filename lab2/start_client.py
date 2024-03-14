from PySide6 import QtWidgets, QtCore, QtGui
import sys


class MainWin(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__init_ui()
        self.__setting_ui()
        self.show()

    def __init_ui(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.tools_h_layout = QtWidgets.QHBoxLayout()
        self.time_edit = QtWidgets.QTimeEdit()
        self.text_line_edit = QtWidgets.QLineEdit('Entry your event')
        self.allow_button = QtWidgets.QPushButton('Add event')
        self.calendar = QtWidgets.QCalendarWidget()
        self.list_widget = QtWidgets.QListWidget()

    def __setting_ui(self) -> None:
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_v_layout)

        self.tools_h_layout.addWidget(self.time_edit)
        self.tools_h_layout.addWidget(self.text_line_edit)
        self.tools_h_layout.addWidget(self.allow_button)

        self.main_v_layout.addWidget(self.calendar)
        self.main_v_layout.addLayout(self.tools_h_layout)
        self.main_v_layout.addWidget(self.list_widget)

        with open('events.txt', 'r') as file:
            events = file.read().split('\n')
        
        for event in events:
            if event == '':
                continue
            self.list_widget.addItem(QtWidgets.QListWidgetItem(event))

        self.allow_button.clicked.connect(self.allow_button_clicked)

    def allow_button_clicked(self) -> None:
        if self.text_line_edit.text() == '':
            QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Icon.Critical, 
                                  title='Error', text='Event entry are empty', 
                                  buttons=QtWidgets.QMessageBox.StandardButton.Ok, 
                                  parent=self)
            return
        self.list_widget.addItem(QtWidgets.QListWidgetItem(f'{self.calendar.selectedDate().toPython()} {self.time_edit.text()} - {self.text_line_edit.text()}'))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        all_items = self.list_widget.findItems("", QtCore.Qt.MatchFlag.MatchContains)
        all_items_text = str([item.text() for item in all_items]).replace('[', "").replace(']', "").replace("\'", '').replace(', ', '\n')

        with open('events.txt', 'w') as file:
            file.write(all_items_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = MainWin()
    app.exec()