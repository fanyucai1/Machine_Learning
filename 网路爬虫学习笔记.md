     
1. 防止IP被封的方法，伪造浏览器登陆

        Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)
        Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)
        Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 530) like Gecko (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)

2. 寻找代理服务器IP地址，防止同一个IP发起过多请求而被封IP

        免费的资源很多：https://www.kuaidaili.com/ops/proxylist/1/，在选择的时候一定要验证其有效性，免费的都有一定的时效性
        
        代理服务器有http有https两种需要仔细区分，还有在选择的时候要选择高匿名以及响应速度快的
        
        如果你可以翻墙还可以推荐给你一个免费的代理IP，来自全世界的http://free-proxy.cz/zh/proxylist/country/all/https/ping/level1，我在爬取cosmic的时候有用到

3. python模块
    
    Requests[https://2.python-requests.org//zh_CN/latest/index.html]
    
        r = requests.get('https://api.github.com/user', auth=('user', 'pass'),verify=False)
        判断是否返回正常则有：
        r.status_code==200
        解析：
        r.txt
        r.json()

    Beautiful Soup  [https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id66]
   
4. 
    代码示例一：cosmicID的状态：Yes（e.g:COSM6918278）No(e.g:COSM6475151)SNP(e.g:COSM6972367)可根据bed文件爬取对应的cosmicID的状态

        import requests
        from bs4 import BeautifulSoup
        import re
        id=input("please input COSMIC ID(e.g:COSM3677745):")
        pattern=re.compile(r'\d+')
        num=pattern.findall(id)
        url="https://cancer.sanger.ac.uk/cosmic/mutation/overview?genome=37&id=%s" %(num[0])
        res=requests.get(url,proxies={"https":"https://163.204.244.194:9999"})
        ret = res.text
        soup=BeautifulSoup(ret,'html.parser')
        dbsnp=soup.find_all(text=re.compile("has been flagged as a SNP."))
        dt = soup.find_all('dt')
        dd = soup.find_all('dd')
        for i in range(len(dt)):
            if dt[i].string == "Ever confirmed somatic?":
                print("%s\t%s" % (id, dd[i].string))
        if dbsnp!=[]:
            print("%s\tSNP" % (id))
    
    示例二：爬取OMIM数据库，测试首先保证你可以打开https://www.omim.org/entry/111600，否则请翻墙，爬取对应的OMIM ID与表型的信息先下载https://www.omim.org/static/omim/data/mim2gene.txt 该文本文件里第二列注明的有表型、以及基因号，
    这里只针对的基因号进行爬取，对于其他类型的号需要适当修改程序 测试脚本一可以用来测试你的代理是否满足需求

        import requests
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        from bs4 import BeautifulSoup
        import random
        import re
        import os
        import time
        from multiprocessing import Process, Pool
        #######################################
        No={}
        if os.path.exists("no_omim.tsv"):
            infile=open("no_omim.tsv",'r')
            for line in infile:
                line = line.strip()
                array = line.split()
                No[array[0]]=1
        #######################################
        dict={}
        if os.path.exists("omim.tsv"):
            infile=open("omim.tsv","r")
            for line in infile:
                line=line.strip()
                array=line.split()
                dict[array[0]]=1
            infile.close()
        else:
            outfile = open("omim.tsv", "w")
            outfile.write("#MIM_Number\tLocation\tPhenotype\tPhenotype_MIM_number\tInheritance\tPhenotype_mapping_key\n")
            outfile.close()
        #######################################
        id=[]
        infile=open("mim2gene.txt","r")#https://www.omim.org/static/omim/data/mim2gene.txt(2019-7-3)
        for line in infile:
            if not line.startswith("#"):
                line=line.strip()
                array=line.split("\t")
                if array[1]!="phenotype" and array[1]!="moved/removed" and array[1]!="predominantly phenotypes":
                    if not array[0] in dict:
                        if not array[0] in No:
                            id.append(array[0])
        infile.close()
        print(len(id))
        #######################################在请求头中把User-Agent设置成浏览器中的User-Agent，来伪造浏览器访问
        def run(omim_id):
            user_agents =['Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
                          'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
                          'Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 530) like Gecko (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'
                          ]#https://www.bing.com/webmaster/help/which-crawlers-does-bing-use-8c184ec0
            ip=["198.27.67.35:3128","134.209.38.101:3128","198.27.67.35:3128","193.19.165.222:53281","89.109.14.179:45644","5.2.211.232:52448",
                "51.38.71.101:8080","95.78.174.9:52141","177.87.15.6:36043","188.18.7.171:57576","122.176.65.143:40280","89.252.87.140:45872",
                "52.151.95.57:3128","51.141.228.88:3128","51.141.228.207:3128","181.129.50.138:46503","181.129.47.162:52426","91.230.199.174:46306",
                "187.189.59.181:52860","181.211.245.74:60918","190.184.144.138:41707","212.230.24.186:61509","136.25.2.43:42215","31.42.173.57:49494",
                "93.170.115.179:47874","94.127.144.179:36904","80.249.229.64:48151","93.171.242.9:58943","83.13.164.202:54661","176.106.186.99:46566",
                "89.121.211.242:48614","177.184.139.81:48738","200.170.76.46:52840","77.252.26.71:55077","217.30.73.152:34947","212.154.58.107:35116",
                "176.113.157.149:38409","159.224.44.19:44253","194.44.236.48:51066","186.226.183.170:58386","93.152.176.241:61384","178.169.196.87:48834",
                "177.103.186.7:31726","82.114.92.122:48795","91.203.27.139:53962","212.230.24.186:61509","212.230.24.186:61509"]
            url="https://omim.org/entry/%s"%(omim_id)
            proxy={"https":"https://"+random.choice(ip)}
            headers = {'User-Agent': random.choice(user_agents)}
            s = requests.session()
            s.keep_alive = False
            res=requests.get(url,headers=headers,proxies=proxy)
            ret=res.text
            soup=BeautifulSoup(ret,'html.parser')
            outfile = open("omim.tsv", "a+")
            try:
                ########################################table
                Pos=soup.table.tbody.find_all('tr')#####判断表格有多少行
                #########################################Location
                Location=soup.table.tbody.td.span.a.text
                Location = Location.strip()
                ##########################################Phenotype
                Phenotype = []
                num=0
                for i in Pos:
                    num+=1
                    if num==1:
                        str=i.find_all('span',limit=2)
                        Phenotype.append(str[1].string.strip())
                    else:
                        str=i.td.span.string.strip()
                        if str:
                            Phenotype.append(str)
                ###########################################Phenotype_MIM_number
                Phenotype_MIM_number=[]
                for i in Pos:
                    str=i.find('a',href=re.compile("entry"))
                    if str:
                        Phenotype_MIM_number.append(str.string)
                    else:
                        Phenotype_MIM_number.append("_")
                ###########################################
                Inheritance = []
                key = []
                for i in Pos:
                    str=i.find_all('abbr')
                    tmp=""
                    for j in str:
                        tmp+=","
                        tmp+=j.string
                    array=re.split(r'(\d+)',tmp)
                    real_key=0
                    real_Inheritance=0
                    for i in array:
                        p1 = re.compile(r'[A-Za-z]')
                        p2 = re.compile(r'(\d+)')
                        a = p1.findall(i)
                        b = p2.findall(i)
                        if i.strip(",") != "":
                            if a != []:
                                Inheritance.append(i.strip(","))
                                real_Inheritance = 1
                            if b != []:
                                key.append(i.strip(","))
                                real_key = 1
                    if real_key==0:
                        key.append("_")
                    if real_Inheritance==0:
                        Inheritance.append("_")
                for i in range(len(Phenotype)):
                    outfile.write(
                        "%s\t%s\t%s\t%s\t%s\t%s\n" % (omim_id,Location, Phenotype[i], Phenotype_MIM_number[i], Inheritance[i], key[i]))
                outfile.close()
            except:
                outfile=open("no_omim.tsv","a+")
                outfile.write("%s\n"%(omim_id))
                outfile.close()
        if __name__=="__main__":
            start = time.time()
            pool = Pool(processes=200)
            pool.map(run, id)
            end = time.time()
            print("Elapse time is %g seconds" % (end - start))