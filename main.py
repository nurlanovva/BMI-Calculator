import warnings
warnings.simplefilter("ignore", DeprecationWarning)

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QMenuBar
from PyQt6.QtGui import QAction

from logic import calculate_bmi


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 300, 200)

        self.weight_label = QLabel("Weight (kg):", self)
        self.weight_input = QLineEdit(self)

        self.height_label = QLabel("Height (cm):", self)
        self.height_input = QLineEdit(self)

        self.calc_button = QPushButton("Calculate BMI", self)
        self.calc_button.clicked.connect(self.calculate_bmi)

        self.result_label = QLabel("Your BMI:", self)

        layout = QVBoxLayout()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.initMenu()

    def initMenu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        help_menu = menubar.addMenu("Help")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_fields)
        file_menu.addAction(clear_action)

        help_action = QAction("How to use", self)
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text()) / 100
            bmi, status = calculate_bmi(weight, height)
            self.result_label.setText(f"Your BMI: {bmi:.1f} ({status})")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values for weight and height.")

    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText("Your BMI:")

    def show_help(self):
        QMessageBox.information(self, "How to Use",
                                "Enter your weight in kg and height in cm, then click 'Calculate BMI'.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())
