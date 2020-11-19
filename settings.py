# -*- coding: utf-8 -*-

# 默认url
DEFAULT_URL = 'https://weibo.com/%s/like?from=page_100406_profile&wvr=6&mod=like'
# 默认ID
DEFAULT_ID = 1811978342

# 默认驱动路径
CHROMEDRIVER_URL = '/usr/local/bin/chromedriver'
# 默认存储位置
XLWT_URL = './%s.xlsx'
# dom默认配置
OPTION = {
    'empty': 'WB_empty',  # 瀑布流对应样式
    'text': 'WB_text',  # 正文对应样式
    'page': 'page',  # 翻页对应样式
    'info': 'WB_info',  # 翻页对应样式
    # 'face': 'W_face_radius',  # 博主头像 # 不确定dom 暂时不存
    'form': 'WB_from'  # 时间以及状态
}
