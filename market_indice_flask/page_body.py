from flask import Flask, render_template
import yfinance as yf
import matplotlib
import datetime, math
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from prettytable import PrettyTable

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main_page.html")


@app.route("/lmi")
def first_indice():
    x = datetime.date.today()
    y = datetime.date.today() - datetime.timedelta(days=7)  # to automate so there are indefinite amount of days back
    data_aug = yf.download("AUG1L.VS", start="2023-01-16", interval="1d")
    data_rsu = yf.download("RSU1L.VS", start=y, interval="1d")
    data_vlp = yf.download("VLP1L.VS", start=y, interval="1d")
    data_pzv = yf.download("PZV1L.VS", start=y, interval="1d")
    data_zmp = yf.download("ZMP1L.VS", start=y, interval="1d")
    data1 = []
    # data2 = [data_zmp, data_pzv, data_vlp, data_rsu, data_aug]
    data3 = data_aug["Close"]
    data4 = data_rsu["Close"]
    data5 = data_zmp["Close"]
    data6 = data_vlp["Close"]
    data7 = data_pzv["Close"]
    # for i in data2:
    #     data1.append(i["Close"])
    #     return data1
    skaiciai = str(data3)
    last_close_aug = float(data3.iloc[-1])
    last_close_rsu = float(data4.iloc[-1])
    last_close_zmp = float(data5.iloc[-1])
    last_close_vlp = float(data6.iloc[-1])
    last_close_pzv = float(data7.iloc[-1])
    last_close_t = round((5*last_close_aug + 0.8*last_close_rsu + 1.15*last_close_zmp
                  + 0.3635*last_close_vlp + 1.3*last_close_pzv), 4)
    # previous indice value
    last_close_aug = float(data3.iloc[-2])
    last_close_rsu = float(data4.iloc[-2])
    last_close_zmp = float(data5.iloc[-2])
    last_close_vlp = float(data6.iloc[-2])
    last_close_pzv = float(data7.iloc[-2])
    last_close_y = round((5 * last_close_aug + 0.8 * last_close_rsu + 1.15 * last_close_zmp
                          + 0.3635 * last_close_vlp + 1.3 * last_close_pzv), 4)

    skaiciu_lent = PrettyTable()
    # skaiciu_lent.add_column("Date", ["2023-01-16", "2023-01-17", "2023-01-18", y, x])
    # skaiciu_lent.add_column("Closing price", ["0.4130", "0.4080", "0.4139", "0.4180", last_close])
    # skaiciu_lent.align = "c"
    # skaiciu_lent.get_string()

    # data_aug["Close"].plot()
    # data_rsu["Close"].plot()
    # data_vlp["Close"].plot()
    # data_pzv["Close"].plot()
    # data3.plot()
    # data4.plot()
    # data5.plot()
    # data6.plot(color='#c0cbc0')
    # data7.plot()
    plt.title("Lithuanian milk indice")
    plt.plot(["2023-01-25", "2023-01-26", "2023-01-27", "2023-01-28"], [9.8, 10.1, last_close_y, last_close_t],
             '#3AA44F')
    plt.xlabel("Days")
    graph = plt.axes(("2023-01-25", 9, 4, 3))
    graph.set_facecolor('#c0cbc0')
    plt.savefig("lmi_companies.png")
    disp_graph = plt.show()

    return render_template("lmi.html", skaiciai=skaiciai, skaiciu_lent=skaiciu_lent, last_close_aug=last_close_aug,
                           last_close_rsu=last_close_rsu, last_close_t=last_close_t, data1=data1, disp_graph=disp_graph)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
