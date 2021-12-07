oct2bin = ['000', '001', '010', '011', '100', '101', '110', '111']
bin2hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
		   '0100': '4', '0101': '5', '0110': '6', '0111': '7',
		   '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
		   '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

octal = input()
binary = ''.join([oct2bin[int(digit)] for digit in octal])
hexrev = []
i = len(binary) - 4
while i >= 0:
	hexrev.append(bin2hex[binary[i:i+4]])
	i -= 4
if i != -4:
	last_digit = hex(int(binary[:4+i], 2))[2:]
	if last_digit != '0' or octal == '0': hexrev.append(last_digit);
print(''.join(reversed(hexrev)))
