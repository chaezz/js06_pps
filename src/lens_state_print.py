#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
from datetime import datetime
import cv2

import time

from PyQt5 import QtWidgets, QtGui, QtCore
import save_path_info
import st01_log
class Lens_State_Thread(QtCore.QThread):
    update_ls_signal = QtCore.pyqtSignal(str)

    def __init__(self, src: str = ""):
        super().__init__()
        self.camera_name = save_path_info.get_data_path("SETTING", "camera_name")
        self.rtsp_path = save_path_info.get_data_path("SETTING", "camera_ip")
        self.cam_id = save_path_info.get_data_path("SETTING", "camera_id")
        self.cam_pwd = save_path_info.get_data_path("SETTING", "camera_pw")
        self.view_profile = save_path_info.get_data_path("SETTING", "save_profile")
        self._run_flag = False
        self.logger = st01_log.CreateLogger(__name__)


    def run(self):
        self._run_flag = True
        
        while self._run_flag:
        
            cap = cv2.VideoCapture( f"rtsp://{self.cam_id}:{self.cam_pwd}@{self.rtsp_path}/{self.view_profile}/media.smp")
            ret, cv_img = cap.read()

                    
            # shut down capture system

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.quit()
        self.wait()