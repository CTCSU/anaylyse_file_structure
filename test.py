import re
import convert
from node import Node

str = """一、我们为什么要沟通？
    生理需求：沟通良好或社交网络更好的人在统计学上拥有更健康的身体和更长的寿命
    认同需求：人类是社会动物，我们只有在社交关系里才能感知到自我，才会有自我认同
    社交需求：积极的关系也需是幸福感唯一也是最重要的来源
    实现需求：在马斯洛五层需求理论中，每一层都需要沟通的参与

二、有哪些沟通的迷思？
	* 
沟通的越多不见得越好
	* 
意思不在字眼里
	* 
成功的沟通并不表示能互相理解
	* 
沟通不会解决所有问题



三、沟通高手的特征是哪些？
	1. 
他掌握着多种沟通方式 
	2. 
他知道在不同的情况下挑选不同的沟通方式 
	3. 
具有表现沟通方法的技巧
	4. 
具有强的同理心
	5. 
具有高的认知复杂度



四、 什么是自我概念？
    自我概念是指长期形成的对自己比较稳定的知觉和认识

五、什么是认同管理？
    我们每个人都有不同面，表现出自己的不同方面就是认同管理。因为有觉知的自我和展现的自我。

五、为什么要做认同管理？
    首先我们每个人都有不同的角色和特征，对一类人我们可以只表现那个方面。
    其次，认同管理是为了达到这些目标：
	* 
开始和经营关系
	* 
获得别人的顺从
	* 
抱住别人的颜面
	* 
探索新的自我



六、 什么是自我坦露？
    是指有意地透露有关于自己的相关信息

七、自我坦露的模式？
    这里我还是不太懂，里面提到了社会穿透模式和乔哈里视窗两种方法，当然，对我个人是否决定去坦露是有帮助的哈。只是不理解模式带给

八、自我坦露的好处？
	* 
宣泄
	* 
互惠
	* 
自我澄清
	* 
自我确认
	* 
关系的建立和维持 
	* 
社会控制



九、自我坦露的风险？
	* 
拒绝
	* 
负面影响
	* 
降低关系满意度
	* 
丧失影响力



十、自我坦露的原则
	* 
这个人对你而言重要吗？
	* 
坦露的量与方式合适吗？
	* 
坦露的风险合适吗？
	* 
有建设性的影响吗？
	* 
坦露是互惠的吗？
	* 
你在道德上有义务坦露吗？



十一、什么是知觉？
    知觉是对感觉信息的整合，成为对我们有意义的类型

十二、知觉的历程有哪些？
	* 
选择
	* 
组织
	* 
诠释
	* 
协商



十三、有哪些归隐谬误的知觉倾向？
	* 
对人严厉，对己仁慈
	* 
先入为主
	* 
以己之心，度人之腹
	* 
我们被期待所影响
	* 
最明显的最有力



十四、知觉检核的方法
	1. 
描述你注意到的行为 
	2. 
列出对此行为至少两种可能的诠释
	3. 
请求对方反正诠释作澄清



十五、什么是同理心？
    是指一个人从另一个人的视角来体验世界，重新创造个人观点的能力

十六、如何提高同理心？
	1. 
耐心地专注的倾听
	2. 
认真地观察，尤其是非语言沟通，表情，动作
	3. 
清空你头脑，不做任何评判
	4. 
从另一个人的视角去感受
	5. 
克制，记住对方没有明确的要求时，请不要给建议，停止你的说教
	6. 
述情，去试着用情绪词汇讲述对方的感受



十七、什么是认知复杂度
    人们看待问题时组织其架构的能力（什么是问题的架构？）

十八、怎么提升认知复杂度？
    枕头法，知觉检核是澄清潜在误会的一个好用又简单的工具，但是有些议题太复杂、太严重，以致难以使用这个技巧。当你发现对方的立场乏善可陈的时候，它可以帮你增强同理心。

十九、枕头法怎么操作：
    对一个问题采用不同的观点去看待
    立场一：我对你错
    立场二：你对我错
    立场三：双方都对，双方都错
    立场四：这个议题并不重要
    立场五：四个立场都有真理

二十、为什么以及怎么扩充情绪词汇 
    可以更准确地描述自己的感觉
    有情绪词汇表的
    另外，可以使用不同的方式来说同一种感觉：单一字词、描述你发生了什么、描述你想要做什么

二十一、有助益情绪和无助益情绪之前有什么区别？
    差异在于强度，无助益情绪会更大一些

二十二、无助益情绪有哪些来源？
	* 
    生理因素
	* 
    情绪记忆
	* 
    自我内言：重新评估包括改变可以管理我们的情绪



二十三、什么是自我内言？
    我们告诉自己的心里话，自我内言可以是正面的也可以是负面的| 是不是也可理解为我们做诠释的模式？

二十三，ABC 理论
     艾利斯认为：人的情绪和行为障碍不是由于某一激发事件（activating event）直接所引起，而是由于经受这一事件的个体对它不正确的认知和评价所引起的信念（Belief），最后导致在特定情景下的情绪和行为后果（consequence），这就称为ABC理论。

二十四、无助益情绪的来源
    许多无助益情绪来自于我们接受了一堆非理性的想法

二十五、有哪些非理性想法的谬误？
	* 
完美的谬误
	* 
赞同的谬误：持有赞同的谬误的人，认为得到别人的赞同是生活中不可或缺的事情
	* 
应该的谬误
	* 
过度推论的谬误
	* 
因果论的谬误
	* 
无助的谬误：指认为生活的满意度受到超过你能控制的压力所决定,只要你了解“如果你真的想做，就有许多事情可以去做”这一点，类似的这些陈述的错误就显而易见
	* 
灾难性预期的谬误



二十六、减少无助益情绪——什么是理性情绪疗法？
	* 
监控你的情绪
	* 
注意引发的事件
	* 
记录你的自我内言
	* 
重新评估你的非理性新年



二十七、如何反驳理性情绪疗法太冷酷，没有人情味的批评？
	* 
一个理性的思考者仍然可以拥有梦想、希望和爱
	* 
理性的人也会有时刻沉浸在非理性情绪里，但通常情况下他们知道自己在做什么。



二十八、什么沟通主导着关系
    非语言沟通

二十九、倾听的定义
    解读别人所哦信息的过程。

三十、为什么有时需要心不在焉的倾听？
    因为我们不能时时刻刻都保持专注，这样太累了

三十一、 倾听过程有什么元素？
	* 
听到
	* 
专注
	* 
理解
	* 
回应 
	* 
记忆



三十二、有哪些无效倾听的类型？
	* 
自恋的倾听
	* 
选择性倾听
	* 
隔绝性倾听
	* 
防卫性倾听
	* 
埋伏性倾听
	* 
鲁钝的倾听



三十三、无法有效倾听的原因有哪些（要去避免）
	* 
超负荷的信息
	* 
心不在焉
	* 
飞快的思想
	* 
需要很大的努力——倾听是一项费力的工
	* 
外在的噪音
	* 
错误的假定
	* 
缺乏明显的益处
	* 
缺乏训练
	* 
听力的问题



三十四、如何做到有效的倾听
	* 
少说话
	* 
拜托注意力分散
	* 
不要过早评断
	* 
寻找关键意思



三十五、有哪些倾听反应的类型？
	* 
借力使力，即顺水推舟地让说话者继续自己的话题，也就是捧哏
	* 
问话
	* 
释义——这个很重要，就是阐述别人感觉以及自己的理解，有点像知觉核验，而且我们平时其实很少用到
	* 
支持
	* 
分析
	* 
忠告
	* 
评断 —— 做出评断暗示了一个事实：你是那个具有权利和资格去评断别人想法和行为的人，所以要谨慎使用




三十六、如何使释义听起来更自然？
	1. 
改变说话者的措辞;
	2. 
从你接收到的信息中，抓一个具体的例子，来向说话者说明你理解的程度
	3. 
反映说话者的潜在寓意



三十七、决定是否释义的因素是什么
	* 
这个问题够复杂吗？——太简单的问题必然没有必要做释义
	* 
对你来说，有必要投入时间和关注吗——释义会占用大量时间的
	* 
你的克制住不去评判吗？
	* 
释义和你的其他反应成比例吗？——过度使用释义会分烦人，特别是如果你突然把这个方法加入你的沟通风格中



三十八、有哪些支持性的回应？
	* 
同理心——我也有类似的感觉
	* 
同意 
	* 
提供协助
	* 
赞美
	* 
恢复信心



三十九、有哪些冷安慰（假支持），要尽量避免
	* 
否认别人拥有感觉的权利
	* 
看轻事情的重要性
	* 
聚焦在“彼时彼地”，而非“此时此地”—— 只是简单地安慰事情总有一天会过去的
	* 
火上浇油的评断
	* 
自我聚焦
	* 
自我防卫



四十、使用分析回应时的原则
	* 
在提出解释时，使用试探性的口气会比绝对性的口气更好
	* 
确定对方愿意接受你的分析
	* 
确认自己提供分析的动机确实基于协助



四十一、为什么分析有的时候会造成更多问题？
	* 
一、你的解释可你不正确
	* 
二、即使你的分析是正确的，如果你直截了当、不加修饰地说出来，可能会引起对方的防卫



四十二、提供忠告的注意事项：
	1. 
 这个忠告有提出来的需要吗？—— 如果某个人已经采取了一些行动，在事后才给予建议是无法得到理解的
	2. 
对方真的想听你的忠告吗？
	3. 
你提出劝告的顺序正确吗 —— 先支持性、释义和问话的回应
	4. 
你的忠告是专家级别的吗？
	5. 
提出忠告的人是关系密切，值得信任的人吗



四十三、选择最佳倾听反应的考虑因素 
	* 
性别  —— 大量的研究表明在困境中，无论男女都偏爱和想要支持性、赞同的信息
	* 
情境 —— 看别人具体需要的是什么。需要合适的倾听
	* 
对象 —— 找出最适合的反法，通过观察，或者直接询问：”你是要听我的忠告，还是只需要倾诉一下？“
	* 
你的个人风格



四十四、我们为什么要建立关系？
	* 
外貌
	* 
相似性
	* 
互补性
	* 
相互吸引力
	* 
能力
	* 
坦露
	* 
接近
	* 
报酬



四十五、亲密关系有哪些向度？
	* 
身体的
	* 
智力的
	* 
情绪的
	* 
共享活动



四十六、男女亲密关系有哪些不同？
	* 
男性更倾向与共享活动
	* 
女性间相互的坦露更多



四十七、有哪些亲密关系与沟通想关联？
	* 
家人间沟通
	* 
友人间沟通
	* 
爱人间沟通



四十八、怎么改善亲密关系？
	* 
关系需要承诺
	* 
关系需要维系与支持
	* 
社会支持




四十九、承诺的感情关系有哪些指标？
	* 
提供喜爱
	* 
提供支持
	* 
保持诚实
	* 
分享彼此的陪伴
	* 
尽力做到定期沟通
	* 
表示尊重
	* 
创造一个共同的未来
	* 
创造一个积极的关系氛围
	* 
处理一些关系中的问题
	* 
重申彼此的承诺让对方安心



五十、关系维持的定义 是什么？
    广义地定义为：为了保持关系平稳地、令人满意地运行而进行的沟通。

五十一、恋人们用来保持沟通满意度的五个策略是什么？
	1. 
积极性，氛围有礼貌，积极向上，避免批评
	2. 
开放性：直接讨论关系的性质，并且坦露个人的需求和关注
	3. 
保证：从语言和非语言的层面上，让对方知道你对他来说是重要的，并且你已经对这段关系作出了承诺
	4. 
社交网络：关注彼此的朋友、家人和亲人
	5. 
共享任务：帮助彼此打理生活中的琐事和义务



五十二、有哪些爱的语言？
	1. 
肯定的语言
	2. 
有品质的时间：当伴侣需要你时，你都能在场并提供帮助，而且在这段重要的时间里，你能给予对方毫无保留的、全心全意的关注。
	3. 
礼物
	4. 
服务行为
	5. 
身体接触



五十三、有哪些社会支持？
	* 
情感支持：当一个人感到压力、伤害或者悲伤的时候，没有什么比心爱的人带着同理心倾听且用关爱的方式作出回应更有助益了
	* 
信息支持：我们生活中最亲近的人往往是我们获取信息的最佳来源。他们可以为我们提供关于购物的建议，对人际关系的看法，以及对于我们盲点的观察。



五十四、什么是沟通气氛？
    是指关系当中的情绪氛围

五十六、是什么引导着正向或负向的沟通气氛？
    一段关系中的分为，取决于人们相信自己在其他人心中的受重视的程度

五十七、有哪些不肯定信息？
	* 
视若无睹
	* 
插嘴
	* 
各说各话
	* 
岔题
	* 
无人情味
	* 
含糊其辞
	* 
表里不一



五十七、有哪些肯定信息？
	* 
重视：比如回复邮件或者电话短信都是常见的例子。
	* 
承认：倾听大概是一种最普遍的“承认”途径，比较积极的“承认”包括问问题、释义问题、反映问题
	* 
赞同：“承认”表示你对别人的意见有兴趣，赞同则表示你同意他们的意见。



五十八、什么是防卫？
    人们在收到批评或否定时，为了维护自我，采取的对立的、驳斥的方式来回应对方。有能力的沟通者除了会照顾自己对面子的需求，也会照顾他人的。

五十九、引起和降低防卫的六种行为类型？
	* 
评价和描述
	* 
支配和问题导向
	* 
策略和自发：“策略"的本质是不诚实以及”操纵“，自发是指单纯地对别人城市而不是操纵他们

		* 
举例：

			* 
“你星期五下班后要做什么？”
			* 
“我星期五下班后要搬钢琴，你能来帮我的忙吗？”
	* 
中立（冷漠）和同理
	* 
优越和平等
	* 
确定和协商



六十、怎么保留面子，使用清晰信息
	* 
行为
	* 
解释
	* 
感觉
	* 
结果
	* 
意图
	* 
使用清晰信息处方

		* 
相关要素的顺序可能会被打乱
		* 
信息的字词要符合你的个人风格
		* 
适时地将两个要素联结在一个句子里
		* 
从容地传达信息



六十一、如何不防卫性地回应批评？
	* 
寻找更多信息

		* 
询问详情
		* 
推测详情
		* 
对说话者的想法予以释义
		* 
询问批评者想要什么
		* 
询问行为的后果
	* 
同意批评者的看法 

		* 
同意事实
		* 
同意批评者的观感



六十二、冲突的本质是什么？
    至少两个相互依赖的个体在实现他们目标的过程中，其中一方察觉到了彼此目标的互不相容、资源的不足和来自另一方的阻挠，并通过斗争的形式表达出来。

六十三、冲突的处理方式有什么？
	* 
逃避（双输）
	* 
调适（一输一赢）
	* 
竞争（一赢一输，有时会转成双输）
	* 
妥协（部分双输）
	* 
合作（双赢）



六十四、破坏性冲突模式有哪四个？
	* 
批评
	* 
防卫
	* 
蔑视
	* 
回避



六十五、建设性处理冲突的步骤
	1. 
确认你的问题和未满足的需要 
	2. 
订立约会 
	3. 
描述你的问题和需求 
	4. 
思考对方的观点
	5. 
商议解决之道
	6. 
追踪解决方案的后效



六十六、怎么使用乔哈里视窗？
    乔哈里视窗是用来审视自我坦露程度的，分为两个维度，
	* 
自己知道的和自己不知道的
	* 
他人知道的和他人不知道的


    所以会形成四个区域：
	* 
开放区
	* 
盲视区
	* 
隐藏区
	* 
未知区


    我理解自我坦露就是要降低隐藏区，提升开放区

六十七、使用“我”的语言
    当需要使用“你“的语言来阐述信息或者评断时，最好转换成“我”的语言。我兹提供了一种比较精确、不那么挑拨的方式来表达不满。例如：
	* 
你把这个地方弄得一团糟
	* 
我不想一个人负责公寓全部的打扫



    也可升级为“我们”，因为过度使用会显得以自我为中心。

六十八、在这本书里学习到哪些可以使用的技巧？
	* 
自我坦露
	* 
乔哈里视窗
	* 
知觉检核
	* 
枕头法
	* 
理性情绪疗法
	* 
“我”的语言
	* 
选择最佳的倾听方式
	* 
维系与支持关系
	* 
避免对他人防卫
	* 
清晰信息处方
	* 
不防卫地回应信息
	* 
建设性处理冲突



六十九、什么是光环效应？
    在某一方面拥有正面形象的人，我们会倾向于认为他们在其他方面也拥有正面形象。

七十、沟通的三大规则
	1. 
尊重他人对于全神贯注的需求
	2. 
注意言论的文明
	3. 
不要影响到局外人



七十一、什么是自我应验预言？
    是指如果我们对于未来有一定预期，并且我们的行为也是建立在这个预期之上的，那么我们的实现预期的可能性就会比没有预期更大一些

七十二、怎么消除刻板印象？
    去除对他人的分类

七十三、什么是归因
    我们对事物赋予意义的过程

七十四、什么是情绪智商
	* 
理解和控制自己情绪的能力
	* 
对他人情绪保持敏感的能力

"""
list = str.splitlines();
# list = ["1.1", "2.2","3.3","4.4","5.5"]
def test1():
    rex_list_str = ["^\d+\..*","^[a-z]\..*","^[a-z]{2}\..*"]
    rex_list = []
    for x in rex_list_str:
        rex_list.append(re.compile(x))

    node = Node()

    convert.convertStringListToNode(list, rex_list,0,node)

    node.toDataFrams()

def test2():
    rex_list_str = ["^.{1,4}\u3001.*"]

    rex_list = []
    for x in rex_list_str:
        rex_list.append(re.compile(x))
    node = Node()
    convert.convertStringListToNode(list, rex_list,0,node)
    node.toDataFrams()

test2()