import requests
import json
import pandas as pd
from time import sleep

def fetch_and_store_comments(start_page, end_page):
    url_base = "https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=512550&index={}&page={}&pageSize=10&tagType=0"
    headers = {
        "cookie": "QN1=0000eb00306c5ea3ab901aff; QN300=s%3Dbing; QN99=864; QunarGlobal=10.68.47.32_-7142fe65_18ee4aec675_-3384|1713237874709; QN601=e4ab456363d7e4b69ebe55ad22d8467e; QN48=0000f3002f105ea3aba02d7b; fid=4f296ff5-abe0-4979-ad02-a02b96a92b1f; QN57=17132378828680.7977768035121533; ctt_june=1683616182042##iK3wasPOVuPwawPwasXnXSHRX%3Dj%2BasXmXPj%3DWSD%3DWPaNEPD8ESoGWSjwX%3DaAiK3siK3saKgnas3%3DaK2%3DWK3AVhPwaUvt; QN271AC=register_pc; QN271SL=c8046ad550613c9ded72bb808e3bba65; QN271RC=c8046ad550613c9ded72bb808e3bba65; _q=U.llmxggz6342; csrfToken=lG24GeOSuGyHpjohfjLzzcMbaeESrRTb; _s=s_R7S7U35AQQJJ3GVSMCKSU3H6KY; _t=28666579; _v=qfWGjijVcr7Fig57wCqY41HS1hM3sbqYCMNrYj-7GyAN5M8rRtaCVV8_kqfvb2qaRZMABSEUGijkhC3JAwQ6LDAo2zkr3qwMf7lb8C5IKmmevmpTP38hOjSU4JVZOE6XvQ112EgZNaRhdXDapg7obWbZO-c5jFVFc5CMETUu_O9G; QN43=""; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; _i=DFiEZnwAyJvw9D7wtz6ra8wjP_fw; quinn=80299d7aa43ec0e5ecb797a583ce81ceff48248bf9a15377fe5ff5da45b9b0e21968791efed0e99468daf36844e3712c; QN100=WyLlpKfov5DmsrPljZrnianppoZ8Il0%3D; QN58=1714914841627%7C1714915235471%7C11; HN1=v1fe91ee1b10d639b695aa22d459f3d41d; HN2=qkzuqkzqrslcu; QN205=s%3Dbing; QN277=s%3Dbing; QN269=E12166431DC511EFADCA42D9F172D4BF; ctf_june=1683616182042##iK3wWKPnWwPwawPwasjOX2asWKa%3DX2DnVP3nXSfIaRvnEK3nW2WhESWGWRXOiK3siK3saKgnWS2NaSDOaSgnWuPwaUvt; cs_june=baa1ad377fe4ed45f596fe0737c05feed016a54a4422e5001d3ec5adb6a2a5cba6eadb36ac92110b1699dae3cbe5aa9d6f0abc1c622b7278c3d836e35e973bc6b17c80df7eee7c02a9c1a6a5b97c1179bad642c65ceba8ad0a88cfbd2ae603775a737ae180251ef5be23400b098dd8ca; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN44=llmxggz6342; QN267=0214725839510ac7c5; _vi=c6yoAgdoQOduVFkMvOIqetgfKJ1SsTbx9e0SR2SKO2nY2I3JPSkkoSMvXY7P8L4v09KgeSqNmwwyixfcERgE13Zd5q4Iagk7dk9dx-Td9L1VTGFN7tvc5D0WPrq9vuBq_6vsSgaFTdAhkP6OhmgngWk765p2uSf2IRCVaWhdraRq; RT=s=1717253043717&r=https%3A%2F%2Fflight.qunar.com%2F; QN271=2f9c1a0e-6e51-4029-9bcd-da3f867999ab",  # 请替换为实际的Cookie值
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    all_data = []

    for page in range(start_page, end_page + 1):
        url = url_base.format(page, page)
        sleep(3)  # 遵守网站访问规则，适当延时
        print(f"正在抓取page={page}")
        response = requests.get(url, headers=headers)
        sleep(3)

        if response.status_code == 200:
            try:
                data = json.loads(response.text.strip())
                comment_list = data['data']['commentList']
                for comment in comment_list:
                    if comment['content'] != "用户未点评，系统默认好评。":
                        all_data.append({
                            '作者': comment['author'],
                            '内容': comment['content'],
                            '日期': comment['date'],
                            '评分': comment['score'],  # 假设评分字段存在
                            '评论ID': comment['commentId'],
                            '城市': comment['cityName']
                        })
            except json.JSONDecodeError as e:
                print(f"解析JSON出错: {e}")
            except KeyError as e:
                print(f"数据提取出错: {e}")
        else:
            print(f"请求失败，状态码: {response.status_code}")

    # 存储到Excel
    df = pd.DataFrame(all_data)
    excel_file = 'comments.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"数据已保存到{excel_file}")

if __name__ == "__main__":
    start_page = 1
    end_page = 4  # 根据需要调整结束页数
    fetch_and_store_comments(start_page, end_page)