## π λͺ©μ°¨

1. [Service](#-service)
2. [κ°λ° κΈ°κ°](#-κ°λ°-κΈ°κ°)
3. [κ°λ° μΈμ](#-κ°λ°-μΈμ)
4. [μκ΅¬μ¬ν­ λ° λΆμ](#-μκ΅¬μ¬ν­-λ°-λΆμ)
5. [κΈ°μ  μ€ν](#-κΈ°μ -μ€ν)
6. [API Endpoints](#api-endpoints)
7. [ERD](#-erd)
8. [API λͺμΈμ](#-api-λͺμΈμ)

## π Service
μ£Όμ΄μ§ κ³ κ° ν¬μ λ°μ΄ν°λ₯Ό μλ΅νλ REST API κ°λ°
## π κ°λ° κΈ°κ°
- 2022.09.16 ~ 2022.09.21(6μΌ)

## π§π»βπ» κ°λ° μΈμ(1λͺ)
- λ°λ―Όν

## π μκ΅¬μ¬ν­ λ° λΆμ
1. λ°μ΄ν° μμ ν¬ν¨λ νΉμ  κ³ κ°μ μμ° μ λ³΄λ₯Ό μ‘°ννλ API

2. μλ νλ©΄μμ νμν μ‘°ν API
- ν¬μ νλ©΄
  - κ³μ’λͺ
  - μ¦κΆμ¬
  - κ³μ’λ²νΈ
  - κ³μ’ μ΄ μμ°
- ν¬μμμΈ νλ©΄
  - κ³μ’λͺ
  - μ¦κΆμ¬
  - κ³μ’λ²νΈ
  - κ³μ’ μ΄ μμ°
  - ν¬μ μκΈ
  - μ΄ μμ΅κΈ (μ΄ μμ° - ν¬μ μκΈ)
  - μμ΅λ₯  (μ΄ μμ΅κΈ / ν¬μ μκΈ * 100)
- λ³΄μ μ’λͺ© νλ©΄ API
  - λ³΄μ  μ’λͺ©λͺ
  - λ³΄μ  μ’λͺ©μ μμ°κ΅°
  - λ³΄μ  μ’λͺ©μ νκ° κΈμ‘ (μ’λͺ© λ³΄μ  μλ * μ’λͺ© νμ¬κ°)
  - λ³΄μ  μ’λͺ© ISIN

## π  κΈ°μ  μ€ν
Language | Framework | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">


## π― API Endpoints
| endpoint | HTTP Method | κΈ°λ₯ | response data |
|----------|-------------|------|-------------------|
|/users | GET | νμ μ λ³΄ μ‘°ν |  "id", "username", "email"
|/users/signup | POST | νμκ°μ | "id", "username", "email"
|/users/signin | GET | λ‘κ·ΈμΈ |  "access_token", "refresh_token"
|/users/:id | PATCH| νμ μ λ³΄ μμ  | "id", "username", "email"
|/users/:id | DELETE | νμ μ λ³΄ μ­μ  | 
|/account/:id | GET | ν¬μ/ν¬μμμΈνμ΄μ§ | "user_id", "account_name", "company", "account_number", "total_assests", "total_profit", "rate"
|/account/asset/:id| GET | λ³΄μ μ’λͺ©νμ΄μ§ |  "user_id", holding_name", "asset_group", "market_value", "isin"
|/account/invest/:id | POST | κ±°λ μ λ³΄ λ±λ‘ νμ΄μ§  | 201 Created </br> 401 Unauthorized
|/account/invest/transfer/:id | GET | μκΈ κ±°λ νμ΄μ§  | "μ£Όλ¬Έ μ  μ΄μμ°", "μ£Όλ¬Έ ν μ΄μμ°"

## π ERD
![](https://velog.velcdn.com/images/miracle-21/post/6e8dad6b-ca12-4e62-9f18-690fa72faf31/image.png)
1. User
- νμ μ λ³΄
- λ³΄μν  λΆλΆ: λ‘κ·ΈμΈ μ ν ν°μ΄ λ°κΈλμ§λ§ μμ§ μ¬μ©λλ κ³³μ΄ μλ€.

2. Holding
- ν¬μ μ’λͺ©μ μ’λͺ©λͺ, ISIN, νμ¬κ°, μμ°κ·Έλ£Ή μ λ³΄

3. Acccount
- νμ κ³μ’μ κ³μ’λͺ, κ³μ’λ²νΈ, μ΄ μμ° μ λ³΄

4. Investment
- μ¦κΆμ¬ μ΄λ¦, ν¬μμκΈ μ λ³΄

5. HoldingsRegist
- κ±°λ μ  κ±°λ μ λ³΄λ₯Ό hashingν μ λ³΄.
- κ±°λμ λ³΄: νμ κ³μ’λ²νΈ, νμ μ΄λ¦, μ’λͺ©λͺ, κ±°λλ
- κ³μ’λ²νΈλ JWT, κ±°λλμ ν΄μ νμ΄λΈ μ¬μ©.
![](https://velog.velcdn.com/images/miracle-21/post/8829083d-73b6-427d-99e2-dd57d7e040da/image.png)

6. FinalHolding
- HoldingsRegistμμ λ±λ‘ν κ±°λμ λ³΄ κ²μ¦ ν μ€μ  κ³ κ°μ μμ°μ μλ°μ΄νΈ.

## π μ°Έμ‘° λ¬Έμ
- [postman API λ§ν¬](https://documenter.getpostman.com/view/18832289/2s7Z7YJuGb)

![](https://velog.velcdn.com/images/miracle-21/post/4578c1c3-016c-4bde-9ee1-9273abde90ed/image.gif)

