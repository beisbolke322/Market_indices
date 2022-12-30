from flask import Flask, render_template, request, url_for, redirect
import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main_page.html")


@app.route("/lmi")
def first_indice():
    data_aug = yf.download("AUG1L.VS", start="2022-12-01", interval="1d")
    data_rsu = yf.download("RSU1L.VS", start="2022-12-01", interval="1d")
    data_vlp = yf.download("VLP1L.VS", start="2022-12-01", interval="1d")
    data_pzv = yf.download("PZV1L.VS", start="2022-12-01", interval="1d")
    data_zmp = yf.download("ZMP1L.VS", start="2022-12-01", interval="1d")
    data2 = [data_zmp, data_pzv, data_vlp, data_rsu, data_aug]
    data3 = data_aug["Close"]
    # for i in data2:
    #     data3.append(i["Close"])
    #     return data3
    skaiciai = data3
    data_aug["Close"].plot()
    data_rsu["Close"].plot()
    data_vlp["Close"].plot()
    data_pzv["Close"].plot()
    data_zmp["Close"].plot()
    plt.savefig("lmi_companies.png")

    return render_template("lmi.html", skaiciai=skaiciai)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
