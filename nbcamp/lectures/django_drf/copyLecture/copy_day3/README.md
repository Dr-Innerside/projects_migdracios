# Django Rest Framework day3

## ๐ 3์ผ์ฐจ ๊ฐ์ ๋ชฉํ
- Rest API์ ๋ํ ์ดํด
- views.py์์ ๋ฆฌํ์คํธ ์ฒ๋ฆฌํ๊ธฐ
- POSTMAN์ ํ์ฉํ ๋ฆฌํ์คํธ ์ค์ต
- DB ORM๊ณผ ๊ตฌ์กฐ์ ๋ํ ์ดํด

## ๐ฉ REST API์ ๋ํ ์ดํด
http method์ ์ข๋ฅ

```python
if request.method == 'GET':
    # ์กฐํ
if request.method == 'GET':
    # ์์ฑ
```

1. get : ์กฐํ
2. post : ์์ฑ
3. put : ์์ 
4. delete : ์ญ์ 

## ๐คนโโ๏ธ FBV, CBV?
django์์ views.py๋ฅผ ํตํด API๋ฅผ ๊ตฌํํ  ๋, ์์ฑํ  ์ ์๋ ๋ฐฉ๋ฒ์ ์๋ฏธํ๋ค.
๊ฐ๊ฐ ํจ์ ๊ธฐ๋ฐ, ํด๋์ค ๊ธฐ๋ฐ์ ์๋ฏธํ๋ค.

### ๐จ Function Base View
ํจ์๋ก view๋ฅผ ์์ฑ

### ๐จ Class Base View
ํด๋์ค๋ก view๋ฅผ ์์ฑ
- ์ผ๋ฐ์ ์ผ๋ก ๋ง์ด ์ฐ์

```python
# Class Base View
class UserView():
def get(self, request):
    # ์ฌ์ฉ์ ์ ๋ณด ์กฐํ
    pass    
def post(self, request):
    # ํ์๊ฐ์
    pass
def put(self, request):
    # ํ์ ์ ๋ณด ์์ 
    pass
def delete(self, request):
    # ํ์ ํํด
    pass

# Function Base View
def user_view(request):
    if request.method == 'GET':
        pass
```
#### โ  CBV ๋ฆฌํ์คํธ ํจ์ ์ด๋ฆ์ ๊ณ ์ ?!
CBV ๋ฐฉ์์ผ๋ก ์์ฑํ  ๋๋ ๋ฐ์์ฌ http method์ธ get, post, put, delete๋ผ๊ณ  ํจ์ ์ด๋ฆ์ ๊ณ ์ ์์ผ ์ฃผ์ด์ผ ์ธ์ํ๋ค.
- ๊ทธ๊ฒ์ด DRF์์ ์ง์ ํ ์ฝ์์ด๊ธฐ์.

#### ๐คนโโ๏ธ ๊ทธ๋ผ method ์์ ํจ์๋ฅผ ์จ์ฃผ๊ณ  ์ถ๋ค๋ฉด?
CBV ๋ฐ์์ ํจ์๋ฅผ ํ๋ ์๋ก ์์ฑํด์ ์์์ ํธ์ถํ๋ ๋ฐฉ์์ ์ฌ์ฉํ๊ธฐ

```python
...์๋ต
def sum_(num1, num2):
    return num1+num2

class UserView(APIView):
    ...
    def get(self, request):
        sum_(**request.data)
        return Response({"msg": "get method!!"})
    ...
```

### ๐ฅ Permission Class?
- Class Base View๋ฅผ ์ฌ์ฉํ  ๋, Django Rest Framework์์ ์ง์ํ๋ ๊ธฐ๋ฅ.
- ์์ฑํ๊ณ  ์๋ CBV์ ๊ถํ์ ์ง์ ํด ์ค ์ ์์
- ์ฌ์ฉ์๊ฐ ์ ๊ทผํ  ๋, ๋๊ตฌ๋ ์กฐํ/๋ก๊ทธ์ธ ํ ์ ์ ๋ง ์กฐํ/๊ด๋ฆฌ์ ๊ณ์ ๋ง ์กฐํ ๋ฑ
- Permission Class๋ฅผ ํ์ฉํ์ฌ ๊ฐ์์ผ ๊ธฐ์ค 1์ฃผ์ผ ์ด์ ์ง๋ ์ฌ์ฉ์๋ง ์ ๊ทผํ๋ ๋ฑ์ ์ ์ฉ๊ฐ๋ฅ

1. import APIView
- Permission Class๋ฅผ ์ฌ์ฉํ๊ธฐ ์ํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
2. APIView๋ฅผ ์์
- ์์ฑํ CBV์ APIView๋ฅผ ์์์์ผ APIView์ ๊ธฐ๋ฅ์ ์ฌ์ฉํ  ์ ์๊ฒ ํจ
3. import permissions
- APIView๋ฅผ ์์๋ฐ์ ์ํ์์ ๊ถํ ์ค์ ์ ์ถ๊ฐ๋ก ๊ฑธ์ด์ค ๋ผ์ด๋ธ๋ฌ๋ฆฌ permissions ์ํฌํธ
4. permission_classes ๋ณ์์ ๊ถํ ์ฃผ๊ธฐ
- permissions.AllowAny๋ ๋ชจ๋์๊ฒ ํ์ฉํ๋ ๊ถํ์ ์ค์ ํ ๊ฒ์ด๋ค!


```python
from rest_framework.views import APIView
from rest_framework import permissions

class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAdminUser]
    ... ์๋ต
```

#### ๐ค ์คํ๊ฐ ๋๋ ์ ๋๋ก ์๋ํ๋ค?
- permission์ ๊ธฐ๋ณธ๊ฐ์ AllowAny์ด๊ธฐ ๋๋ฌธ์, AllowAny๋ก ์ธํํ๋๋ฐ ์คํ๊ฐ ์์๋ค๋ฉด ์๋ํ์ ๊ฒ์ด๋ค!
- ๋ง์ฐฌ๊ฐ์ง๋ก rest_framework settings.py ์์๋ ํด์ผํ์ง๋ง, ์ด๊ฒ๋ ์์ผ๋ฉด ๊ธฐ๋ณธ ๊ฐ์ธ AllowAny๋ฅผ ์ฌ์ฉํ๋๋ก ๋์ด์๋ค!

### ๐ฅ return Response?
๊ธฐ์กด๋ฐฉ์์ render, redirect๋ฅผ ์ฌ์ฉํ์์ผ๋ DRF์์๋ Response๋ฅผ ํ์ฉํ์ฌ API๋ฅผ ์ฒ๋ฆฌํ  ๊ฒ

1. import Response
2. Response ๋ฐฉ์ 
```python
# render
return render(request, 'index.html')

# redirect
return redirect('/home')

# Response
from rest_framework.response import Response

return Response({"msg": "GET method!"})
```

## ๐ฉ POSTMAN ํ์ฉ
ํ๋ก ํธ์๋ UI๊ฐ ์กด์ฌํ์ง ์์ ๋ view๋ฅผ ํ์คํธํ๊ธฐ ์ํด์ ํ์ํ ํ๋ก๊ทธ๋จ

1. ์ํฌ์คํ์ด์ค๋ฅผ ๋ง๋ค์ด ํ์๊ณผ ๊ณต์ ํ์!
- ์ํฌ์คํ์ด์ค๋ฅผ ๋ง๋ค์ด ํ์๊ณผ ๋ง๋ค์ด ๋ ํ์คํธ ํํ๋ฅผ ๋ชจ๋ ๋ฐ๋ณต์ ์ผ๋ก ์์ฑํ  ํ์์์ด ์ด์ฉํ  ์ ์์ผ๋ฉฐ, ๋ํ ์์ ๋ ๊ฐ๋ฅํ๊ธฐ์ ํ์์ ์ฉ์ด
2. ์๋ก์ด request๋ฅผ ๋ง๋ค์ด ์ฃผ์์ http method๋ฅผ ์๋ ฅํ๊ณ  send๋ฅผ ํด์ ํ์คํธํด๋ณด๊ธฐ

### ๐ POSTMAN์ ๋ฐ์ดํฐ๋ฅผ ๋ด์์ ๋ฐฑ์๋๋ก ๋ณด๋ด๊ธฐ
1. Collection -> ์ํ๋ Request -> Body -> raw
- ๋ณด๋ด์ค ๋ฐ์ดํฐ ํ์์ JSON์ผ๋ก ๋ณ๊ฒฝํด์ฃผ๊ธฐ!
- JSON์ dict์ ๊ฐ๊ฒ ์์ฑํด์ฃผ๋ฉด ๋จ(""ํฐ ๋ฐ์ดํ๋ก ์์ฑํด์ผ ํ๋ค!)
2. ๋ฐฑ์๋ request.data์์ ํด๋น ๊ฐ์ ๋ฐ์์ ์ฒ๋ฆฌ!

```
# POSTMAN-body-raw
{
    "num1" : 5,
    "num2" : 10
}
```

```python
def get(self, request):
    print(request.data) # JSON ํ์์ ๋ฐ์ดํฐ
    result = sum_(**request.data) # request.data ์ธํจํน
    Response({"msg": f"get method -- sum result->{result}})
```
#### ๐ฅ ์ธํจํน ์์ฉ! kwargs๊ฐ ์๋, args๋ฅผ POSTMAN์์ JSON์ผ๋ก ๋ณด๋ธ๋ค๋ฉด?
```python
# ์์ฉ! *args ๋ก ์ธํจํนํด์ ๋ฐ์ดํฐ ์ฌ์ฉํ๊ธฐ
# postman
{
    "numbers": [1,2,3,4,5,6]
}
# def sum
sum_(*args):
    return sum(args)
# def get
numbers = request.data.get("numbers",[])
result = sum_(*numbers)
```

### โ  POST/PUT/DELETE ํต์  ์ csrf error๊ฐ ๋ฐ์ํ  ๋?!
django์์ csrf๋ก ๋ฐ์ดํฐ ์ ํจ์ฑ ๊ฒ์ฌ๋ฅผ ์คํํ๋ฏ์ด DRF์์๋ ์ฌ์ฉํด์ค์ผ ํ๋ค.
POSTMAN์์ ์๋์ ์ฝ๋๋ฅผ ํจ๊ป ์์ฑํด์ผ ํ๋ค!

```
var xsrfCookie = postman.getResponseCookie("csrftoken");
postman.setGlobalVariable('csrftoken', xsrfCookie.value);
```
๋ํ ํค๋์ ๋ด์์ ๋ณด๋ด์ค์ผ ํ๋ค
- KEY : X-CSRFToken
- VALUE : {{ csrftoken }}
- test์์ ์ ์ ๊ฒ๋ณด๋ค ์ ์์, ํ๋จ๋ถ Cookies์์ csrftoken์ value๋ฅผ ๋ณต์ฌํด์ ํค๋ value์ ๋ถ์ฌ๋ฃ์ด send!
- ์ด๋ฅผ ์๋ํ ํ๊ฒ์ด test ์คํฌ๋ฆฝํธ

## ๐ฉ DB ORM๊ณผ ๊ตฌ์กฐ์ ๋ํ ์ดํด

### queryset, object์ ์ฐจ์ด์ ๋ํ ์ดํด
1. queryset
- ์ฟผ๋ฆฌ์์ ์ค๋ธ์ ํธ์ ์งํฉ
```python
users = User.objects.filter(id=id) # return queryset
# queryset : [obj1, obj2, obj3]
# objects.filter๋ ์ค๋ธ์ ํธ ๊ฐ์์๋ ํฐ ๊ด๋ จ์ด ์๋ค
```
2. object
- ์ค๋ธ์ ํธ๋ ๋จ์ผ ์ค๋ธ์ ํธ
```python
user = User.objects.get(id=id) # return object
# objects.get์ ๋ฐ๋์ ํ๋์ ์ค๋ธ์ ํธ ๋ง์ ํ์๋ก ํ๋ค. ์๊ฑฐ๋, ๋ ๊ฐ ์ด์์ผ ๊ฒฝ์ฐ ์๋ฌ!
```
### โ ORM์ผ๋ก ๋ฐ์ดํฐ ์ถ๊ฐ,์กฐํ,์์ ,์ญ์ ํ๊ธฐ
```python
# ์ถ๊ฐ1
model = Model(
    field1="value1",
    field2="value2"
)
model.save()

# ์ถ๊ฐ2
Model.objects.create(
    field1="value1",
    field2="value2"
)

# ์กฐํ
Model.objects.all()
Model.objects.filter()
Model.objects.get()

# ์์ 1
model = Model.objects.get(id=obj_id)
model.field = value
model.save()

# ์์ 2
Model.objects.filter(field__contains=value).update(
    field1="value1",
    field2="value2"
)

# ์ญ์ 
Model.objects.filter(field="value").delete()
Model.objects.get(id=obj_id).delete()
```

๐คนโโ๏ธ ์์ 2์์ field__contains=value, double underbar?
- ์ถ๊ฐ ์์ . LINK--

### ๐ฅ ์์ฃผ ์ฌ์ฉํ๋ ํจํด ์ฝ๋
1. objects.get() ์ด ์์ ๋ ์ฌ์ฉํ๋ ์ด๋ฒคํธ
```python
try:
    Model.objects.get(id=obj_id)
except Model.DoesNotExist:
    # some event
    return Response("์กด์ฌํ์ง ์๋ ์ค๋ธ์ ํธ ์๋๋ค.")
```
2. order_by()๋ฅผ ์ฌ์ฉํ์ฌ ๊ฐ์์ผ์ ์กฐํ
```python
Model.objects.all().order_by("join_date")

# ์ถ๊ฐ
# -join_date๋ฅผ ๋ถ์ด๋ฉด ์ญ์์ผ๋ก ์ ๋ ฌ
# .order_by("?") ์ฌ์ฉ ์ ๋ฌด์์ ์ํ
```
3. ์ฒซ๋ฒ ์งธ ์ฟผ๋ฆฌ์์ ๊ฐ์ ธ์ค๋ ๋ฉ์๋ .first()
```python
Model.objects.all().first()
# all()[0] ๊ณผ ๋์ผํ ๋ฉ์๋
```
4. get_or_create()
- ์๋ ฅํ object๊ฐ ์กด์ฌํ  ๊ฒฝ์ฐ ํด๋น object๋ฅผ ๊ฐ์ ธ์ค๊ณ ,
- ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ ์๋ก ์์ฑํจ
```python
model, created = Model.objects.get_or_create(
    field1="value1",
    field2="value2"
)
if created:
    # created event
else:
    # already exist event
```

## ๐ฏ DRF Custom UserModel ์์ฑ ๋ฐ ์ฌ์ฉ์ ๋ก๊ทธ์ธ ๊ตฌํ
์ค์  ์ค๋ฌด์์๋ django์์ ๊ธฐ๋ณธ์ผ๋ก ์ ๊ณตํ๋ AbstractUser๊ฐ ์๋, DRF ์ปค์คํ ์ฌ์ฉ์ ๋ชจ๋ธ์ ์ฌ์ฉํ์ฌ ๊ฐ๋ฐํ๋ค.
- custom user model์ ์์ฑ ์ ํ๋ ๋ค์ ์์ ๋กญ๊ฒ ์ปค์คํ ํ  ์ ์๊ธฐ ๋๋ฌธ!
- custom user model์ ๋ง๋ค๊ธฐ ์ํด ํ์ํ ์ค์ ์ ์ธ์ฐ์ง ์๊ณ  ๊ฐ์ ธ๋ค ์ฐ๊ธฐ!

1. import BaseUserManager, AbstractBaseUser
- ์ปค์คํ ๋ชจ๋ธ์ ์ฌ์ฉํ๊ธฐ ์ํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
2. AbstarctBaseUser ์์
- ์ปค์คํ ์ ์  ๋ชจ๋ธ์ ๋ฐ๊ธฐ ์ํด ์์ํ๋ ํด๋์ค
3. ํ๋ ์์ฑ
- ์์ด๋, ๋น๋ฐ๋ฒํธ, ์ด๋ฉ์ผ, ๊ฐ์์ผ ๋ฑ์ ๋ชจ๋ธ ํ๋์ ์ถ๊ฐํ๋ค.
4. settings.py์ AUTH_USER_MODEL = 'user.User' ์ธํ
- global settings.py๋ฅผ ์ฐธ์กฐํ๋ฉด ๊ธฐ๋ณธ AUTH_USER_MODEL = 'auth.model' ๋ก ๋์ด์๋ค.
- ๋ด๊ฐ ์ฌ์ฉํ  ์ปค์คํ ๋ชจ๋ธ์ ์ ์  ๋ชจ๋ธ์ด๋ผ๋ ๊ฒ์ ์ค์ ํด ์ฃผ์ด์ผ ์๋ํ๋ค.
5. USERNAME_FIELD = 'username'
- ์น๋ง๋ค ์์ด๋/ํจ์ค์๋, ์ด๋ฉ์ผ/ํจ์ค์๋๋ฅผ ๋ค๋ฅด๊ฒ ์๋ ฅ๋ฐ๋ ๊ณณ์ด ์๋ค.
- ๊ทธ๋์ ๋ญ ์์ด๋๋ก ๋ฐ์ ๊ฑด๋ฐ? ์ ํด๋นํ๋ ์ค์ ์ด๋ค.
- ์์ ๊ฒฝ์ฐ username, ์ฆ ํ์ด๋ธ์์ ์ฌ์ฉ์ ๊ณ์ ์ ์์ด๋๋ก ๋ฐ๊ฒ ๋ค๋ ๊ฒ์ด๋ค.
- ์ด๋ฉ์ผ์ ์์ด๋๋ก ๋ฐ๊ณ  ์ถ์ ๋๋, USERNAME_FIELD = 'email' ์ด๋ ๊ฒ ํ๋ฉด ๋๋ค!
6. REQUIRED_FIELD = []
- ๋ฑํ ์ฌ์ฉํ  ์ผ์ ์์
- createsuperuser๋ฅผ ๋ํ์ ์ผ๋ก ์ฌ์ฉํ๊ฒ ๋  ์ฌ๋ฌ ๊ธฐ๋ฅ๋ค์ ์๋ํ๊ฒ ํด์ค ์ค์ 
- ์ค์ ํ  ๋ ๊ฐ์ email, fullname ๋ฑ์ ์ ์ด์ค๋ค๋ฉด, createsuperuser ๋ฑ์ ๊ธฐ๋ฅ์ ์๋ํ  ๋ ์๋ ฅ ๋ฐ๊ฒ ๋๋ค.
7. is_active, is_admin ์ค์ 
- ํ์ฑํ ๊ณ์ ์ธ์ง, ๊ด๋ฆฌ์ ๊ณ์ ์ธ์ง ์ค์ ํ๋ ๊ฐ
8. ๊ฐ๋์ฑ์ ์ํ str(self) ํจ์
- ์ค๋ธ์ ํธ๋ฅผ ์์ฑํ๋ฉด object(1) ์ด๋ฐ ์์ผ๋ก ์กฐํํ๊ฒ ๋๋๋ฐ,
- ์ด๋ฅผ strํจ์์ ๋ฆฌํด ๊ฐ์ ์ง์ ํด์ฃผ์ด ๋ณด๊ธฐ ์ฝ๊ฒ ํ  ์ ์๋ค.
```python
def __str__(self):
    return fullname
# ์ด๋ ๊ฒ ์์ฑํด๋๋ฉด, ์ฌ์ฉ์๊ฐ ๊ณ์ ์ ์์ฑํ  ๋ ์ค๋ธ์ ํธ์ ์ด๋ฆ์ object(1) ๋์ , ๊น์ฒ ์ ๋ก ๋ฐ๊ฒ ๋๋ค.
```
9. has_perm, has_module_perm ์ค์ 
- ํ์ด๋ธ์ ๊ถํ์ ์ค์ 
- ๊ด๋ฆฌ์ ๊ณ์ ์ด๋ผ๋ฉด ๊ถํ์ ์ฃผ๊ณ , ์๋๋ผ๋ฉด ์์ฃผ๊ณ .
- admin์ผ ๊ฒฝ์ฐ ๋ฌด์กฐ๊ฑด True, ๋นํ์ฑ ์ฌ์ฉ์(is_active=False)์ ๊ฒฝ์ฐ ํญ์ False
- ๊ธฐ๋ณธ ์ธํ ์ดํ ์๋์ง ์์
10. is_staff ์ค์ 
11. UserManager ์ง์ 
- ๋ชจ๋ธ์ objects = UserManager() ์ถ๊ฐ
- ์ฌ์ฉ์ ๊ณ์ , superuser ๊ณ์  ์์ฑ ํจ์๋ฅผ ๋ง๋ค์ด์ ์ค์  ์์ฑ์ ํจ์๋ฅผ ํ๊ณ  ์คํ๋จ

### โ  migration ์๋ฌ ๋ฐ์์์๋ ์์ถ๋ฐํ๊ธฐ
- ์์ฑํ ์ฑ์ migrations ํด๋์ 0001~๊ณผ ๊ฐ์ ๋ง์ด๊ทธ๋ ์ด์ ํ์ผ์ ์ง์ด๋ค.
- db.sqlite3 ํ์ผ์ ์ญ์ ํ๋ค.
- makemigrations, migrate ์ปค๋งจ๋๋ฅผ ๋ค์ ์๋ ฅ!

### ๐ฅ Custom User Model์ ํ์ฉํ์ฌ ๋ก๊ทธ์ธํ๊ธฐ!
1. Permissions ํ์ธ!
- AllowAny๋ ๋ชจ๋  ์ฌ์ฉ์, IsAuthenticated๋ ๋ก๊ทธ์ธํ ์ฌ์ฉ์! ํ์ธํด๋ณด๊ณ  ๋ก๊ทธ์ธ ๋ทฐ ๋ง๋ค๊ธฐ
2. UserAPIView ์์ฑ
- UserView๋ IsAuthenticated๋ก ๋ณ๊ฒฝํ ๋ค, AllowAny๋ก ์ ์ฉ๋๋ ์๋ก์ด CBV ์์ฑ
3. import login, authenticate
- django.contrib.auth์์ ๊ฐ์ ธ์จ๋ค

#### โ API์ ์ฃผ์๋ฌ๊ธฐ
- ๊ฐ๋์ฑ์ ์ํด์!
- ์กฐ๊ธ ๋ ์์ธํ๊ฒ ์์ฑํ๋ ค๋ฉด Docstring ์ ํ์ฉํด๋ณด์!
```python
# ํ์ค ์ฃผ์
def get():
    '''
    Docstring:
    ๋ก๊ทธ์ธ ํ ์ฌ์ฉ์์ ์ ๋ณด๋ฅผ ๋ฐ์ดํฐ์ ํฌํจ์์ผ์ ๋ฆฌํด
    '''
```

### ๐ข Custom User Model์ ํ์ฉํ์ฌ ๋ก๊ทธ์์ํ๊ธฐ!
1. http method DELETE!
2. contrib.auth import logout
3. logout(request)

```python
def delete(self, request):
    logout(request)
    return Response({"message": "delete method!"})
```