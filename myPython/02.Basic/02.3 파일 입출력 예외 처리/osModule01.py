import os   #os 모듈을 사용

myfolder = 'd:\\'
newpath = os.path.join(myfolder, 'hello')

try:
    # mkdir : make directory
    os.mkdir(path=newpath)

    for idx in range(1, 11):
        newfile = os.path.join(newpath, 'somefolder' + str(idx).zfill(2))
        # .zfill(2)는 남는 자리에 0으로 채움 ex)str(1).zfill(3)은 001
        os.mkdir(path=newfile)
except FileExistsError:
    print('해당 디렉토리가 이미 존재합니다.')

print('fin')
