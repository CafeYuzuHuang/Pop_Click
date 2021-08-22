# -*- coding: utf-8 -*-
# Date: Aug. 22, 2021
# Author: SamH

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, askquestion
import threading
from time import sleep
import webbrowser
import pop_click


def OpenLink(url):
    """ 使用預設網路瀏覽器開啟網頁 """
    try:
        webbrowser.open_new(url)
    except Exception:
        msg = "非預期錯誤！\n發生於開啟連結：\n" + url
        showerror("不明錯誤", msg)


class MainWindow:
    """ 主視窗類別 """
    def __init__(self):
        """ 主視窗初始化 """
        # 建立視窗，tk物件實體化
        self.master = tk.Tk() # Toplevel widget
        self.master.protocol("WM_DELETE_WINDOW", self.quitloop)
        self.master.title("Pop Click")
        self.master.geometry("{}x{}+{}+{}".format(400, 300, 150, 150))
        
        # 框架建立，用於置放其他元件
        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand = 1, fill = "both")
        
        # 控制變數設定
        self.url = tk.StringVar()
        self.url.set(pop_click.Dst_Url)
        self.counts = tk.StringVar()
        self.counts.set('0')
        self.fun_handler = self.cc # function handler for threading
        
        # 元件
        self.rba = ttk.Radiobutton(self.master, text = "Pop Xi", \
                                   variable = self.url, \
                                   value = pop_click.Dst_Url)
        self.rba.place(relx = 0.1, rely = 0.1, \
                       relwidth = 0.4, relheight = 0.15)
        self.rbb = ttk.Radiobutton(self.master, text = "Pop Cat", \
                                   variable = self.url, \
                                   value = pop_click.Dst_Url2)
        self.rbb.place(relx = 0.5, rely = 0.1, \
                       relwidth = 0.4, relheight = 0.15)
        
        self.getcc_ttl = ttk.Label(self.master, text = "選擇點擊次數")
        self.getcc_ttl.place(relx = 0.1, rely = 0.35, \
                             relwidth = 0.4, relheight = 0.15)
        
        self.getcc = ttk.Combobox(self.master, textvariable = self.counts)
        self.getcc["values"] = ('64', '426', '1989', '4826', '8964', \
                                '48426', '198964')
        self.getcc["state"] = "readonly"
        self.getcc.place(relx = 0.5, rely = 0.35, \
                         relwidth = 0.4, relheight = 0.15)
        self.getcc.bind("<<ComboboxSelected>>", self.cc_update)
        
        self.btn_go = ttk.Button(self.master, text = "開始點擊！", \
                                command = self.th_run)
        self.btn_go.place(relx = 0.5, rely = 0.55, \
                          relwidth = 0.4, relheight = 0.15)
        self.btn_go["state"] = "disabled"
        
        self.drlink = ttk.Label(self.master, text = "取得 Chrome webdriver", \
                                foreground = "blue", \
                                background = "alice blue", \
                                cursor = "hand2", relief = "flat", \
                                font = ("Microsoft JhengHei UI", 9, "underline"))
        self.drlink.place(relx = 0.1, rely = 0.8, \
                          relwidth = 0.8, relheight = 0.15)
        self.drlink.bind("<Button-1>", lambda e: \
                         OpenLink("https://chromedriver.chromium.org/downloads"))
        
        # 外觀參數
        style = ttk.Style(self.master)
        style.configure("TFrame", 
                        background = "alice blue", 
                        foreground = "cornflower blue", 
                        font = ("Microsoft JhengHei UI", 12, "bold"))
        style.configure("TLabel", 
                        background = "alice blue", 
                        foreground = "cornflower blue", 
                        font = ("Microsoft JhengHei UI", 12, "bold"))
        """
        style.configure("TCombobox", 
                        background = "ivory", 
                        foreground = "dark slate blue", 
                        font = ("Microsoft JhengHei UI", 12))
        """
        style.configure("TButton", 
                        background = "alice blue", 
                        foreground = "cornflower blue", 
                        font = ("Microsoft JhengHei UI", 12, "bold"))
        """
        style.map('TButton', 
                  background = [('active', 'azure'), 
                                ('!active', '!disabled', 'alice blue'), 
                                ('disabled', 'gray')], 
                  foregroud = [('active', 'dark slate blue'), 
                               ('!active', '!disabled', 'cornflower blue'), 
                               ('disabled', 'navy')])
        """
        style.configure("TRadiobutton", 
                        background = "alice blue", 
                        foreground = "cornflower blue", 
                        font = ("Microsoft JhengHei UI", 12, "bold"))
        
    def cc_update(self, Event):
        """ 更新點擊參數 """
        if int(self.counts.get()) > 0:
            self.btn_go["state"] = "normal"
        # msg = "目前選擇的點擊次數為 " + self.counts.get()
        # showinfo(title = "參數更新", message = msg)
        
    def th_run(self):
        """ 使用多執行緒，fun_handler為一函式物件需被定義 """
        try:
            th = threading.Thread(target = self.fun_handler)
            th.setDaemon(True) # 守護執行緒
            th.start()
        except RuntimeError as e:
            showerror("執行緒錯誤", e)
        except Exception as e:
            showerror("執行緒不明錯誤", e)
        
    def cc(self):
        """ 執行網頁點擊！ """
        try:
            _counts = int(self.counts.get())
            assert _counts > 0
            pop_click.Main(counts = _counts, dst_url = self.url.get())
        except Exception as e:
            showerror("無效的點擊數設定", e)
        return None
    
    def mainloop(self, isfixedsize = False):
        """ 執行視窗主程式 """
        if isfixedsize: # 凍結視窗大小
            self.master.resizable(width = False, height = False)
        self.master.mainloop()
    
    def quitloop(self):
        """ 離開視窗主程式 """
        msgbox = askquestion("離開程式", "請確認是否離開？")
        if msgbox == "yes":
            self.master.destroy()
        # self.master.destroy()


if __name__ == "__main__":
    sleep(1)
    window = MainWindow()
    # window.mainloop(True) # Fixed window size
    window.mainloop() # Default: resizable window
    # window.quitloop()
    sleep(1)
# Done
