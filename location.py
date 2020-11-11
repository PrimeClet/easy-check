import operator
a = 2
x = {'us': 1, 'cmr': 12, 'nig': 2}
for k in x:
    x[k] = x[k] + 1
sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
out_dict = {}
for idx, (key, _) in enumerate(sorted_x):
    out_dict[key] = idx + 1
print(out_dict)
