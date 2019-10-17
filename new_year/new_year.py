def generate_aswners_from_mask(mask):
    one_zero_binaries = []
    for i in range(2, len(mask)):
        aux_bin = '0b'
        aux_bin += mask[2:]
        aux_bin = list(aux_bin)
        aux_bin[i] = '0'
        aux_bin = "".join(aux_bin)
        one_zero_binaries.append(aux_bin)
    return one_zero_binaries


input_numbers = input()
input_numbers = input_numbers.split(" ")
input_numbers = list(map(int, input_numbers))

masks = []

a = input_numbers[0]
b = input_numbers[1]
a_sz = len(bin(a)[2:]) 
b_sz = len(bin(b)[2:])

for i in range(a_sz, b_sz+1):
    mask = ((1 << i) - 1)
    masks.append(bin(mask))


all_aswners = []

for i in masks:
   all_aswners = all_aswners + generate_aswners_from_mask(i)


final_aswners = []

for i in all_aswners:
    int_rep = int(i,2)
    if(int_rep < input_numbers[0] or int_rep > input_numbers[1] or i[2] == '0'):
        continue
    final_aswners.append(i)


print(len(final_aswners))