import jieba
import gensim
from gensim import corpora,models,similarities
import numpy
import os
q=["你好，在吗？",
   "可以货到付款吗?",
   "包邮吗？",
   "产品什么材质面料，组成成分?",
   "我身高XX ，体重XX 的，应该穿什么尺码？",
   "发什么快递？",
   "可以发顺丰或邮政吗？",
   "我怎么补邮费呢？",
   "可以发其他快递吗？",
   "你们的产品有色差吗？",
   "如果不满意，可以退货吗？",
   "退换货邮费谁负责？",
   "能不能便宜一点或者送礼品?",
   "什么时候发货？",
   "几天能到？",
   ]
a=["在的，亲，欢迎您光临“XX官方旗舰店”，我是售前客服小智，请问有什么可以帮助您？",
   "亲，不好意思，，本店暂时还没有开货到付款的服务。但是亲不用担心的，现在京东支付方式是非常很多的，而且支付也很方便安全的。现有支付方式：信用卡，网银，快捷支付都是行的。",
   "亲，您好，我们全国大部分地区是包邮的，但是部分偏远地区(新疆、西藏、青海、甘肃、内蒙等) 是不包邮, 不知亲是哪个地方的？",
   "亲，本产品是由30%的亚麻，48%的粘胶 12%的聚酯纤维组成。亚麻面料 夏季清凉，聚酯纤维亲肤透气，韩版修身，穿这款衣服既帅气又舒适。",
   "an01",
   "我们是默认发汇通和中通的哦。",
   "可以的，但是由于顺丰/邮政收费比普通快递要高，您如果要发顺丰/邮政 要补一定的快递费用的。",
   "请您稍等一下，我把补邮链接发给你http://item.jd.com/1037266211.html（补邮链接金额为1元，也就是说你这边要补多少元，数量选择多少个就行）。",
   "你好，亲这边目前收什么快递方便呢？我帮您看一下我们是否可以发。",
   "亲，请您放心，我们是官方正品，没有什么色差的哦，我们有针对200位客户做过售后调查, 根据收到货的客户反映都是可以接受的，不会影响您的穿着，请您放心选购，按照你喜欢的颜色进行选购就可以了。",
   "只要不影响我们二次销售的情况下 我们都是支持七天无理由退换货的 所以请你放心购买。",
   "亲，如果是产品质量问题我们承担来回邮费。如果不是产品质量问题（如尺码，颜色不合适等因客户个人喜好的问题造成的退换货）运费需要客户自己承担的。",
   "亲，不好意思，产品微利已近成本价销售，是不送小礼品/不议价的哦，请您谅解。",
   "您好，我们是根据店铺订单量的多少来确定的。正常情况16：00之前付款的，当天都可以发货的。订单量多或者其他特殊情况则是次日发货的。",
   "亲，发货后江浙沪1-2天左右到货，其他地区3-5天左右到货的。",]
qcut=[]
for i in q:
    data1=""
    thisdata=jieba.cut(i)
    for item in thisdata:
        data1+=item+" "
    qcut.append(data1)
docs=qcut
tall=[[w1 for w1 in doc.split()]
		for doc in docs]
dictionary=corpora.Dictionary(tall)
corpus=[dictionary.doc2bow(text) for text in tall]
tfidf=models.TfidfModel(corpus)
num=len(dictionary.token2id.keys())
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=num)
#加载待计算的问题
while True:
    question=input("请输入问题:")
    data3=jieba.cut(question)
    data31=""
    for item in data3:
        data31+=item+" "
    new_doc=data31
    new_vec=dictionary.doc2bow(new_doc.split())
    sim=index[tfidf[new_vec]]
    pos=sim.argsort()[-1]
    answer=a[pos]
    if(answer=="an01"):
        h=input("请输入您的身高，单位默认为cm:")
        w=input("请输入您的体重，单位默认为kg:")
        if(int(h)>=160 and int(h)<=170):
            if(int(w)<50):
                cm="S"
            elif(int(w)>65):
                cm="XXL"
            else:
                cm="XL"
        elif(int(h)>=170 and int(h)<=180):
            if(int(w)<65):
                cm="XL"
            elif(int(w)>85):
                cm="XXXL"
            else:
                cm="XXL"
        else:
            cm="没有符合条件尺码的衣服"
        print("根据您的身高与体重，我们给您推荐的衣服尺寸是"+str(cm)+"，购物愉快！")
        continue
    print(answer)
