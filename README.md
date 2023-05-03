# Knowledge Base trained with RASA Platform

## INTERACTIVE

- pengajian
- solat
- obat
- penyakit

## NON INTERACTIVE

- reminder kegiatan
- ulang tahun
- lagu kesukaan

## CATATAN

- nlu di perbanyak
- ketika selesai langsung mati
- tidak bisa menampilkan object representation lebh dari 5

## COBA TTS dan STT

- buka 3 terminal
- terminal 1 run `bot_speech.py`
- terminal 2 run `rasa run actions`
- terminal 3 run `rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml`

## MENJALANKAN RASA MODEL

- terminal 1 run `rasa run actions`
- terminal 2 run `rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml`
- terminal 3 run `rasa run --enable-api --cors "*"`

## MENCOBA INTERAKSI LEWAT TERMINAL

- terminal 1 run `rasa run actions`
- terminal 2 run `rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml`
- terminal 3 run `rasa shell`

## DOKUMENTASI

- <https://drive.google.com/drive/folders/1L3cDgHGiyxP_GpPCTKIYgpFclBDEPYd5?usp=sharing>

### CATATAN INSTALASI

- semua perintah/command dapat dijalankan langsung lewat terminal pada Visual Studio Code
- pastikan versi Python tidak lebih dari Python 3.10. Untuk cek versi python, jalankan `python -V` atau `python3 -V`
- pastikan RASA Platform sudah terpasang. jalankan `rasa help` untuk cek apakah sudah terpasang
- jika belum terpsang, jalankan `pip3 install rasa`
- setelah _pull_ dari repository, jalankan `pip install -r requirements.txt` untuk menginstall _packages_ tambahan yang dipakai pada model ini, ke komputer/laptop yang dipakai
- **Linux/UNIX dengan python 3.10:** jika muncul error seperti di bawah ini ketika menjalankan `rasa run actions`, jalankan `sudo apt-get install python3-tk python3-dev`

  `NOTE: You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev`

- jika muncul error `punkt not found`, jalankan `python`. setelah itu, akan masuk ke python environment melalui terminal (barisnya dimulai dengan ">> " tanpa petik).
- masih di dalam python environment, jalankan `import nltk`, kemudian jalankan `nltk.download("punkt")`
- jika sudah selesai, keluar dari python environment dengan menjalankan `exit()`
- model rasa terbaru butuh minimal versi rasa 3.5.0 , untuk upgrade ke latest version (3.5.4) : `pip3 install --upgrade rasa`
- untuk upgrade ke versi spesifik, misal versi 3.5.0: `pip3 install rasa==3.5.0`
- cek versinya di <https://pypi.org/project/rasa/#history>

#### contoh menjalankan python environment pada linux

```bash
heydarlaptop@LENOVO-HEYDAR:~/Documents/knowledge-base-robot-lansia$ python3
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import nltk
>>> nltk.download("punkt")
[nltk_data] Downloading package punkt to
[nltk_data]     /home/heydarlaptop/nltk_data...
[nltk_data]   Unzipping tokenizers/punkt.zip.
True
>>> exit()
```
