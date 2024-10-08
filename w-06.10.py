# start
import random

a: list[int] = [i for i in range(95, 105 + 1)]
print(a)

b: list[int] = [i for i in range(10, 20 + 1, 2)]
print(b)

c: list[bool] = []
for i in range(5):
    c.append(random.choice([True, False]))
print(c, end=" ")

c: list[bool] = [random.choice([True, False]) for i in range(5)]
print(c)

d: list[int] = []
for i in range(10):
    d.append(random.randint(1, 100))
print(d)

d: list[int] = [random.randint(1, 100) for i in range(10)]
print(d)

e: list[int] = []
for i in range(len(d)):
    if d[i] > 50:
        e.append(d[i])
print(e, end=" ")
print()

e: list[int] = [d[i] for i in range(len(d)) if d[i] > 50]
print(e)

f:list[int]=[ random.randint(1, 100)  for x in d  if x > 50]
print(f)
# ניסיתי חח אשמח להסבר בשיעור
# g:
g: list[str] = []
sentence: str = str(input("what is sentence ? "))
for i in range(len(sentence)):
    if not sentence[i] == "t" and not sentence[i] == " ":
        g.append(sentence[i])
print(g)

sentence: str = str(input("what is sentence ? "))
g: list[str] = [sentence[i] for i in range(len(sentence)) if not sentence[i] == "t" and not sentence[i] == " "]
print(g)

# h:
h:list[int]=[]
for i in range(10):
    h.append(random.randint(1,99+1))
print(h)

h:list[int]=[(random.randint(1,99+1)) for i in range (10)]
print(h)

h1:list[int]=[]
for i in range(len(h)):
    h1.append(h[i] % 10)
print(h1)

h1:list[int]=[(h[i] % 10)for i in range(len(h))]
print(h1)

# stop
