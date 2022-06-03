n = int(input())
k_list = [[] for _ in range(101)]
e_list = [[] for _ in range(101)]
m_list = [[] for _ in range(101)]
name_list = [[] for _ in range(101)]

for _ in range(n):
    data = list(input().split())
    for i in range(1, 4):
        data[i] = int(data[i])

    k_list[data[1]].append((data[0], data[1], data[2], data[3]))

for i in range(1, 101):
    if len(k_list[i]) >= 2:
        for student in k_list[i]:
            e_list[student[2]].append(student)

for i in range(1, 101):
    if len(e_list[i]) >= 2:
        for student in e_list[i]:
            m_list[student[3]].append(student)

for i in range(1, 101):
    if len(m_list[i]) >= 2:
        m_list[i].sort(key = lambda x: x[0])

for i in range(100, 0, -1):
    if len(k_list[i]) >= 2:
        for j in range(1, 101):
            if len(e_list[j]) >= 2:
                for k in range(100, 0, -1):
                    if len(m_list[k]) >= 2:
                        for student in m_list[k]:
                            print(student[0])
                    elif len(m_list[k]) == 1:
                        print(m_list[k][0][0])
            elif len(e_list[j]) == 1:
                print(e_list[j][0][0])
    elif len(k_list[i]) == 1:
        print(k_list[i][0][0])