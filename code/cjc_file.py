#This file is from work at the CJC.
import binascii


#
#Look at hex code of wave file:
#
# How is hex code designed?


#n represents the number of hex values you want
def capture_hex_into_list(filename, n):
	with open(filename, 'rb') as f:
		content = f.read()
	hex_file = binascii.hexlify(content)
	hex_file = hex_file.decode("utf-8")
	hex_list = []
	for i in range(n):
		hex_list.append(hex_file[2*i] + hex_file[2*i+1])

	print("first four represent ASCII characters 52 49 46 46 is RIFF:")
	for i in range(4):
		print(hex_list[i])
	
	print('next four bytes are the chunk size "little endian?"')
	for i in range(4,8):
		print(hex_list[i])

	print('next 8 bytes represent ascii characters again: 57 41 56 45 is WAVE, 66 6d 74 20 is fmt')
	for i in range(8,16):
		print(hex_list[i])
	
	print('next 4 represent the chunk size, "little endian". More intricate than expected.')
	for i in range(16,20):
		print(hex_list[i])
	
	print('next 2 bytes represent audio format 01 00 is PCI')
	for i in range(20,22):
		print(hex_list[i])

	
	print('next 2 bytes represent the number of audio channels 02 00 is 2 channels')
	for i in range(22,24):
		print(hex_list[i])

	
	print('The next 4 bytes represent the sample rate')
	for i in range(24,28):
		print(hex_list[i])


	print('The next 4 bytes represent the byte rate(little endian)')
	for i in range(28,32):
		print(hex_list[i])


	








	return hex_list

def explain_hex_WAV(hex_list):
	print("first four represent ASCII characters 52 49 46 46 is RIFF:")
        for i in range(4):
                print(hex_list[i])

        print('next four bytes are the chunk size "little endian?"')
        for i in range(4,8):
                print(hex_list[i])

        print('next 8 bytes represent ascii characters again: 57 41 56 45 is WAVE, 66 6d 74 20 is fmt')
        for i in range(8,16):
                print(hex_list[i])

        print('next 4 represent the chunk size, "little endian". More intricate than expected.')
        for i in range(16,20):
                print(hex_list[i])

        print('next 2 bytes represent audio format 01 00 is PCI')
        for i in range(20,22):
                print(hex_list[i])


        print('next 2 bytes represent the number of audio channels 02 00 is 2 channels')
        for i in range(22,24):
                print(hex_list[i])


        print('The next 4 bytes represent the sample rate')
        for i in range(24,28):
                print(hex_list[i])

        print('The next 4 bytes represent the byte rate')
        for i in range(28,32):
                print(hex_list[i])

        print('The next 2 bytes represent the block align, also known as the number of bytes in a frame.')
        for i in range(32,34):
                print(hex_list[i])

        print('The next 2 bytes represent the bits per sample, 10 00 is 16')
        for i in range(34,36):
                print(hex_list[i])


	print('The next 4 bytes should say 64 61 74 61, which means data')
	for i in range(36,40):
		print(hex_list[i])


	print('after this you need 4 bytes representing your chunk 2 size')
	for i in range(40,44):
		print(hex_list[i])

	print('after this you should have the data stream')


	







def main():
	print(capture_hex_into_list('100475__iluppai__saxophone-weep.wav',20))

main()

