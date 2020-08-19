# Machine Learning Platform - Kubeflow  
#### SK C&amp;C - Cloud Architecture Unit Intern   
---
## BM 혁신 플랫폼 내 PMS 구축 지원
- Cloud 개발 환경을 제공하는 `PMS : Platform Managed Service` 지원  
  - Time to Market 이 가능하게 하는 개발 환경 제공
  - Cloud 환경 제공을 통한 고객사 가치 제공
### Machine Learning Platform with Kubeflow  
- PMS를 이용할 고객사의 입장으로서 PMS 내 구축 가능한 `Kubernetes-머신러닝 개발 플랫폼` 구현
- Kubeflow ML Platform 서비스 구성요소  
  - Experimental Phase 
    - Jupyter 학습환경 제공
    - Katib을 통한 하이퍼 파라미터 최적화  
  - Production Phase
    - Online/batch Prediction을 위한 KF Serving / TF Serving 을 통한 모델 배포
    - MetaData/TensorBoard 를 통한 Model Performance 모니터
    - ML Pipeline 구축 : `Model-Training` -> `Serving` -> `Monitoring`    
---  
### ML Pipeline with KubeFlow  
- PMS를 이용할 고객사의 입장에서, 쿠버네티스를 활용한 `머신러닝 파이프라인` 구축 및 `ML 추론 서비스` 구현  
  - TensorFlow 이용한 모델 학습
  - Katib 이용하여 Hyper Parameter 자동 Tuning  
  - TF 모델 저장  
  - 저장된 모델을 이용하여 Wev Service 배포  
#### Index  
- 1. Traing Fashion Mnist with Fairing
- 2. Tuning Hyper Parameter with Katib  
- 3. Saving TF Model  
- 4. ML Inference Service with KFserving

#### Docker File  
[Jaewoo Park - Docker Repositories](https://hub.docker.com/u/jaewoo201)  
    
