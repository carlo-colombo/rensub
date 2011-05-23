import shelve
d=shelve.open('episode_db')
for k in d:
    print k, d[k]
d.close()