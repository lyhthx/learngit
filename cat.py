# -*- coding:utf-8 -*-

import sys
import os
from time import strptime as TimeStrptime
import traceback

startTime = "2019-11-13-22-55-42"
endTime = "2019-12-13-22-55-42"


#  获取文件架的路径  #
def getFolderPath():
     return sys.argv[1]


def isOK_getParameter():
    if len(sys.argv) != 2:
        return False, ""
    else:
        inputPath = getFolderPath()
        return os.path.isdir(inputPath), inputPath

def autoReport():
    os.system("sh auto_report.sh")

if __name__ == '__main__':
    isDirFlag, inputPath = isOK_getParameter()
    if(isDirFlag):
        pass
    else:
        print("Error -- > Please enter the folder path!")
        sys.exit(0)

    print("Get Folder Path -->", inputPath)

    startTimeStrut = TimeStrptime(startTime, "%Y-%m-%d-%H-%M-%S")
    endTimeStrut = TimeStrptime(endTime, "%Y-%m-%d-%H-%M-%S")


    #  遍历车型的文件夹  #
    for carType in os.listdir(inputPath):
        carTypePath = os.path.join(inputPath, carType)
        if not os.path.isdir(carTypePath):
            print("Get A Not Dir Path -->", carTypePath)
            continue
        #  遍历车型和时间文件夹  #
        for carTypeWithTime in os.listdir(carTypePath):
            carTypeWithTimePath = os.path.join(carTypePath, carTypeWithTime)
            if not os.path.isdir(carTypeWithTimePath):
                print("Get A Not Dir Path -->", carTypeWithTimePath)
                continue
            #  遍历ONLINE文件夹  #
            for ONLINE in os.listdir(carTypeWithTimePath):
                ONLINEPath = os.path.join(carTypeWithTimePath, ONLINE)
                if not os.path.isdir(ONLINEPath):
                    print("Get A Not Dir Path -->", ONLINEPath)
                    continue

                #  遍历ONLINE文件夹  #
                for timeDirName in os.listdir(ONLINEPath):
                    timeDirNamePath = os.path.join(ONLINEPath, timeDirName)
                    if not os.path.isdir(timeDirNamePath):
                        print("Get A Not Dir Path -->", timeDirNamePath)
                        continue

                    try:
                        nowDirTime = TimeStrptime(timeDirName, "%Y-%m-%d-%H-%M-%S")
                        if (nowDirTime > startTimeStrut) and (nowDirTime < endTime):
                            autoReport()
                    except:
                        traceback.print_exc()