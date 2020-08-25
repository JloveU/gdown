import os

from gdown.download import download


def test_download():
    download("https://download-ssl.firefox.com.cn/releases/firefox/79.0/zh-CN/Firefox-latest.dmg", byte_range="10485760-", split_size=10 * 1024 * 1024)

    url = "https://raw.githubusercontent.com/wkentaro/gdown/3.1.0/gdown/__init__.py"  # NOQA
    output = "/tmp/gdown_r"

    # Usage before https://github.com/wkentaro/gdown/pull/32
    assert download(url, output, quiet=False) == output
    os.remove(output)
