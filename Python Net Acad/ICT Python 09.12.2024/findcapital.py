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

# Gjej shtetitin sipas qytetit
qyteti = input("Vendos qytetit per te gjetur kryeqytetin:")
for k,v in shtetet.items():
    for m in shtetet.get(k):
        for o in shtetet.get(k).get(m):
            if o.get("emri") == qyteti:
                print(k)