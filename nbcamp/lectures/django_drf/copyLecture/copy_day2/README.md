# Django Rest Framework day2

## ๐ 2์ผ์ฐจ ๊ฐ์ ๋ชฉํ
- ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ฉ์ด ์ ๋ฆฌ
- django ํ๋ก์ ํธ ๊ตฌ์กฐ์ ๋ํ ์ดํด

## ๐ฉ ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ฉ์ด ์ ๋ฆฌ
1. RDBMS(RDB, Relational Database Management System)
- ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค ๊ด๋ฆฌ ์์คํ, MySql, OracleDB ๋ฑ ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค๋ฅผ ์ง์นญํ๋ค.
2. Sql(Structured Query Language)
- select, insert ๋ฑ๊ณผ ๊ฐ์ ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ฟผ๋ฆฌ๋ฅผ ๋ ๋ ค ๋ฐ์ดํฐ๋ฒ ์ด์ค์ CRUD๋ฅผ ์ํด ์ฌ์ฉ๋จ
3. NoSql(Not Only Sql)
- ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค๊ฐ ์๋ ๋ค๋ฅธ ํํ๋ก ๋ฐ์ดํฐ๋ฅผ ์ ์ฅํ๋ฉฐ, mongoDB๊ฐ ์ด์ ํด๋น
- ๊ด๊ณํ ๋ฐ์ดํฐ๋ฒ ์ด์ค ๋งํผ ์ ํจ์ฑ์ ์ง์ผ์ฃผ์ง๋ ์์
- ๋์ฉ๋์ ๋ฐ์ดํฐ๋ฅผ ๋ฃ๊ณ  ๊ฐ์ ธ์ค๋๋ฐ ์ ๋ฆฌํจ
4. Table
- DB๋ ๊ธฐ๋ณธ์ ์ผ๋ก ํ์ด๋ธ๋ก ์ด๋ฃจ์ด์ ธ ์์ผ๋ฉฐ, ํ๋์ ๋ ์ฝ๋(django์์๋ object)๊ฐ ์กด์ฌํ๋ค.

```python
# models.py
class User(models.Model):
    username = models.CharField("์ฌ์ฉ์ ๊ณ์ ", max_length=50)
    password = models.CharField("๋น๋ฐ๋ฒํธ", max_length=50)

    # User๋ผ๋ ํ์ด๋ธ์ username, password๋ผ๋ ํ๋๊ฐ ์กด์ฌํจ
    # ์ฌ์ฉ์๊ฐ ํ์๊ฐ์์ ํ  ๋๋ง๋ค ๋ ์ฝ๋๊ฐ ํ๋์ฉ ์ถ๊ฐ๋จ.
    # ์ฆ, ๋ ์ฝ๋๋ ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์ ์ฅ ๋๋ ๊ฐ๋ค์ ์ง์นญํ๋ ๊ฒ
```

5. key
- FK : Foreign Key์ ์ฝ์์ด๋ฉฐ, ๋ค๋ฅธ ํ์ด๋ธ์ ์ฐธ์กฐ ํ  ๋ ์ฌ์ฉ๋๋ค.
- UK : Unique Key์ ์ฝ์์ด๋ฉฐ, ์ค๋ณต ๊ฐ์ ํ์ฉํ์ง ์๋๋ค.
    - ํ์๊ฐ์ํ  ๋, ์ฌ์ฉ์ ๊ณ์ ์ด ๋ํ์ ์ธ UK
- PK : Primary Key์ ์ฝ์์ด๋ฉฐ, ํ์ด๋ธ์์ ๋ฐ๋์ ์กด์ฌํด์ผ ํ๋ค.
    - ํ ํ์ด๋ธ์ ๋ ๊ฐ ์ด์ ์กด์ฌํ  ์ ์์
    - UK์ ์์๊ฐ๋
    - FK๋ฅผ ์ฌ์ฉํ  ๊ฒฝ์ฐ ์ฐธ์กฐ ํ  ํ์ด๋ธ์ PK๋ฅผ ๋ฐ๋ผ๋ณธ๋ค.
    - ํ์ด๋ธ์ ์ถ๊ฐํ๊ณ  migration ํ์ผ์ ์ฐพ์๋ณด๋ฉด id๊ฐ์ด ๋ฐ๋ก PK์ธ๋ฐ,
    - models.py๋ก ์ง์ ํด์ฃผ์ง ์์ผ๋ฉด ์๋์ผ๋ก ์์ฑ๋๋ค.

```python
username = models.CharField("์ฌ์ฉ์ ๊ณ์ ", max_length=50, unique_key=True)
# UK๋ ์ฌ๋ฌ ๊ฐ ์ผ ์๋ ์๋ค! ๋ค๋ง ์ด๊ฒ์ ๋ค๋ฅธ ๋ ์ฝ๋ ๊ฐ๋ค๊ณผ๋ ๋ค๋ฅธ ํน๋ณํ ๊ฐ
password = models.CharField("๋น๋ฐ๋ฒํธ", max_length=50, primary_key=True)
# PK๋ ๋ ๊ฐ ์๋ค๋ฉด ๋ฐ๋ก ์ค๋ฅ๋ฅผ ๋ด๋ฑ๋๋ค! ์์ด๋, ๋ ๊ฐ ์ด์์ด์ด๋ ์๋๋ ๊ฐ
```

## ๐ฉ django ํ๋ก์ ํธ ๊ตฌ์กฐ์ ๋ํ ์ดํด
1. settings.py
- django ํ๋ก์ ํธ๋ฅผ ์คํํ  ๋ ํด๋น ํ์ผ์ ์ฐธ์กฐํ๋ค
- ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ค์ , ์ฑ ์ค์ , ๊ธฐ๋ณธ ์ ์ฑ ์ค์ ๋ฑ์ ํ  ์ ์๋ค.
2. models.py
- DB์ ํ์ด๋ธ์ ์ถ๊ฐํ๊ณ  ๊ด๋ฆฌํ  ๋ ์ฌ์ฉ๋๋ค.
- ํ์ด๋ธ์ ๋ค์ด๊ฐ ํ๋, ํ๋์ ์์ฑ ๊ฐ ๋ฑ์ ์ค์ ํ  ์ ์๋ค.
- python manage.py makemigrations/migrate ๋ช๋ น์ด๋ฅผ ํตํด ์ค์ ์ DB์ ๋ฐ์์ํฌ ์ ์๋ค.
3. views.py
- django์์ request ๋ฐ์ดํฐ๋ฅผ ๋ฐ์ ํ ์ฒ๋ฆฌํ  ์ ๋ฐ์ ์ธ ๋ก์ง์ด ๋ค์ด๊ฐ๋ค.
- urls.py์์ views์ ์๋ class๋ ํจ์๋ฅผ ํธ์ถํด์ ์ฌ์ฉํ๊ฒ ๋๋ค.
4. urls.py
- ์น์์ django ํ๋ก์ ํธ๋ก request๋ฅผ ์ ๋ฌํ  ๋ ๋ฐ์์ค ๊ฒฝ๋ก๋ฅผ ์ค์ ํ  ์ ์๋ค.

## ๐คนโโ๏ธ DB ๋ชจ๋ธ๋ง ์ค์ต
```python
#  models.py
from django.db import models

# ์ฌ์ฉ์ ๋ชจ๋ธ : ๊ธฐ๋ณธ์ ์ธ ์ฌ์ฉ์ ์ ๋ณด
class User(models.Model):
    username = models.CharField("์ฌ์ฉ์ ๊ณ์ ", max_length=20, unique=True)
    email = models.EmailField("์ด๋ฉ์ผ ์ฃผ์", max_length=100, unique=True)
    password = models.CharField("๋น๋ฐ๋ฒํธ", max_length=60)
    fullname = models.CharField("์ด๋ฆ", max_length=20)
    join_date = models.DateTimeField("๊ฐ์์ผ", auto_now_add=True)

# ์ฌ์ฉ์ ํ๋กํ ๋ชจ๋ธ : ์ฌ์ฉ์ ์์ธ ์ ๋ณด
class UserProfile(models.Model):
    # ์ฌ์ฉ์๋ฅผ One-to-One ์ผ๋ก ๋ฐ๋ผ๋ด
    user = models.OneToOneField(to=User, verbose_name="์ฌ์ฉ์", on_delete=models.CASCADE)
    # ์ฌ์ฉ์๋ฅผ Many-to-Many ๋ก ๋ฐ๋ผ๋ด
    hobby = models.ManyToManyField(to="Hobby", verbose_name="์ทจ๋ฏธ")
    introduction = models.TextField("์๊ฐ")
    birthday = models.DateField("์์ผ")
    age = models.IntegerField("๋์ด")

# ์ทจ๋ฏธ ๋ชจ๋ธ
class Hobby(models.Model):
    name = models.CharField("์ทจ๋ฏธ", max_length=50)
```

### ๐ฅ FK์์ ์ฌ์ฉ๋๋ on_delete ์์ฑ์ ๋ํ์ฌ
์ ์ฝ๋๋ฅผ ์์๋ก ์ฌ์ฉ์๋ชจ๋ธ์ ์ฐธ์กฐํ๋ ์ฌ์ฉ์ ํ๋กํ์ ์ ์ ์,
์ทจ๋ฏธ๋ชจ๋ธ์ ์ฐธ์กฐํ๋ ์ฌ์ฉ์ ํ๋กํ์ ์ทจ๋ฏธ๋ ๊ฐ๊ฐ ์ฌ์ฉ์๋ชจ๋ธ๊ณผ, ์ทจ๋ฏธ๋ชจ๋ธ์ ๋ ์ฝ๋๊ฐ ์ญ์ ๋๋ค๋ฉด ์ด๋ป๊ฒ ๋๋ ๊ฒ์ธ๊ฐ?

1. CASCADE : FK๋ก ์ฐธ์กฐํ๋ ๋ ์ฝ๋๊ฐ ์ญ์  ๋  ๊ฒฝ์ฐ ํด๋น ๋ ์ฝ๋๋ฅผ ์ญ์ ํ๋ค.
2. SET_NULL : FK ํ๋์ ๊ฐ์ Null๋ก ๋ณ๊ฒฝํด์ค๋ค. null=True๊ฐ ์ ์๋์ด ์์ด์ผ ์ฌ์ฉ ๊ฐ๋ฅํ๋ค.
3. PROTECT : ํด๋น ๋ ์ฝ๋๊ฐ ์ญ์ ๋์ง ์๋๋ก ๋ณดํธํด์ค๋ค.
4. SET_DEFAULT : FK ํ๋์ ๊ฐ์ default๋ก ๋ณ๊ฒฝํด์ค๋ค. default=""๊ฐ ์ ์๋์ด ์์ด์ผ ์ฌ์ฉ ๊ฐ๋ฅํ๋ค.
5. SET() : FK ํ๋์ ๊ฐ์ SET์ ์ค์ ๋ ํจ์๋ฅผ ํตํด ์ํ๋ ๊ฐ์ผ๋ก ๋ณ๊ฒฝํ  ์ ์๋ค.
6. DO_NOTHING : ์๋ฌด๋ฐ ๋์์ ํ์ง ์๋๋ค. ์ฐธ์กฐ ๊ด๊ณ์ ๋ฌด๊ฒฐ์ฑ์ด ์์๋  ์ ์๊ธฐ ๋๋ฌธ์ ๊ถ์ฅํ์ง ์๋๋ค.

### โ  DateField์ DateTimeField๋ ๋ค๋ฅด๋ค?!
DateField์ DateTimeField๋ default ๊ฐ์ ์ฌ๋ฌ ํํ๋ก ์ง์ ํ  ์ ์๋ค.

1. default = $date : ์ง์ ํ ๊ฐ์ ๊ธฐ๋ณธ ๊ฐ์ผ๋ก ์ค์ ํ๋ค.
2. auto_now_add = True : ๋ ์ฝ๋๊ฐ ์์ฑ๋  ๋์ date๋ฅผ ๊ธฐ์ค์ผ๋ก ๊ฐ์ ์ง์ ํ๋ค.
3. auto_now = True : ๋ ์ฝ๋๊ฐ save() ๋  ๋๋ง๋ค ๊ฐฑ์ ๋๋ค.

โ ์์ ๊ฐ์ ๋ ๊ฐ ์ด์ ๊ฐ์ด ์ธ ์ ์๋ค!

## admin ํ์ด์ง ํ์ฉ
๋ชจ๋ธ๋ง ํ ํ์ด๋ธ๋ค์ admin์์ ์ถ๊ฐ, ํ์ธ, ์์ ํ๊ธฐ

```python
# admin.py
from django.contrib import admin
from user.models import User, UserProfile, Hobby

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)
```

admin ์ปค์คํ์ ์ฌํ๊ณผ์ ์์--LINK(์ฐจํ ์ถ๊ฐ)