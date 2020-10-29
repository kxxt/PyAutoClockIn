# PyAutoClockIn For SDUWH

这是一个用python编写的自动打卡程序，使用selenium框架。
> Made by a sduwh student for sduwh students.

## 使用方法

将学号写入users.txt,一行一个

```bash
pip3 install selenium
python3 clockin.py
```

如无错误则打卡成功

## 可选参数

打开`clockin.py`可以看到以下两个参数。

- `retrymax` : 为最大重试次数
- `printToConsole` : 为是否打印到控制台
- `silent` : 为是否静默运行 , 若要在服务器上运行请把此项设置为`True`
- `chromeBinaryPath` : 自己指定Chrome浏览器路径 , 常用于Windows下
- `logSucceededRecord` : 将成功打卡的记录也进行Log

## 应用场景

- 在电脑上手动运行来一键打卡
- 在电脑上设置定时任务打卡(在手机上不太好办)
- 部署到云服务器上自动定时打卡
- 修改程序给sduwh所有人打一遍卡（危）（手动滑稽）

## 打赏

给开发者投食：)

![打赏](sponsor-qrcode.png)