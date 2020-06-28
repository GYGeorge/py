import pymysql
import random

lastname = ["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许",
            "何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章",
            "云","苏","潘","葛","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳",
            "酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤","滕","殷","罗","毕","郝","邬","安","常",
            "乐","于","时","傅","皮","卞","齐","康","伍","余","元","卜","顾","孟","平","黄"]
firstname = [ "靖衡","维亨","城蕾","艾韵","汛如","维朋","康博","伯胜","顺斌","壹燕","跃吉","伟威","长莉","培烘","森远",
              "均贺","漫绮","雨澜","一稼","笑蔚","舒岑","显旗","享益","广炎","鹤嘉","昀凌","稼俊","柯雅","艺堂","启赢",
              "极峰","陵雅","历远","凌箫","沛俊","兴万","炳润","钟策","云雨","忆和","良湘","学启","伟科","逸昊","渭云",
              "尉城","必先","俊薪","世银","哲翡","相中","念桐","凤路","值瑜","斯嘉","前路","瑶泽","沁楚","铠维","睿峻",
              "启朋","秦彰","亮树","哲严","仲锦","远淮","静睿","芯培","士鸿","宝瑶","惠辰","植园","庭婕","运程","钟钦",
              "瑾芝","增誉","千友","聆先","培胜","荣腾","立晋","天青","沐翰","鼎峙","弋歌","州炳","奕真","懿仁","杏泉","润潮","益恒",
              "绍天","颖宣","自瑞","正帅","胤彰","银希","民望","自甜","玖妮","夏闰","斌魁","渤昊","仲前","杰德","科中","任卫","无相",
              "梦琪","之桃","慕青","尔岚","初夏","沛菡","傲珊","曼文","乐菱","惜文","香寒","新柔","语蓉","海安","夜蓉","涵柏","水桃","醉蓝",
              "语琴","从彤","傲晴","语兰","又菱","碧彤","元霜","怜梦","紫寒","妙彤","曼易","南莲","紫翠","雨寒","易烟","如萱","若南","寻真",
              "晓亦","向珊","慕灵","以蕊","映易","雪柳","海云","凝天","沛珊","寒云","冰旋","宛儿","绿真","晓霜","碧凡","夏菡","曼香","若烟",
              "半梦","雅绿","冰蓝","灵槐","平安","书翠","翠风","代云","梦曼","幼翠","听寒","梦柏","醉易","访旋","亦玉","凌萱","访卉","怀亦","笑蓝","靖柏","夜蕾","冰夏",
              "梦松","书雪","乐枫","念薇","靖雁","从寒","觅波","静曼","凡旋","以亦","念露","芷蕾","千兰","新波","代真","新蕾","雁玉","冷卉","紫山","千琴","傲芙","盼山",
              "怀蝶","冰兰","山柏","翠萱","问旋","白易","问筠","如霜","半芹","丹珍","冰彤","亦寒","之瑶","冰露","尔珍","谷雪","乐萱","涵菡","海莲","傲蕾","青槐","易梦",
              "惜雪","宛海","之柔","夏青","亦瑶","妙菡","紫蓝","幻柏","元风","冰枫","访蕊","芷蕊","凡蕾","凡柔","安蕾","天荷","含玉","书兰","雅琴","书瑶","从安","夏槐",
              "念芹","代曼","幻珊","谷丝","秋翠","白晴","海露","代荷","含玉","书蕾","听白","灵雁","雪青","乐瑶","含烟","涵双","平蝶","雅蕊","傲之","灵薇","含蕾","从梦",
              "从蓉","初丹。听兰","听蓉","语芙","夏彤","凌瑶","忆翠","幻灵","怜菡","紫南","依珊","妙竹","访烟","怜蕾","映寒","友绿","冰萍","惜霜","凌香","芷蕾","雁卉",
              "迎梦","元柏","代萱","紫真","千青","凌寒","紫安","寒安","怀蕊","秋荷","涵雁","以山"]

con = pymysql.connect(host = 'localhost', user = 'root', port = 3306, password = '496532343', db = "curriculum")

cursor = con.cursor()

for i in range(1, 90):
    cno = i
    name = random.choice(lastname) + random.choice(firstname)
    passwd = "123456"
    tno = ""
    tno = "t" + str(i)  
    insertsql = "INSERT INTO t(Tno,Cno,Tname,Tpasswd) VALUES('%s','%s','%s','%s')"% (tno, cno, name, passwd)
    cursor.execute(insertsql)

con.commit()
cursor.close()
con.close()
   