from os import close, remove 
import requests, random, sys 
from lxml import etree 
from pagermaid.listener import listener 
from pagermaid.utils import alias_command 
from pagermaid.utils import obtain_message 
@listener(is_plugin=True, outgoing=True, command=alias_command("yahoo"), 
description="回复一个关键词或自己输入，使用雅虎引擎搜索\n(只有你想不到的，就没有我能搜得到的🤪)",parameters='<keyword>') 
async def baidu1(context): 
    header={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'Accept-Encoding': 'gzip, deflate, br', 
    'Cache-Control': 'max-age=0', 
    'Connection': 'keep-alive', 
    'Host': 'tw.search.yahoo.com', 
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"', 
    'sec-ch-ua-mobile': '?0', 
    'sec-ch-ua-platform': '"Windows"', 
    'Sec-Fetch-Dest': 'document', 
    'Sec-Fetch-Mode': 'navigate', 
    'Sec-Fetch-Site': 'none', 
    'Sec-Fetch-User': '?1', 
    'Upgrade-Insecure-Requests': '1', 
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57' 
} 
    await context.message.edit('正在搜索...') 
    try: 
        keyword = await obtain_message(context) 
    except: 
            await context.message.edit('请输入参数) 
    try: 
        for _ in range(3): 
            res = requests.get('https://tw.search.yahoo.com/search?p='+keyword+'&.tsrc=yfp-hrmob-sb', headers=header) 
            if res.status_code == 200: 
                break 
    except: 
        await context.message.edit('搜索失败～') 
        sys.exit(0) 
    res_xpath = etree.HTML(res.text) 
    with open ('b.txt','w+',encoding='utf-8')as f: 
        for i in range(10,21): 
            try: 
                url = res_xpath.xpath('//div[@id='+str(i)+']//h3/a/@href')[0] 
                title = ''.join(res_xpath.xpath('//div[@id='+str(i)+']//h3//text()')) 
            except: 
                    continue 
            urlc = '('+url+')';titlec = '['+title+']' 
            f.write(titlec);f.write(urlc+'\n\n') 
    file = open("b.txt", 'r', encoding='utf-8') 
    await context.edit('**🛸雅虎搜索🔍**\n\n搜索结果🔎|'+keyword+'\n\n'+file.read()) 
    file.close() 
    remove("b.txt")