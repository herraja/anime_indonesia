# MyAnimeList Indonesia

Proyek ini merupakan replika dari website yang sudah ada bernama [MyAnimeList.net](https://www.myanimelist.net/) yang saya buat menggunakan bahasa pemrograman Python dan web framework Django.

## Latar Belakang

Proyek ini saya buat untuk tugas perkuliahan mobile programming. Sebenarnya platform aplikasi ini nantinya tidak berjalan atau berbentuk sebagai aplikasi web. Namun karena sempat mengalami miskomunikasi, jadi proyek ini tidak selesai sampai pada akhir kuliah mobile programming. Dan sekarang proyek aplikasi ini saya lanjutkan sendiri diluar kuliah, hanya sebagai portofolio proyek pribadi saja.

-----

## Instalasi

Untuk ikut berkolaborasi mengembangkan proyek ini, silahkan lakukan git clone atau download menjadi zip pada halaman Github. Pastikan jika kamu juga sudah menginstal Python versi 3 di komputer atau laptopmu.

### Siapkan Workspace

Buat direktori bernama `anime-indo` pada drive yang kamu inginkan (misalnya C, D, atau E pada OS Windows). OS lainnya bisa menyesuaikan saja dimana biasanya menaruh file pribadi dan proyek.

Dibawah ini adalah contoh struktur direktori milik saya

```console
D:\mobile_development\anime-indonesia|____animelist\
                                     |____api\
                                     |____artikel\
                                     |____backup\
                                     |____Env\
                                     |____myanimelist\
                                     |____statics\
                                     |____templates\
                                     |____.gitignore
                                     |____manages.py
                                     |____Readme.md
                                     |____requirements.txt
```

Setelahnya kamu bisa melakukan pull menggunakan **git pull**, atau mengekstrak file zip jika kamu download menjadi zip. Tempatkan pada direktori anime-indo yang sudah dibuat.

### Virtual Environment Python

Setelah sudah mendownload project, kamu perlu membuat virtual enviroment Python untuk menginstal modul yang dibutuhkan termasuk web framework Django. Dibawah ini caranya :

1. Buat virtual environment melalui terminal / cmd
   
   ```console
   D:\mobile_development\anime-indonesia> python -m venv Env
   ```
   Maka akan muncul suatu folder bernama ```Env``` di dalam workspace kita ```anime-indonesia```

2. Aktifkan mode virtual environment dengan perintah seperti ini
   
    ```console
    # Sebelum di aktifkan
    D:\mobile_development\anime-indonesia> Env\Scripts\activate

    # Setelah di aktifkan
    (Env) D:\mobile_development\anime-indonesia>
    ```

3. Selanjutnya adalah menginstal modul Python yang sesuai untuk proyek ini. Supaya kita bisa menginstal bersamaan, maka pastikan file bernama `requirements.txt` ada di dalam folder ini.
   
4. Ketikkan perintah ini untuk mulai menginstal modul Python
   
   ```console
   pip install -r requirements.txt
   ```

5. Jika sudah selesai dan tidak mendapati pesan Error, selanjutnya periksa modul yang terinstal dengan perintah `pip list` maka akan tampil seperti ini
   
   ```console
    Package             Version
    ------------------- ---------
    asgiref             3.6.0
    certifi             2022.12.7
    charset-normalizer  3.0.1
    dj-database-url     1.2.0
    Django              3.2.18
    django-cors-headers 3.14.0
    django-filter       22.1
    django-guardian     2.4.0
    djangorestframework 3.14.0
    idna                3.4
    Markdown            3.4.1
    mysqlclient         2.1.1
    pip                 23.0.1
    Pygments            2.14.0
    python-dotenv       1.0.0
    pytz                2022.7.1
    requests            2.28.2
    setuptools          63.2.0
    sqlparse            0.4.3
    urllib3             1.26.14
   ```

6. Instalasi selesai

-----

## Next Step (will be update next time)

-----

## Social Media

Jika ingin berdiskusi atau berkolaborasi untuk melanjutkan proyek ini bisa menghubungi saya, atau sekedar mampir pada sosmed-sosmed milik saya di :

1. Instagram [@uzumakiaji](https://www.instagram.com/uzumakiaji)
2. Github [Maulanawesome5](https://www.github.com/Maulanawesome5)
3. LinkedIn [Maulana Aji Wicaksono](https://www.linkedin.com/in/aji-wicaksono300699)

## Will be update next time ...
