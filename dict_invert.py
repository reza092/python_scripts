def dic_invert(d):
    new_d = dict()
    for k,v in d.items():
        new_d.setdefault(v,list()).append(k)
    return new_d

d = {4:True, 2:True, 0:True}
y = dic_invert(d)