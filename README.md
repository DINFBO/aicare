# AICARE
AI 기반 정신건강 플랫폼 

[![logo](https://github.com/osamhack2021/AI_WEB_AICARE_AIM/blob/main/WEB(FE)/facebook_cover_photo_2.png?raw=true)](https://github.com/osamhack2021/AI_WEB_AICARE_AIM)  

  

## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%ED%8C%80-%EC%A0%95%EB%B3%B4-team-information)팀 정보 (Team Information)
![asd (1)](https://user-images.githubusercontent.com/86407466/137922558-d06564d5-7221-4eed-9c79-a703ad4f187f.png)

- 성정환 (육군 지작사 1공병여단)  
고려대학교 산업경영공학과  
2021 국방부 데이터활용 경진대회 국방부장관상 수상  

- 기윤호 (해군 정보체계관리단)  
한동대학교 전산전자공학부 컴퓨터공학심화전공

- 하철환 (육군 1군단 25사단 72여단)  
국민대학교 소프트웨어융합학과   

- 조성우 (국직 국군의무사령부 국군구리병원)  
세종대학교 데이터사이언스학과


## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%ED%94%84%EB%A1%9C%EC%9E%AD%ED%8A%B8-%EC%86%8C%EA%B0%9C)프로젝트 소개
  
**AICARE**는 군대에서 나라를 지키고 있는 국군 장병 및 간부님들의 정신건강을 AI를 기반으로 관리하는 플랫폼입니다.  
마음속 이야기가 담긴 음성의 내용과 음향학적 특성을 활용하여 정신건강을 객관적으로 분석합니다.  
그리고 코로나로 1년넘게 휴가 및 외출이 통제되어 있는 폐쇄적인 상황에서 정신적으로 어려움을 겪고 스트레스를 받는 장병들과 간부님들의 상황에 맞는 개인맞춤형 해결책을 제공합니다.  
![image](https://user-images.githubusercontent.com/86407466/138117915-b7477017-0fd7-460c-b544-24208ab5f6ad.png)  <br>  

## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EA%B8%B0%EB%8A%A5-%EC%84%A4%EB%AA%85)모델 설명

### - 데이터 수집  
- 기존모델의 한계1 : 감성을 파악하는데 있어서 기존사례를 분석해보니 단일 데이터를 사용하는 모델의 정확도가 낮음  
- 기존모델의 한계2 : 단순 긍/부정만을 판단하기때문에 구체적인 상황에서 실질적인 활용이 어려움  
- 따라서 상세한 감성정보를 가지고있는 멀티모달 데이터(텍스트와 음성)을 동시에 분석하여 감성을 파악하기로 결정  
- 상세감성 및 텍스트와 음성을 모두 보유하고 있는 데이터로 한국지능정보사회진흥원에서 제공하는 감성대화말뭉치를 찾았고, 이 데이터를 활용하기로 결정  
- 해당 데이터를 수집하고, 전체적인 구조와 특성을 파악  <br>  
<img src="/img/m1.PNG" title="데이터 수집" alt="데이터 수집"><br><br/>    

### - 데이터 가공
- 음성과 텍스트 각각의 데이터에 맞는 모델 구조를 설계
- 해당 모델에 맞게 데이터를 적절하게 가공(Preprocessing)
- 음성은 주파수기반의 스펙트로그램으로 변형하여 벡터화하여 활용
- 텍스트는 Transformer기반의 ko-Bert모델에서 주어지는 토큰화함수를 이용하여 벡터화하여 활용<br>  
<img src="/img/m2.PNG" title="데이터 가공" alt="데이터 가공" style='display:inline'>
<img src="/img/m4.PNG" title="데이터 가공" alt="데이터 가공" style='display:inline'> <br/> <br>


### - 모델 개발
- LSTM, RNN, TRANSFORMER등의 여러가지 모델을 각각 적용해보고 데이터에 맞는 세부 모델을 탐색
- 최적의 모델을 찾은뒤 multi-weight 방식의 fusion을 통하여 텍스트모델과 음성모델을 앙상블  <br>
<img src="/img/m3.PNG" title="모델 개발" alt="모델 개발"><br/><br/><br/>        




## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EA%B8%B0%EB%8A%A5-%EC%84%A4%EB%AA%85)기능 설명

### - 감성일기장 / 마음일기  
- 오늘 하루의 마음/감성을 음성으로 기록합니다.  
<img src="/img/fc1.PNG" title="감성일기장" alt="감성일기장"><br/>  <hr/>
<img src="/img/fc1-1.PNG" title="감성분석" alt="감성분석"><br/>    

### - 감성분석 / 마음분석  
- 음성으로 기록된 감성을 AI기반으로 분석합니다.  
- 시간에 따른 감성의 변화를 시각화하여 보여줍니다.  
<img src="/img/fc3.PNG" title="감성분석" alt="감성분석"><br/>      <hr/>
<img src="/img/fc4-1.PNG" title="감성분석" alt="감성분석"><br/>    <hr/>
<img src="/img/fc4-2.PNG" title="감성분석" alt="감성분석"><br/>   
### - 음악추천
- 분석된 감성에 따라 맞춤형으로 음악을 추천하여 들려줍니다.
- 추천된 음악을 통해서 불안함과 우울함같은 감성들을 조절합니다.  
<img src="/img/fc8.PNG" title="감성분석" alt="감성분석"><br/>  <hr/>
<img src="/img/fc8-1.PNG" title="감성분석" alt="감성분석"><br/>  


### - 비대면상담
- 분석된 감성에 알맞는 전문 상담사를 추천하여 보여줍니다.    
- 감성 분석내용을 바탕으로 세부적인 감정 및 상황에 대해서 심도깊게 상담합니다.  
<img src="/img/fc9.PNG" title="감성분석" alt="감성분석"><br/>   

### - 로그인/회원가입
<img src="/img/fc10.PNG" title="감성분석" alt="감성분석"><br/>  


### - 마이페이지
- 상담내역 및 감성기록들을 확인하고 체계적으로 관리합니다.  
<img src="/img/fc9-1.PNG" title="감성분석" alt="감성분석"><br/>



## AICARE 기대효과  

### 일상의 데이터를 활용하여 정신건강을 상세하게 측정
- 강제적이고 작위적인 설문조사가 아닌 매일 기록하는 마음일기를 통하여 자연스럽게 정신건강을 분석
- 데이터의 의미와 특징을 모두 활용하여 분석함으로서 분석결과에 대한 높은 신뢰성 확보
- 단순감성이 아닌 의학적으로 의미있는 감성을 상세하게 분석하여 제공


### 정신건강의 객관적, 수치적 분석  
- 기존의 주관적인 정신건강 검사의 문제점을 해결
- 다양한 감정을 앱을 통하여 기록하고 보관하여 체계적으로 관리
  
  
### 위험하거나 불안정한 상태를 조기에 발견하여 대처가능
- 일기를 통하여 정신건강을 기록하고 분석하여 정신건강을 시간의 흐름에 따라 파악
- 주의가 필요하거나 불안정한 감정상태를 조기에 선제적으로 파악, 대처 가능


### 정신건강상태에 따른 맞춤형케어
- 각 개인별 정신건강상태에 따라 맞춤형으로 해결책을 제시 
- 비교적 가벼운 경우에는 음악을 추천하고, 정도가 심한 경우에는 감성에 맞는 전문상담을 연결
<br><br>

## AICARE의 경쟁력

### 개발문서의 구체성
구체적인 개발문서의 양호도 및 구체적 표현성

- 활용한 데이터에 대한 구조를 시각적으로 표현
- 데이터의 전처리과정을 상세하게 설명하고, 코드상의 주석으로 문서화
- 모델의 앙상블과정에 대해서 코드와 시각자료를 통해 상세하게 표현
- 모델의 서비스화 상세 과정을 Issue에 적어놓음으로서, 구현과정에 대한 상세 설명
  
### 독창성
뚜렷한 독창성 유무 정도

- 단순긍부정이 아닌 의학적으로 의미가 있는 상세감성에 대한 분석
- 텍스트와 음성을 동시에 활용한 멀티모달 모델을 구성
- 각각의 감성에 따라 맞춤형 해결책을 제공
- 모바일 완벽 지원 및 PWA를 이용한 앱 활용 가능  


### 발전 가능성
커뮤니티, 비즈니스 등에 대한 발전 가능성

- 상세감성분석을 통하여 감성분석이 다양한 분야에 활용될 수 있는 토대를 구축
- 멀티모달 모델을 통하여 2차원, 3차원의 데이터를 활용한 모델의 가이드를 제공
- 간부님 및 관리자가 손쉽게 관리할 수 있도록 관리 시스템 구축


### 완성도(작품데모)
데모 결과에 대한 시현 능숙도 및 원활한 작동

- 즉시 서비스를 시행할 수 있도록 완성도 있게 제작
- 관리자 페이지를 제공하여 보다 체계적인 관리가 가능


## 기술 스택 (Technique Used)

### AI
<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://www.tensorflow.org/?hl=ko" target="_blank"> <img src="https://blog.kakaocdn.net/dn/bFxR1Q/btqSDtQKld6/iYtHWEess8z9op5fu8JMW0/img.png" alt="git" width="40" height="40"/> </a><br>Tensorflow</div>
  </td>
  <td>
   <div align="center"><a href="https://pytorch.org/" target="_blank"> <img src="https://pytorch.org/assets/images/pytorch-logo.png" alt="docker" width="40" height="40"/> </a><br>PyTorch</div>
  </td>
  <td>
   <div align="center"><a href="https://www.python.org/" target="_blank"> <img src="https://media.vlpt.us/images/taeil77/post/0860d033-75cf-4101-b236-1a261c8c2c8a/python.png" alt="docker" width="40" height="40"/> </a><br>Python</div>
  </td>     
 </tr>
 </tbody></table>
 
### Back-end
<table><tbody>
 <tr>
  <td width="60">
   <div align="center"><a href="https://www.php.net/" target="_blank"> <img src="https://blog.kakaocdn.net/dn/pVD59/btquknGhVh1/ArEncBG0uVuOvaF8TAdw31/img.jpg" alt="nodejs" width="40" height="40"/> </a><br>PHP</div>
  </td>
  <td width="60">
   <div align="center"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png" alt="javascript" width="40" height="40"/> </a><br>Javascript</div>
  </td>
  <td width="60">
   <div align="center"><a href="https://laravel.kr/docs/8.x/README" target="_blank"> <img src="https://lh3.googleusercontent.com/proxy/n3d5sN51xBolWMvVxsq2hOv2UmsJxb-r_kDgNpGtpAcphTnJSFMvdZ-MtqgLGNtIaOZKTBlPDUrI-NbFVf0-NZKuCVRl6zW08ca7uoYr40d-I1CIXWLp5gPcXzE" alt="strapi" width="40" height="40"/> </a><br>Laravel</div>
  </td>
  <td width="60">
   <div align="center"><a href="https://ubuntu.com" target="_blank"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs8-BJ-KbWYEXH2yN_4cS-bky7mlDhGo4rIQ&usqp=CAU" alt="linux" width="40" height="40"/> </a><br>ubuntu</div>
  </td>
  <td width="60">
   <div align="center"><a href="https://www.nginx.com" target="_blank"> <img src="https://media.vlpt.us/images/kimkevin90/post/05c9c888-1a3e-43fc-8eed-7b745fb5ae38/nginx.png" alt="nginx" width="40" height="40"/> </a><br>Nginx</div>
  </td>


 </tr>
 </tbody></table>
  
### Front-end
<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://reactjs.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Sass_Logo_Color.svg/1200px-Sass_Logo_Color.svg.png" alt="react" width="40" height="40"/> </a><br>SCSS</div>
  </td>
  <td>
   <div align="center"><a href="https://nextjs.org/" target="_blank"> <img src="https://cdn.worldvectorlogo.com/logos/nextjs-3.svg" alt="nextjs" width="40" height="40"/> </a><br>Next.js</div>
  </td>
  <td>
   <div align="center"><a href="https://www.typescriptlang.org/" target="_blank"> <img src="https://miro.medium.com/max/724/1*5QD8DKhOjRe-gcYjozlLNQ.png" alt="typescript" width="40" height="40"/> </a><br>Tailwind</div>
  </td>
  <td width="60">
   <div align="center"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png" alt="javascript" width="40" height="40"/> </a><br>Javascript</div>
  </td>
  <td>
   <div align="center"><a href="https://www.w3.org/html/" target="_blank"> <img src="https://media.vlpt.us/images/0jiiino/post/7487c872-93d6-4397-9865-22b7ddee9e26/img.png" alt="html5" width="40" height="40"/> </a><br>Html5</div>
  </td>
  <td>
   <div align="center"><a href="https://sass-lang.com" target="_blank"> <img src="https://media.vlpt.us/images/hikoand/post/7a027ba4-e221-42c3-9b43-998757a9f156/2541853857EA02BC16.gif" alt="sass" width="40" height="40"/> </a><br>JQUERY</div>
  </td>
 
 </tr>
 </tbody></table>
 
 ### Database
 <table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://www.mongodb.com/" target="_blank"> <img src="https://ww.namu.la/s/d59b18ca16c075c57c5ebe902e14d46c58e2df1d638605017382993a696c0c8c2313077356a2bd90892fa9e00c704b6832c07c8981482d4d3b88ccb2848da73142a440a665710e13ce579236ead5ce33" alt="mongodb" width="40" height="40"/> </a><br>Mysql</div>
  </td></tr>
 </tbody></table>
 
 ### Web Skills
<table>
	<tbody>
		<tr>
			<td width="200" align="center">
				크로스 브라우징<br>
				(Cross Browsing)
	  		</td>
			<td width="200" align="center">
				웹 표준<br>
				(Web Standards)
	  		</td>
			<td width="200" align="center">
				SEO 검색엔진최적화<br>
				(Search Engine Optimization)
	  		</td>
		</tr>
	 </tbody>
</table>
<table>
	<tbody>
		<tr>
			<td width="200" align="center">
				SSR<br>
				(Server Side Rendering)
	  		</td>
			<td width="200" align="center">
				CSR<br>
				(Client Side Rendering)
	  		</td>
			<td width="200" align="center">
				PWA<br>
				(Progressive Web Apps)
	  		</td>
		</tr>
	 </tbody>
</table>
<br><br>



## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%EC%84%A4%EC%B9%98-%EC%95%88%EB%82%B4-installation-process)설치 안내 (Installation Process)

mxnet  
torch  
scikit-learn<0.23  
gluonnlp  
sentencepiece  
transformers==3.0.2  
speechrecognition  
git+https://git@github.com/SKTBrain/KoBERT.git@master  
librosa  



## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%82%AC%EC%9A%A9%EB%B2%95-getting-started)프로젝트 사용법 (Getting Started)

USAGE  
Start the server:  
	python -m ai.simple-keras-rest-api.run_keras_server  
Submit a request via cURL:  
	curl -X POST -F wav=@ai/test.wav https://yhkee0404-osamhack2021-ai-web-aicare-aim-xxrpgj9v3q6q-5000.githubpreview.dev/score  
Submit a request via Python:  
	python -m ai.simple-keras-rest-api.simple_request ai/test.wav https://yhkee0404-osamhack2021-ai-web-aicare-aim-xxrpgj9v3q6q-5000.githubpreview.dev/score  


## [](https://github.com/osamhack2021/Repo_Sample-Main-Technology_Sub-Technology_ProjectName_TeamName#%ED%8C%80-%EC%A0%95%EB%B3%B4-team-information)팀 정보 (Team Information)

- 성정환 ([mn99134@korea.ac.kr](mailto:mn99134@korea.ac.kr)), Github Id: DINFBO
- 기윤호 ([yhkee0404@gmail.com](mailto:yhkee0404@gmail.com)), Github Id: yhkee0404
- 하철환([layton3534@gmail.com](mailto:layton3534@gmail.com)), Github Id: hwna00
- 조성우([seouk77@gmail.com](mailto:seouk77@gmail.com)), Github Id: seouk812

## Software Credits

![image](https://user-images.githubusercontent.com/86407466/138116713-12cc2608-65b5-45d0-97ca-b190c43ec827.png)  


The development of this software was made possible using the following components:

> ### [KoBERT](https://github.com/SKTBrain/KoBERT) by **SK T-Brain**
>
> *Licensed Under: [Apache License 2.0 (Apache-2.0)](http://www.tldrlegal.com/license/apache-license-2.0-(apache-2.0))*
> <br> Korean BERT pre-trained cased (KoBERT)

> ### [A Simple Keras + deep learning REST API](https://https://github.com/jrosebr1/simple-keras-rest-api) by **Adrian Rosebrock**
>
> *Licensed Under: [MIT License](http://www.tldrlegal.com/license/mit-license)*
> <br> A simple Keras REST API using Flask

*Attribution document generated using [tldrLegal](http://www.tldrlegal.com)*
<br> *Rewritten in markdown*

## [](https://en.wikipedia.org/wiki/MIT_License)저작권 및 사용권 정보 (Copyleft / End User License)

-   [MIT](https://en.wikipedia.org/wiki/MIT_License)

This project is licensed under the terms of the MIT license.
