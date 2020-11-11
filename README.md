# animalface


## 파이썬 크롤러 설치 안내 (Installation Process)


### install python library


- install bs4

```bash
pip install bs4
```



- install google_images_download

Python Script for ‘searching’ and ‘downloading’ hundreds of Google images to the local hard disk!

```bash
pip install google_images_download
```

Information: https://pypi.org/project/google_images_download/


- install selenium

```bash
pip install selenium
```


## 가상 환경 만들기

가상 환경은 venv 명령을 실행해서 만들어집니다:

```bash
python -m venv selenium
```

이 명령을 실행하면 대상 디렉터리가 만들어지고 (이미 존재하지 않는 부모 디렉터리도 만듭니다) 명령이 실행된 파이썬 설치를 가리키는 home 키가 있는 pyvenv.cfg 파일이 배치됩니다 (대상 디렉터리의 일반적인 이름은 .venv입니다). 또한 파이썬 바이너리/바이너리들의 사본/심볼릭 링크를 포함하는 bin (또는 윈도우의 경우 Scripts) 서브 디렉터리를 만듭니다 (플랫폼이나 환경 생성 시에 사용된 인자에 적절하게). 또한 (처음에는 비어있는) lib/pythonX.Y/site-packages (윈도우에서는, Lib\site-packages) 서브 디렉터리를 만듭니다. 기존 디렉터리가 지정되면 재사용됩니다.

## 가상 환경 실행

- 가상환경 내에서 패키지들을 설치, 실행 가능
- 다른 프로젝트들과 독립적인 공간에서 개발환경 구성 가능

리눅스 환경:

```bash
source selenium/bin/activate
```

윈도우 환경:

```bash
cd selenium\Scripts
activate
```


## ChromeDriver - WebDriver for Chrome

- version
```bash
ChromeDriver: 86.0.4240.22
```
```bash
Supports Chrome version 86
```

- 크롬드라이버 다운로드 링크
```bash
https://chromedriver.chromium.org/downloads
```


## React Native, Expo 설치 안내 (Installation Process)



```bash
expo install react-native-webview
```


### Install Expo CLI

Expo CLI is the tool for developing and building Expo apps.

```bash
npm install -g expo-cli
```


### expo-permissions module


When you are creating an app that requires access to potentially sensitive information on a user's device, such as their location or contacts, you need to ask for the user's permission first. The expo-permissions module makes requesting these permissions easy, fast, and reliable.

```bash
expo install expo-permissions
```

## icon, splash size


### icon.png size

1024x1024 is a good size. The Expo build service will generate the other sizes for you. The largest size it generates is 1024x1024.

### splash.png size

I'll go with 1242 pixels wide and 2436 pixels tall -- this is the width of the iPhone 8 Plus (the widest iPhone) and the height of the iPhone X (the tallest iPhone)


## Start the build

### Run expo build:android or expo build:ios.

```bash
expo build:android
```

```bash
expo build:ios
```



### build for Android (APK or Android App Bundle)
APK

```bash
expo build:android -t apk
```

Android App Bundle

```bash
expo build:android -t app-bundle
```

## keystore 관리

Backup keystore and credentials 

```bash
expo fetch:android:keystore
```

