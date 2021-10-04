# AI_WEB_AICARE_AIM
AI 기반 정신건강 플랫폼
- 음성의 언어적 의미와 비언어적 특성을 활용하여 정신건강을 객관적으로 진단하고 이에 맞는 해결책을 추천해주는 플랫폼

## Quickstart

```
git clone --recurse-submodules --remote-submodules https://github.com/osamhack2021/AI_WEB_AICARE_AIM.git -b ai-koremo
cd AI_WEB_AICARE_AIM
conda env create -n python3.7 --file environment.yml
conda activate python3.7
# Start the server:
python -m ai.simple-keras-rest-api.run_keras_server ai/koremo/model/model_for_6.h5
# Submit a request via cURL:
curl -X POST -F wav=@ai/으악-내눈.wav http://localhost:5000/predict
# Submit a request via Python:
python -m ai.simple-keras-rest-api.simple_request ai/으악-내눈.wav
conda deactivate
```

## Software Credits

The development of this software was made possible using the following components:

> ### [KorEmo](https://github.com/warnikchow/koremo) by **warnikchow**
>
> *Licensed Under: [MIT License](http://www.tldrlegal.com/license/mit-license)*
> <br> 5-class Korean speech emotion classifier

> ### [A Simple Keras + deep learning REST API](https://https://github.com/jrosebr1/simple-keras-rest-api) by **Adrian Rosebrock**
>
> *Licensed Under: [MIT License](http://www.tldrlegal.com/license/mit-license)*
> <br> A simple Keras REST API using Flask

*Attribution document generated using [tldrLegal](http://www.tldrlegal.com)*
<br> *Rewritten in markdown*