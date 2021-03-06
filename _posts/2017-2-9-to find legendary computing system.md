---
layout: post
title: 전설의 컴퓨팅을 찾아 떠나는 모험 강의 계획
date: 2016-11-24
---

## 1강. BOOTLOADER: 개발환경 세팅하기

라즈베리 파이와 아날로그 비디오 인풋이 가능한 CRT 모니터, 키보드와 기타 등등으로 작업 환경을 구축한다.

### 워밍업: LED 메트릭스 출력

적당한 크기의 LED 매트릭스와 광센서 매트릭스로 간단한 OMR 카드 리더를 고안한다. OMR 카드를 통해 신호를 전달할 방법을 찾아본다. 이렇게 전달한 신호를 처리해 모니터로 확인해보자. 또한 디지털 처리 없이 모니터 혹은 모니터에 준하는 환경에 OMR 카드의 신호를 시연/상영할 방법과 조건을 상상하고 고안해보자.

### 도전과제
- LED의 열을 이용해 종이에 신호를 현상해보기(잘 안되면 감열지를 사용해 본다).
- 간단한 코드 반복을 통해 애니메이션을 만들어 보자.

## 2강. 오르골과 영사기: 하나의 좌표가 시간과 대응할 때 ― 1

### 프로그램 손뜨게: 천공카드와 OMR, 2차원 평면의 좌표와 1:1 대응하는 기록 시스템

적당한 크기의 LED 매트릭스와 광센서 매트릭스로 간단한 OMR 카드 리더를 고안한다. OMR 카드를 통해 신호를 전달할 방법을 찾아본다. 이렇게 전달한 신호를 처리해 모니터로 확인해보자. 또한 디지털 처리 없이 모니터 혹은 모니터에 준하는 환경에 OMR 카드의 신호를 시연/상영할 방법과 조건을 상상하고 고안해보자.

### OMR 오르골

1강때 만든 만능기판을 이용해 광센서 매트릭스를 제작하고 LED 매트릭스와 OMR 카드를 조합해 신호를 읽어본다. 이를 이용해 소리를 출력할 방법을 궁리해본다.

### 도전과제

- 각 머신들을 기계적으로 정확도와 성능을 개선해보자!
- 제작한 OMR - SOUND 머신으로 오르골을 만들어 보자!

## 3강. 오르골과 영사기: 하나의 좌표가 시간과 대응할 때 ― 2

오르골의 천공테이프, 자기 테이프, 영사용 필름의 사례를 설명하고 일전의 천공 카드의 기록 방식이 이들과의 공통점과 차이점에 대해 이야기해본다.

### 영사기

간단한 구조의 영사 장치를 만들어본다. 미리 만들어둔 LED 매트릭스를 이용해 애니메이션을 만들 방법을 궁리해보자.

### 도전과제

- 남는 LED와 종이 리본을 활용해 간단한 영사기를 만들어보자.
- 만들다만 에니메이션을 마저 만들어 완성한다.

## 4강. 단 하나의 시간: 시간을 담은 미디어

LP가 소리 정보를 어떻게 담고 있고, 이 정보를 어떻게 재생해내는지 종이컵 포노앰프를 이용해 알아보기. 또한 LP의 RPM 개념에 대해 알아보고, 이것이 LP가 담고 있는 정보의 성격과 어떤 관계가 있는지 알아보기.

### 턴테이블

종이컵으로 턴테이블 포노앰프를 만들어보고 이를 이용해 레코드판을 플레이해본다. 종이컵 포노앰프를 개선하기 위해 피에조 픽업을 설치하고 아두이노를 통해 신호를 증폭하고 변조해본다.

준비된 카세트 테이프와 카세트 테이프 플레이어를 사용해 이전과는 달리 만져지지도, 보이지도 않는 자기 테이프와 같은 매체가 정보를 어떻게 담아내는지 알아본다.

### 도전과제

- 기계식 메트로놈의 리듬에 맞춰 종이컵 포노앰프로 LP의 음악을 바르게 연주해보기.
- 우리가 가지고 있는 신문물을 사용해 종이컵 포노앰프의 소리를 보다 크게 키울 수 있는 방법을 찾아보기.

## 5강. 비밀을 저장하는 방법

글을 신호로 인코딩하고 카세트 플레이어를 이용하여 자기테이프에 저장하고 다시 글로 복원하는 작업을 한다. 이를 통해 신호를 인코딩하고 디코딩하는 개념에 대해 배우고,  이상의 개념이 디지털 신호와 디지털 신호를 아날로그 매체에 담는 방법과 어떤 관계가 있는지 알아본다.

### 비밀을 저장하는 방법

- 글자를  2진수로 인코딩 해보자(손으로)
- 인코딩 된 글자을 서로 바꿔서 다시 손으로 디코딩 해보자.
- 같은 동작을 코드로 해보자.
- 펀치 카드를 붙여보자.
- OMR 리더기를 붙여보자.
- 인코딩된 내용을 소리로 바꿔보자.
- 바꾼 소리를 녹음해서 저장해본다.
- 녹음된 소리를 다시 글로 바꿔본다.
- 서로의 글소리를 교환해보자.
- 기존에 만든 장치들을 연결해보자. 신호에 개입해 변조하고 증폭해보자.

## 6강. 슈퍼 괴물 기계 만들기

지금까지 궁리한 내용을 바탕으로 세상을 놀라게 할만한 슈퍼 괴물 기계를 만들어 보자. 신호를 증폭하고 변조해 만든 괴물로 온 세상을 놀래켜보자. 하지만 세상이 놀라지 않는다면, 다음 기회를 노려봅시다.
