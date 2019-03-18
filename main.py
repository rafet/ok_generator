from flask import Flask
arr = Flask(__name__)
@app.root('/')
def generate():
    sessiz = list("llllkmttnptp")
    sesli = list("ioaooaooii")
    s = "oki"
    rand = random.randint(1,3)
    for i in range(rand):
        r2 = random.randint(1,100)
        if r2 % 2 == 0:
            a = random.choice(sessiz) +random.choice(sessiz)
        else:
            a = random.choice(sessiz)
        if a[-1] == 'l':
            b='o'
        else:
            b = random.choice(sesli)
        s+=a+b
    return s


if name == '__main__':
    app.run(host='0.0.0.0')
