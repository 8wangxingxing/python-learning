import json
import requests

# 数据文件路径（保存收藏的城市）
WEATHER_FILE = 'weather.json'
# 天气接口地址，{city} 会替换成要查询的城市
WEATHER_URL = 'https://wttr.in/{city}?format=j1&lang=zh'

# 天气代码对应的中文（来自 wttr.in 的天气代码）
WEATHER_CODE = {
    113: '晴',
    116: '多云',
    119: '阴',
    122: '阴',
    143: '薄雾',
    176: '局部有阵雨',
    179: '局部有阵雪',
    182: '局部有雨夹雪',
    185: '局部有冻毛毛雨',
    188: '可能有雷阵雨',
    191: '刮风下雪',
    200: '暴风雪',
    227: '刮风下雪',
    230: '暴风雪',
    248: '雾',
    260: '冻雾',
    263: '局部有毛毛雨',
    266: '毛毛雨',
    281: '冻毛毛雨',
    284: '强冻毛毛雨',
    293: '局部有小雨',
    296: '小雨',
    299: '局部有中雨',
    302: '中雨',
    305: '局部有大雨',
    308: '大雨',
    311: '小冻雨',
    314: '中或强冻雨',
    317: '小雨夹雪',
    320: '中或大雨夹雪',
    323: '局部有小雪',
    326: '小雪',
    329: '局部有中雪',
    332: '中雪',
    335: '局部有大雪',
    338: '大雪',
    350: '冰粒',
    353: '小阵雨',
    356: '中或强阵雨',
    359: '强降雨',
    362: '小雨夹雪阵雨',
    365: '中或强雨夹雪阵雨',
    368: '小阵雪',
    371: '中或强阵雪',
    374: '小冰粒阵雨',
    377: '中或强冰粒阵雨',
    386: '雷雨',
    389: '中或强雷雨',
    392: '雷雪',
    395: '中或强雷雪',
}


def load_cities():
    """读取收藏的城市列表"""
    try:
        with open(WEATHER_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_cities(cities):
    """保存收藏的城市列表"""
    with open(WEATHER_FILE, 'w', encoding='utf-8') as f:
        json.dump(cities, f, ensure_ascii=False, indent=4)


def get_weather(city):
    """查询一个城市的当前天气"""
    try:
        response = requests.get(WEATHER_URL.format(city=city), timeout=15)
        if response.status_code != 200:
            print('查询失败，请稍后再试')
            return
        data = response.json()
        if not data.get('current_condition'):
            print(f'没有找到 {city} 的天气信息，请检查城市名是否正确')
            return

        now = data['current_condition'][0]
        area = data['nearest_area'][0]['areaName'][0]['value']
        code = now.get('weatherCode')
        if code:
            desc = WEATHER_CODE.get(int(code), now['weatherDesc'][0]['value'])
        else:
            desc = now['weatherDesc'][0]['value']
        print(now)
        print(f'查询城市：{city}（匹配到：{area}）')
        print(f'天气：{desc}')
        print(f'温度：{now["temp_C"]}°C    体感温度：{now["FeelsLikeC"]}°C')
        print(f'湿度：{now["humidity"]}%    风向：{now["winddir16Point"]}')
        print(f'风速：{now["windspeedKmph"]} km/h    降水量：{now.get("precipMM", "0.0")} mm')
    except requests.exceptions.RequestException:
        print('网络连接失败，请检查网络后重试')
    except Exception as error:
        print(f'查询出错：{error}')


def query():
    """手动输入城市名查询天气"""
    print('查询城市天气')
    city = input('请输入要查询的城市（如：北京）：').strip()
    if city:
        get_weather(city)
    else:
        print('城市名不能为空')


def show_favorites():
    """显示收藏的城市列表"""
    print('收藏的城市：')
    if not city_list:
        print('（暂无收藏，请先添加）')
        return
    for i, city in enumerate(city_list, 1):
        print(f'{i}、{city}')


def query_favorites():
    """查询所有收藏城市的天气"""
    print('查询收藏城市的天气')
    if not city_list:
        print('还没有收藏的城市，请先添加')
        return
    for city in city_list:
        print('-' * 40)
        get_weather(city)
    print('-' * 40)


def add():
    """添加收藏城市"""
    print('添加收藏城市')
    city = input('请输入要收藏的城市名：').strip()
    if not city:
        print('城市名不能为空')
        return
    if city in city_list:
        print(f'{city} 已经在收藏列表里了')
        return
    city_list.append(city)
    save_cities(city_list)
    print(f'已收藏：{city}')


def remove():
    """删除收藏城市"""
    print('删除收藏城市')
    if not city_list:
        print('还没有收藏的城市，请先添加')
        return
    show_favorites()
    city = input('请输入要删除的城市名：').strip()
    if city in city_list:
        city_list.remove(city)
        save_cities(city_list)
        print(f'已删除：{city}')
    else:
        print('收藏列表里没有这个城市')


def main():
    global city_list
    while True:
        print('''
    ===天气查询系统===
    1、查询城市天气
    2、查看收藏城市的天气
    3、添加收藏城市
    4、删除收藏城市
    5、显示收藏城市列表
    0、退出系统
''')
        city_list = load_cities()
        choice = input('输入你要操作的选项：')
        if choice == '1':
            query()
        elif choice == '2':
            query_favorites()
        elif choice == '3':
            add()
        elif choice == '4':
            remove()
        elif choice == '5':
            show_favorites()
        elif choice == '0':
            print('已退出天气查询系统')
            break
        else:
            print('输入错误，请重新输入')


if __name__ == '__main__':
    main()
