"""
Chapter 4
Python Advanced(4)
Keyword - png(jpg) to gif, pil, image

"""
"""
패키지 작성
-> GIF 이미지 변환기 -> 패키지 호출 형태로 작성

"""

import glob
from PIL import Image


class GifConverter:
    def __init__(self, path_in=None, path_out=None, resize=(320,240)):
        """

        :param path_in: 원본 여러 이미지 경로(Ex: images/*.png)
        :param path_out: 결과 이미지 경로(Ex: output/filename.gif)
        :param resize: resizing 크기 ((320, 240))
        """
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize

    def convert_gif(self):
        """
        GIF 이미지 변환 기능 수행
        :return:
        """
        img, *images = \
            [Image.open(f).resize((320, 240), Image.ANTIALIAS) for f in sorted(glob.glob(self.path_in))]

        try:
           img.save(
               fp=self.path_out,
               format='GIF',
               append_images=images,
               save_all=True,
               duration=500,
               loop=0
           )
        except IOError:
            print('Cannot convert!', img)


if __name__ == '__main__':
    # class
    c = GifConverter('../project/images/*.png', '../project/image_out/result.gif', (320, 240))
    # 변환
    c.convert_gif()

    print(GifConverter.convert_gif.__doc__)
