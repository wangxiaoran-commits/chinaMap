import pandas as pd
import numpy as np
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

# 数据
data = {
    'Monitoring_province': ['Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong', 'Guangxi', 'Guizhou', 'Hainan', 'Hebei', 'Heilongjiang', 'Henan', 'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu', 'Jiangxi', 'Jilin', 'Liaoning', 'Ningxia', 'Qinghai', 'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Sichuan', 'Tianjin', 'Xinjiang', 'Yunnan', 'Zhejiang'],
    'HI-improve': [0.234909078, 0.088363414, -0.0024677, -1.32718E-05, 1.61559E-06, 0.240590773, 0.002150823, -0.00030688, -0.068470662, -0.020679594, 0.055557462, 0.033880438, -0.00561682, 2.24358E-08, -4.21451E-05, 0.128740684, 0.128740684, 0.00488313, -0.000918038, 0.000168892, 0.001000218, -6.16307E-07, 0.271631734, 0.032445814, 0.005212625, 0.233899162, -0.163017937, 1.30159E-05, 0.492160834, 0.078406098]
}

df = pd.DataFrame(data)
pd.set_option('display.float_format', lambda x: f'{x:.10f}')

df['HI-improve_exp'] = np.sqrt(np.exp(df['HI-improve'])+1)

# 英文省份名称到中文的映射
province_map = {
    'Anhui': '安徽省', 'Beijing': '北京市', 'Chongqing': '重庆市', 'Fujian': '福建省', 'Gansu': '甘肃省',
    'Guangdong': '广东省', 'Guangxi': '广西壮族自治区', 'Guizhou': '贵州省', 'Hainan': '海南省', 'Hebei': '河北省',
    'Heilongjiang': '黑龙江省', 'Henan': '河南省', 'Hubei': '湖北省', 'Hunan': '湖南省', 'Inner Mongolia': '内蒙古自治区',
    'Jiangsu': '江苏省', 'Jiangxi': '江西省', 'Jilin': '吉林省', 'Liaoning': '辽宁省', 'Ningxia': '宁夏回族自治区',
    'Qinghai': '青海省', 'Shaanxi': '陕西省', 'Shandong': '山东省', 'Shanghai': '上海市', 'Shanxi': '山西省',
    'Sichuan': '四川省', 'Tianjin': '天津市', 'Xinjiang': '新疆维吾尔自治区', 'Yunnan': '云南省', 'Zhejiang': '浙江省',
    'Tibet': '西藏自治区', 'Hong Kong': '香港特别行政区', 'Macau': '澳门特别行政区', 'Taiwan': '台湾省'
}

# 将英文省份名称转换为中文
df['Monitoring_province'] = df['Monitoring_province'].map(province_map)

# 准备数据
map_data = [list(z) for z in zip(df['Monitoring_province'], df['HI-improve_exp'])]

# 创建地图
map_chart = (
    Map()
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),showLegendSymbol=False)
    .add(
        "HI-improve_exp",
        map_data,
        "china",
        label_opts=opts.LabelOpts(
            is_show=True,
            position='inside',
            formatter=JsCode("""
            function(params) {
                var names = {
                    '安徽省': 'Anhui', '北京市': 'Beijing', '重庆市': 'Chongqing', '福建省': 'Fujian', '甘肃省': 'Gansu',
                    '广东省': 'Guangdong', '广西壮族自治区': 'Guangxi', '贵州省': 'Guizhou', '海南省': 'Hainan', '河北省': 'Hebei',
                    '黑龙江省': 'Heilongjiang', '河南省': 'Henan', '湖北省': 'Hubei', '湖南省': 'Hunan', '内蒙古自治区': 'Inner Mongolia',
                    '江苏省': 'Jiangsu', '江西省': 'Jiangxi', '吉林省': 'Jilin', '辽宁省': 'Liaoning', '宁夏回族自治区': 'Ningxia',
                    '青海省': 'Qinghai', '陕西省': 'Shaanxi', '山东省': 'Shandong', '上海市': 'Shanghai', '山西省': 'Shanxi',
                    '四川省': 'Sichuan', '天津市': 'Tianjin', '新疆维吾尔自治区': 'Xinjiang', '云南省': 'Yunnan', '浙江省': 'Zhejiang',
                    '西藏自治区': 'Xizang', '香港特别行政区': 'HK', '澳门特别行政区': 'Macao', '台湾省': 'Taiwan'
                };
                return names[params.name];
            }
            """)
        )
    )
    .set_series_opts(showLegendSymbol=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各省HI-improve指数图"),
        visualmap_opts=opts.VisualMapOpts(
            min_=1.2042135623,
            max_=1.6242135623,
            is_piecewise=False,
            range_color=[
                "#0000FF", "#FFFFFF", "#FF0000"  # 蓝色到白色再到红色渐变
            ],
            precision=10,
            range_opacity=[0.3, 1],
            pos_top="15%",  # 向上移动图例
            pos_left="6%" , # 移动图例到左边
        )
        )
    )



# 渲染图表到HTML文件
map_chart.render("china_map_hi_improve2.html")