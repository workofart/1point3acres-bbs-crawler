# coding=utf-8
import csv, itertools as it

with open ('result.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        writer = csv.writer(f2, delimiter='|')
        for key, group in it.groupby(f, lambda line: line.startswith('------------------------------\n')):
            if not key:
                group = list(group)
                if (len(group) >= 12):
                    row = []
                    group = [item.decode('gbk') for item in group];

                    row.append(group[0].encode('utf-8'))
                    row.append(group[1].encode('utf-8'))
                    row.append(group[2].replace(u'背景见定位贴:', ' ').encode('utf-8'))
                    row.append(group[3].replace(u'本科:', ' ').encode('utf-8'))
                    row.append(group[4].replace(u'研究生:', ' ').encode('utf-8'))
                    row.append(group[5].replace(u'T单项和总分:', ' ').encode('utf-8'))
                    row.append(group[6].replace(u'G单项和总分:', ' ').encode('utf-8'))
                    row.append(group[7].replace(u'sub专业和分数:', ' ').encode('utf-8'))
                    row.append(group[8].replace(u'背景的其他说明（如牛推等）:', ' ').encode('utf-8'))
                    row.append(group[9].replace(u'提交时间:', ' ').encode('utf-8'))
                    row.append(group[10].replace(u'结果学校国家、地区:', ' ').encode('utf-8'))
                    row.append(group[11].replace(u'查到status的方式:', ' ').encode('utf-8'))

                    writer.writerow(row)