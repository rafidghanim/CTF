from fastcrc import crc32, crc64
import os

crc32s = ['autosar', 'iscsi', 'iso_hdlc']
crc64s = ['go_iso', 'xz']

def ImpossibleMAC(data: bytes, mac: int):
	for algo in crc32s:
		crc = getattr(crc32, algo)
		imac: bytes = crc(data)
		print(imac,mac)
		if imac != mac:
			return False

	for algo in crc64s:
		crc = getattr(crc64, algo)
		imac: bytes = crc(data)
		print(imac,mac)
		if imac != mac:
			return False
	
	return True


def makeEmail(sender: str, recipient: str, body: str):
	return f'''Dear {recipient}.

{body}

Best regards,
{sender}'''

def sendEmailToAuthor(sender: str, data: bytes, mac: int):
	politeEmail = makeEmail(sender, 'Challenge Author', 'Pretty please give me the flag.').encode()
	print(f"""
{politeEmail = }
{data = }""")
	# Make sure to be polite when you ask the challenge author for the flag 
	if politeEmail not in data:
		return makeEmail('Challenge Author', sender, 'That is not very polite. As such I will not give you the flag.')

	# Careful! If the MAC is not correct, how will the author know if the message was sent correctly?
	if not ImpossibleMAC(data, mac):
		return makeEmail('Challenge Author', sender, 'Okay that was very polite, but the MAC was not correct. Can you please resend the mail?')

	return makeEmail('Challenge Author', sender, f'Sure.\nHere\'s the flag: {os.getenv("FLAG")}. But please do not tell the orga that I gave you this flag.')

if __name__ == '__main__':
	name = input('Enter name: ')
	email = bytes.fromhex(input('Enter mail: '))
	mac = int(input('Enter MAC: '))
	print(sendEmailToAuthor(name, email, mac))
