def foo(tpl,a):
    if not (a in tpl):
        return tpl
    else:
        k=tpl.index(a)
        return tuple(list(tpl)[0:k]+list(tpl[k+1:]))

print(foo((1,2,3,4,2),2))