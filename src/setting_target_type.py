from PyQt5.QtWidgets import QDialog, QVBoxLayout, QRadioButton, QButtonGroup, QPushButton

class TargetTypeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("타겟 유형 선택")
        self.setGeometry(300, 300, 250, 150)
        
        layout = QVBoxLayout(self)

        # 라디오 버튼을 그룹으로 설정
        self.button_group = QButtonGroup(self)
        
        self.day_radio_btn = QRadioButton("낮")
        self.night_radio_btn = QRadioButton("밤")
        self.common_radio_btn = QRadioButton("공통")
        
        # 기본값 설정 (낮 타겟을 기본으로 선택)
        self.day_radio_btn.setChecked(True)
        
        # 라디오 버튼을 그룹에 추가
        self.button_group.addButton(self.day_radio_btn)
        self.button_group.addButton(self.night_radio_btn)
        self.button_group.addButton(self.common_radio_btn)
        
        # 레이아웃에 라디오 버튼 추가
        layout.addWidget(self.day_radio_btn)
        layout.addWidget(self.night_radio_btn)
        layout.addWidget(self.common_radio_btn)
        
        # 확인 버튼
        self.ok_button = QPushButton("확인", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

    def get_selected_type(self):
        if self.day_radio_btn.isChecked():
            return "daytime"
        elif self.night_radio_btn.isChecked():
            return "night"
        else:
            return "common"