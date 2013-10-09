q1 = 0
q2 = 0
q3 = 0
q4 = 0
on_x = 0
on_y = 0
i = 1
n = raw_input()
n = float(n)
q_list = []
while i <= n:
    dot_raw = raw_input()
    dot_xy = dot_raw.split(' ')
    dot_xy_2 = tuple(dot_xy)
    q_list.append(dot_xy_2)
    i += 1
j = 0
length = len(q_list)
'''
q_list[j][0] >> x point
q_list[j][1] >> y point
'''
while j <= length-1:
    if float(q_list[j][1]) == float(0):
        on_x += 1
        j += 1
    elif float(q_list[j][0]) == float(0):
        on_y += 1
        j += 1
    elif float(q_list[j][0]) > float(0) and float(q_list[j][1]) > float(0):
        q1 += 1
        j += 1
    elif float(q_list[j][0]) < float(0) and float(q_list[j][1]) > float(0):
        q2 += 1
        j += 1
    elif float(q_list[j][0]) < float(0) and float(q_list[j][1]) < float(0):
        q3 += 1
        j += 1
    elif float(q_list[j][0]) > float(0) and float(q_list[j][1]) < float(0):
        q4 += 1
        j += 1
print q1
print q2
print q3
print q4
print on_x
print on_y 
    
    
