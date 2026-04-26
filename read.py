import datetime

date = datetime.date.today()
with open("log.txt", "w", encoding="utf-8") as f:
    f.write(f"Hello, Ryohta!\nToday is {date}.")

while True:
    text = str(input("メモ(`exit`で終了)："))
    if text == "exit":
        break
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{text}")

with open("log.txt", "r", encoding="utf-8") as f:
    print(f.read())