#!/usr/bin/env python3
from operator import index
import os
import pandas as pd
import numpy as np
from datetime import datetime

import cv2
import time
import cal_ext_coef
import save_path_info
import st01_log
import sun_observer

logger = st01_log.CreateLogger(__name__)

def minprint(epoch, left_range, right_range, distance, cv_img):
    """A function that outputs pixels for calculating the dissipation coefficient in the specified areas"""
    # print("minprint 시작")
    # epoch = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    cp_image = cv_img.copy()
    result = ()
    cnt = 1
    min_x = []
    min_y = []
    
    # 현재 시간이 낮인지 밤인지 확인
    now_time = time.time()
    dn_time = sun_observer.sun_observer(now_time)  # 'daytime' 또는 'nighttime'을 반환

    # 낮에는 minrgb, 밤에는 maxrgb 사용
    if dn_time == "daytime":
        rgb_func = minrgb
    else:
        rgb_func = maxrgb

    for upper_left, lower_right in zip(left_range, right_range):
        result = rgb_func(upper_left, lower_right, cp_image)
        min_x.append(result[0])
        min_y.append(result[1])
        cnt += 1

    visibility = get_rgb(epoch, min_x, min_y, cp_image, distance)
    
    # days = epoch[:-4]
    # vis_folder_path = os.path.join(save_path_info.get_data_path('Path', 'data_csv_path'))
    # vis_file_path = os.path.join(vis_folder_path,f"{days}.csv")
    # os.makedirs(vis_folder_path, exist_ok=True)
    
    # if os.path.isfile(vis_file_path):
    #     vis_df = pd.read_csv(vis_file_path)
    # else:
    #     cols = ["time",'visibility']
    #     vis_df = pd.DataFrame(columns=cols)
    
    # dt_epoch = datetime.strptime(epoch, '%Y%m%d%H%M')
    # vis_df = vis_df.append({'time': dt_epoch,'visibility': visibility}, ignore_index=True)
    
    # vis_df.to_csv(vis_file_path,mode="w", index=False)
    
    return visibility

def minrgb(upper_left, lower_right, cp_image):
    """Extracts the minimum RGB value of the dragged area"""

    up_y = min(upper_left[1], lower_right[1])
    down_y = max(upper_left[1], lower_right[1])

    left_x = min(upper_left[0], lower_right[0])
    right_x = max(upper_left[0], lower_right[0])

    test = cp_image[up_y:down_y, left_x:right_x, :]

    r = test[:, :, 0]
    g = test[:, :, 1]
    b = test[:, :, 2]

    r = np.clip(r, 0, 765)
    sum_rgb = r + g + b

    t_idx = np.where(sum_rgb == np.min(sum_rgb))
    
    # print("red : ", cp_image[t_idx[0][0] + up_y, t_idx[1][0] + left_x,0])
    # print("green : ", cp_image[t_idx[0][0] + up_y, t_idx[1][0] + left_x,1])
    # print("blue : ", cp_image[t_idx[0][0] + up_y, t_idx[1][0] + left_x,2])
    show_min_y = t_idx[0][0] + up_y
    show_min_x = t_idx[1][0] + left_x

    return (show_min_x, show_min_y)

def maxrgb(upper_left, lower_right, cp_image):
    """Extracts the maximum RGB value of the dragged area (used during nighttime)"""
    up_y = min(upper_left[1], lower_right[1])
    down_y = max(upper_left[1], lower_right[1])
    left_x = min(upper_left[0], lower_right[0])
    right_x = max(upper_left[0], lower_right[0])

    test = cp_image[up_y:down_y, left_x:right_x, :]
    r, g, b = test[:, :, 0], test[:, :, 1], test[:, :, 2]
    r, g, b = np.clip(r, 0, 765), np.clip(g, 0, 765), np.clip(b, 0, 765)

    sum_rgb = r + g + b
    t_idx = np.where(sum_rgb == np.max(sum_rgb))  # 최대값을 찾음
    show_max_y = t_idx[0][0] + up_y
    show_max_x = t_idx[1][0] + left_x

    return (show_max_x, show_max_y)


def get_rgb(epoch: str, min_x, min_y, cp_image, distance):
    """Gets the RGB values ​​of the coordinates."""
    r_list = []
    g_list = []
    b_list = []

    for x, y in zip(min_x, min_y):

        r_list.append(cp_image[y, x, 0])
        g_list.append(cp_image[y, x, 1])
        b_list.append(cp_image[y, x, 2])
    
    print("red list : ", r_list)
    print("green list : ", g_list)
    print("blue list : ", b_list)

    visibility = save_rgb(r_list, g_list, b_list, epoch, distance)
    return visibility

def save_rgb(r_list, g_list, b_list, epoch, distance):
    """Save the rgb information for each target."""
    
    rgb_csv_path = save_path_info.get_data_path("Path", "rgb_csv_path")
    camera_name = save_path_info.get_data_path('SETTING', 'camera_name')
    try:
        save_path = os.path.join(f"{rgb_csv_path}/{camera_name}")
        os.makedirs(save_path)
        logger.info(f'Create folder RGB save path')

    except Exception as e:
        pass

    if r_list:
        
        r_list = list(map(int, r_list))
        g_list = list(map(int, g_list))
        b_list = list(map(int, b_list))       
        
        col = ["target_name", "r", "g", "b", "distance"]
        result = pd.DataFrame(columns=col)
        result["target_name"] = [f"target_{num}" for num in range(1, len(r_list) + 1)]
        result["r"] = r_list
        result["g"] = g_list
        result["b"] = b_list
        result["distance"] = distance
        list1, list2, list3, select_color = cal_ext_coef.cal_curve(result)
        visibility = extinc_print(list1, list2, list3, select_color)
        print("Save rgb")
        logger.info(f'Save RGB values')
        
        result = result.sort_values(by=['distance'])
        
        r_list = list(result.loc[:,'r'])
        g_list = list(result.loc[:,'g'])
        b_list = list(result.loc[:,'b'])
        distance = list(result.loc[:,'distance'])        
        
        save_rgb_value(r_list, distance, list3[0], "red", epoch)
        save_rgb_value(g_list, distance, list3[1], "green", epoch)
        save_rgb_value(b_list, distance, list3[2], "blue", epoch)
        
        save_ext(list3, epoch)
    
    return visibility

def save_rgb_value(value_list, distance_list, ext_value, select_color, epoch):
    
    data_save_path = save_path_info.get_data_path("Path", "rgb_csv_path")
    camera_name = save_path_info.get_data_path('SETTING', 'camera_name')
    days = epoch[:-4]
    rgbsavedir = os.path.join(f"{data_save_path}/{camera_name}/{select_color}")
    
    try:
        os.makedirs(rgbsavedir)
        logger.info(f'Create folder {select_color} channel save path')
        
    except Exception as e:
        pass
    
    rgb_file_path = os.path.join(rgbsavedir,f"{days}.csv")
    
    
    if os.path.isfile(rgb_file_path):
        rgb_df = pd.read_csv(rgb_file_path)
    
    else:  
        column_list = ['time', 'target_distance', 'intensity_val', 'ext_coeff', 'visibility']
        cols = column_list        
        rgb_df = pd.DataFrame(columns=cols)    
    
    dt_epoch = datetime.strptime(epoch, '%Y%m%d%H%M')
    
    visibility_value = 3.912/ext_value
    
    new_row = pd.DataFrame({
    'time': [dt_epoch],
    'target_distance': [distance_list],
    'intensity_val': [value_list],
    'ext_coeff': [ext_value],
    'visibility': [visibility_value]
    })

    # 기존 데이터프레임과 새로운 데이터프레임을 concat으로 결합
    rgb_df = pd.concat([rgb_df, new_row], ignore_index=True)
    
    rgb_df.to_csv(rgb_file_path,mode="w", index=False)
    print(f"Save {select_color} channel value")
    logger.info(f'Save {select_color} channel value')
    
    
def save_ext(ext_list, epoch):
    
    data_save_path = save_path_info.get_data_path("Path", "ext_csv_path")
    camera_name = save_path_info.get_data_path('SETTING', 'camera_name')
    days = epoch[:-4]
    extsavedir = os.path.join(f"{data_save_path}/{camera_name}")
    try:
        os.makedirs(extsavedir)
        logger.info(f'Create folder RGB Ext save path')
    except Exception as e:
        pass
    
    ext_file_path = os.path.join(extsavedir,f"{days}.csv")
    
    if os.path.isfile(ext_file_path):
        ext_df = pd.read_csv(ext_file_path)
    
    else:        
        cols = ["time",'r_ext','g_ext','b_ext']
        ext_df = pd.DataFrame(columns=cols)
    
    dt_epoch = datetime.strptime(epoch, '%Y%m%d%H%M')
    # 새로운 행을 딕셔너리로 만들고 이를 데이터프레임으로 변환
    new_row = pd.DataFrame({
        'time': [dt_epoch],
        'r_ext': [ext_list[0]],
        'g_ext': [ext_list[1]],
        'b_ext': [ext_list[2]]
    })

    # 기존 데이터프레임과 새로운 데이터프레임을 concat으로 결합
    ext_df = pd.concat([ext_df, new_row], ignore_index=True)
    
    ext_df.to_csv(ext_file_path,mode="w", index=False)
    
    print("Save extinction")
    logger.info(f'Save extinction')
    

def extinc_print(c1_list: list = [0, 0, 0], c2_list: list = [0, 0, 0], alp_list: list = [0, 0, 0], select_color: str = ""):
    """Select an appropriate value among visibility by wavelength."""
    print("alp_list : ", alp_list)
    g_ext = round(alp_list[1], 1)

    if select_color == "red" : 
        visibility = visibility_print(alp_list[0])
    elif select_color == "green" : 
        visibility = visibility_print(alp_list[1])
    else:
        visibility = visibility_print(alp_list[2])

    return visibility

def visibility_print(ext_g: float = 0.0):
    """Print the visibility based on day/night time"""
    vis_value = 0
    cam_name = save_path_info.get_data_path('SETTING', 'camera_name')
    
    # 현재 시간이 낮인지 밤인지 판단
    now_time = time.time()
    dn_time = sun_observer.sun_observer(now_time)  # 'daytime' 또는 'nighttime'을 반환

    # 타겟 정보 가져오기
    _, _, _, distance, target_type= get_target(cam_name)
    
     # 낮 시간이라면 낮 타겟과 공통 타겟 중에서 최대 거리 선택
    if dn_time == "daytime":
        filtered_distance = [dist for dist, t_type in zip(distance, target_type) if t_type == "daytime" or t_type == "common"]
    else:
        # 밤 시간이라면 밤 타겟과 공통 타겟 중에서 최대 거리 선택
        filtered_distance = [dist for dist, t_type in zip(distance, target_type) if t_type == "nighttime" or t_type == "common"]
    
    # 최대 거리 설정
    try:
        max_value = float(max(filtered_distance))  # 최대 거리 값을 찾음
    except Exception as e:
        max_value = 20  # 기본 최대 거리값

    # 소산 계수를 바탕으로 시정 계산
    vis_value = 3.912 / ext_g
    if vis_value > max_value:
        vis_value = max_value
    elif vis_value < 0.01:
        vis_value = 0.01

    vis_value_str = f"{vis_value:.3f}"
    return vis_value_str
        
def get_target(camera_name: str):
    """Retrieves target information of a specific camera."""
    target_path = save_path_info.get_data_path('Path', 'target_csv_path')
    save_path = os.path.join(f"{target_path}/{camera_name}")
    
    if os.path.isfile(f"{save_path}/{camera_name}.csv"):
        target_df = pd.read_csv(f"{save_path}/{camera_name}.csv")
        target_df = target_df.sort_values(by=['distance'])
        
        target_name = target_df["target_name"].tolist()
        left_range = str_to_tuple(target_df["left_range"].tolist())
        right_range = str_to_tuple(target_df["right_range"].tolist())
        distance = target_df["distance"].tolist()

        # target_type이 존재하지 않는 경우 처리
        if "target_type" not in target_df.columns:
            print("target_type 컬럼이 존재하지 않습니다. 자동으로 설정 중입니다.")
            target_type = []
            for dist in distance:
                if dist < 20:
                    target_type.append("common")
                else:
                    target_type.append("daytime")
            
            # 기존 타겟 파일에 target_type 추가 저장
            target_df["target_type"] = target_type
            target_df.to_csv(f"{save_path}/{camera_name}.csv", mode="w", index=False)
            print(f"타겟 파일에 target_type 추가 완료: {save_path}/{camera_name}.csv")
        else:
            target_type = target_df["target_type"].tolist()  # 이미 target_type이 있는 경우

        return target_name, left_range, right_range, distance, target_type
    else:
        return [], [], [], [], []

def str_to_tuple(before_list):
    """A function that converts the tuple list, which is the location information of the stored targets, 
    into a string and converts it back into a tuple form."""
    tuple_list = [i.split(',') for i in before_list]
    tuple_list = [(int(i[0][1:]), int(i[1][:-1])) for i in tuple_list]
    return tuple_list