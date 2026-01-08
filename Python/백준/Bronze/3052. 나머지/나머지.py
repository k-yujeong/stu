num_list = [int(input())for i in range(10)]

mod_list = []

for i in range(10):
    mod_list.append((num_list[i] % 42))

diff_mod = len(set(mod_list))   # set 중복 허용 X

print(diff_mod)