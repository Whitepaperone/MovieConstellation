# 일정

## 11/16 (수)

- 회의:
  
  - 일정 계획 수립

- 목표: 
  
  - 업무 분담
  
  - 일정 계획 수립
  
  - 데이터 정제 후 DB저장
    
    - Schema 설계
    
    - 모델을 거쳐 JSON으로 fixtures에 저장
      
      - api에서 데이터 수령
    
    - loaddata로 저장된 데이터가 잘 들어왔는지 확인
  
  - URL 설계
  
  - ERD, Story Board 작성
  
  - VUE와 DRF 연동

- 완료: 
  
  - ERD, Story Board 작성

- 발생한 문제점:
  
  - dumpdata는 DB에 저장된 Data를 JSON으로 만드는 과정이므로 model을 작성해서 DB로 만든 뒤 dumpdata를 실행하면 정제된 JSON 추출 가능
    
    - model 제작이 우선이 되어야 함
  
  - 업무 분담: 하루에 얼마나 할 수 있는지 모름.
    
    - 오늘 해보고 내일 결정, 근데 시간이 부족함
  
  - Profile의 followings에 JSONRESPONSE가 어떻게 도달하는지 VUE에서 확인을 못함
    
    - VUE에서 데이터 확인해보고 VUE 작성

- 수정여부:

## 11/17 (목)

- 회의: 
  - 오늘 목표 설정
  - 업무 분담
- 목표:
  - movie search 기능 구현
  - movie Detail 페이지 구현
  - followers followings 기능 구현
- 완료: 
  - profile 페이지 생성
  - movie search 페이지 생성
- 발생한 문제점: 
  - 라이프 사이클을 고려하지 않은 변수 선언
  - 영화 검색 시 즉각적인 동기화가 이루어지지 않음
  - 새로고침하면 state에 저장된 모든 USER 관련 자료가 사라짐
    - APP.vue에 있는 username이 state에 반영될 때를 감시하고 있다가, 반영이 되면 axios를 찍을 수 있게 watch로 구현
- 수정여부:
  - accounts 나중에 하기로
  - 일단 community와 movie 기능들부터 하는 것으로

## 11/18 (금)

- 회의:
  - Playlist DB Schema 구성
  - 업무 분담
  - 
- 목표:
  - Playlist Modeling
  - DetailView.vue 구현
  - RandomView.vue 구현
  - Follower/Following views.py 구현
  - Follower/Following data 받기
- 완료:
  - Playlist Modeling
  - RandomView.vue 구현
  - Follower/Following views.py 구현
  - Follower/Following data 받기(0.5)

- 발생한 문제점:
  - DetailView props 전달이 되지 않음
  - JSONResponse를 통한 데이터 전달 시, axios오류 발생
  
- 수정여부:

## 11/19 (토)

- 회의:
- 목표:
- 완료:
- 발생한 문제점:
- 수정여부:

## 11/20 (일)

- 회의:
- 목표:
- 완료:
- 발생한 문제점:
- 수정여부:

## 11/21 (월)

- 회의:
- 목표:
- 완료:
- 발생한 문제점:
- 수정여부:

## 11/22 (화)

- 회의:
- 목표:
- 완료:
- 발생한 문제점:
- 수정여부:

## 11/23 (수)

- 회의:
- 목표:
- 완료:
- 발생한 문제점:
- 수정여부:

## 11/24 (목)

- 회의:
- 목표:
- 완료:
- 발생한 문제점:
- 수정여부:

# 업무분담

## 노준호 (팀장)

### 기능

- 세부내용

## 백지원

### 기능

- 세부내용

# 아키텍처

## Version 1

### [ERD]

![img](./process/ERD/ERD%20v1.PNG)

### [Story Board]