obfs_flag = list("dSoo{}o_lft_pk_chchbSi_laeS_")
parts = [
    20,
    0,
    24,
    18,
    3,
    27,
    11,
    13,
    23,
    12,
    14,
    21,
    9,
    26,
    17,
    25,
    15,
    6,
    7,
    22,
    2,
    8,
    5,
    19,
    4,
    16,
    1,
    10,
]

flag_dict = dict(zip(parts, obfs_flag))
flag_dict = dict(sorted(flag_dict.items()))

flag = ""
for char in flag_dict.values():
    flag += char

print(flag)
