from PySide6.QtWidgets import QDialog, QMessageBox
from ui.my01_ui import Ui_Form
import time
import hashlib
from PySide6.QtCore import QTimer

class TokenDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.btn7.clicked.connect(self.show_token_content)
        self.salt = ""
        self.setup_ui()

    def setup_ui(self):
        self.update_salt()  # 初始化时生成一次盐值和更新时间
        self.timer = QTimer(self)  # 创建一个定时器
        self.timer.timeout.connect(self.update_salt_and_labels)  # 连接定时器的超时信号到更新方法
        self.timer.start(5000)  # 每隔5秒触发一次定时器的超时信号

    def generate_salt(self, timestamp):
        return hashlib.sha256(str(timestamp).encode()).hexdigest()[:8]

    def update_salt(self):
        current_timestamp = int(time.time())
        self.salt = self.generate_salt(current_timestamp)
        self.next_update_time = current_timestamp + 5  # 5秒后更新

    def update_salt_and_labels(self):
        current_timestamp = int(time.time())
        
        if current_timestamp >= self.next_update_time:
            self.update_salt()
        
        current_minute = current_timestamp // 60
        self.ui.lbl01.setText(f"时间戳：{current_minute}")
        self.ui.lbl02.setText(f"盐值：{self.salt}")

    def show_token_content(self):
        current_timestamp = int(time.time())
        
        if current_timestamp >= self.next_update_time:
            self.update_salt()
        
        current_minute = current_timestamp // 60
        self.ui.lbl01.setText(f"时间戳：{current_minute}")
        self.ui.lbl02.setText(f"盐值：{self.salt}")
        QMessageBox.information(self, "消息框", f"按钮7令牌内容被点击了！\n盐值：{self.salt}")
