import sys
input = sys.stdin.readline

id_list = input()
id_list = list(id_list[2:-3].split('\", \"'))

report = input()
report = list(report[2:-3].split('\", \"'))

k = int(input())

solution(id_list, report, k)


def solution(id_list, report, k):
    answer = []
    
    warn_dict = {}
    report_list = []
    count = 0

    for item in report:
        try:
            index = warn_dict[item[1]]

        except:
            count += 1
            warn_dict[item[1]] = count
            index = count

        try:
            report_list[index].append(item[0])
        except:
            report_list[index] = [item[0]]

    for item in report_list:
        answer.append(len(set(item)))
    
    return answer


