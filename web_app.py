#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author: https://github.com/Evil0ctal/
# @Time: 2021/11/06
# @Update: 2022/11/06
# @Function:
# 用于在线批量解析Douyin/TikTok的无水印视频/图集。
# 基于 PyWebIO，将scraper.py返回的内容显示在网页上。

import configparser
import os
import re
import time

from pywebio import *
from pywebio import config as pywebio_config
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info as session_info
from scraper import Scraper

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# 创建一个Scraper类的实例/Create an instance of the Scraper class
api = Scraper()


# 自动检测语言返回翻译/Auto detect language to return translation
def t(zh: str, en: str) -> str:
    return zh if 'zh' in session_info.user_language else en


# 解析抖音分享口令中的链接并返回列表/Parse the link in the Douyin share command and return a list
def find_url(string: str) -> list:
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url


# 校验输入值/Validate input value
def valid_check(input_data: str) -> str or None:
    # 检索出所有链接并返回列表/Retrieve all links and return a list
    url_list = find_url(input_data)
    # 总共找到的链接数量/Total number of links found
    total_urls = len(url_list)
    if total_urls == 0:
        return t('没有检测到有效的链接，请检查输入的内容是否正确。',
                 'No valid link detected, please check if the input content is correct.')
    else:
        # 最大接受提交URL的数量/Maximum number of URLs accepted
        max_urls = config['Web_APP']['Max_Take_URLs']
        if total_urls > int(max_urls):
            warn_info = t('URL数量过多，只会处理前{}个URL。'.format(max_urls),
                          'Too many URLs, only the first {} URLs will be processed.'.format(max_urls))
            return warn_info
        else:
            # 对每一个链接进行校验/Verify each link
            for i in url_list:
                if 'douyin.com' or 'tiktok.com' in i:
                    return None
                else:
                    warn_info = t('请确保输入链接均为[抖音|TikTok]链接， 请移除输入值：{}'.format(i),
                                  'Please make sure that the input link is a [Douyin|TikTok] link, please remove the input value: {}'.format(
                                      i))
                    return warn_info


# 错误处理/Error handling
def error_do(reason: str, value: str) -> None:
    # 输出一个毫无用处的信息
    put_html("<hr>")
    put_error(
        t("发生了了意料之外的错误，输入值已被记录。", "An unexpected error occurred, the input value has been recorded."))
    put_html('<h3>⚠{}</h3>'.format(t('详情', 'Details')))
    put_table([
        [t('原因', 'reason'), t('输入值', 'input value')],
        [reason, value]])
    put_markdown(t('可能的原因:', 'Possible reasons:'))
    put_markdown(t('服务器可能被目标主机的防火墙限流(稍等片刻后再次尝试)',
                   'The server may be limited by the target host firewall (try again after a while)'))
    put_markdown(t('输入了错误的链接(API-V1暂不支持主页链接解析)',
                   'Entered the wrong link (the home page link is not supported for parsing with API-V1)'))
    put_markdown(
        t('如果需要解析个人主页，请使用API-V2', 'If you need to parse the personal homepage, please use API-V2'))
    put_markdown(t('API-V2 文档: [https://api-v2.douyin.wtf/docs](https://api-v2.douyin.wtf/docs)',
                   'API-V2 Documentation: [https://api-v2.douyin.wtf/docs](https://api-v2.douyin.wtf/docs)'))
    put_markdown(t('该视频已经被删除或屏蔽(你看的都是些啥(⊙_⊙)?)',
                   'The video has been deleted or blocked (what are you watching (⊙_⊙)?)'))
    put_markdown(t('其他原因(请联系作者)', 'Other reasons (please contact the author)'))
    put_markdown(t('你可以在右上角的关于菜单中查看本站错误日志。',
                   'You can view the error log of this site in the about menu in the upper right corner.'))
    put_markdown('[{}](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/issues)'.format(
        t('点击此处在GitHub上进行反馈', 'Click here to give feedback on GitHub')))
    put_html("<hr>")
    if config['Web_APP']['Allow_Logs'] == 'True':
        # 将错误记录在logs.txt中
        error_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"{error_date}: 正在记录错误信息...")
        with open('logs.txt', 'a') as f:
            f.write(error_date + ":\n" + str(reason) + '\n' + "Input value: " + value + '\n')


# iOS快捷指令弹窗/IOS shortcut pop-up
def ios_pop_window():
    with popup(t("iOS快捷指令", "iOS Shortcut")):
        version = config["Web_API"]["iOS_Shortcut_Version"]
        update = config["Web_API"]['iOS_Shortcut_Update_Time']
        link = config["Web_API"]['iOS_Shortcut_Link']
        link_en = config["Web_API"]['iOS_Shortcut_Link_EN']
        note = config["Web_API"]['iOS_Shortcut_Update_Note']
        note_en = config["Web_API"]['iOS_Shortcut_Update_Note_EN']
        put_markdown(t('#### 📢 快捷指令介绍:', '#### 📢 Shortcut Introduction:'))
        put_markdown(
            t('快捷指令运行在iOS平台，本快捷指令可以快速调用本项目的公共API将抖音或TikTok的视频或图集下载到你的手机相册中，暂时只支持单个链接进行下载。',
              'The shortcut runs on the iOS platform, and this shortcut can quickly call the public API of this project to download the video or album of Douyin or TikTok to your phone album. It only supports single link download for now.'))
        put_markdown(t('#### 📲 使用方法 ①:', '#### 📲 Operation method ①:'))
        put_markdown(t('在抖音或TikTok的APP内，浏览你想要无水印保存的视频或图集。',
                       'The shortcut needs to be used in the Douyin or TikTok app, browse the video or album you want to save without watermark.'))
        put_markdown(t('然后点击右下角分享按钮，选择更多，然后下拉找到 "抖音TikTok无水印下载" 这个选项。',
                       'Then click the share button in the lower right corner, select more, and then scroll down to find the "Douyin TikTok No Watermark Download" option.'))
        put_markdown(t('如遇到通知询问是否允许快捷指令访问xxxx (域名或服务器)，需要点击允许才可以正常使用。',
                       'If you are asked whether to allow the shortcut to access xxxx (domain name or server), you need to click Allow to use it normally.'))
        put_markdown(t('该快捷指令会在你相册创建一个新的相薄方便你浏览保存的内容。',
                       'The shortcut will create a new album in your photo album to help you browse the saved content.'))
        put_markdown(t('#### 📲 使用方法 ②:', '#### 📲 Operation method ②:'))
        put_markdown(t('在抖音或TikTok的视频下方点击分享，然后点击复制链接，然后去快捷指令APP中运行该快捷指令。',
                       'Click share below the video of Douyin or TikTok, then click to copy the link, then go to the shortcut command APP to run the shortcut command.'))
        put_markdown(t('如果弹窗询问是否允许读取剪切板请同意，随后快捷指令将链接内容保存至相册中。',
                       'if the pop-up window asks whether to allow reading the clipboard, please agree, and then the shortcut command will save the link content to the album middle.'))
        put_html('<hr>')
        put_text(t(f"最新快捷指令版本: {version}", f"Latest shortcut version: {version}"))
        put_text(t(f"快捷指令更新时间: {update}", f"Shortcut update time: {update}"))
        put_text(t(f"快捷指令更新内容: {note}", f"Shortcut update content: {note_en}"))
        put_link("[点击获取快捷指令 - 中文]", link, new_window=True)
        put_html("<br>")
        put_link("[Click get Shortcut - English]", link_en, new_window=True)


# API文档弹窗/API documentation pop-up
def api_document_pop_window():
    with popup(t("API文档", "API Document")):
        put_markdown(t("💾API-V2文档", "💾API-V2 Document"))
        put_markdown(t('API-V2 支持抖音和TikTok的更多接口， 如主页解析，视频解析，视频评论解析，个人点赞列表解析等...',
                       'API-V2 supports more interfaces of Douyin and TikTok, such as home page parsing, video parsing, video comment parsing, personal like list parsing, etc...'))
        put_link('[API-V2 Docs]', 'https://api-v2.douyin.wtf/docs', new_window=True)
        put_html('<hr>')
        put_markdown(t("💽API-V1文档", "💽API-V1 Document"))
        put_markdown(t("API-V1 支持抖音和TikTok的单一视频解析，具体请查看接口文档。",
                       "API-V1 supports single video parsing of Douyin and TikTok. For details, please refer to the API documentation."))
        put_link('[API-V1 Docs]', 'https://api.douyin.wtf/docs', new_window=True)


# 日志文件弹窗/Log file pop-up
def log_popup_window():
    with popup(t('错误日志', 'Error Log')):
        put_html('<h3>⚠️{}</h3>'.format('关于解析失败可能的原因', 'About the possible reasons for parsing failure'))
        put_markdown(t('服务器可能被目标主机的防火墙限流(稍等片刻后再次尝试)',
                       'The server may be limited by the target host firewall (try again after a while)'))
        put_markdown(t('输入了错误的链接(API-V1暂不支持主页链接解析)',
                       'Entered the wrong link (the home page link is not supported for parsing with API-V1)'))
        put_markdown(
            t('如果需要解析个人主页，请使用API-V2', 'If you need to parse the personal homepage, please use API-V2'))
        put_markdown(t('API-V2 文档: [https://api-v2.douyin.wtf/docs](https://api-v2.douyin.wtf/docs)',
                       'API-V2 Documentation: [https://api-v2.douyin.wtf/docs](https://api-v2.douyin.wtf/docs)'))
        put_markdown(t('该视频已经被删除或屏蔽(你看的都是些啥(⊙_⊙)?)',
                       'The video has been deleted or blocked (what are you watching (⊙_⊙)?)'))
        put_markdown(t('[点击此处在GitHub上进行反馈](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/issues)',
                       '[Click here to feedback on GitHub](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/issues)'))
        put_html('<hr>')
        # 判断日志文件是否存在
        if os.path.exists('logs.txt'):
            put_text(t('点击logs.txt可下载日志:', 'Click logs.txt to download the log:'))
            content = open(r'./logs.txt', 'rb').read()
            put_file('logs.txt', content=content)
            with open('./logs.txt', 'r') as f:
                content = f.read()
                put_text(str(content))
        else:
            put_text(t('日志文件不存在，请等发生错误时再回来看看。',
                       'The log file does not exist, please come back and take a look when an error occurs.'))


# 关于弹窗/About pop-up
def about_popup_window():
    with popup(t('更多信息', 'More Information')):
        put_html('<h3>👀{}</h3>'.format(t('访问记录', 'Visit Record')))
        put_image('https://views.whatilearened.today/views/github/evil0ctal/TikTokDownload_PyWebIO.svg',
                  title='访问记录')
        put_html('<hr>')
        put_html('<h3>⭐Github</h3>')
        put_markdown('[Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API)')
        put_html('<hr>')
        put_html('<h3>🎯{}</h3>'.format(t('反馈', 'Feedback')))
        put_markdown('{}：[issues](https://github.com/Evil0ctal/Douyin_TikTok_Download_API/issues)'.format(
            t('Bug反馈', 'Bug Feedback')))
        put_html('<hr>')
        put_html('<h3>💖WeChat</h3>')
        put_markdown('WeChat：[Evil0ctal](https://mycyberpunk.com/)')
        put_html('<hr>')


# 网站标题/Website title
title = config['Web_APP']['Web_Title']

# 网站描述/Website description
description = config['Web_APP']['Web_Description']


# 网站设置/Website settings
# web_config = pywebio_config(title=title, description=description)
# 程序入口/Main interface
@pywebio_config(title=title, description=description, theme='minty')
def main():
    # 关键字信息
    keywords = config['Web_APP']['Keywords']
    # 设置favicon
    favicon_url = "https://raw.githubusercontent.com/Evil0ctal/Douyin_TikTok_Download_API/main/favicon/android-chrome-512x512.png"
    session.run_js("""
    $('head').append('<meta name=referrer content=no-referrer>');
    $('#favicon32,#favicon16').remove(); 
    $('head').append('<link rel="icon" type="image/png" href="%s">')
    """ % favicon_url)
    # 设置Keywords
    session.run_js("""
        $('head').append('<meta name="keywords" content={}>')
        """.format(keywords))
    # 修改footer
    session.run_js("""$('footer').remove()""")
    # 网站标题/Website title
    title = t(config['Web_APP']['Web_Title'], config['Web_APP']['Web_Title_English'])
    put_markdown("""<div align='center' ><font size='20'>😼{}</font></div>""".format(title))
    put_html('<hr>')
    put_row(
        [put_button(t("iOS快捷指令", 'iOS Shortcuts'), onclick=lambda: ios_pop_window(), link_style=True, small=True),
         put_button("API", onclick=lambda: api_document_pop_window(), link_style=True, small=True),
         put_button(t("日志", "Log"), onclick=lambda: log_popup_window(), link_style=True, small=True),
         put_button(t("关于", 'About'), onclick=lambda: about_popup_window(), link_style=True, small=True)
         ])
    placeholder = t(
        "批量解析请直接粘贴多个口令或链接，无需使用符号分开，支持抖音和TikTok链接混合，暂时不支持作者主页链接批量解析。",
        "Batch parsing, please paste multiple passwords or links directly, no need to use symbols to separate, support for mixing Douyin and TikTok links, temporarily not support for author home page link batch parsing.")
    input_data = textarea(t('请将抖音或TikTok的分享口令或网址粘贴于此',
                            "Please paste the share code or URL of [Douyin|TikTok] here"),
                          type=TEXT,
                          validate=valid_check, required=True,
                          placeholder=placeholder,
                          position=0)
    url_lists = find_url(input_data)
    # 解析开始时间
    start = time.time()
    # 成功/失败统计
    success_count = 0
    failed_count = 0
    # 解析成功的url
    success_list = []
    # 解析失败的url
    failed_list = []
    # 输出一个提示条
    with use_scope('loading_text'):
        # 输出一个分行符
        put_row([put_html('<hr>')])
        put_warning(t('Server酱正收到你输入的链接啦！(◍•ᴗ•◍)\n请稍等片刻...',
                      'ServerChan is receiving your input link! (◍•ᴗ•◍)\nPlease wait a moment...'))
    # 遍历链接列表
    for url in url_lists:
        # 链接编号
        url_index = url_lists.index(url) + 1
        # 解析
        data = api.hybrid_parsing(video_url=url)
        # 判断是否解析成功/失败
        status = True if data.get('status') == 'success' else False
        # 如果解析成功
        if status:
            # 创建一个视频/图集的公有变量
            url_type = t('视频', 'Video') if data.get('type') == 'video' else t('图片', 'Image')
            platform = data.get('platform')
            table_list = [[t('类型', 'type'), t('内容', 'content')],
                          [t('解析类型', 'Type'), url_type],
                          [t('平台', 'Platform'), platform],
                          [f'{url_type} ID', data.get('aweme_id')],
                          [t(f'{url_type}描述', 'Description'), data.get('desc')],
                          [t('作者昵称', 'Author nickname'), data.get('author').get('nickname')],
                          [t('作者ID', 'Author ID'), data.get('author').get('unique_id')],
                          [t('API链接', 'API URL'), put_link(t('点击查看', 'Click to view'),
                                                             f"{config['Web_API']['Domain']}/api?url={url}&minimal=false",
                                                             new_window=True)],
                          [t('API链接-精简', 'API URL-Minimal'), put_link(t('点击查看', 'Click to view'),
                                                                          f"{config['Web_API']['Domain']}/api?url={url}&minimal=true",
                                                                          new_window=True)]
                          ]
            # 如果是视频/If it's video
            if url_type == t('视频', 'Video'):
                # 添加视频信息
                table_list.insert(4, [t('视频链接-水印', 'Video URL-Watermark'),
                                      put_link(t('点击查看', 'Click to view'),
                                               data.get('video_data').get('wm_video_url_HQ'), new_window=True)])
                table_list.insert(5, [t('视频链接-无水印', 'Video URL-No Watermark'),
                                      put_link(t('点击查看', 'Click to view'),
                                               data.get('video_data').get('nwm_video_url_HQ'), new_window=True)])
                table_list.insert(6, [t('视频下载-水印', 'Video Download-Watermark'),
                                      put_link(t('点击下载', 'Click to download'),
                                               f"{config['Web_API']['Domain']}/download?url={url}&prefix=true&watermark=true",
                                               new_window=True)])
                table_list.insert(6, [t('视频下载-无水印', 'Video Download-No-Watermark'),
                                      put_link(t('点击下载', 'Click to download'),
                                               f"{config['Web_API']['Domain']}/download?url={url}&prefix=true&watermark=false",
                                               new_window=True)])
            # 如果是图片/If it's image
            elif url_type == t('图片', 'Image'):
                # 添加图片下载链接
                table_list.insert(4, [t('图片打包下载-水印', 'Download images ZIP-Watermark'),
                                      put_link(t('点击下载', 'Click to download'),
                                               f"{config['Web_API']['Domain']}/download?url={url}&prefix=true&watermark=true",
                                               new_window=True)])
                table_list.insert(5, [t('图片打包下载-无水印', 'Download images ZIP-No-Watermark'),
                                      put_link(t('点击下载', 'Click to download'),
                                               f"{config['Web_API']['Domain']}/download?url={url}&prefix=true&watermark=false",
                                               new_window=True)])
                # 添加图片信息
                no_watermark_image_list = data.get('image_data').get('no_watermark_image_list')
                for image in no_watermark_image_list:
                    table_list.append([t('图片直链: ', 'Image URL:'),
                                       put_link(t('点击打开图片', 'Click to open image'), image, new_window=True)])
                    table_list.append([t('图片预览(如格式可显示): ', 'Image preview (if the format can be displayed):'),
                                       put_image(image, width='50%', height='50%')])
            # 向网页输出表格/Put table on web page
            with use_scope(str(url_index)):
                # 显示进度
                put_info(t(f'正在解析第{url_index}个链接: {url}', f'Parsing the {url_index}th link: {url}'))
                put_table(table_list)
                put_html('<hr>')
            scroll_to(str(url_index))
            success_count += 1
            success_list.append(url)
            # print(f'success_count: {success_count}, success_list: {success_list}')
        # 如果解析失败/Failed to parse
        else:
            failed_count += 1
            failed_list.append(url)
            # print(f'failed_count: {failed_count}, failed_list: {failed_list}')
            error_msg = data.get('message').split('/')
            error_msg = t(error_msg[0], error_msg[1])
            with use_scope(str(url_index)):
                error_do(reason=error_msg, value=url)
            scroll_to(str(url_index))
    # 全部解析完成跳出for循环/All parsing completed, break out of for loop
    with use_scope('result'):
        # 清除进度条
        clear('loading_text')
        # 滚动至result
        scroll_to('result')
        # for循环结束，向网页输出成功提醒
        put_success(t('解析完成啦 ♪(･ω･)ﾉ\n请查看以下统计信息，如果觉得有用的话请在GitHub上帮我点一个Star吧！',
                      'Parsing completed ♪(･ω･)ﾉ\nPlease check the following statistics, and if you think it\'s useful, please help me click a Star on GitHub!'))
        # 将成功，失败以及总数量显示出来并且显示为代码方便复制
        put_markdown(
            f'**{t("成功", "Success")}:** {success_count} **{t("失败", "Failed")}:** {failed_count} **{t("总数量", "Total")}:** {success_count + failed_count}')
        # 成功列表
        if success_count > 0:
            put_markdown(f'**{t("成功列表", "Success list")}:**')
            put_code('\n'.join(success_list))
        # 失败列表
        if failed_count > 0:
            put_markdown(f'**{t("失败列表", "Failed list")}:**')
            put_code('\n'.join(failed_list))
        # 将url_lists显示为代码方便复制
        put_text(t('以下是您输入的所有链接', 'The following are all the links you entered'))
        put_code('\n'.join(url_lists))
        # 解析结束时间
        end = time.time()
        # 计算耗时,保留两位小数
        time_consuming = round(end - start, 2)
        # 显示耗时
        put_markdown(f"**{t('耗时', 'Time consuming')}:** {time_consuming}s")
        # 放置一个按钮，点击后跳转到顶部
        put_button(t('回到顶部', 'Back to top'), onclick=lambda: scroll_to('1'), color='success', outline=True)
        # 返回主页链接
        put_link(t('再来一波 (つ´ω`)つ', 'Another wave (つ´ω`)つ'), '/')


if __name__ == '__main__':
    # 获取空闲端口
    if os.environ.get('PORT'):
        port = int(os.environ.get('PORT'))
    else:
        # 在这里修改默认端口(记得在防火墙放行该端口)
        port = int(config['Web_APP']['Port'])
    # 判断是否使用CDN加载前端资源
    cdn = True if config['Web_APP']['PyWebIO_CDN'] == 'True' else False
    # 启动Web服务\Start Web service
    start_server(main, port=port, debug=False, cdn=cdn)
