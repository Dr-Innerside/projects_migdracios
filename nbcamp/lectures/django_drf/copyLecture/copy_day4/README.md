# Django Rest Framework day4

## ๐ 4์ผ์ฐจ ๊ฐ์ ๋ชฉํ
- ์ธ๋ ํค์ ๋ํ ์ดํด
- ์ญ์ฐธ์กฐ์ ๋ํ ์ดํด
- drf Serializer์ ๋ํ ์ดํด

### ๐ฉ ์ธ๋ํค์ ๋ํ ์ดํด
์ธ๋ ํค์ ์ข๋ฅ
#### 1. ForeignKey
- one-to-many ํํ๋ก ํน์  ํ์ด๋ธ์์ ๋ค๋ฅธ ํ์ด๋ธ์ ์ฐธ์กฐํ  ์ ์๋ค.
- ์์๋ก ์ํ๊ด๊ณผ ์์ฒญ์์ ๊ด๊ณ๋ฅผ ๋ํ๋ผ ๋, ์์ฒญ์ ํ์ด๋ธ์์ ์ํ๊ด ํ์ด๋ธ์ FK๋ก ์ฐธ์กฐํ  ์ ์๋ค.

#### 2. OneToOneField
- one-to-one ํํ๋ก FK์ ๋์ผํ์ง๋ง, ์ผ๋์ผ ๊ด๊ณ๋ง ๊ฐ๋ฅํ๋ค.
- ์ฌ์ฉ์ ๊ณ์  ํ์ด๋ธ๊ณผ ์ฌ์ฉ์ ํ๋กํ ํ์ด๋ธ์ด ๋ณ๋๋ก ์กด์ฌํ  ๋, ๊ณ์  ํ์ด๋ธ์ ํ๋กํ์์ ์ผ๋์ผ๋ก ๊ด๊ณ๋ฅผ ๋งบ์ ์ ์๋ค.

##### ๐ต๏ธโโ๏ธ ์ฌ์ฉ์ ํ๋กํ ๋ชจ๋ธ ์์ฑํ๊ธฐ(O:O)
- ์ ์ ์ ์์ธ์ ๋ณด๋ฅผ ๋ด๊ณ  ์๋ UserProfile์ด๋ผ๋ ํ์ด๋ธ์ ์์ฑํ๋ค.
- User ํ์ด๋ธ์์๋ ์ด๋ฆ, ์ด๋ฉ์ผ, ๋น๋ฐ๋ฒํธ ์ด์ธ์ ์๊ธฐ์๊ฐ, ์์ผ ๋ฑ์ ์ ๋ณด๋ฅผ ์ ์ฅํ๋ค.
- User ํ์ด๋ธ์์ ์์ ๋ด์ฉ์ ์ ์ฅํ์ง ์๋ ๊ฒ์ User์์๋ ๋ณด์ ์ ๋ฏผ๊ฐํ ์ ๋ณด๋ง์ ๋ด๊ณ  ์ด์ธ์ ํ๋กํ ์์ธ ๋ด์ฉ์ UserProfile์์ ๋ค๋ฃจ๋ ์ธก๋ฉด์ด ์์
- ์ํ๋ ํ๋๋ฅผ ์์ฑํ๊ณ  ๋ ๋ค, ์ฌ์ฉ์-์ฌ์ฉ์ํ๋กํ ๊ด๊ณ๋ฅผ ์ฐธ์กฐํ์ฌ User๋ฅผ ์ฐธ์กฐํ๋ OneToOneField๋ฅผ ์์ฑํ๋ค.
- FK์ unique=True ์ดํธ๋ฆฌ๋ทฐํธ๋ฅผ ์ถ๊ฐํ ๊ฒ๊ณผ ์ ์ฌํ์ง๋ง ์ผ๋ฐ์ ์ผ๋ก OneToOneField๋ก ์ฌ์ฉํ๋ค.

```python
# user detail info table
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="์ ์ ", on_delete=models.CASCADE)
    introduction = models.TextField("์๊ธฐ์๊ฐ")
    birthday = models.DateField("์์ผ")
    age = models.IntegerField("๋์ด")
    hobby = models.CharField("์ทจ๋ฏธ", max_length=50)

    def __str__(self):
    return f"{self.user.username} ๋์ ํ๋กํ์๋๋ค"

# user - user detail : 1:1
# ํ ์ ์ ๊ฐ ๋ ํ๋กํ์ ๊ฐ์ง ์๋ ์์
```


#### 3. ManyToManyField
- many-to-many ํํ๋ก ํ ๊ฐ์ ํ๋์์ ์ฌ๋ฌ ๊ฐ์ ํ์ด๋ธ์ ์ฐธ์กฐํ  ์ ์๋ค.
- ์ํ๋ผ๋ ํ์ด๋ธ์์ ์นดํ๊ณ ๋ฆฌ ํ์ด๋ธ์ ์ค๋ธ์ ํธ๋ฅผ ์ฐธ์กฐํ๊ณ  ์ถ์ ๋, many-to-many ๊ด๊ณ๋ฅผ ์ฌ์ฉํด ๋ ๊ฐ ์ด์์ ์ค๋ธ์ ํธ๋ฅผ ์ฐธ์กฐํ  ์ ์๋ค.
- O:O, O:M ํํ๋ ํ๋์ ๋์ ๋ง์ ๋ฐ๋ผ๋ณด๊ณ  ์์ง๋ง, M:M์ ์ฌ๋ฌ ๊ฐ์ ๋์์ ๋ฐ๋ผ๋ณด๊ณ  ์์ ์ ์๋ค!

#### Hobby <-> UserProfile(M:M)
1. ์ทจ๋ฏธ ์ด๋ฆ์ด ๋ด๊ธด Hobby Model ์์ฑ
2. UserProfile Model์์ Hobby๋ฅผ ManyToMany๋ก ์ฐธ์กฐ
3. Hobby์ on_delete ์ต์์ SET_NULL
4. FK ์ต์์ Null ํ์ฉ

```python
# hobby table
class Hobby(models.Model):
    name = models.CharField("์ทจ๋ฏธ ์ด๋ฆ", max_length=20)
        
# user detail info table
class UserProfile(models.Model):
    user = models.OneToOneField(to=User, verbose_name="์ ์ ", on_delete=models.CASCADE, primary_key=True)
    ...
    hobby = models.ManyToManyField(Hobby, verbose_name="์ทจ๋ฏธ", null=True)
    ...
```

โ  ์ CASCADE๊ฐ ์๋๊น?
- User <-> UserProfile ์ ๊ฒฝ์ฐ, ์ฐธ์กฐ ์ค์ธ User ์ค๋ธ์ ํธ๊ฐ ์ญ์ ๋๋ฉด UserProfile๋ ์ญ์ ๋์ด์ผ ํ๋ค! ๊ทธ๋ฆฌ๊ณ  ๊ทธ๊ฒ์ ์ํํด์ฃผ๋ ๊ฒ์ด on_delete=CASCADE
- ๊ทธ๋ฌ๋ Hobby <-> UserProfile์ ๊ฒฝ์ฐ, ์ฐธ์กฐ ์ค์ธ Hobby ์ค๋ธ์ ํธ๊ฐ ์ญ์ ๋๋ฉด UserProfile๋ ์ญ์ ๋์ด์ผ ํ๋๊ฐ? ์๋๋ค!
- ๋ฐ๋ผ์ ์ฌ๋ผ์ง ์ทจ๋ฏธ ์ค๋ธ์ ํธ๊ฐ ์ฌ๋ผ์ง๋ฉด Null๋ก ๋น์์ฃผ๋ SET_NULL ์ต์์ ์ฌ์ฉํ๋ค!

### ๐ฅ ์ญ์ฐธ์กฐ์ ๋ํ ์ดํด
#### ๐ค ์ญ์ฐธ์กฐ๊ฐ ๋ญ๋ฐ?
- ์ทจ๋ฏธ<->์ฌ์ฉ์ํ๋กํ์ ๊ด๊ณ์์ ํน์  ์ฌ์ฉ์๊ฐ ์ ํํ ์ทจ๋ฏธ๋ฅผ ๊ฐ์ ธ์จ๋ค๋ฉด ๊ทธ๊ฒ์ ์ ์ฐธ์กฐ๋ผ๊ณ  ํ๋ค.
- ๋ฐ๋ผ์ ์ ์ฐธ์กฐ๋ฅผ ์ฌ์ฉํด์ ์ฌ์ฉ์์ ์ทจ๋ฏธ ์ค๋ธ์ ํธ๋ฅผ ๊ฐ์ ธ์ฌ ์ ์๋ค.
- ๋ฐ๋๋ก ์ฌ์ฉ์ํ๋กํ์์ ์ทจ๋ฏธ๋ฅผ ํ๋ ํน์ ํด ์ด๋ฅผ ์ ํํ ์ ์  ๋ชฉ๋ก์ ๊ฐ์ ธ์ค๋ ๊ฒ์ ๋ฐ๋๋ก ์ญ์ฐธ์กฐ๋ผ๊ณ  ํ๋ค.
- ๋ฐ๋ผ์ ์ญ์ฐธ์กฐ๋ฅผ ์ฌ์ฉํด์ ์ทจ๋ฏธ๋ฅผ ๊ณ ๋ฅธ ์ฌ์ฉ์ ์ค๋ธ์ ํธ๋ฅผ ๊ฐ์ ธ์ฌ ์ ์๋ค.

#### ๐ค ์ญ์ฐธ์กฐ๋ฅผ ์ ์จ์ผํ๋๋ฐ?
- ๋ง์ฝ ํน์  ์ทจ๋ฏธ๋ฅผ ์ ํํ ์ฌ์ฉ์ ์ค๋ธ์ ํธ ๋ฆฌ์คํธ๋ฅผ ๊ฐ์ ธ์ค๊ณ  ์ถ๋ค๋ฉด? ์ ์ฐธ์กฐ๋ก๋ ๊ฐ์ ธ์ฌ ์๊ฐ ์๋ค..!
- ๋ฐ๋ผ์ ์ญ์ฐธ์กฐ๋ฅผ ์ฌ์ฉํด์ผ ํ๋ ๊ฒฝ์ฐ๊ฐ ์กด์ฌํ๋ฉฐ, ๊ฐ๋์ ๋ํ ์ดํด๊ฐ ํ์ํ๋ค! 

#### ๐ ์ญ์ฐธ์กฐ์ ๋ํ ์ดํด
- ์ธ๋ํค๋ฅผ ์ฌ์ฉํด ์ฐธ์กฐํ๋ object๋ฅผ ์ญ์ผ๋ก ์ฐพ์ ์ ์๋ค.
- ์ธ๋ ํค ์ง์  ์ related_name ์ต์์ ์ฌ์ฉํด ์ญ์ฐธ์กฐ์ ์ฌ์ฉ๋  ์ด๋ฆ์ ์ง์ ํ  ์ ์๋ค.
    - models.py์์ related_name์ user_hobby๋ก ์ง์ ํ๋ค๋ฉด hobby.user_hobby์ ๊ฐ์ด ์ฌ์ฉํ๋ค.
- ์ญ์ฐธ์กฐ ์ "relate_name"_set ์ ์ฌ์ฉํ์ฌ ์ญ์ฐธ์กฐ๋ฅผ ์ง์ ํด ์ค๋ค.
    - OneToOneField์ ๊ฒฝ์ฐ์๋ ์์ธ์ ์ผ๋ก _set์ ๋ถ์ด์ง ์๋๋ค!

```python
user_profile.hobby # ์ ์ฐธ์กฐ
hobby.userprofile_set 
# hobby๋ฅผ ์ฐธ์กฐํ๊ณ  ์๋ UserProfile ํ์ด๋ธ์ object๋ฅผ ๊ฐ์ ธ์ด
```

```python
# ์ฌ์ฉ์ ์ ๋ณด ์กฐํ
    def get(self, request):
        user = request.user

        # ์ ์ฐธ์กฐ
        # user_profile = UserProfile.objects.get(user=user)
        # hobbys = user_profile.hobby.all()

        # ์ญ์ฐธ์กฐ
        # User๋ชจ๋ธ์๋ ์๋ userprofile์ ์ฌ์ฉํด์ ๊ฐ์ ธ์ด
        hobbys = user.userprofile.hobby.all()   # OneToOneField๋ ์์ธ๋ก _set์ ๋ถ์ด์ง ์์
        hobbys = str(hobbys)
        
        return Response({"message": f"get method! && hobbys->{hobbys}"})
```

#### โ ์ญ์ฐธ์กฐ๋ฅผ ํ์ฉํด ๋์ ๊ฐ์ ์ทจ๋ฏธ๋ฅผ ๊ฐ์ง ์ฌ๋์ ์ฐพ๋ ์ฝ๋
```python
from django.db.models import F

def get(self, request):
    user = request.user
    hobbys = user.userprofile.hobby.all()
    for hobby in hobbys:
        # exclude : ๋งค์นญ ๋ ์ฟผ๋ฆฌ๋ง ์ ์ธ, filter์ ๋ฐ๋
        # annotate : ํ๋ ์ด๋ฆ์ ๋ณ๊ฒฝํด์ฃผ๊ธฐ ์ํด ์ฌ์ฉ, ์ด์ธ์๋ ์ํ๋ ํ๋๋ฅผ ์ถ๊ฐํ๋ ๋ฑ ๋ค์ํ๊ฒ ํ์ฉ ๊ฐ๋ฅ
        # values / values_list : ์ง์ ํ ํ๋๋ง ๋ฆฌํดํ  ์ ์์. values๋ dict๋ก return, values_list๋ tuple๋ก return
        # F() : ๊ฐ์ฒด์ ํด๋น๋๋ ์ฟผ๋ฆฌ๋ฅผ ์์ฑํจ
        hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).value_list('username', flat=True)
        hobby_members = list(hobby_members)
        print(f"hobby : {hobby.name} / hobby members : {hobby_members}")

# result print
"""
hobby : ์ฐ์ฑ / hobby members : ['user1']
hobby :  ์์๊ฐ์ / hobby memebers : ['user1', 'user2']
hobby : ์ค์ฟ ๋ฒ๋ค์ด๋น / hobby memebers : ['user2']
hobby : ์ฌํ / hobby memebers : ['user2']
"""
```

์ญ์ฐธ์กฐ๋ฅผ ํ์ฉํ์ฌ ํน์  ์ทจ๋ฏธ๋ฅผ ์ ํํ ์ฌ์ฉ์๋ฅผ ๋ถ๋ฌ์ค๋ ๊ธฐ๋ฅ์ด ๊ตฌํ๋์ด ์๋ค.

**๐ต๏ธโโ๏ธ ๋ก์ง ์์ฑ ์์๋ ๋ค์๊ณผ ๊ฐ๋ค.**
1. user.userprofile.hobby.all()
- OneToOne์ผ๋ก ์ฐธ์กฐํ๋ UserProfile ํ์ด๋ธ์ด userprofile๋ก ๋ฐ๋์ด request.user์ ๋ฉ์๋๋ก ๋ฐ๋ก ๋ฐ๋ก ์ญ์ฐธ์กฐ๊ฐ ๊ฐ๋ฅํ๋ค
- _set์ ์ฐ์ง ์๊ณ  user.userprofile์ ์ ์ฅ๋ ๋ด์ฉ ์ค hobby์ ๋ชจ๋  ์ค๋ธ์ ํธ๋ค์ ๊ฐ์ ธ์ค๋ ๊ตฌ๋ฌธ
2. for hobby in hobbys:
- ๋ชจ๋  ์ทจ๋ฏธ ์ค๋ธ์ ํธ๋ค์ ๋ฐ๋ณต๋ฌธ์ผ๋ก ์ฌ๋ผ์ด์ฑํ๋ค.
3. ํน์  ์ทจ๋ฏธ์ ๋ฐ์ดํฐ๋ฅผ ์ญ์ฐธ์กฐํ๋ ์ฌ์ฉ์ with exclude, annotate
- hobby์ userprofile_set์ด๋ผ๊ณ  ์์ฑํ์ฌ ์ญ์ฐธ์กฐ ๋ฐ UserProfile object๋ก return
- exclude(user=user)๋ผ๊ณ  ์์ฑํ์ฌ ๊ทธ ์ค ์๋ ฅ๋ฐ์ ์ฌ์ฉ์๋ ์ ์ธ
- annotate(username=F('user__username'))์ด๋ผ๊ณ  ์์ฑํ์ฌ ์ฟผ๋ฆฌ์ ์์ ์ค๋ธ์ ํธ๋ฅผ ์ด๋ฆ์ ๋ณ๊ฒฝํ์ฌ ์ฟผ๋ฆฌ๋ก ์ ์ฅ
    - annotate(์ด๋ฆ์ ๋ฐ๊ฟ ๋ด์ฉ)
    - username(username์ด๋ผ๋ ๋ฉ์๋๋ก ์์ฑ)=F(UserProfile ์์ user ํญ๋ชฉ-->์ User๋ชจ๋ธ์ username)
    - ์ฟผ๋ฆฌ์ ์ค๋ธ์ ํธ๊ฐ ์๋ username=user1 ์ ์ฟผ๋ฆฌ, ํํ ํํ๋ก ์ ์ฅ
4. .values_list๋ฅผ ์์ฑํ์ฌ username์ด๋ผ๊ณ  ์ ์ฅ๋ ๋ฐ์ดํฐ๋ฅผ ๋ชจ๋ ๋ชจ์ ๋ฆฌ์คํธ๋ก ์ ์ฅ
5. flat=True๋ฅผ ์์ฑํ์ฌ ํํ์ ํด์ ํ ์ฟผ๋ฆฌ์ ํ์์ผ๋ก ์ ์ฅ๋จ
6. list(hobby_members)๋ฅผ ์์ฑํ์ฌ ์ฟผ๋ฆฌ์์ ์ฌ์ฉํ  ์ ์๊ฒ ๋ฆฌ์คํธ๋ก ๋ณํ

โ  ์์ ๊ตฌ๋ฌธ์ ์์งํ๊ณ  ์์ด์ผ ํ์ง๋ง, Serializer๋ก ๋์ฒด๋๋ ๊ฒฝ์ฐ๊ฐ ๋ง๋ค.

## ๐ก dir ๋ฉ์๋์ ๋๋ฒ๊น
- dir ๋ฉ์๋๋ ์ธ์์์ ์ฌ์ฉํ  ์ ์๋ ํด๋์ค ๋ฐ ํจ์๋ฅผ ๋ชจ๋ ์ถ๋ ฅํ๋ค.
- ์ญ์ฐธ์กฐ ์์๋ฅผ ๋ค์ด ์ ์ธํด์ฃผ์ง ์์ userprofile์ ์ด๋์ ๋์๋๊ฐ? ํ๊ณ  ์ฐพ์๋ณด๊ธฐ์ํด dir์ ์ถ๋ ฅํด๋ณธ๋ค
```python
user = request.user # ์๋ ฅ๋ฐ์ ์ ์ 
print(dir(user))    # ์ ์ ์์ ์ฌ์ฉํ  ์ ์๋ ๋ฉ์๋ ๋ณด๊ธฐ
```
- dir์ด ๋๋ฒ๊น์ ์ ๋ฆฌํ ์ ์ ๋น์ฅ ์ฌ์ฉํ  ์ ์๋ ๋ฉ์๋ ์ค ๋ชํํ๊ฒ ๋ณด์ด๋ ๊ฒ์ 
- ๋ฌธ์๋ฅผ ์ฐธ์กฐํ์ฌ ์์ฑํ๋ ๊ฒ๋ณด๋ค ๋น ๋ฅด๊ฒ ์ ์ฉํ  ์ ์๋ค๋ ์ ์ ์๋ค.

## ๐ก eval ๋ฉ์๋
- eval ๋ฉ์๋ ๋ด๋ถ์ ์ธ์๋ฅผ ๋ฌธ์์ด๋ก ์์ฑํ์ฌ ๋ฉ์๋๋ฅผ ์ ์ฉํ  ์ ์๋ค.
- dir ๋ฉ์๋์ ๋ณ์ฉํ์ฌ ๋๋ฒ๊น์ ์์ํ๊ฒ ์๋ํ  ์ ์๋ค.
- โ ๊ทธ๋ฌ๋ delete์ ๊ฐ์ ๋ฉ์๋๊ฐ ํฌํจ ๋  ์ ์์ด ์ฃผ์ํด์ผ ํ๋ฉฐ, ๋ํ ๋๋ฒ๊น ์ด์ธ์ ์ค์  ํ๋ก์ ํธ ๋ด๋ถ์์๋ ์ฌ์ฉํด์๋ ์๋๋ค!!
    - ์์์  ์ฌ์ฉ์(ํด์ปค)๊ฐ ์์๋ก eval ๋ฉ์๋์ ๊ฐ๋ฅ์ฑ์ ๊ฐ์ํ์ฌ ์ ๋ง์ ๋ฉ์๋๋ฅผ ์๋ ฅ ๊ฐ์ ์๋ํ๊ฒ ๋๋ค๋ฉด,
    - ๊ฐ๋ฐ์์ ์๋ ์ด์ธ์ ๋ถ์ ์  ๋ฐฉํฅ์ผ๋ก ํ๋ก์ ํธ๊ฐ ์์ ๋  ๊ฐ๋ฅ์ฑ์ด ์๊ธฐ ๋๋ฌธ์ด๋ค!

```python
print(eval("1+1")) # ์ ๊ฐ์ ๋ชจ์ต์ผ๋ก ์ ๊ณ์ฐ๋ ๊ฐ๋ฅํ๋ค.
```
```python
# dir, eval ๋ฉ์๋๋ฅผ ์ฌ์ฉํด ์๋ํ๋ ๋ฉ์๋ ํ์ธํ๊ธฐ

hobbys = user.userprofile.hobby
for command im dir(hobbys):
    try:
        print(f"command: {command} / ", eval(f"hobbys.{command}()"))
        print(f"command: {command} / ", eval(f"hobbys.{command}"))
    except:
        pass
```

## โญ DRF Serializer
Serializer, ์ง๋ ฌํ๋?
- django์ object, queryset ์ธ์คํด์ค ๋ฑ ๋ณต์กํ ๋ฐ์ดํฐ๋ค์ JSON๊ฐ์ ๋ค๋ฅธ ์ปจํ์ธ  ์ ํ์ผ๋ก ์ฝ๊ฒ ๋ณํํ  ์ ์์

### ๐ค Serializer๋ฅผ ์ฌ์ฉํ์ ๋์ ์ฅ์ ์ ๋๋์ฒด ๋ฌด์์ธ๊ฐ?
- ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์ค๊ณ  ๋ฆฌํดํด์ฃผ๋ ๊ฒ์ด๋ผ๋ ์ธก๋ฉด์ ๋ณผ ๋๋ '๊ตณ์ด ์จ์ผํ๋?' ๋ผ๋ ์๊ฐ์ด ๋ ๋ค.
- ๊ทธ๋ฌ๋ ๊ฐ์ ธ์ฌ ๋ฐ์ดํฐ๊ฐ ๋ ์ด์์ ํ์ด๋ธ๋ถํฐ ์ธ์ธํ๊ฒ ๋ฐ์ดํฐ๋ฅผ ์ถ๋ ค๋ด ํ๋๋ก ๋ฌถ์ด ๋ณด์ฌ์ฃผ๊ณ  ์ถ๋ค๋ฉด?
- ์ด๋ฐ ๋ฐ์ดํฐ ์ ์ ๋ฅผ view์์ ์ฌ์ฉํ๋ฉด ๊ฐ๋์ฑ๋ ๋ณ๋ก ์ข์ง ์์ ๊ฒ์ด๋ฉฐ, ๋์ฑ ๋ณต์กํด ์ง ๊ฒ์ด๋ค!
- Serializer๋ฅผ ์ฌ์ฉํ๋ ๊ฒ์ผ๋ก ๋ณต์กํ ๋ฐ์ดํฐ๋ฅผ ์ ์ ํ๋๋ฐ ์ต์ ํ ๋์ด ์์ผ๋ฉฐ, ์ฌ์ฉ์ฑ, ๊ฐ๋์ฑ ๋ํ ๋ฐ์ด๋๋ค!
- OPEN API์ธ ๋ฏธ์ธ๋จผ์ง ๋ฐ์ดํฐ ๋ฑ๊ณผ ์ ์ฌํ JSON ํ์์ ๋ฐ์ดํฐ๋ฅผ ์ถ๋ ฅํ  ์ ์๋ค!

### ๐ Serializer ์ฌ์ฉ๋ฒ
๐ต๏ธโโ๏ธ ์ฌ์ฉ์์

```python
# serializers.py
from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
```
```python
# views.py
from .serializers imoprt UserSerializer

def get(self, request):
    return Response(UserSerializer(request.user).data)
```
1. serializers.py ํ์ผ ์์ฑ
2. serializer ํด๋์ค ์์ฑ
- ๋ช์นญ์ ํฌ๊ฒ ์ค์ํ์ง ์์ผ๋,
- ์ฌ์ฉ์ ์ง๋ ฌ ํด๋์ค๋ผ๋ฉด User + Serializer ๋ฑ์ ์ปจ๋ฒค์์ ์งํค๋ฉด ๊ฐ๋์ฑ์ด ์ข๋ค

3. meta ํด๋์ค ์์ฑ
4. model ์ดํธ๋ฆฌ๋ทฐํธ ์์ฑ
- ์ ์ฉํ  ๋ชจ๋ธ์ ์ ํํ๋ค. import๋ก ๋ชจ๋ธ์ ๋ฏธ๋ฆฌ ๊ฐ์ ธ์์ค์ผ ์ฌ์ฉํ  ์ ์๋ค.

5. fields ์ดํธ๋ฆฌ๋ทฐํธ ์์ฑ
- ์ ์ฉํ  ํ๋๋ฅผ ์ ํํ๋ค. ๋ชจ๋  ๊ฒ์ ๊ฐ์ ธ์ค๊ณ  ์ถ์๋๋ ```"__all__"```์ ์ฌ์ฉํ๋ค.
- ๊ฐ์ ธ์ค๊ณ  ์ถ์ ํ๋๊ฐ ์๋ค๋ฉด ```["field1", "field2"]``` ์ ๊ฐ์ด ์์ฑํ๋ค
- ํ๋๋ ๋ง๋ค๊ณ  ์ถ์ ๋๋ก ๋ง๋๋ ๊ฒ์ด ์๋๋ค! ์์ฑ๋์ด ์๋ ํ๋๋ฅผ ์คํ ์์ด ๊ฐ์ ธ์์ผ ํ๋ค.

6. view์์ import serializer 
- ์ค์  view์์ API๋ฅผ ์์ฑํ๊ธฐ ์ํด์ Serializer๋ฅผ ์ฌ์ฉํ๋ ๊ฒ์ด๋ฏ๋ก ์ํฌํ!

7. return Response์ serializer ์ ์ฉํ๊ธฐ
- ์์ฑํ Serializer๋ฅผ Response์ ์ ์ฉํ  ๋ฐ์ดํฐ๋ฅผ ์ธ์๋ก ๋ด๋๋ค.
- ``` return Response(UserSerializer(user).data) ``` ๊ณผ ๊ฐ์ด ์ฌ์ฉํ๋ฉฐ, request.user์๋ ๋ณ์ user๋ฅผ ์ธ์๋ก ๊ฐ์ ธ๊ฐ ๊ฒ.
- ๐ ๋ณด๋ด๊ณ  ๋ฐ๋ ๋ฐ์ดํฐ ๋ฐฉ์์ JSON ์ด๊ธฐ ๋๋ฌธ์ serializer().data ํ์์ผ๋ก ํญ์ ์์ฑํ๊ฒ ๋๋ค!

### ๐ฅ OneToOneField ๋ฐ์ดํฐ๋ฅผ Serializer ์ถ๊ฐ
์๋ ฅ๋ฐ์ ์ฌ์ฉ์์ ์ ๋ณด(์์ด๋,๋น๋ฐ๋ฒํธ,์ด๋ฉ์ผ,ํ๋ค์ ๋ฑ)์ ์ฌ์ฉ์ ํ๋กํ์ ๋ณด(์์ผ, ์๊ฐ, ๋์ด ๋ฑ)๋ฅผ ์ถ๊ฐ๋ก ๊ฐ์ ธ์ฌ ๊ฒ์ด๋ค.

```python
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer() # object

    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date", "userprofile"]
```

โ  OneToOneField์ ๊ฒฝ์ฐ์๋ Serializer๋ก ๊ฐ์ ธ์จ ๊ฐ์ด object์ด๋ค!
- OneToOne ๊ด๊ณ๋ก ๊ฐ์ ธ์จ ๊ฒฝ์ฐ์๋ _set์ ์ถ๊ฐํ์ง ์๊ณ ๋ ๋ฐ๋ก ์ฐธ์กฐ๊ฐ ๊ฐ๋ฅํ๊ธฐ ๋๋ฌธ์
- UserSerializer ํด๋์ค Meta fields์ userprofile ์ด๋ฆ์ผ๋ก ๊ทธ๋๋ก ๊ฐ์ ธ์จ๋ค!
- ์ด๋ ๊ฒ ๋ฐ๋ก ์ฌ์ฉํ  ์๊ฐ ์๋ค!

### ๐ฅ ManyToManyField ๋ฐ์ดํฐ๋ฅผ Serializer๋ก ์ถ๊ฐ
์ฌ์ฉ์ ํ๋กํ ์ค์์ ManyToMany ๊ด๊ณ๋ฅผ ๊ฐ๋ ํ๋ ์ทจ๋ฏธ๋ฅผ HobbyModel์์ ์ถ๊ฐ๋ก ๊ฐ์ ธ์ค๊ณ  ์ถ๋ค!

```python
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyModel
        fields = ["name"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True) # input data๊ฐ queryset์ผ ๊ฒฝ์ฐ many=True ์ต์ ํ์

    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby"]
```

โ  ManyToManyField์ ๊ฒฝ์ฐ์๋ Serializer๋ก ๊ฐ์ ธ์จ ๊ฐ์ด queryset์ด๋ค!
- ManyToMany ๊ด๊ณ๋ก ๊ฐ์ ธ์จ ๊ฒฝ์ฐ, ์๋ฆฌ์ผ๋ผ์ด์ ์ ๋ฐ์ดํฐ ํ์์ queryset์ด๊ธฐ ๋๋ฌธ์ ๋ฐ๋ก ๊ฐ์ ธ๋ค ์ธ ์ ์๋ค.
- ๋ง์ฐฌ๊ฐ์ง๋ก ํ๋กํ์ ๋ฉํ ํ๋์ ์ทจ๋ฏธ ํ๋๋ฅผ ์ถ๊ฐํด์ค ๋ค, ์ทจ๋ฏธ ํ๋๋ฅผ ์๋ฆฌ์ผ๋ผ์ด์ ๋ก ๋ฐ๊ฟ์ฃผ๋ฉด์ many=True ๋ฅผ ์ถ๊ฐ๋ก ์์ฑํด ์ฃผ์ด์ผ ํ๋ค.
- ์ด๋ฐ ์ทจ๋ฏธ ํ๋๋ฅผ ์ ์  ์๋ฆฌ์ผ๋ผ์ด์ ์์๋ ์ฌ์ฉํ  ์ ์์ง๋ง, ์ถ๊ฐ์ ์ธ ์์์ด ํ์ํ๋ค!

### ๐ฅ Serializer๋ฅผ ์ฌ์ฉํ์ฌ ๊ฐ์ ์ทจ๋ฏธ๋ฅผ ๊ฐ์ง๊ณ  ์๋ ์ ์ ๋ฅผ ์ญ์ฐธ์กฐ๋ก ๊ฐ์ ธ์ค๊ธฐ
- ์๋๋ ์๋ฆฌ์ผ๋ผ์ด์  ๋ฉํ์ ํ๋๋ ์๋ ์ด๋ฆ์ ์์ฑํ  ์ ์์ง๋ง, SerializerMethodField()๋ฅผ ์ฌ์ฉํ์ฌ ์ถ๊ฐํด์ค ์๋ ์๋ค!

```python
class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        # return "TEST" # ํ๋ ์ฝ๋ฉ
        user_list=[]
        # print(f'obj->{obj}, type(obj)->{type(obj)}') # hobby model์ object
        # print(dir(obj)) # userprofile_set ์ด ์๋ค?!
        # print(obj.userprofile_set.all())
        '''
        ๋ฐฉ๋ฒ 1. ๋ฐ๋ณต๋ฌธ
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)
        return user_list
        '''
        # ๋ฐฉ๋ฒ 2. List Comprehension
        return [up.user.username for up in obj.userprofile_set.all()]

        class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]
```

1. SerializerMethodField ๋ณ์ same_hobby_users ์ถ๊ฐํ๊ธฐ
2. def get_๋ณ์ ํจ์ ์ถ๊ฐํ๊ธฐ
- ๋ฐ๋์ ๋ณ์ ์ด๋ฆ ์์ ```get_```๊ฐ ๋ค์ด ์์ด์ผ ํ๋ค!!
- ํจ์๋ self, obj๋ฅผ ์ธ์๋ก ๋ฐ๋๋ค
- ๋ฆฌํด ๊ฐ์ ๋ฌด์์ ๋ฃ๋๋์ ๋ฐ๋ผ ์ ๋์ ์ธ ๊ฐ์ ๋ฃ์ ์ ์๋ ํ๋๋ฅผ ๋ง๋ค ์ ์๋ค.
3. ํจ์ get_same_hobby_users ์ญ์ฐธ์กฐ ๋ฐ์ดํฐ ๋ฐ์ดํฐ ์ ์ , ๋ฆฌํด
- obj๋ก ๋ฐ์์จ ๊ฐ์ ๋ฑ์ฐ, ์ด๋ ๋ฑ๋ฑ์ ์ทจ๋ฏธ ์ด๋ฆ๋ค์ด๋ค.
- dir(obj)๋ก ์ฌ์ฉํ  ์ ์๋ ๋ฉ์๋๋ฅผ ์ฐพ๋๋ค. M:M์ผ๋ก ์ฐธ์กฐ ์ค์ธ UserProfile์ ์ญ์ฐธ์กฐ ํ  ์ ์๋ userprofile_set์ด ์กด์ฌํ๋ค!
- ๊ฐ ์ทจ๋ฏธ๋ฅผ ๊ฐ์ง๊ณ  ์๋ ์ ์ ๋ฅผ ์ญ์ฐธ์กฐ๋ก ๊ฐ์ ธ์ค๋๋ก obj.userprofile_set.all() ๋ฉ์๋๋ฅผ ๊ฐ๊ฐ ์ทจ๋ฏธ๋ง๋ค ๋ณผ ์ ์๊ฒ ๋ฐ๋ณต๋ฌธ์ ์ฌ์ฉํ๋ค.
- ๋น ๋ฆฌ์คํธ์ ์ฌ๋ผ์ด์ฑ ๋ ์ฟผ๋ฆฌ์์ ์ดํ๋ฉํ๋ค.
- ์ทจ๋ฏธ๋ง๋ค ์ ํํ ์ ์ ๋ค์ ๋ฐ์ดํฐ๊ฐ ๋ด๊ธด ๋ฆฌ์คํธ๋ฅผ ๋ฆฌํดํ๋ค.
4. ๋ฉํ ํ๋์ same_hobby_users ์ถ๊ฐํ๊ธฐ
5. view์์ UserSerializer(user) ๋ก Response๋ฅผ return ํ๋ค.
- UserSerializer->UserProfileSerializer->HobbySerializer ๋ฅผ ๋ชจ๋ ํ๊ณ  ๊ฐ๋ฉด์ ์ ์ ๋ ํ๋์ JSON ๋ฐ์ดํฐ๋ฅผ ๋ฐ์ ๋ณผ ์ ์๋ค.

### ๐ฅ request.user๊ฐ ์๋ ํ์๊ฐ์ํ ์ ์ฒด ์ ์ ๋ฅผ ๋์์ผ๋ก ๋ฐ์ดํฐ ๊ฐ์ ธ์ค๊ธฐ
```python
# views.py

def get(self, request):
    all_users = UserModel.objects.all()
    return Response(UserSerializer(all_users, many=True).data)

```
1. ์ ์ฒด ์ ์ ๋ฅผ ์ฟผ๋ฆฌ์์ผ๋ก ๋ฐ์์ค๊ธฐ
2. ์ ์ฒด ์ ์  ๋ฐ์ดํฐ๊ฐ ํ ๊ฐ๊ฐ ์๋๋ฏ๋ก return Response์ many=True ์์ฑ

### ๐ก Serializer source๋ฅผ ์ฌ์ฉํด JSON ๋ฐ์ดํฐ ํ๋ ์ด๋ฆ ๋ณ๊ฒฝํ๊ธฐ
```python
class UserSerializer(serializers.ModelSerializer):
    user_detail = UserProfileSerializer(source="userprofile") # object

    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date", "user_detail"]
```

- Serializer source ์์ฑ์ผ๋ก ์๋ ํ๋๋ฅผ ์ง์ ํ๊ณ , ๋ณ์ ์ด๋ฆ์ ์ํ๋ ์ด๋ฆ์ผ๋ก ๋ณ๊ฒฝํ๋ค.
- ๋ฉํ ํ๋์ ๋ณ์๋ฅผ ๋ฃ์ด์ค๋ค.

## ๐ฉ permission_classes๋ฅผ ํ์ฉํ ์ ๊ทผ ๊ถํ ์ค์ 
### ๐ permission ๋ผ์ด๋ธ๋ฌ๋ฆฌ ํด๋์ค ํ์ธํ๊ธฐ
๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ํ๊ณ  ๋ค์ด๊ฐ๊ธฐ
- OperationHolderMixin
- SingleOperandHolder
- BasePermissionMetaclass
- AllowAny
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly
- DjangoModelPermissions
- DjangoModelPermissionsOrAnonReadOnly 
...

### ๐ต๏ธโโ๏ธ AllowAny
- ๋ฌด์กฐ๊ฑด True ๋ฐํ

### ๐ต๏ธโโ๏ธ IsAuthenticated
- is_authenticated ๋ฉ์๋ ํ์ธ ํ Bool ๋ฐํ

### ๐ต๏ธโโ๏ธ IsAdminUser
- is_staff ๋ฉ์๋ ํ์ธ ํ Bool ๋ฐํ

### ๐ต๏ธโโ๏ธ IsAuthenticatedOrReadOnly
- request.method in SAFE_METHOD ์ฆ, http method ๊ฐ get์ด๊ฑฐ๋
- ์ธ์ฆ๋ ์ฌ์ฉ์๋ผ๋ฉด True ๋ฐํ

### โ ํผ๋ฏธ์์ ์ดํด
- ํผ๋ฏธ์ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ํ๊ณ  ๋ค์ด๊ฐ์ ๋ค์ํ permission ์กฐ๊ฑด๋ค์ด ์กด์ฌ ํ๋ค๋ ๊ฒ์ ์ ์ ์๋ค.
- ํด๋์ค๋ฅผ ํ์ธํด์ ์ปค์คํ ํผ๋ฏธ์์ ์์ฑํ  ์๋ ์๋ค.
    - ์์๋ก, ๊ฐ์ 7์ผ ์ด์์ธ ์ฌ์ฉ์๋ง True๋ฅผ ๋ฐํํ๋ ํผ๋ฏธ์
- ํผ๋ฏธ์์ ํ๋ ๋ฟ๋ง์ด ์๋ ๋ ์ด์, ํน์ ์ ์ฒด ํ๋ก์ ํธ์์ ๋ชจ๋ ์ฌ์ฉํ๋ ๋ฒ์ฉ์ฑ์ด ์์ผ๋ฏ๋ก, ํ๋์ ์ฑ ์์ด ์๋ ํ๋ก์ ํธ์์ ์์ฑํ๋ค!

### ๐ฉ ์ปค์คํ ํผ๋ฏธ์ ์์ฑํ๊ธฐ!
1. ํ๋ก์ ํธ์ permissions.py ํ์ผ์ ์์ฑํ๋ค.
2. ๋ผ์ด๋ธ๋ฌ๋ฆฌ์ ์๋ฌด ํผ๋ฏธ์์ด๋ ํ๋ ๊ฐ์ ธ์จ๋ค!
```python
from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermision):
    """
    Allow access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
```
3. โ  ํด๋์ค ์ด๋ฆ๊ณผ ํผ๋ฏธ์์ ์ฌ์ฉ๋  ๋ก์ง์ ๋ณ๊ฒฝํ๋ค.
4. views.py์ import ํผ๋ฏธ์
```python
# views.py

from ai.permissions import MyCustomPermission
```
5. ์ปค์คํ ํผ๋ฏธ์์ ์ฌ์ฉํ  ํจ์ ์์ ๋ฃ์ด์ค๋ค.
```python
def get(self, request):
    permission_classes = [MyCustomPermission]
```

### ๐ฅ ๊ฐ์์ผ์ด 7์ผ ์ด์์ธ ์ ์ ์๊ฒ๋ง True๋ฅผ ๋ฐํํ๋ ์ปค์คํ ํผ๋ฏธ์
```python
from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta

class RegistedMoreThanAWeekUser(BasePermission):
    def ha_permission(self, request, view):
        # ์ฌ์ฉ์ ์ธ์ฆ ํ์ธ
        user = request.user
        if not user or not user.is_authenticated:
            return False
        
        # DateField : 2020-10-01
        # DateTimeField : 2020-10-10 10:22:21

        """
        ๊ฐ์์ผ : 6/01
        ํ์ฌ - 7์ผ : 6/10 - 7 = 6/03
        ๊ฐ์ํ ๋ ์ง๋ก๋ถํฐ 7์ผ ๋ค์ธ 6/08์ผ๋ถํฐ ํผ๋ฏธ์์ True๊ฐ ๋๋ฏ๋ก,
        if ๊ฐ์์ผ < ํ์ฌ - 7์ผ : True
        True False ๋ฐํํ๊ธฐ ๋๋ฌธ์ if๊ฐ ์์ด๋ ์ ์ฉ๋จ!
        """
        print(f"user join date -> {user.join_date}")
        print(f"now date -> {datetime.now().date()}")
        print(f"a week ago -> {datetime.now().date()-timedelta(days=7)}")
        return bool(user.join_date < (datetime.now().date()-timedelta(days=7)))
```