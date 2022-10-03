"""
Chapter 4
Python Advanced(4)
Keyword - Github, package deploy

"""

# py_ad_4_3: 완성된 패키지 임포트
from py_ad_4_3 import GifConverter as gfc

# 클래서 생성
c = gfc('../project/images/*.png', '../project/image_out/result.gif', (320, 240))

# 실행
c.convert_gif()

"""
패키지 배포 순서(Github)
1. https://github.com 회원가입
2. git 설치 확인(생략) -> .gitignore 파일 고려
3. git add -> commit -> push
    - git repository 저장소 생성
    - git init
    - git add .
    - git status
    - git commit -m 'message'
    - git remote add origin 'your_repository'
    - git push origin master
4. PyPI 형태의 패키지 구조를 github repository에 push
5. 설치 확인(pip install git+https://your-repository-url)

"""