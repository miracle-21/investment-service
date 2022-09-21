## 📎 목차

1. [Posting Service](#-posting-service)
2. [개발 기간](#-개발-기간)
3. [개발 인원](#-개발-인원)
4. [요구사항 및 분석](#-요구사항-및-분석)
5. [기술 스택](#-기술-스택)
6. [API Endpoints](#api-endpoints)
7. [ERD](#-erd)
8. [API 명세서](#-api-명세서)

## 🚀Posting Service
주어진 고객 투자 데이터를 응답하는 REST API 개발
## 📆 개발 기간
- 2022.09.16 ~ 2022.09.21(6일)

## 🧑🏻‍💻 개발 인원(1명)
- 박민하

## 📝 요구사항 및 분석
1. 데이터 셋에 포함된 특정 고객의 자산 정보를 조회하는 API

2. 아래 화면에서 필요한 조회 API
- 투자 화면
  - 계좌명
  - 증권사
  - 계좌번호
  - 계좌 총 자산
- 투자상세 화면
  - 계좌명
  - 증권사
  - 계좌번호
  - 계좌 총 자산
  - 투자 원금
  - 총 수익금 (총 자산 - 투자 원금)
  - 수익률 (총 수익금 / 투자 원금 * 100)
- 보유종목 화면 API
  - 보유 종목명
  - 보유 종목의 자산군
  - 보유 종목의 평가 금액 (종목 보유 수량 * 종목 현재가)
  - 보유 종목 ISIN


## 🛠 기술 스택
Language | Framework | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">


## 🎯 API Endpoints
| endpoint | HTTP Method | 기능 | response data |
|----------|-------------|------|-------------------|
|/users | GET | 회원 정보 조회 |  "id", "username", "email"
|/users/signup | POST | 회원가입 | "id", "username", "email"
|/users/signin | GET | 로그인 |  "access_token", "refresh_token"
|/users/:id | PATCH| 회원 정보 수정 | "id", "username", "email"
|/users/:id | DELETE | 회원 정보 삭제 | 
|/account/:id | GET | 투자/투자상세페이지 | "user_id", "account_name", "company", "account_number", "total_assests", "total_profit", "rate"
|/account/asset/:id| GET | 보유종목페이지 |  "user_id", holding_name", "asset_group", "market_value", "isin"
|/account/invest/:id | POST | 거래 정보 등록 페이지  | 201 Created </br> 401 Unauthorized
|/account/invest/transfer/:id | GET | 입금 거래 페이지  | "주문 전 총자산", "주문 후 총자산"

## 📚 ERD
![](https://velog.velcdn.com/images/miracle-21/post/6e8dad6b-ca12-4e62-9f18-690fa72faf31/image.png)


## 🔖 참조 문서
- [postman API 링크](https://documenter.getpostman.com/view/18832289/2s7Z7YJuGb)

![](https://velog.velcdn.com/images/miracle-21/post/5f3f385a-54f3-4d69-b14b-5f0dd0557e49/image.png)

