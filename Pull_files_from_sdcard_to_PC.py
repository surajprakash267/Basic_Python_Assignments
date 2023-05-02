# Q9. Pull all the videos from device to laptop. Hint:- (Use adb commands)
# Ans.

import subprocess
a= subprocess.call("adb pull /storage/sdcard1/TCS_Ninja_NQT_Repeat_Quants_Questions_-_Part_5(360p).mp4 D:\\test",shell=True)
print(a)