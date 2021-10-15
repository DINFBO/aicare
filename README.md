# AICARE
AI 기반 정신건강 플랫폼 

[![logo](https://github.com/osamhack2021/AI_WEB_AICARE_AIM/blob/main/web/facebook_cover_photo_2.png?raw=true)](https://github.com/osamhack2021/AI_WEB_AICARE_AIM)

## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%ED%8C%80-%EC%A0%95%EB%B3%B4-team-information)팀 정보 (Team Information)

- 성정환 (육군 지작사 1공병여단)  
고려대학교 산업경영공학과  
2021 국방부 데이터활용 경진대회 국방부장관상 수상  

- 기윤호 ()  

- 하철환 ()  

- 조성우 ()  



## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%ED%94%84%EB%A1%9C%EC%9E%AD%ED%8A%B8-%EC%86%8C%EA%B0%9C)프로젝트 소개
**AICARE**는 군대에서 나라를 지키고 있는 국군 장병 및 간부님들의 정신건강을 AI를 기반으로 관리하는 플랫폼입니다.  
마음속 이야기가 담긴 음성의 내용과 음향학적 특성을 활용하여 정신건강을 객관적으로 분석합니다.  
그리고 코로나로 1년넘게 휴가 및 외출이 통제되어 있는 폐쇄적인 상황에서 정신적으로 어려움을 겪고 스트레스를 받는 장병들과 간부님들의 상황에 맞는 개인맞춤형 해결책을 제공합니다.  


## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EA%B8%B0%EB%8A%A5-%EC%84%A4%EB%AA%85)모델 설명

### - 데이터 수집  
- 기존모델의 한계1 : 감성을 파악하는데 있어서 기존사례를 분석해보니 단일 데이터를 사용하는 모델의 정확도가 낮음  
- 기존모델의 한계2 : 단순 긍/부정만을 판단하기때문에 구체적인 상황에서 실질적인 활용이 어려움  
- 따라서 상세한 감성정보를 가지고있는 멀티모달 데이터(텍스트와 음성)을 동시에 분석하여 감성을 파악하기로 결정  
- 상세감성 및 텍스트와 음성을 모두 보유하고 있는 데이터로 한국지능정보사회진흥원에서 제공하는 감성대화말뭉치를 찾았고, 이 데이터를 활용하기로 결정  
- 해당 데이터를 수집하고, 전체적인 구조와 특성을 파악   
<img src="/img/m1.PNG" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"><br/>  

### - 데이터 가공
- 음성과 텍스트 각각의 데이터에 맞는 모델 구조를 설계
- 해당 모델에 맞게 데이터를 적절하게 가공(Preprocessing)
- 음성은 주파수기반의 스펙트로그램으로 변형하여 벡터화하여 활용
- 텍스트는 Transformer기반의 ko-Bert모델에서 주어지는 토큰화함수를 이용하여 벡터화하여 활용
<img src="/img/m2.PNG" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"><br/>   

### - 모델 개발
- LSTM, RNN, TRANSFORMER등의 여러가지 모델을 각각 적용해보고 데이터에 맞는 세부 모델을 탐색
- 최적의 모델을 찾은뒤 multi-weight 방식의 fusion을 통하여 텍스트모델과 음성모델을 앙상블
<img src="/img/m3.PNG" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"><br/><br/><br/>        




## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EA%B8%B0%EB%8A%A5-%EC%84%A4%EB%AA%85)기능 설명

### - 감성일기장 / 마음일기  
- 오늘 하루의 마음/감성을 음성으로 기록합니다.  
<img src="/img/fc1.PNG" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"><br/>

### - 감성분석 / 마음분석  
- 음성으로 기록된 감성을 AI기반으로 분석합니다.  
- 시간에 따른 감성의 변화를 시각화하여 보여줍니다.  
<img src="/img/fc2.PNG" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"><br/>  

### - 음악추천
- 분석된 감성에 따라 맞춤형으로 음악을 추천하여 들려줍니다.
- 추천된 음악을 통해서 불안함과 우울함같은 감성들을 조절합니다.

### - 비대면상담
- 분석된 감성에 알맞는 전문 상담사를 추천하여 보여줍니다.    
- 감성 분석내용을 바탕으로 세부적인 감정 및 상황에 대해서 심도깊게 상담합니다.   

### - 로그인/회원가입

### - 마이페이지
- 상담내역 및 감성기록들을 확인하고 체계적으로 관리합니다. <br/><br/>   



## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EC%BB%B4%ED%93%A8%ED%84%B0-%EA%B5%AC%EC%84%B1--%ED%95%84%EC%88%98-%EC%A1%B0%EA%B1%B4-%EC%95%88%EB%82%B4-prerequisites)컴퓨터 구성 / 필수 조건 안내 (Prerequisites)

-   ECMAScript 6 지원 브라우저 사용
    
-   브라우저 지원 버젼
    
[!["browser img"](https://github.com/osamhack2020/WEB_Meditact_Meditact/raw/client/src/images/forReadme/browser.png)](https://github.com/osamhack2020/WEB_Meditact_Meditact/blob/client/src/images/forReadme/browser.png)





## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EA%B8%B0%EC%88%A0-%EC%8A%A4%ED%83%9D-technique-used)기술 스택 (Technique Used)

### Deep Learning
| Python |![enter image description here](https://camo.githubusercontent.com/fb9e18f7ca2a84b570706b0c725d31f01587805c6bc02814986fcd31f17a7d64/68747470733a2f2f7777772e707974686f6e2e6f72672f7374617469632f696d672f707974686f6e2d6c6f676f4032782e706e67)  
|-|--|
|Tensorflow  | ![enter image description here](https://camo.githubusercontent.com/4700da25bb75885497f514172b3eb8a187d40f4cea660c06939e1199402064da/68747470733a2f2f7777772e677374617469632e636f6d2f64657672656c2d646576736974652f70726f642f76666538616636323539396563343435353532633366623433363038633337666634363436336339666365336231346438656536336232653731656464646666642f74656e736f72666c6f772f696d616765732f6c6f636b75702e7376673f6463625f3d302e36303530373736343931303735343435)
|keras  | ![enter image description here](https://camo.githubusercontent.com/d441b09246a1e2c7ef0eaf05f1523d5250885a27b5b23324e1196d78aa30f056/68747470733a2f2f6b657261732e696f2f696d672f6c6f676f2e706e67) |
|Pytorch|![--](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/PyTorch_logo_black.svg/1200px-PyTorch_logo_black.svg.png)|--|--|



### [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#serverback-end)Server(back-end)

|PHP 8.0|![enter image description here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZQxcchmR7ecpvPM0oJqfjY8Awrt4BrbOKjQ&usqp=CAU)  
|-|--|
|Mysql 8.0 | ![enter image description here](https://img1.daumcdn.net/thumb/R1200x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/797z/image/3r7sR9IJuBZfq4M5yKrLWIt3rZE.jpg)


### [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#front-end)Front-end

|React.js|![enter image description here](https://miro.medium.com/max/1200/0*XCgoYU9sqt95P8J0.png)  
|-|--|
|Javascript | ![enter image description here](https://media.vlpt.us/images/realryankim/post/fc649a62-b232-41c6-8a0e-64fe3d9c1116/JS.jpg)





## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EC%84%A4%EC%B9%98-%EC%95%88%EB%82%B4-installation-process)설치 안내 (Installation Process)

$ git clone git주소
$ yarn or npm install
$ yarn start or npm run start



## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-getting-started)프로젝트 사용법 (Getting Started)

**마크다운 문법을 이용하여 자유롭게 기재**

잘 모를 경우 구글 검색 - 마크다운 문법  [https://post.naver.com/viewer/postView.nhn?volumeNo=24627214&memberNo=42458017](https://post.naver.com/viewer/postView.nhn?volumeNo=24627214&memberNo=42458017)

편한 마크다운 에디터를 찾아서 사용 샘플 에디터  [https://stackedit.io/app#](https://stackedit.io/app#)


## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%ED%8C%80-%EC%A0%95%EB%B3%B4-team-information)팀 정보 (Team Information)

- 성정환 ([mn99134@korea.ac.kr](mailto:mn99134@korea.ac.kr)), Github Id: DINFBO
- 기윤호 ([yhkee0404@gmail.com](mailto:yhkee0404@gmail.com)), Github Id: yhkee0404
- 하철환([](mailto:)), Github Id: hwna00
- 조성우([](mailto:)), Github Id: seouk812



## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EC%A0%80%EC%9E%91%EA%B6%8C-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EA%B6%8C-%EC%A0%95%EB%B3%B4-copyleft--end-user-license)저작권 및 사용권 정보 (Copyleft / End User License)

-   [MIT](https://github.com/osam2020-WEB/Sample-ProjectName-TeamName/blob/master/license.md)

This project is licensed under the terms of the MIT license.
