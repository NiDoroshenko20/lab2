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

        self.main_h_layout = QtWidgets.QHBoxLayout()

        self.group_1_layout = QtWidgets.QVBoxLayout()
        self.group_2_layout = QtWidgets.QVBoxLayout()
        self.group_3_layout = QtWidgets.QVBoxLayout()

        self.button_group_1 = QtWidgets.QButtonGroup()
        self.button_group_2 = QtWidgets.QButtonGroup()
        self.button_group_3 = QtWidgets.QButtonGroup()

    def __setting_ui(self) -> None:

        self.setCentralWidget(self.central_widget)

        self.central_widget.setLayout(self.main_h_layout)

        for button_group, group_layout in zip((self.button_group_1, self.button_group_2, self.button_group_3), (self.group_1_layout, self.group_2_layout, self.group_3_layout)):
            label = QtWidgets.QLabel('Null')
            for color in ['Red', 'Green', 'Yellow']:
                radio_button = QtWidgets.QRadioButton(color)
                button_group.addButton(radio_button)
                group_layout.addWidget(radio_button)
                
            group_layout.addWidget(label)
            self.main_h_layout.addLayout(group_layout)
            button_group.buttonClicked.connect(lambda button, layout=group_layout: self.on_button_clicked(button, layout))

    def on_button_clicked(self, button, layout: QtWidgets.QVBoxLayout):
        
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QLabel):
                break
        
        widget.setStyleSheet(f'background: {button.text()}')
        widget.setText(button.text())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = MainWin()
    app.exec()