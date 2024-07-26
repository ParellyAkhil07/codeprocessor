
from playwright import playwright

def test_maven_wrapper_download(playwright: playwright):
    base_directory = "/path/to/your/project/directory"
    downloader = MavenWrapperDownloader(base_directory)
    downloader.download_maven_wrapper_jar()
    assert downloader.is_maven_wrapper_jar_downloaded()