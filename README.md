<h1 align="center">
 Douyin_TikTok_Download_API(抖音/TikTok无水印解析API)
 <br><br>
 <a href="https://douyin.wtf/" alt="logo" ><img src="https://raw.githubusercontent.com/Evil0ctal/Douyin_TikTok_Download_API/main/logo/logo192.png" width="120"/></a>
</h1>
<p align="center">
 <a href="https://github.com/Evil0ctal/Douyin_TikTok_Download_API#%E8%BF%90%E8%A1%8C%E8%AF%B4%E6%98%8E%E7%BB%8F%E8%BF%87%E6%B5%8B%E8%AF%95%E8%BF%87%E7%9A%84python%E7%89%88%E6%9C%AC%E4%B8%BA38">📝运行说明</a> •
  <a href="https://github.com/Evil0ctal/Douyin_TikTok_Download_API/#%EF%B8%8Fapi使用">👽️API使用</a> •
  <a href="https://github.com/Evil0ctal/Douyin_TikTok_Download_API#%E9%83%A8%E7%BD%B2%E6%96%B9%E5%BC%8F%E4%B8%80-%E6%89%8B%E5%8A%A8%E9%83%A8%E7%BD%B2">🔧手动部署</a> •
  <a href="https://github.com/Evil0ctal/Douyin_TikTok_Download_API#%E9%83%A8%E7%BD%B2%E6%96%B9%E5%BC%8F%E4%BA%8C-docker">🚧Docker部署</a> •
  <a href="https://hub.docker.com/repository/docker/evil0ctal/douyin_tiktok_download_api">📦️Docker镜像</a> •
  <a href="https://github.com/Evil0ctal/Douyin_TikTok_Download_API#%EF%B8%8F-贡献者">🧑‍💻贡献者</a>
</p>
<br>

![](https://views.whatilearened.today/views/github/Evil0ctal/TikTokDownloader_PyWebIO.svg)[![GitHub license](https://img.shields.io/github/license/Evil0ctal/TikTokDownloader_PyWebIO)](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/blob/main/LICENSE)[![GitHub issues](https://img.shields.io/github/issues/Evil0ctal/TikTokDownloader_PyWebIO)](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/issues)[![GitHub forks](https://img.shields.io/github/forks/Evil0ctal/TikTokDownloader_PyWebIO)](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/network)[![GitHub stars](https://img.shields.io/github/stars/Evil0ctal/TikTokDownloader_PyWebIO)](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/stargazers)[![Docker Image size](https://img.shields.io/docker/image-size/evil0ctal/douyin_tiktok_download_api?style=flat-square)](https://hub.docker.com/repository/docker/evil0ctal/douyin_tiktok_download_api)

Language:  [[English](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/main/README.en.md)]  [[简体中文](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/main/README.md)]  [[繁体中文](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/main/README.zh-TW.md)]

## 👻介绍

本项目使用 [PyWebIO](https://github.com/pywebio/PyWebIO)，[FastAPI](https://fastapi.tiangolo.com/)，[Requests](https://requests.readthedocs.io/)，利用Python编写并实现可以在线批量解析下载抖音/TikTok的无水印视频/图片，部署你自己的解析|无水印API，调用scraper.py作为解析库等功能.....

*一些简单的运用场景：*

*下载禁止下载的视频，进行数据爬取分析，iOS无水印下载（搭配[iOS自带的快捷指令APP](https://apps.apple.com/cn/app/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/id915249334)
配合本项目API实现应用内|剪贴板下载）等.....*

## 🖥公共站点: 我很脆弱...请不要随意打我 ‎(·•᷄ࡇ•᷅ ）

> **API-V2:** 支持输入`Douyin|TikTok`用户主页爬取该作者[主页视频数据(去水印链接, 已点赞视频列表(权限需为公开), 视频评论数据, 背景音乐视频列表数据, 等等...), 详细信息请查看V2文档, 服务器响应时间有时会变长, 使用时请将`timeout`值设高.

🍔Web APP: [https://douyin.wtf/](https://douyin.wtf/)

🍟API-V1: [https://api.douyin.wtf/](https://api.douyin.wtf/)

🌭API-V2: [https://api-v2.douyin.wtf/docs](https://api-v2.douyin.wtf/docs)

💾iOS Shortcut(快捷指令): [issue#53](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/issues/53)

🗂快捷指令历史版本: [Shortcuts release](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/issues/53)

📦️Tiktok/抖音下载器(桌面应用)：[Tairraos/TikDown](https://github.com/Tairraos/TikDown/)

## ⚗️技术栈

* [web_app.py]("https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/Stable/web_app.py") - [PyWebIO](https://www.pyweb.io/)
* [web_api.py]("https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/Stable/web_app.py") - [FastAPI](https://fastapi.tiangolo.com/)
* [scraper.py](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/Stable/scraper.py) - [Requests](https://requests.readthedocs.io/)

> ***scraper.py:***

- 向[Douyin|TikTok]的API提交请求并取回数据，处理后返回字典(dict)。

> ***web_api.py:***

- 获得参数并使用`Scraper()`类处理数据后以JSON形式返回，视频下载，

> ***web_app.py:***

- 为`web_api.py`以及`scraper.py`制作的简易Web程序，将网页输入的值进行处理后使用`Scraper()`类处理并配合`web_api.py`的接口输出在网页上(类似前后端分离，参数大多可在`config.ini`中进行修改。)

## 💡项目文件结构

```
# 请根据需要自行修改config.ini中的内容
.
└── Douyin_TikTok_Download_API/
    ├── /static(PyWebIO静态前端资源)
    ├── web_app.py(网页APP)
    ├── web_api.py(API)
    ├── scraper.py(解析库)
    ├── config.ini(所有项目的配置文件，包含端口及代理等，如需请自行修改该文件。)
    ├── logs.txt(web_错误日志，自动生成。)
    └── API_logs.txt(API调用日志，自动生成。)
```

## 💯已支持功能：

- 抖音（抖音海外版TikTok）视频/图片解析
- Web APP批量解析(支持抖音/TikTok混合提交)
- Web APP中文/英文自动切换
- Web APP解析结果页批量下载无水印视频(V3.0.0暂时删除)
- API调用
- 制作[pip包](https://pypi.org/project/DT-Scraper/)方便使用
- [[iOS快捷指令快速调用API]](https://apps.apple.com/cn/app/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/id915249334)实现应用内下载无水印视频/图集

- 解析作者主页内所有视频([API-V2](https://api-v2.douyin.wtf/docs) 支持抖音/TikTok)

- 解析视频内所有评论信息([API-V2](https://api-v2.douyin.wtf/docs) 支持抖音/TikTok)

---

## 🤦‍后续功能：

- [ ] 欢迎提出新的并将你的思路在issue中与我分享

---

## 🧭运行说明(Python版本 > 3.0):

> 🚨如果你要部署本项目，请参考部署方式([Docker部署](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/main/README.md#%E9%83%A8%E7%BD%B2%E6%96%B9%E5%BC%8F%E4%BA%8C-docker "Docker部署"), [手动部署](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/main/README.md#%E9%83%A8%E7%BD%B2%E6%96%B9%E5%BC%8F%E4%B8%80-%E6%89%8B%E5%8A%A8%E9%83%A8%E7%BD%B2 "手动部署"))

- 克隆本仓库：

```console
git clone https://github.com/Evil0ctal/Douyin_TikTok_Download_API.git
```

- 移动至仓库目录：

```console
cd Douyin_TikTok_Download_API
```

- 安装依赖库：

```console
pip install -r requirements.txt
```

- 修改config.ini(可选)：

```console
vim config.ini
```

- 网页解析

```console
# 运行web_app.py
python3 web_app.py
```

- API

```console
# 运行web_api.py
python3 web_api.py
```

- 调用解析库

```python
# pip install DT-Scraper
from DT_scraper.scraper import Scraper

api = Scraper()

def main_test():
	while True:
		url = input("Enter your Douyin/TikTok url here to test: ")
		if 'douyin.com' in url:
			video_id = api.get_douyin_video_id(url)
			if video_id:
				video_data = api.get_douyin_video_data(video_id)
				print(video_data)
		else:
			video_id = api.get_tiktok_video_id(url)
			if video_id:
				tiktok_data = api.get_tiktok_video_data(video_id)
				print(tiktok_data)
```

- 入口(端口可在config.ini文件中修改)

```text
Web入口:
http://localhost(服务器IP):8080/
API入口:
http://localhost(服务器IP):8000/
```

## 🗺️支持的提交格式(包含但不仅限于以下例子)：

- 抖音分享口令  (APP内复制)

```text
例子：7.43 pda:/ 让你在几秒钟之内记住我  https://v.douyin.com/L5pbfdP/ 复制此链接，打开Dou音搜索，直接观看视频！
```

- 抖音短网址 (APP内复制)

```text
例子：https://v.douyin.com/L4FJNR3/
```

- 抖音正常网址 (网页版复制)

```text
例子：
https://www.douyin.com/video/6914948781100338440
```

- 抖音发现页网址 (APP复制)

```text
例子：
https://www.douyin.com/discover?modal_id=7069543727328398622
```

- TikTok短网址 (APP内复制)

```text
例子：
https://vm.tiktok.com/TTPdkQvKjP/
```

- TikTok正常网址 (网页版复制)

```text
例子：
https://www.tiktok.com/@tvamii/video/7045537727743380782
```

- 抖音/TikTok批量网址(无需使用符合隔开)

```text
例子：
2.84 nqe:/ 骑白马的也可以是公主%%百万转场变身  https://v.douyin.com/L4FJNR3/ 复制此链接，打开Dou音搜索，直接观看视频！
8.94 mDu:/ 让你在几秒钟之内记住我  https://v.douyin.com/L4NpDJ6/ 复制此链接，打开Dou音搜索，直接观看视频！
9.94 LWz:/ ok我坦白交代 %%knowknow  https://v.douyin.com/L4NEvNn/ 复制此链接，打开Dou音搜索，直接观看视频！
https://www.tiktok.com/@gamer/video/7054061777033628934
https://www.tiktok.com/@off.anime_rei/video/7059609659690339586
https://www.tiktok.com/@tvamii/video/7045537727743380782
```

## 🛰️API文档

> 也可以在web_api.py的代码中看到接口文档

***API-V1文档：***
[http://localhost(服务器IP):8000/docs]("http://localhost:8000/docs")
[https://api.douyin.wtf/docs]("https://api.douyin.wtf/docs")

***API-V2文档：***
[https://api.douyin.wtf/docs]("https://api-v2.douyin.wtf/docs")

---

## 💾部署(方式一 手动部署)

> 注：
> 截图可能因更新问题与文字不符，一切请优先参照文字叙述。

> 最好将本项目部署至海外服务器(优先选择美国地区的服务器)，否则可能会出现奇怪的问题。

例子：
项目部署在国内服务器，而人在美国，点击结果页面链接报错403 ，目测与抖音CDN有关系。
项目部署在韩国服务器，解析TikTok报错 ，目测TikTok对某些地区或IP进行了限制。

> 使用宝塔Linux面板进行部署(
> 中文宝塔要强制绑定手机号了，很流氓且无法绕过，建议使用宝塔国际版，谷歌搜索关键字aapanel自行安装，部署步骤相似。)

- 首先要去安全组开放8080和8000端口（Web默认8080，API默认8000，可以在文件config.ini中修改。）
- 在宝塔应用商店内搜索python并安装项目管理器 (推荐使用1.9版本)

![](https://raw.githubusercontent.com/Evil0ctal/TikTokDownloader_PyWebIO/main/Screenshots/BT_Linux_Panel_Deploy_1.png)

---

- 创建一个项目名字随意
- 路径选择你上传文件的路径
- Python版本需要至少3以上(在左侧版本管理中自行安装)
- 框架修改为`Uvicorn`
- 启动方式修改为`python`
- Web启动文件选择`web_app.py`
- API启动文件选择`web_api.py`
- 勾选安装模块依赖
- 开机启动随意
- 请自行判断端口是否被占用，运行端口可在文件config.ini中修改。
- 如果有大量请求请使用 *进程守护* 启动防止进程关闭

![](https://raw.githubusercontent.com/Evil0ctal/TikTokDownloader_PyWebIO/main/Screenshots/BT_Linux_Panel_Deploy_2.png)

---

## 💾部署(方式二 Docker)

- 安装docker

```yaml
curl -fsSL get.docker.com -o get-docker.sh&&sh get-docker.sh &&systemctl enable docker&&systemctl start docker
```

- 留下config.int和docker-compose.yml文件即可
- 运行命令,让容器在后台运行

```yaml
docker compose up -d
```

- 查看容器日志

```yaml
docker logs -f douyin_tiktok_download_api
```

- 删除容器

```yaml
docker rm -f douyin_tiktok_download_api
```

- 更新

```yaml
docker compose pull && docker compose down && docker compose up -d
```

## ❤️ 贡献者

[![](https://github.com/Evil0ctal.png?size=50)](https://github.com/Evil0ctal)
[![](https://github.com/jw-star.png?size=50)](https://github.com/jw-star)
[![](https://github.com/Jeffrey-deng.png?size=50)](https://github.com/Jeffrey-deng)
[![](https://github.com/chris-ss.png?size=50)](https://github.com/chris-ss)
[![](https://github.com/weixuan00.png?size=50)](https://github.com/weixuan00)
[![](https://github.com/Tairraos.png?size=50)](https://github.com/Tairraos)

## 🎉截图

> 注：
> 截图可能因更新问题与文字不符，一切请优先参照文字叙述。

<details><summary>点击展开截图</summary>

<hr>

- 主界面

![](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/blob/main/Screenshots/home.png)

---

- 解析完成

> 单个

![](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/blob/main/Screenshots/single_result.png)

---

> 批量

![](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/blob/main/Screenshots/multi_results.png)

---

- API提交/返回

> 视频返回值

![](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/blob/main/Screenshots/api_video_result.png)

> 图集返回值

![](https://github.com/Evil0ctal/TikTokDownloader_PyWebIO/blob/main/Screenshots/api_image_result.png)

> TikTok返回值

![](https://raw.githubusercontent.com/Evil0ctal/TikTokDownloader_PyWebIO/main/Screenshots/tiktok_API.png)

---

</details>

## 📜 脚注

[MIT License]("https://github.com/Evil0ctal/Douyin_TikTok_Download_API/blob/Stable/LICENSE")

> Start: 2021/11/06
> GitHub [@Evil0ctal](https://github.com/Evil0ctal)
> Email Evil0ctal1985@gmail.com



