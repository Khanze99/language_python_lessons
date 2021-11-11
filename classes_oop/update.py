import shelve

db = shelve.open('persondb')

for key in sorted(db.keys()):
    print(key, '\t=>', db[key])


sue = db['Sue Jones']
sue.give_raise(.10)
db['Sue Jones'] = sue
db.close()