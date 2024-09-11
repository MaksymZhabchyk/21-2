val = [1, "hello", 3.14, True, [1, 2, 3], 10, 20, 30]

data_type = [type(item) for item in val]
type_count = {}

for t in data_type:
    if t in type_count:
        type_count[t] += 1
    else:
        type_count[t] = 1

m_c_type = None
m_c_count = 0

for t, count in type_count.items():
    if count > m_c_count:
        m_c_type = t
        m_c_count = count



print("Тип даних, який зустрічається найчастіше:", m_c_type)
print("Кількість появ:", m_c_count)