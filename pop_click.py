# -*- coding: utf-8 -*-
# Date: Aug. 22, 2021
# Author: SamH

from os import getcwd, path
from random import random, randint
from time import sleep
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


if __name__ == "__main__": WD_Path = getcwd() # executed
else: WD_Path = path.dirname(__file__) # imported
WD_Path += "\\chromedriver.exe" # 使用的Webdriver所在路徑

Dst_Url = "https://popxi.click/"
Dst_Url2 = "https://popcat.click/"
Default_Counts = 8964


def BruteClicking(counts, dst_url):
    """ 網頁暴力點擊 """
    # 找尋 webdriver
    wd_path = ""
    win_path = ".\\chromedriver.exe"
    mac_path = "./chromedriver.exe"
    try:
        assert path.isfile(WD_Path) is True
        wd_path = WD_Path
    except:
        print("Webdriver not found! \nChecked path: ", WD_Path)
    if wd_path == "":
        try:
            assert path.isfile(win_path) is True
            wd_path = win_path
        except:
            print("Invalid path: '.\\chromedriver.exe', probably in Mac OS?")
    if wd_path == "":
        try:
            assert path.isfile(mac_path) is True
            wd_path = mac_path
        except:
            print("Invalid path: './chromedriver.exe', now exit function...")
            return None
    print("\n\nFind webdriver in: %s \n\n" % wd_path)
    # 找到webdriver之後，準備開啟網頁與點擊
    try:
        # PhantomJS support has been depreciated, so we use Chrome instead
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless') # Chrome瀏覽器開啟無頭模式
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options = options, 
                                  executable_path = wd_path)
        driver.implicitly_wait(3)
        driver.get(dst_url)
    except Exception as e:
        print(e)
        driver.close()
        return None
    try:
        sleep(2)
        lowlim = ord('a')
        uplim = ord('z')
        for _ in range(counts):
            k = chr(randint(lowlim, uplim))
            ActionChains(driver).send_keys(k).perform()
            # print("Send key: ", k)
            sleep(random()*0.1) # wait 0.0 to 0.1 s
    except Exception as e:
        print(e)
    finally:
        print("BruteClicking finishes successfully.")
        print("Clicks = ", counts)
        driver.close()
    return None

def Main(counts, dst_url):
    """ 主函式 """
    t_start = dt.datetime.now()
    BruteClicking(counts, dst_url)
    t_end = dt.datetime.now()
    print("Total ellapsed time is: ", t_end - t_start)
    return None

if __name__ == "__main__":
    Main(counts = 10, dst_url = Dst_Url) # 程式測試
    # Main(counts = Default_Counts, dst_url = Dst_Url) # 8964下，約需要10分鐘
# Done
