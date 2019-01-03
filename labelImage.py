from selenium import webdriver
import requests,shutil
import base64,time,os
from PIL import Image
import matplotlib.pyplot as plt
import subprocess,io
import tkinter as tk
from PIL import Image,ImageTk
from functools import partial

#ppath验证码路径
#firstImage第一个验证码，用来撑起来label,直接enter跳过
#香醋要创建labelImage文件夹用来存储打过标签的图片
current = 0
def tkLabelImg(ppath, firstImg):
    ppath = "verificationData"
    # ppath="gifData"
    fileList = os.listdir(ppath)
    window = tk.Tk()
    window.geometry("%dx%d+%d+%d" % (200, 100, 500, 500))
    photo0 = tk.PhotoImage(file=firstImg)  # file：t图片路径
    imgLabel = tk.Label(window, image=photo0)  # 把图片整合到标签类中
    imgLabel.pack(side=tk.LEFT)  # 自动对齐
    # 下一个图片
    # 这里是窗口的内容


    def getContent(self):
        global current
        current += 1
        url1 = ppath + "/" + fileList[current]
        im = Image.open(url1)
        im1 = ImageTk.PhotoImage(im)
        imgLabel['image'] = im1
        imgLabel.image = im1
        codeTxt = t.get()
        preImgSrc = ppath + "/" + fileList[current - 1]
        labelImagePname = "labelImg/" + codeTxt + ".png"
        if os.path.exists("labelImg/.png"):
            os.remove("labelImg/.png")
        try:
            os.rename(preImgSrc, labelImagePname)
        except:
            print("已有该文件"+labelImagePname)
        t.delete(0, 4)

    t = tk.Entry()  # 这里设置文本框高，可以容纳两行
    t.bind("<Return>", getContent)
    t.pack(side=tk.RIGHT)
    window.mainloop()

if __name__ == '__main__':
    ppath="verificationData"
    firstImage="xx.png"
    tkLabelImg(ppath,firstImage)