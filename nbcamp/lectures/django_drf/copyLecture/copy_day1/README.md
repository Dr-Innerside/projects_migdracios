# Django Rest Framework day1

## ๐ 1์ผ์ฐจ ๊ฐ์ ๋ชฉํ
- Pycharm์ ํจํค์ง ๊ด๋ฆฌ, Django ์คํ, ์ฝ๋ ์ค๋ํซ ๋ฑ์ ์์กดํ์ง ์๊ณ  ํ๋ก์ ํธ๋ฅผ ์ง์  ๊ตฌํ ๋ฐ ์คํํ  ์ ์์ด์ผ ํจ
    - ํธ์ง๊ธฐ์์ ์ ๊ณตํด์ฃผ๋ ๊ธฐ๋ฅ๋ค์ ๊ฐ๋ฐ ์๋๋ฅผ ํฅ์์ํค๊ธฐ ์ํ ๋ชฉ์ ์ผ ๋ฟ, ๋๋ฌด ์์กดํด์๋ ์๋จ
- DRF๋ฅผ ํ์ฉํด ๋ฏธ๋ํ๋ก์ ํธ๋ฅผ ๊ตฌ์ถํ  ์ ์์ด์ผ ํจ

## ๐โโ๏ธ Django Rest Framework๋?
- Django์ ํ์ฅํ. ๊ธฐ์กด django์์ ํ์ฅ๋ ๊ธฐ๋ฅ์ ์ด์ฉํ  ์ ์์
- ๋ํ์ ์ผ๋ก Serializer๋ฅผ ์ฌ์ฉํ๋ฉด, ๊ฐ์ ๊ธฐ๋ฅ์ ๊ตฌํํ๋๋ฐ ์์ด์ ๊ธฐ์กด django์์๋ณด๋ค ์์๊ณ , ํธํด์ง๊ณ , ๊ฐ๋์ฑ์ด ์ข์์ง๋ ๋ฑ์ ํจ๊ณผ๋ฅผ ๋ณผ ์ ์์

## โ  ํ๋ก ํธ์๋์ ๋ฐฑ์๋๋ฅผ ๊ตฌ๋ถํ๋ค?!
- ํ๋ก ํธ์๋๋ฅผ ์ต๋ํ ๋ฐฐ์ ํ๊ณ , ๋ฐฑ์๋ ์์ฃผ๋ก๋ง ์งํํ  ๊ฒ!
- ๊ทธ๊ฒ์ ์ํด ์ฌ์ฉํ  ํ๋ก๊ทธ๋จ POSTMAN
- UI ์์์ django admin ์ ๋

---

## ๐ฉ DRF๋ฅผ ์ฌ์ฉํ๊ธฐ ์ํ ์ค๋น
### 1. drf ์ค์นํ๊ธฐ 
```
pip install django
pip install djangorestframework
```

### 2. settings.py ์ค์ 
INSTALLED_APPS์ 'rest_framework' ์ถ๊ฐํ๊ธฐ
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [ # ๊ธฐ๋ณธ์ ์ธ view ์ ๊ทผ ๊ถํ ์ง์ 
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [ # session ํน์ token์ ์ธ์ฆ ํ  ํด๋์ค ์ค์ 
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PARSER_CLASSES': [ # request.data ์์ฑ์ ์ก์ธ์ค ํ  ๋ ์ฌ์ฉ๋๋ ํ์
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ]
}
```

## ๐ฉ ๊ธฐ์ด Python ๋ฌธ๋ฒ
### def, ํจ์์ ๋ํ ์ดํด
ํจ์ ๊ธฐ๋ณธ ํํ
```python
def test():
    pass
    return True
test()
```

### class, ํด๋์ค์ ๋ํ ํ์ฉ ๋ฐ ์์์ ๋ํ ์ดํด
ํด๋์ค ๊ธฐ๋ณธ ํํ
```python
class Test():
    def test(self):
        pass
        return True
```

ํด๋์ค ์์์ด๋?
- django๋ฅผ ํ๋ฉด์ ๋ง์ด ๋ค๋ฃฐ ๊ฐ๋
- ์ง์  ๊ตฌํํ๋ ์ ๋๋ ํ์ํ์ง ์์ ๊ฒ
- ๋ถ๋ชจ ํด๋์ค, ์์ ํด๋์ค๊ฐ ์กด์ฌํ๋๋ฐ ์์ ํด๋์ค์์ ๋ถ๋ชจ ํด๋์ค์ ๋ด์ฉ์ ๋ฐ์์ ์ฌ์ฉํ๋ค!

### ์๋ฃํ(int, str, list, dict ...)
### list, iterator์ ๋ฐ๋ณต๋ฌธ์ ๋ํ ์ดํด
### mutable๊ณผ immutable์ ์ฐจ์ด
```python
immutable = "String is immutable!"
mutable = ["list is mutable!"]

string = immutable
list_ = mutable

string += "immutable string!"
list_.append("mutable list!")

print(immutable)
print(mutable)
print(string)
print(list_)

# ํด๋น ์ฝ๋๋ฅผ ์คํํ์ ๋ ๋์ค๋ ๊ฒฐ๊ณผ๋ฅผ ์ ์ถํ๊ณ 
# mutable ์๋ฃํ๊ณผ immutable ์๋ฃํ์ ์ด๋ค ๊ฒ ์๋์ง ์์์ผ ํจ
```
mutable ๊ฐ์ฒด๋ ๋ค๋ฅธ ๋ณ์์ ๊ฐ์ ํ ๋นํ  ๋ | ์ฃผ์ ๊ฐ์ ๋ฃ๋๋ค
- mutable ๋ณ์์ list_ ๋ณ์๋ ๊ฐ์ ์ฃผ์๋ฅผ ๋ฐ๋ผ๋ณด๊ณ  ์๋ค
immutable ๊ฐ์ฒด๋ ๋ค๋ฅธ ๋ณ์์ ๊ฐ์ ํ ๋นํ  ๋ | ๊ฐ์ ๋ฃ๋๋ค

### deepcopy()
mutable ๊ฐ์ฒด๋ ์ฃผ์๊ฐ์ ๋ฐ๋ผ๋ณด์ง ์๊ณ , ๊ฐ์ ํ ๋นํ  ์ ์๊ฒ ํด์ค
django ๊ธฐ๋ณธ ๋ผ์ด๋ธ๋ฌ๋ฆฌ์ ์๊ธฐ ๋๋ฌธ์ ๋ฐ๋ก ์ฌ์ฉํ  ์ ์์
```python
mutable = ["list is mutable!"]
list_ = deepcopy(mutable)
# list_ = mutable[:] ์ด๊ฒ๋ ๊ฐ์ ๊ฐ์ ์ค
list_.append("mutable list!")
```
### kwargs, args์ ์ดํด
```python
def test(num1, num2, *args, **kwargs):
# def test(num1, num2):
    print(f"num1: {num1}")
    print(f"num2: {num2}")
    print(args)
    print(kwargs)
    return 

# test(1, 2)
# test(1, 2, 3) # ์ค๋ฅ๊ฐ ๋ฐ์ํจ
test(1,2,
        3,4,5,6,7,8,
        num3=5, num4=2)
```
args(arguments)
- ํจ์์์ ์ ํด์ง ์ธ์ ๊ฐ ์ด์์ ๊ฐ์ ํ์๋ก ํ  ๋๋ง๋ค ํจ์ ์์ ์์ ํด ์ฃผ๋ ๊ฒ์ ๋ถํธํ๋ค
- ๋ช์ํ  ๋ณ์ ์ด์ธ์ ๊ฒ์ args๋ก ์์ ๋กญ๊ฒ ๋ชจ๋ ๋ฐ์ ์ ์๋ค

kwargs(keyword arguements)
- args์ ํค์๋๊ฐ ๋ถ์
- ๋์๋๋ฆฌ ํํ๋ก ๋ค์ด๊ฐ

---

```python
def test(*args, ** kwargs):
    print(args)
    return True

sample_list = [1,2,3,4,5]
sample_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
}
test(*sample_list)
```

โ  *args, **kwargs?
```python
a = [1,2,3,4,5]
print(a) # == print([1,2,3,4,5])
print(*a) # == print(1,2,3,4,5)
```
* ์ ์คํฐ๋ฆฌ์คํฌ(asterisk) ํ ๊ฐ๋ฅผ ์จ์ฃผ๋ฉด ๋ฆฌ์คํธ ํ์์ด ํ๋ ค์ ๊ฐ์ด ์๋ ฅ๋๋ค
- ๋ฐ๋ผ์ ์์ ์์ ์์ ํจ์(*์ธ์๊ฐ) ํํ๋ก ์ฌ์ฉํ๋ฉด, ํจ์ ์์์ ๊ฐ์ด ๋ฆฌ์คํธ๊ฐ ํ๋ ค์ ๋ค์ด๊ฐ๋ค
** ์ ์คํฐ๋ฆฌ์คํฌ ๋ ๊ฐ๋ฅผ ์จ์ฃผ๋ฉด ๋์๋๋ฆฌ ํ์์ด ํ๋ ค์ ๊ฐ์ด ์๋ ฅ๋๋ค

๐ค args, kwargs๋ฅผ ์ฌ์ฉํ์ง ์์ ๊ธฐ๋ณธ ์์ 
```python
from user.models import User

def user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')

        user = User.objects.create(
            username=username,
            fullname=fullname,
            gender=gender,
            birthday=birthday
        )
```

๐ *args, **kwargs๋ฅผ ์ฌ์ฉํ ์์ 
```python
... ์๋ต

def user(request):
    if request.method == "POST":
        user = User.objects.create(
            **request.POST
        )

```

### db์์ ์ฌ์ฉ๋๋ CRUD์ django orm์ ์ดํด

### module์ importํ๋ ๊ตฌ์กฐ์ ๋ํ ์ดํด

### fstring์ ๋ํ ์ดํด

### try, exception์ ํ์ฉํ ์๋ฌ ์ฒ๋ฆฌ

### stacktrace์ ๋ํ ์ดํด
stacktrace๋ฅผ ๊ฐ์ฅ ๋ง์ด ๋ณผ ์ ์๋ ๊ณณ์ ์คํ ์ฝ์ ์ฐฝ!
```python
def run_a():
    print(f"{a}ํจ์๊ฐ ์คํ๋์์ต๋๋ค")
    run_b()
    return 
def run_b():
    print(f"{b}ํจ์๊ฐ ์คํ๋์์ต๋๋ค")
    run_c()
    return 
def run_c():
    print(f"{c}ํจ์๊ฐ ์คํ๋์์ต๋๋ค")
    run_d()
    return 
def run_d():
    print(f"{d}ํจ์๊ฐ ์คํ๋์์ต๋๋ค")
    run_e()
    return 
def run_e():
    print(f"{e}ํจ์๊ฐ ์คํ๋์์ต๋๋ค")
    raise Exception("์๋ฌ ๋ฐ์!!")
    return 

run_a()
```
๐โโ๏ธ stacktrace?
- ์ ํจ์์ ๊ฒฝ์ฐ run_a() ํจ์๋ฅผ ์คํํ๋ฉด b๋ฅผ ํ๊ณ , c๋ฅผ ํ๊ณ , d๋ฅผ ํ๊ณ , e๋ฅผ ํ๊ฒ ๋๋ค.
- ๊ทธ ์์ค์ e๋ฅผ ํต๊ณผํ๋ค๊ฐ ์๋ฌ๋ฐ์!! ์ด๋ผ๋ ๋ฌธ๊ตฌ๋ฅผ ์คํ ์ฝ์์ ์ถ๋ ฅํ๊ฒ ๋๋ค.
- ์๋ฌ ์คํ ์ฝ์์๋ ๋จ์ํ ์๋ฌ๊ฐ ๋ฐ์ํ e ๋ฟ๋ง ์๋๋ผ, e๋ฅผ ํฌํจํ๊ณ  ์๊ฒ ๋๋ a/b/c/d ๋ชจ๋๋ฅผ ์ถ๋ ฅํ๊ฒ ๋๋ค.
- django ํ๋ก์ ํธ ๋ด๋ถ์์ ์์ฑํ ๋ค์ํ python ํ์ผ๋ค์ ์์๊ตฌ์กฐ์ ์๋ ํ๋ก์ ํธ ํ์ผ๋ค์ด stacktrace์ ์ํด ์ฝ์์ ์ถ๋ ฅ๋๋ ์ฐธ์กฐํ  ์ ์๊ฒ ๋๋ค.


## ๐ฉ ํ์์ ์ํ Python ํ์ฉ๋ฒ
### ํ์ด์ฌ ๊ฐ์ํ๊ฒฝ venv
```
# python terminal
python -m venv venv # ๊ฐ์ํ๊ฒฝ ์์ฑ
venv/Scripts/activate # ๊ฐ์ํ๊ฒฝ ์ง์
```

### requirements.txt
ํจํค์ง๋ฅผ ๊ด๋ฆฌํ๊ธฐ ์ํ ํ์ผ
```
# python terminal
pip install django                  # ์ฅ๊ณ  ์ค์น
pip install djangorestframework     # drf ์ค์น
pip freeze > requirements.txt       # requirements.txt์ ์ค์นํ pip list ์ ์์ฑ
pip install -r requirements.txt     # requirements.txt์ ๊ธฐ์๋ pip install
```

### ์ฝ๋ ์ปจ๋ฒค์
ํ์ ์ ์ฝ๋๋ฅผ ์งค ๋ ๊ท์น์ ์ง์ผ์ ์์ฑํ๊ฒ ๋ค๊ณ  ํ๋ ์ฝ์
- ์งํค์ง ์์์ ์, ์๋ฅ ํ๋ฝํ  ๊ฐ๋ฅ์ฑ์ด ๋์..
- ๋์ค์ ์์ฐ์ฑ๊ณผ ๊ด๋ฆฌ๋ฅผ ์ํด์ ์์ฑํจ
    - class LogINUSERView ์ด๋ฐ ์์ผ๋ก ์์ฑํ๋ค๋ฉด, ๋ค๋ฅธ ํ์๋ค์ด ๋ชป์์๋จน์ ํ๋ฅ  ๋์
    - class A ์ด๋ฐ ์์ผ๋ก ์์ฑํ๋ค๋ฉด, ์ด๋ค ํด๋์ค์ธ์ง ๋ค๋ฅธ ํ์๋ค์ด ์ง์ํ๊ธฐ ํ๋ฆ

ํ์ด์ฌ์์์ ์ฝ๋ ์ปจ๋ฒค์์ Pascal, Snake ๋ ์ข๋ฅ๋ก ๊ตฌ๋ถ๋๋ค.
1. Pascal : UserLoginView
- class ๋ง๋ค ๋ ์ฌ์ฉ
2. Snake : user_login_view
- class ์ด์ธ์ ๋ชจ๋  ๊ฒฝ์ฐ์์ ์ฌ์ฉ

์ฝ๋ ์ปจ๋ฒค์์ ์ง์ผ์ ์์ฑํ๋ฉด ์ด๋ค ๊ฒ์ด ํด๋์ค, ์ผ๋ฐ ๋ณ์๋ ํจ์๋ฅผ ๊ตฌ๋ถํ  ์ ์๊ฒ ๋๋ค.

3. ๋ชจ๋ ๋๋ฌธ์ : PIE = 3.14
- ์์์์ ์ฌ์ฉ, ์ ๋ ๋ฐ๋์ง ์์ ๊ฐ์ด๊ธฐ์ ๋๋ฌธ์๋ก ํํ
4. ๋จ์, ๋ณต์ ๋ช์ฌ
- ํ ๊ฐ๋ ๋จ์์ฌ์ผ ํ๊ณ , ๋ ๊ฐ ์ด์์ ๋ณต์์ฌ์ผ ํ๋ค
- user = "user1"
- user_list = ["user1", "user2", "user3"]
- users = ["user1"] -> ํ ๊ฐ์ ๊ฐ๋ง ๋ค์ด์์ง๋ง ๋ฆฌ์คํธ ํํ์ด๊ธฐ ๋๋ฌธ์!
    - users = User.objects.all() ํ ๊ฐ์ผ ์๋, ๋ ๊ฐ์ผ ์๋, ์ฌ๋ฌ ๊ฐ์ผ ์๋ ์์ง๋ง 
    - ์ฌ๋ฌ ๊ฐ๋ฅผ ์กฐํํ๋ฏ๋ก, ๋ฐ๋ณต๋ฌธ์ ์ฌ์ฉํ๋ฏ๋ก ๋ณต์ ๊ฐ๋ฅผ ์ฒ๋ฆฌํ๊ธฐ ์ํ ๋ชฉ์ ์ด ์๋ค๋ ๊ฒ์ ์์๊ฐ ์์

### Http Status Code ์ ๋ํ ์ดํด 
1. 2xx : normal
2. 3xx : redirect
- http://naver.com -> https://naver.com ์ผ๋ก ๋ฆฌ๋ค์ด๋ ์
3. 4xx : client error
- 404 not found
4. 5xx : server error

### ๊ธฐ๋ณธ์ ์ธ ํฐ๋ฏธ๋ ํ์ฉ
๋ฆฌ๋์ค ๋ฐ ํฐ๋ฏธ๋๊ณผ ๊ฐ์ CLI(Command Line Interface) ํ๊ฒฝ์ด ๋งค์ฐ ๋ง์ผ๋ฏ๋ก ์ฌ์ฉ์ ์ต์ํด์ ธ์ผํจ
