import random
from flask import Flask
app = Flask(__name__)
@app.route('/')
def generate():
    sessiz = list("llllkttnptp")
    sesli = list("ioaooaooii")
    s = "oki"
    rand = random.randint(2,4)
    for i in range(rand):
        r2 = random.randint(1,100)
        if r2 % 2 == 0:
            a = random.choice(sessiz) + random.choice(sessiz)
        else:
            a = random.choice(sessiz)
            
        if a[-1] == 'l':
            b = 'o'
        elif a[-1] == 't':
            b = 'i'
        else:
            b = random.choice(sesli)
        s += a + b
    return s


if __name__ == '__main__':
    app.run(host='0.0.0.0')
