#密碼重試程式
password = "a123456"
i = 3
while i > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break
	elif pwd != password:
		print('密碼錯誤!', '還有', i - 1, '次機會')
		i = i - 1
