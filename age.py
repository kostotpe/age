#年齡測試程式(包含第一項回答驗證的指令raise)
driving = input('請問你是否開過車: ')
if driving != '是' or driving !='否':
    print('請輸入是或否')
    raise SystemExit
age = input('請問你的年齡: ')
age = int(age)
if driving == '是':
    if age >= 18:
        print('你通過測驗')
    else:
        print('死屁孩去死')
elif driving == '否':
    if age < 18:
        print('你很乖')
    else:
        print('去考個駕照吧')