# Transit_Insights


## 프로젝트 주제 및 개요
  지하철 혼잡도 분석, 예측 모델 개발 및 웹 서비스 구현


## 수행 방향
  ● 수행도구
  - 웹 배포: Django, AWS
  - 머신러닝: Scikit-learn, LightGBM, XGBoost
  - 시각화: Highcharts

  ● 데이터소개 
  - 지하철 데이터 (서울교통공사 관할인 1~8호선 데이터 사용)
    - [서울시열린데이터광장 : 서울교통공사 역별 시간대별 혼잡도]([https://data.seoul.go.kr/dataList/OA-12928/F/1/datasetView.do](https://data.seoul.go.kr/dataList/OA-12928/F/1/datasetView.do))
    - [서울시열린데이터광장 : 서울교통공사 연도별 일별 역별 시간대별 승하차인원(1_8호선)](https://data.seoul.go.kr/dataList/OA-12252/S/1/datasetView.do)
    - [서울시열린데이터광장 : 서울시 지하철 호선별 역별 시간대별 지하철 인원 정보)](https://data.seoul.go.kr/dataList/OA-12252/S/1/datasetView.do)
    - [서울시 지하철 실시간 도착 정보](https://data.seoul.go.kr/dataList/OA-12764/F/1/datasetView.do)

## 프로젝트 조직 (역할 분담) - 본인 파트: 머신러닝
- 팀장(1명): 프로젝트 총괄
- 웹개발(1명): 스타일 및 구성, 웹서비스 분포
- 데이터 수집 및 전처리(3명): API 및 크롤링으로 데이터 수집, EDA, 최종 혼잡도 데이터 파일로 정리
- 머신러닝 및 분석(1명): 학습 모델 선정 및 최적화, 평가지표 선정


## 프로젝트 추진 일정
  ● 일정 
  - 09/01~09/04 : 기획
  - 09/03~09/09 : 웹 서비스, 대시보드 기초 논리 작성
  - 09/03~09/09 : 데이터 수집 및 분석
  - 09/07~09/18 : 데이터 정제, 변환, 전처리
  - 09/10~09/16 : 웹 서비스, 대시보드 세부 논리 작성, 수정
  - 09/15~09/23 : 머신러닝 모델 선정, 최적 모델 구현
  - 09/17~09/23 : 웹 서비스, 대시보드 CSS + HTML 수정, 배포
  - 09/25 : 프로젝트 완료(프로젝트 설계, 구현, 테스트), 프로젝트 수행
  - 09/24~09/25 : 웹 마무리
  - 09/26 : 최종 발표일


## 그 외 프로젝트 상세 내용
  - '프로젝트_상세.pdf' 파일 참조


## 머신러닝 설명
  - 머신러닝 코드
  1. 효율적인 모델 학습을 위해 각 호선별로 데이터를 분리 및 학습시킴
  2. 테스트한 모델의 종류에는 Sklearn(LinearRegression, RandomForestRegressor), LightGBM(LGBMRegressor), XGBoost(XGBRegressor)가 있음
  3. 훈련데이터/테스트 데이터의 split 비율은 7:3과 8:2를 시도해보았고 평가지표가 좋은 7:3을 최종 사용
  4. '모델개요.ipynb'에서 모델의 구조를 확인 가능
  5. 하이퍼파라미터 튜닝 진행하였으며, 코드 실행에는 오랜 시간이 소요되므로 결과 확인만 하기를 권장.
  
  - 학습완료 모델
  1. 사용한 4가지 모델 종류의 학습완료 후 pkl 파일로 저장하였음
  2. 이는 웹 서비스 제공 시 원할한 사용을 위함


## 사용방법
  - 파이썬 화경에서 'requirements.txt' 안의 패키지 설치 후 '웹서비스_산출물 > manage.py' 실행
  - [웹 환경 예시](https://www.youtube.com/watch?v=phZRdA8Wsik)
