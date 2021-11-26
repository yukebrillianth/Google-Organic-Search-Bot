# Google Search Traffic BOT

- Indonesia: Ini adalah blog untuk menghasilkan traffic dari google organic search.

- Translated By Google: This is a blog to generate traffic from google organic search.

## System

> if you are not using windows OS, replace the firefox driver (_geckodriver.exe_) with a driver that is compatible with your OS.

## How to install

1. Clone this repository

```shell
git clone https://github.com/yukebrillianth/Google-Organic-Search-Bot.git GOSB

cd GOSB
```

2. Install required packages

```shell
pip install -r ./requirements.txt
```

3. Edit proxy.json, fill with rotating proxy if you use rotating proxy
4. Edit config.json
5. Run main.py

```shell
py ./main.py
```

## Kamus

1. **_keyword_** = Keyword yang akan dicari
2. **_website_uri_** = Url artikel anda yang dicari
3. **_use_proxy_** = Menggunakan rotating proxy atau tidak
4. **_amount_** = Jumlah traffic (jika tidak menggunakan proxy)
5. **_headless_** = Menampilkan browser atau tidak
6. **_interval_** = Selang waktu
