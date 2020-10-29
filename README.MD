# PyAutoClockIn
这是一个用python编写的自动打卡程序，使用selenium框架

## 使用方法
将学号写入users.txt,一行一个
```bash
pip3 install selenium
python3 clockin.py
```
如无错误则打卡成功

## 可选参数
打开`clockin.py`可以看到以下两个参数。
```python
retrymax=2
printToConsole=True
```
- `retrymax`为最大重试次数
- `printToConsole`为是否打印到控制台

## 应用场景
- 在电脑上手动运行来打卡
- 在电脑、手机上设置定时任务打卡
- 部署到云服务器上自动定时打卡
- 修改程序给sduwh所有人打一遍卡（危）（手动滑稽）