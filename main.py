def replace_string_reverse(my_string: str, num: int) -> str:
    if num == 0:
        return my_string
    string_in_reverse = my_string[:-num] + "B" * num
    return string_in_reverse


def replace_string_forward(input_string: str, num: int) -> str:
    string_forward = input_string
    string_forward = "B" * num + string_forward[num:]
    return string_forward


def replace_string_to_a(string: str, num: int) -> str:
    replaced_string = string[:num] + "A" + string[num + 1 :]
    return replaced_string


def string_ab(n: int, k: int) -> list:
    dap_an = []
    dap_an_dung = []
    full_a_string = "A" * n
    dap_an.append(full_a_string)
    for i in range(n - k + 1):
        subject_string = full_a_string
        subject_string = replace_string_reverse(subject_string, (n - k) - i)
        subject_string = replace_string_forward(subject_string, i)
        dap_an.append(subject_string)

    for i in dap_an:
        for j in range(len(i)):
            if i[j] == "B":
                dap_an.append(replace_string_to_a(i, j))
    dap_an = list(set(dap_an))
    for i in dap_an:
        if "A" * (k + 1) not in i and i.count("A" * k) == 1:
            dap_an_dung.append(i)
    return sorted(dap_an_dung)


print(string_ab(2, 1))
