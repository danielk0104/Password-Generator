import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QSlider
import random
import string

# Main window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Password Generator")

        # Set the window size
        self.setFixedSize(QSize(400, 170))

        # Set up layout
        self.layout = QVBoxLayout()

        # Title
        title = QLabel("Password Generator")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        self.layout.addWidget(title)

        # Subtitle
        subtitle = QLabel("Generate a unique, random password")
        self.layout.addWidget(subtitle)

        # Edit box
        self.edit_box = QLineEdit()
        self.edit_box.setReadOnly(True)
        self.layout.addWidget(self.edit_box)

        # Set character limit
        self.characters = QSlider(Qt.Horizontal)
        self.characters.setRange(1, 128)
        self.characters.valueChanged.connect(self.character_value)
        self.layout.addWidget(self.characters)

        # Display character limit
        self.character_display = QLabel("Character Limit: 1")
        self.layout.addWidget(self.character_display)

        # Generate button
        generate_button = QPushButton("Generate Password")
        self.layout.addWidget(generate_button)

        # Button workings
        generate_button.clicked.connect(self.random_string)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    # Display slider value
    def character_value(self, value):
        self.character_display.setText(f"Character Limit: {str(value)}")

    # Generate a random string
    def random_string(self):
        self.edit_box.setText(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(self.characters.value())))

# Running the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())