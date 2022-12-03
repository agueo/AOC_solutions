from typing import List
from copy import deepcopy

with open('day3_input.txt') as f:
    input_data = [int(input.strip()) for input in f]

#### PART 1 ####
def calc_gamma(t: List, bit_len: int) -> int:
    gamma = 0
    for i in range(0,bit_len):
        # Get each bit in the given pos
        bits = list(map(lambda n: 1 if (n >> i) & 0x1 == 1 else 0, t))
        gamma |= (1 << i) if bits.count(1) > bits.count(0) else 0
    return gamma

def calc_epsilon(gamma: int, bit_len: int) -> int:
    return ~gamma + 2**bit_len

gamma = calc_gamma(input_data, 12)
epsilon = calc_epsilon(gamma, 12)
print(gamma * epsilon)

#### PART 2 ####
def calc_oxy(t: List, start: int) -> list:
    # Get each bit in the given pos
    bits = list(map(lambda n: 1 if (n >> start) & 0x1 == 1 else 0, t))

    # if there are more 1's keep them, otherwise keep the 0s
    to_keep = 1 if bits.count(1) >= bits.count(0) else 0
    filtered_list = [item for item in t if ((item >> start) & 0x1) == to_keep]
    return filtered_list

def calc_c02(t: List, start: int) -> list:
    # Get each bit in the given pos
    bits = list(map(lambda n: 1 if (n >> start) & 0x1 == 1 else 0, t))
    # if there are more 1's keep the 0s, otherwise keep the 1s
    to_keep = 0 if bits.count(1) >= bits.count(0) else 1
    filtered_list = [item for item in t if ((item >> start) & 0x1) == to_keep]
    return filtered_list

oxygen_list = deepcopy(input_data)
co2_list = deepcopy(input_data)

for i in range(11,-1,-1):
    if len(oxygen_list) != 1:
        oxygen_list = calc_oxy(oxygen_list,i)
    if len(co2_list) != 1:
        co2_list = calc_c02(co2_list, i)

print(f'{oxygen_list[0]} * {co2_list[0]} = {oxygen_list[0] * co2_list[0]}')




