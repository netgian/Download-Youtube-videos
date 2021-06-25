from pytube import YouTube


class Ytdownload(YouTube):
    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def _genFormats():
        quality = ["2160p", "1040p", "1080p", "720p", "480p", "360p", "240p", "144p"]
        formats = []
        for q in quality:
            for i in range(60, 0, -1):
                formats.append(f'mime_type="video/mp4" res="{q}" fps="{i}fps"')
        return formats

    def _sortStreams(self):
        for f in self._genFormats():
            for i, s in enumerate(self.streams):
                if f in str(s):
                    return self.streams[i]

    def downloadVideo(self):
        video = self._sortStreams()
        video.download() if video else input("Error")


if __name__ == '__main__':
    a = Ytdownload(input("Youtube url: "))
    a.downloadVideo()
