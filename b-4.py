def main():
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

# Q1. 全国の平均気温を計算してください(9.5となればOK)
    ave_temp = [temperature.get('temperature') for temperature in weather_information]
    ave1 = sum(ave_temp) / len(ave_temp)
    print(ave1)

# Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka = [i for i in weather_information if i['prefecture'] == '大阪府' ]
    get_osaka_stn = [stn.get('station') for stn in osaka]
    print(get_osaka_stn)

# Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fukuoka = [i for i in weather_information if i['prefecture'] == '福岡県']
    get_fukuoka_temp = [temp.get('temperature') for temp in fukuoka]
    ave2 = sum(get_fukuoka_temp) / len(get_fukuoka_temp)
    print(ave2)

if __name__ == '__main__':
    main() # 取り敢えずできた
