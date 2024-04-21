from flask import Flask, render_template, request

app = Flask(__name__)

def converter(num):
    dec_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_num = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ''
    i = 0
    while num > 0:
        for x in range(num // dec_num[i]):
            result += rom_num[i]
            num -= dec_num[i]
        i += 1
    return result


@app.route("/")
def index():
    return render_template("index.html", developer_name="Seydan Gülyeşil")

@app.route("/conv", methods=["POST"])
def calculate():
    number_decimal = request.form.get("number")
    if number_decimal.isdigit() and 1<= int(number_decimal) <=3999:
        number_decimal = int(number_decimal)
        return render_template("result.html", number_decimal=number_decimal, number_roman=converter(number_decimal), developer_name='Seydan Gülyeşil')
    else:
        return render_template("index.html", not_valid = True, developer_name="Seydan Gülyeşil")

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
