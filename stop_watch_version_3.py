import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QTimer, QTime, Qt

class SimpleStopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Stopwatch")

        #this is the  Stopwatch logic
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer()

        # the is ui Elements
        self.label = QLabel("00:00:00.00")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 60px; background-color: lightblue; padding: 20px; border-radius: 10px;")

        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.reset_btn = QPushButton("Reset")

        # Connect buttons to methods
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_time)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        btn_layout.addWidget(self.reset_btn)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()
        self.show_elapsed_time()  # this shows  the final time when stopped

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.label.setText("00:00:00.00")

    def update_time(self):
        self.time = self.time.addMSecs(10)
        h, m, s, ms = self.time.hour(), self.time.minute(), self.time.second(), self.time.msec() // 10
        self.label.setText(f"{h:02}:{m:02}:{s:02}.{ms:02}")

    def show_elapsed_time(self):
        h = self.time.hour()
        m = self.time.minute()
        s = self.time.second()
        ms = self.time.msec() // 10
        elapsed = f"Elapsed Time: {h:02}:{m:02}:{s:02}.{ms:02}"
        QMessageBox.information(self, "Time Info", elapsed)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleStopwatch()
    window.show()
    sys.exit(app.exec_())
