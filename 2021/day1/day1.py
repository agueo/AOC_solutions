with open('input.txt') as f:
    data = [int(num) for num in f]

increased = 0
prev_num = data[0]
for num in data:
    if prev_num < num:
        increased += 1
    prev_num = num

print(increased)

sum_increased = 0
prev_sum = sum(data[0:3])
for i,num in enumerate(data):
    try:
        cur_sum = sum(data[i:i+3])
        if cur_sum > prev_sum:
            sum_increased += 1
        prev_sum = cur_sum
    except Exception as e:
        print(str(e))
        break

print(sum_increased)
