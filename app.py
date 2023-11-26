from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dl = float(request.form['dl'])
        pz = float(request.form['pz']) / 100
        rg = int(request.form['rg'])
        sl = int(request.form['sl'])
        zb = float(request.form['zb'])
        lr = 0
        dj = 0
        result = []
        for i in range(0, 13):
            lr = dl * (1 + pz * i) * sl - sl * dj - rg*zb
            while lr > 0:
                dj = dj + 1
                lr = dl * (1 + pz * i) * sl - sl * dj - rg
            else:
                result.append((i, dj))
        return render_template_string('''
            <form method="post">
                大楼价格： <input type="number" name="dl" value="{{ dl }}" required><br>
                品质加成： <input type="number" name="pz" step="0.01" value="{{ pz }}" required><br>
                人工费： <input type="number" name="rg" value="{{ rg }}" required><br>
                数量： <input type="number" name="sl" value="{{ sl }}" required><br>
                人工费占比： <input type="number" name="zb" step="0.01" value="{{ zb }}" required><br>
                <input type="submit" value="计算">
            </form>
            {% for i, dj in result %}
                q {{ i }} 交易价格 {{ dj }}<br>
            {% endfor %}
        ''', dl=dl, pz=pz, rg=rg, sl=sl, zb=zb, result=result)
    return render_template_string('''
        <form method="post">
            大楼价格： <input type="number" name="dl" required><br>
            品质加成： <input type="number" step="0.01" name="pz" required><br>
            人工费： <input type="number" name="rg" required><br>
            数量： <input type="number" name="sl" required><br>
            人工费占比： <input type="number" step="0.01" name="zb" required><br>
            <input type="submit" value="计算">
        </form>
    ''')

if __name__ == '__main__':
    app.run()
