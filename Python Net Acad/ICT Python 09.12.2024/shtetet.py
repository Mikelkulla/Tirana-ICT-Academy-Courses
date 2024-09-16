shtetet = {
    "angli": {
        "qytetet": [
            {
                "emri": "londer",
                "popullsia": 8900000,
                "siperfaqe": 1572,
                "kryeqytet": True
            },
            {
                "emri": "manchester",
                "popullsia": 553230,
                "siperfaqe": 115.6,
                "kryeqytet": False
            },
            {
                "emri": "liverpul",
                "popullsia": 491500,
                "siperfaqe": 111.8,
                "kryeqytet": False
            }
        ]
    },

    "franca": {
        "qytetet": [
            {
                "emri": "paris",
                "popullsia": 2161000,
                "siperfaqe": 105.4,
                "kryeqytet": True
            },
            {
                "emri": "marseje",
                "popullsia": 861635,
                "siperfaqe": 240.62,
                "kryeqytet": False
            },
            {
                "emri": "lion",
                "popullsia": 516092,
                "siperfaqe": 47.87,
                "kryeqytet": False
            }
        ]
    },

    "gjermania": {
        "qytetet": [
            {
                "emri": "berlin",
                "popullsia": 3669491,
                "siperfaqe": 891.8,
                "kryeqytet": True
            },
            {
                "emri": "hamburg",
                "popullsia": 1841179,
                "siperfaqe": 755.2,
                "kryeqytet": False
            },
            {
                "emri": "mynih",
                "popullsia": 1471508,
                "siperfaqe": 310.7,
                "kryeqytet": False
            }
        ]
    },

    "italia": {
        "qytetet": [
            {
                "emri": "rome",
                "popullsia": 2873000,
                "siperfaqe": 1285,
                "kryeqytet": True
            },
            {
                "emri": "milano",
                "popullsia": 1366180,
                "siperfaqe": 181.8,
                "kryeqytet": False
            },
            {
                "emri": "napoli",
                "popullsia": 962003,
                "siperfaqe": 119.02,
                "kryeqytet": False
            }
        ]
    }
}
# Printimi i kryeqytetit te france me .get()
"""for j in range(len(shtetet.get("franca").get("qytetet"))):
    if shtetet.get("franca").get("qytetet")[j].get("kryeqytet") == True:
        print(shtetet.get("franca").get("qytetet")[j].get("emri"))"""

"""# Printimi i kryeqytetit te frances me indeks
for i in range(len(shtetet["franca"]["qytetet"])):
    if shtetet["franca"]["qytetet"][i]["kryeqytet"] == True:
        print(shtetet["franca"]["qytetet"][i]["emri"])"""
###############################################################################
# Gjej popullsine totale te nje shteti
def popullsia():
    """ Printimi i totalit te popullsise se qyteteve """
    totalPopullsi = 0
    shteti = input("Vendos emrin e shtetit")
    for i in range(len(shtetet.get(shteti).get("qytetet"))):
        totalPopullsi += shtetet.get(shteti).get("qytetet")[i].get("popullsia")
    print("Popullsia totale e", shteti.upper(), "eshte", totalPopullsi)
# Gjej siperfaqen totale te nje shteti
def siperfaqja_e_qyteteve():
    """ Printimi i totalit te siperfaqes se qyteteve """
    totalSip = 0
    shteti = input("Vendos emrin e shtetit")
    for i in range(len(shtetet.get(shteti).get("qytetet"))):
        totalSip += shtetet.get(shteti).get("qytetet")[i].get("siperfaqe")
    print("Siperfaqja totale e", shteti.upper(), "eshte", totalSip)
    return shteti, totalSip
# Gjej siperfaqen mesatare te qyteteve te nje shteti
def siperfaqja_mesatare():

    shteti, totalSip = siperfaqja_e_qyteteve()
    print("Siperfaqja mesatare e qyteteve te", shteti.upper(), "eshte", totalSip/len(shtetet.get(shteti).get("qytetet")))
# Printo kryeqytetin e shtetit
def kryeqyteti_shteti():
    """ Printimi i kryeqytetit te nje shteti"""
    shteti = input("Vendos emrin e shtetit")
    for j in range(len(shtetet.get("franca").get("qytetet"))):
        if shtetet.get("franca").get("qytetet")[j].get("kryeqytet") == True:
            print("Kryeqyteti i", shteti.upper(), "eshte", shtetet.get("franca").get("qytetet")[j].get("emri"))
# Gjej shtetitin sipas qytetit
def shteti_i_qytetit():
    # Gjej shtetitin sipas qytetit
    qyteti = input("Vendos qytetit per te gjetur shtetin:")
    for k, v in shtetet.items():
        for m in shtetet.get(k):
            for o in shtetet.get(k).get(m):
                if o.get("emri") == qyteti:
                    print("Shteti i",qyteti,"eshte",k)
# Gjej popullsine totale te nje shteti

popullsia()
siperfaqja_mesatare()
kryeqyteti_shteti()
shteti_i_qytetit()