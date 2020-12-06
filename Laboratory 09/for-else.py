# Podejście z dodatkowym sprawdzeniem flagi
'''
flagfound = False
for i in mylist:
    if i == theflag:
        flagfound = True
        break
    process(i)

if not flagfound:
    raise ValueError("List argument missing terminal flag.")
'''
# Podejście z for-else
'''
for i in mylist:
    if i == theflag:
        break
    process(i)
else:
    raise ValueError("List argument missing terminal flag.")
'''
