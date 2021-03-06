# Django Rest Framework day4

## ๐ 5ํ์ฐจ ๊ฐ์ ๋ชฉํ
- status code๋ฅผ ์ดํดํ๊ณ , ํ๋ก์ ํธ์ ์ ์ฉํ  ์ ์๋ค.

## ๐ฉ Status Code
### ๐ค Status Code๋ฅผ ์ง์ ํด ์ฃผ์ง ์์ ๊ฒฝ์ฐ?
Status Code๋ฅผ ์ง์ ํด์ฃผ์ง ์๋๋ค๋ฉด, ๊ธฐ๋ณธ์ผ๋ก 200์ ๊ฐ๋ฆฌํจ๋ค.
- ๊ธฐ๋ณธ์ผ๋ก ๋์ด ์๋ค๊ณ  ํ๋๋ผ๋ ์ง์ ํ๋ ํธ์ด ์ข๋ค!
    - ์๋ํ๋ฉด?

### Status Code๋ฅผ ์ง์ ํ๋ ๋ฐฉ๋ฒ
1. status ์ํฌํธ
2. return์ ์ฝ๋ ๋๋ฒ ์์ฑ
    - return Response({}, status=...) ์ ํ์์ผ๋ก ์์ฑํ๋ค

Status Code ์ฌ์ฉ์์
```python
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        # some error
        return ResPonse({"error": "some error message"}, status=status.HTTP_400_BAD_REQUEST)
        return ResPonse({"error": "some error message"}, status=400)
        return Response({"msg": "login success!"}, status=status.HTTP_200
        )
```

## โ settings.py ์ ์์ฃผ ์ฌ์ฉํ๋ ์ค์ 
### ๐ต๏ธโโ๏ธ SQL ๋๋ฒ๊น ๋ก๊ทธ
ORM์ ์ ๊ทผํ  ๋ ๋ง๋ค ์ด๋ค ์ฟผ๋ฆฌ๊ฐ ์์ฑ๋์๋์ง ๋ณด์ฌ์ฃผ๊ณ , ๊ทธ ์๋ ๋ํ ํ์๋๋ค.
    - ์ด๋ฅผ ํตํด์ ์ด๋ ๋ถ๋ถ์์ ๋ฉ๋ชจ๋ฆฌ ์ด์๊ฐ ์๋์ง, ํ๋ก๊ทธ๋จ์ด ๋๋ ค์ง๋์ง ํ์ธํ  ์ ์๋ค!
```python
# https://docs.djangoproject.com/en/1.11/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
```

## ๐ฉ ์ปค์คํ ์ ์  ๋ชจ๋ธ admin
์ปค์คํ์ผ๋ก ์ ์  ๋ชจ๋ธ์ ์์ฑํ๊ณ , admin.py์ ๋ชจ๋ธ์ ๋ฑ๋กํ ๋ค ๊ด๋ฆฌ์ ํ์ด์ง์์ ๋ ์ฝ๋๋ฅผ ๊ด๋ฆฌํ  ๋, ์ฌ์ฉ์ ๋น๋ฐ๋ฒํธ๊ฐ ํด์ฑ๋์ง ์๊ณ  ํ๋ฌธ์ผ๋ก ์์ฑ๋์ด ์ฌ์ฉํ  ์ ์๋ ํ์์ด ๋ฐ์ํ๋ค.

์ด๋ฅผ ํด๊ฒฐํ๊ธฐ ์ํด UserAdmin ์ค์ ์ ํด์ฃผ์ด์ผ ํ๋ค!

```python 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date', )}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),
    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )

admin.site.register(UserModel, UserAdmin)
```

1. UserAdmin as BaseUserAdmin ์ํฌํธ
    - ๊ธฐ์กด UserAdmin์ BaseUserAdmin์ผ๋ก ๋ณ๊ฒฝํ๋ค. 
    - ์์ํ๊ธฐ ์ํ ํด๋์ค์ด๋ฏ๋ก Base๋ฅผ ๋ถ์ฌ์ฃผ์ด ๊ฐ๋์ฑ์ ๋์ด๋ ๋ฏ ํ๋ค
2. class UserAdmin ์์ฑ
    - ์ด๋ฆ์ ์์ ๋กญ๊ฒ ์ง์ ๊ฐ๋ฅํจ
3. register์ ๋ฑ๋ก
    - ์์ฑํ ํด๋์ค๋ฅผ admin.site.register์ ์ฌ์ฉํ  ๋ชจ๋ธ๊ณผ ๊ฐ์ด ๋ฑ๋ก


## ๐ฅ Permission class ์ฌํ
### ๐ admin์ ๋ชจ๋ ๊ฐ๋ฅํ๊ณ , ๋ก๊ทธ์ธ ์ฌ์ฉ์๋ ์กฐํ๋ง ๊ฐ๋ฅํ Permission
์ปค์คํ ํผ๋ฏธ์์ ํตํด์ ์ฌ์ฉ์๊ฐ ์ด๋๋ถํฐ ์ด๋๊น์ง ์ ๊ทผํ  ์ ์๋์ง ์์ธํ๊ฒ ์กฐ์ํ  ์ ์๋ค.

์๋์ ๊ฒฝ์ฐ๋ ๊ด๋ฆฌ์ ๊ณ์ ์ธ ๊ฒฝ์ฐ ๋ชจ๋  ๊ฒ์ ์ ๊ทผ์ด ๊ฐ๋ฅํ์ง๋ง, ๋ก๊ทธ์ธํ ์ฌ์ฉ์๋ ์กฐํ๋ง ๊ฐ๋ฅํ๋๋ก ์ค์ ํ๋ค!

```python
from rest_framework.exceptions import APIException

class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    """
    admin ์ฌ์ฉ์๋ ๋ชจ๋ ๊ฐ๋ฅ, ๋ก๊ทธ์ธ ์ฌ์ฉ์๋ ์กฐํ๋ง ๊ฐ๋ฅ
    """
    SAFE_METHODS = ('GET', )
    message = '์ ๊ทผ ๊ถํ์ด ์์ต๋๋ค.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "์๋น์ค๋ฅผ ์ด์ฉํ๊ธฐ ์ํด ๋ก๊ทธ์ธ ํด์ฃผ์ธ์.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and user.is_admin:
            return True
            
        if user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
        
        return False
```
์ฐธ๊ณ ์ฌํญ
1. SAFE_METHOD๋ฅผ ํตํด์ ํน์  HTTP METHOD ๋ง๋ค ๋ค๋ฅธ ๊ถํ์ ์ค์ ํ  ์ ์๋ค!
    - ์กฐํ, ์์ฑ์ ๊ฐ๋ฅํ๊ฒ ํ๋ค๋ฉด ```('GET', 'POST', )``` ์ฒ๋ผ ์์ฑํ๋ฉด ๋๋ค
2. ๊ด๋ฆฌ์/๋ก๊ทธ์ธ ๊ณ์  ์ด์ธ์ ์  3์ ๋ถ๊ธฐ์ธ ๋น๋ก๊ทธ์ธ ์ฌ์ฉ์์ ๋ํ GenericAPIException
    - ๊ด๋ฆฌ์ ๊ณ์ ๋, ๋ก๊ทธ์ธํ ๊ณ์ ๋ ์๋ ๋ถ๊ธฐ๊ฐ ์กด์ฌํ๋ค. ๋ฐ๋ก ๋ก๊ทธ์ธ ํ์ง ์์ ์ฌ์ฉ์!
    - ๋ก๊ทธ์ธ ํ์ง ์์ ์ฌ์ฉ์๋ ์์ ๊ถํ์ด ์๋ ๊ฒฝ์ฐ์ด๋ฏ๋ก ์์ ํ๋ ๋ถ๊ธฐ๊ฐ ๋ค๋ฅด๋ค!
    - class GenericAPIException์ ์์ฑํ๊ณ , ๋ก๊ทธ์ธ ์กฐํ ํ ๋น๋ก๊ทธ์ธ์ด๋ผ๋ฉด exception์ผ๋ก ๋ณด๋ด๋ฒ๋ฆฐ๋ค
    - ์ปค์คํ ํผ๋ฏธ์ ๋ด๋ถ์ ์ ๊ทผ ๊ถํ ์์ ๋ฉ์์ง๋ ๊ด๋ฆฌ์ ์ด์ธ์ ๋ก๊ทธ์ธํ ์ ์  ์ค ๊ถํ์ด ์๋ ๋ถ๋ถ์ ๋ํ ์๋ฆผ ๋ฉ์์ง์ด๋ค!
3. views.py ์ ํผ๋ฏธ์์ ์ํฌํํ๊ณ  POSTMAN์ผ๋ก ํ์คํธํด๋ณด์
    - is_admin์ ์ฒดํฌ๋์ด ์์ง ์์ ์ ์ (adminํ์ด์ง์์ ํ์ธ ๊ฐ๋ฅ)๋ ๋ฉ์์ง์ ํจ๊ปPOST ์ ๊ทผ์ด ๊ฑฐ๋ถ๋๋ค.
        - detail : ์ ๊ทผ ๊ถํ์ด ์์ต๋๋ค.
    - ๋ก๊ทธ์ธ ํ์ง ์์ ์ฌ์ฉ์๋ ๋ฉ์์ง์ ํจ๊ป API ์ ๊ทผ ์์ฒด๊ฐ ๊ฑฐ๋ถ๋๋ค.
        - detail : ์๋น์ค๋ฅผ ์ด์ฉํ๊ธฐ ์ํด ๋ก๊ทธ์ธ ํด์ฃผ์ธ์
    - admin ๊ณ์ ์ ๋ชจ๋  ๊ถํ์ ์ ๋๋ก ์ ๊ทผํ๋ค!

## ๐ฅ django admin ์ฌํ

```python
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date', )}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),
    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )
```

### list_display
    - admin์์ ํ์ด๋ธ ํ์์ผ๋ก ๋ณด์ฌ์ค ํ๋
### list_display_link
    - ํด๋ฆญ ์ ์์ธ ํ์ด์ง๋ก ๋ค์ด๊ฐ ์ ์๋ ํ๋
### list_filter
    - filter๋ฅผ ์ ์ฉํ  ์ ์๋ ํ๋
### search_fields
    - ๊ฒ์์ฐฝ์ด ์๊ธฐ๊ณ , ๊ฒ์ ๋ฐ์ ํญ๋ชฉ ํ๋
### fieldsets
    - ์์ธ ํ์ด์ง๋ฅผ ๋ ๊น๋ํ๊ฒ ๋ณผ ์ ์์
### readonly_fields
    - ์์ ํ  ์ ์์ง๋ง ๋ณผ ์ ์๊ฒ ๋ง๋ค ํ๋
    - ์์ฑํ  ๋๋ ์ ์ ์ ์๊ณ , ์์ ์ ๋ถ๊ฐ๋ฅํ๊ฒ ํ๋ ค๋ฉด?
        - ๋ณ์๊ฐ ์๋ ํจ์ get_readonly_fields๋ก ์์ฑํด์ผ ํ๋ค!

### tabularinline / stackline
    - ์ญ์ฐธ์กฐ๊ด๊ณ์์๋ง ๊ฐ๋ฅํ ์ด๋๋ฏผ์์ ์ญ์ฐธ์กฐ ๋ชจ๋ธ๋ ๊ฐ์ด ๋ณด์ฌ์ค
    - tabularline์ ์ธ๋ก, stackline์ ๊ฐ๋ก๋ก ๋ณด์ฌ์ค
        
### filter_horizontal
    - ํ๋๋ฅผ ๋ฃ์ด 