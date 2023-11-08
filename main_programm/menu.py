import pygame
import pyautogui

screen_width, screen_height = pyautogui.size()  # 获取屏幕分辨率
menu_width, menu_height = screen_width, screen_height # 为菜单的长宽
test_width, test_height = 600,400 # 用于测试用

def DrawMainMenu():
    pass



def CreateWindow():
    pygame.init() # 初始化组件
    pygame.display.set_caption("")