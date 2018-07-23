import pickle

f = open('players.bin', 'wb')
data = {"baseball": 9}
pickle.dump(data, f)
f.close()

f = open('players.bin', 'rb')
data = pickle.load(f)
f.close()
print(data)


with open("players.bin","wb") as f:
    pickle.dump({"baseball": 9})
    pickle.dump({"soccer": 11})
    pickle.dump({"basketball": 5})

with open("players.bin","rb") as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))

