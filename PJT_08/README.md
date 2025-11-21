# 맞춤 음악 추천 서비스 🎶

## 서비스 개요 📋
이 프로젝트는 맞춤 음악 추천 서비스로, 사용자에게 음악 추천을 제공하고, 다양한 페이지와 기능을 통해 음악을 즐길 수 있습니다.

---

## 📐 서비스 구조

- **메인 페이지**: 기본적으로 서비스에 대한 정보와 주요 기능을 제공합니다.
- **로그인 페이지**: 사용자 인증을 위한 로그인 페이지입니다.
- **마이 페이지**: 사용자 개인 정보와 음악 추천 기록을 확인할 수 있습니다.
- **프로필 수정 페이지**: 사용자가 자신의 프로필을 수정할 수 있는 페이지입니다.

---

## 🖥️ 웹 테마 설정
- **Bootstrap**: 웹의 전체적인 스타일을 설정하는데 Bootstrap을 사용하여 반응형 디자인을 적용했습니다.
  
  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  ```

---

## 🏠 페이지 구성

### 1. 메인 페이지 (`index.html`) 🎉
- 서비스 소개 및 추천 기능을 한눈에 볼 수 있는 페이지입니다.
- 사용자는 여기서 음악을 추천받거나 서비스에 대해 알아볼 수 있습니다.

### 2. 로그인 페이지 (`login.html`) 🔑
- 사용자 로그인 및 회원가입을 위한 페이지입니다.
- 로그인 후 개인화된 음악 추천 서비스를 이용할 수 있습니다.

### 3. 마이 페이지 (`mypage.html`) 👤
- 사용자가 자신의 개인 정보를 확인하고 수정할 수 있는 페이지입니다.
- 추천 받은 음악과 설정을 볼 수 있습니다.

### 4. 프로필 수정 페이지 (`profile_edit.html`) ✏️
- 사용자가 프로필 정보를 수정할 수 있는 페이지입니다.
- 이름, 이메일, 프로필 사진 등을 변경할 수 있습니다.

---

## 🧑‍💻 Django UserModel 생성
- 사용자 정보를 관리하기 위해 **Django UserModel**을 사용하여 로그인 및 회원 가입 기능을 구현했습니다.

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
```


---

## 🛠️ 프로젝트 사용 기술
- **Django**: 백엔드 프레임워크
- **Bootstrap**: 프론트엔드 디자인
- **HTML/CSS/JS**: 페이지 구조 및 인터랙션
- **Python**: 서버 사이드 로직
