#!/usr/bin/env python3
import os
from tkinter import image_names
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import shutil
import cv2
from multiprocessing import Process, Queue
import multiprocessing as mp
import time

from PyQt5 import QtWidgets, QtGui, QtCore

import st01_log
import save_path_info

class Auto_Remove_Thread(QtCore.QThread):
    update_remove_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._run_flag = False
        self.logger = st01_log.CreateLogger(__name__)


    def run(self):
        self._run_flag = True
        self.logger.info('Start auto remove thread')
        while self._run_flag:
            
            image_path = save_path_info.get_data_path("Path", "image_save_path")
            month = save_path_info.get_data_path("SETTING", "delete_cycle")
            if os.path.exists(image_path):
                folder_list = os.listdir(image_path)
                today = datetime.now()
                delete_threshold_date = today - timedelta(days=int(month)*30)
                
                for folder in folder_list:
                    folder_path = os.path.join(image_path, folder)
                    if os.path.isdir(folder_path):
                        for filename in os.listdir(folder_path):
                            filepath = os.path.join(folder_path, filename)
                    
                            # 파일인지 확인
                            if os.path.isfile(filepath):
                                # 파일이 이미지 파일인지 확인
                                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                                    # 파일의 수정 시간 확인
                                    modification_time = os.path.getmtime(filepath)
                                    
                                    # 현재 시간과 파일의 수정 시간을 비교하여 삭제 여부 결정
                                    if time.time() - modification_time > int(month) * 30 * 24 * 3600:
                                        # 파일 삭제
                                        os.remove(filepath)
                                        # print(f"Deleted: {filename}")
                                        self.logger.info(f"Deleted: {filename}")
                                        self.update_remove_signal.emit(f"Deleted: {filename}")
                    try:
                        folder_date = datetime.strptime(folder, "%Y%m%d")
                    except ValueError:
                        continue  # 날짜 형식이 아닌 폴더는 건너뜀
                        
                    if folder_date < delete_threshold_date:
                        shutil.rmtree(folder_path)
                        print(f"Deleted folder: {folder_path}")
    
                                
    # shut down capture system
    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.quit()
        self.wait()