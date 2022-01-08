import subprocess as sb


class WIFI:
	def __init__(self):
		self.command = "netsh wlan show profile"
		self.names = self._names()
		self._password()
	def _names(self) -> list:
		return [x.split(':')[1].strip() for x  in sb.getoutput(self.command).split('\n') if 'All User Profile' in x]


	def _password(self) -> list:
		self.pwd_ = []
		for name in self.names:	
			result = sb.getoutput(f'{self.command} {name} key=clear').split('\n')
			password = [x.split(':')[1].strip() for x  in result if 'Key Content' in x]
			password = ['<blank>'] if not password else password
			self.pwd_.append(password[0])
		return self.pwd_

	def getNames(self) -> list:
		return self.names

	def getPasswords(self) -> list:
		return self.pwd_

wifi = WIFI()
names=wifi.getNames()
passwords=wifi.getPasswords()
for name, password in zip(names, passwords):
	print(f"{name}:{password}")