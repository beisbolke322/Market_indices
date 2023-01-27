from flask import Flask, render_template
import yfinance as yf
import matplotlib
import datetime, math
matplotlib.use('Agg')
# import matplotlib.pyplot as plt
from prettytable import PrettyTable

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main_page.html")


@app.route("/lmi")
def first_indice():
    x = datetime.date.today()
    data_aug = yf.download("AUG1L.VS", start="2023-01-16", interval="1d")
    data_rsu = yf.download("RSU1L.VS", start=x, interval="1d")
    data_vlp = yf.download("VLP1L.VS", start=x, interval="1d")
    data_pzv = yf.download("PZV1L.VS", start=x, interval="1d")
    data_zmp = yf.download("ZMP1L.VS", start=x, interval="1d")
    # data2 = [data_zmp, data_pzv, data_vlp, data_rsu, data_aug]
    data3 = data_aug["Close"]
    data4 = data_rsu["Close"]
    # for i in data2:
    #     data4.append(i["Close"])
    #     return data4
    skaiciai = str(data3)
    last_close_aug = float(data3.iloc[-1])
    last_close_rsu = float(data4.iloc[-1])
    last_close = round((2*last_close_aug + 0.5*last_close_rsu))
    y = datetime.date.today() - datetime.timedelta(days=1)  # to automate so there are indefinite amount of days back
    skaiciu_lent = PrettyTable()
    skaiciu_lent.add_column("Date", ["2023-01-16", "2023-01-17", "2023-01-18", y, x])
    skaiciu_lent.add_column("Closing price", ["0.4130", "0.4080", "0.4139", "0.4180", last_close_aug])
    skaiciu_lent.align = "c"
    skaiciu_lent.get_string()

    # data_aug["Close"].plot()
    # data_rsu["Close"].plot()
    # data_vlp["Close"].plot()
    # data_pzv["Close"].plot()
    # data_zmp["Close"].plot()
    # plt.savefig("lmi_companies.png")

    return render_template("lmi.html", skaiciai=skaiciai, skaiciu_lent=skaiciu_lent, last_close_aug=last_close_aug,
                           last_close_rsu=last_close_rsu, last_close=last_close)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
