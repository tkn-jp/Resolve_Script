# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\fusion\python\rs_fusion\tool\characters\characters.ui',
# licensing of 'C:\Users\yoshi\PycharmProjects\Resolve_Script\app\fusion\python\rs_fusion\tool\characters\characters.ui' applies.
#
# Created: Sat Feb  4 01:26:34 2023
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 356)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 82, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_5.addWidget(self.lineEdit_17)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_5.addWidget(self.lineEdit_9)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout_5.addWidget(self.lineEdit_18)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_5.addWidget(self.lineEdit_10)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout_6.addWidget(self.lineEdit_19)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_6.addWidget(self.lineEdit_11)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout_6.addWidget(self.lineEdit_20)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_6.addWidget(self.lineEdit_12)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_13.setAutoFillBackground(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_14.setAutoFillBackground(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_15.setAutoFillBackground(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_16.setAutoFillBackground(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_21)
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_22)
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_23)
        self.verticalLayout_8.addLayout(self.formLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "半角", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "0123456789", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "全角", None, -1))
        self.lineEdit_2.setText(QtWidgets.QApplication.translate("MainWindow", "０１２３４５６７８９", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "漢数字", None, -1))
        self.lineEdit_3.setText(QtWidgets.QApplication.translate("MainWindow", "〇一二三四五六七八九十百千万", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "大字", None, -1))
        self.lineEdit_4.setText(QtWidgets.QApplication.translate("MainWindow", "零壱弐参肆伍陸漆捌玖拾陌阡萬", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "ローマ数字", None, -1))
        self.lineEdit_5.setText(QtWidgets.QApplication.translate("MainWindow", "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "丸囲み数字", None, -1))
        self.lineEdit_6.setText(QtWidgets.QApplication.translate("MainWindow", "⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "丸囲み数字", None, -1))
        self.lineEdit_7.setText(QtWidgets.QApplication.translate("MainWindow", "⓿❶❷❸❹❺❻❼❽❾❿⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "丸囲み漢数字", None, -1))
        self.lineEdit_8.setText(QtWidgets.QApplication.translate("MainWindow", "㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "数字", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "常用漢字", None, -1))
        self.plainTextEdit.setPlainText(QtWidgets.QApplication.translate("MainWindow", "亜哀愛悪握圧扱安暗案以位依偉囲委威尉意慰易為異移維緯胃衣違遺医井域育一壱逸稲芋印員因姻引飲院陰隠韻右宇羽雨渦浦運雲営影映栄永泳英衛詠鋭液疫益駅悦謁越閲円園宴延援沿演炎煙猿縁遠鉛塩汚凹央奥往応押横欧殴王翁黄沖億屋憶乙卸恩温穏音下化仮何価佳加可夏嫁家寡科暇果架歌河火禍稼箇花荷華菓課貨過蚊我画芽賀雅餓介会解回塊壊快怪悔懐戒拐改械海灰界皆絵開階貝劾外害慨概涯街該垣嚇各拡格核殻獲確穫覚角較郭閣隔革学岳楽額掛潟割喝括活渇滑褐轄且株刈乾冠寒刊勘勧巻喚堪完官寛干幹患感慣憾換敢棺款歓汗漢環甘監看管簡緩缶肝艦観貫還鑑間閑関陥館丸含岸眼岩頑顔願企危喜器基奇寄岐希幾忌揮机旗既期棋棄機帰気汽祈季紀規記貴起軌輝飢騎鬼偽儀宜戯技擬欺犠疑義議菊吉喫詰却客脚虐逆丘久休及吸宮弓急救朽求泣球究窮級糾給旧牛去居巨拒拠挙虚許距漁魚享京供競共凶協叫境峡強恐恭挟教橋況狂狭矯胸脅興郷鏡響驚仰凝暁業局曲極玉勤均斤琴禁筋緊菌襟謹近金吟銀九句区苦駆具愚虞空偶遇隅屈掘靴繰桑勲君薫訓群軍郡係傾刑兄啓型契形径恵慶憩掲携敬景渓系経継茎蛍計警軽鶏芸迎鯨劇撃激傑欠決潔穴結血月件倹健兼券剣圏堅嫌建憲懸検権犬献研絹県肩見謙賢軒遣険顕験元原厳幻弦減源玄現言限個古呼固孤己庫弧戸故枯湖誇雇顧鼓五互午呉娯後御悟碁語誤護交侯候光公功効厚口向后坑好孔孝工巧幸広康恒慌抗拘控攻更校構江洪港溝甲皇硬稿紅絞綱耕考肯航荒行衡講貢購郊酵鉱鋼降項香高剛号合拷豪克刻告国穀酷黒獄腰骨込今困墾婚恨懇昆根混紺魂佐唆左差査砂詐鎖座債催再最妻宰彩才採栽歳済災砕祭斎細菜裁載際剤在材罪財坂咲崎作削搾昨策索錯桜冊刷察撮擦札殺雑皿三傘参山惨散桟産算蚕賛酸暫残仕伺使刺司史嗣四士始姉姿子市師志思指支施旨枝止死氏祉私糸紙紫肢脂至視詞詩試誌諮資賜雌飼歯事似侍児字寺慈持時次滋治璽磁示耳自辞式識軸七執失室湿漆疾質実芝舎写射捨赦斜煮社者謝車遮蛇邪借勺尺爵酌釈若寂弱主取守手朱殊狩珠種趣酒首儒受寿授樹需囚収周宗就州修愁拾秀秋終習臭舟衆襲週酬集醜住充十従柔汁渋獣縦重銃叔宿淑祝縮粛塾熟出術述俊春瞬准循旬殉準潤盾純巡遵順処初所暑庶緒署書諸助叙女序徐除傷償勝匠升召商唱奨宵将小少尚床彰承抄招掌昇昭晶松沼消渉焼焦照症省硝礁祥称章笑粧紹肖衝訟証詔詳象賞鐘障上丈乗冗剰城場壌嬢常情条浄状畳蒸譲醸錠嘱飾植殖織職色触食辱伸信侵唇娠寝審心慎振新森浸深申真神紳臣薪親診身辛進針震人仁刃尋甚尽迅陣酢図吹垂帥推水炊睡粋衰遂酔錘随髄崇数枢据杉澄寸世瀬畝是制勢姓征性成政整星晴正清牲生盛精聖声製西誠誓請逝青静斉税隻席惜斥昔析石積籍績責赤跡切拙接摂折設窃節説雪絶舌仙先千占宣専川戦扇栓泉浅洗染潜旋線繊船薦践選遷銭銑鮮前善漸然全禅繕塑措疎礎祖租粗素組訴阻僧創双倉喪壮奏層想捜掃挿操早曹巣槽燥争相窓総草荘葬藻装走送遭霜騒像増憎臓蔵贈造促側則即息束測足速俗属賊族続卒存孫尊損村他多太堕妥惰打駄体対耐帯待怠態替泰滞胎袋貸退逮隊代台大第題滝卓宅択拓沢濯託濁諾但達奪脱棚谷丹単嘆担探淡炭短端胆誕鍛団壇弾断暖段男談値知地恥池痴稚置致遅築畜竹蓄逐秩窒茶嫡着中仲宙忠抽昼柱注虫衷鋳駐著貯丁兆帳庁弔張彫徴懲挑朝潮町眺聴脹腸調超跳長頂鳥勅直朕沈珍賃鎮陳津墜追痛通塚漬坪釣亭低停偵貞呈堤定帝底庭廷弟抵提程締艇訂逓邸泥摘敵滴的笛適哲徹撤迭鉄典天展店添転点伝殿田電吐塗徒斗渡登途都努度土奴怒倒党冬凍刀唐塔島悼投搭東桃棟盗湯灯当痘等答筒糖統到討謄豆踏逃透陶頭騰闘働動同堂導洞童胴道銅峠匿得徳特督篤毒独読凸突届屯豚曇鈍内縄南軟難二尼弐肉日乳入如尿任妊忍認寧猫熱年念燃粘悩濃納能脳農把覇波派破婆馬俳廃拝排敗杯背肺輩配倍培媒梅買売賠陪伯博拍泊白舶薄迫漠爆縛麦箱肌畑八鉢発髪伐罰抜閥伴判半反帆搬板版犯班畔繁般藩販範煩頒飯晩番盤蛮卑否妃彼悲扉批披比泌疲皮碑秘罷肥被費避非飛備尾微美鼻匹必筆姫百俵標氷漂票表評描病秒苗品浜貧賓頻敏瓶不付夫婦富布府怖扶敷普浮父符腐膚譜負賦赴附侮武舞部封風伏副復幅服福腹複覆払沸仏物分噴墳憤奮粉紛雰文聞丙併兵塀幣平弊柄並閉陛米壁癖別偏変片編辺返遍便勉弁保舗捕歩補穂募墓慕暮母簿倣俸包報奉宝峰崩抱放方法泡砲縫胞芳褒訪豊邦飽乏亡傍剖坊妨帽忘忙房暴望某棒冒紡肪膨謀貿防北僕墨撲朴牧没堀奔本翻凡盆摩磨魔麻埋妹枚毎幕膜又抹末繭万慢満漫味未魅岬密脈妙民眠務夢無矛霧婿娘名命明盟迷銘鳴滅免綿面模茂妄毛猛盲網耗木黙目戻問紋門匁夜野矢厄役約薬訳躍柳愉油癒諭輸唯優勇友幽悠憂有猶由裕誘遊郵雄融夕予余与誉預幼容庸揚揺擁曜様洋溶用窯羊葉要謡踊陽養抑欲浴翌翼羅裸来頼雷絡落酪乱卵欄濫覧利吏履理痢裏里離陸律率立略流留硫粒隆竜慮旅虜了僚両寮料涼猟療糧良量陵領力緑倫厘林臨輪隣塁涙累類令例冷励礼鈴隷零霊麗齢暦歴列劣烈裂廉恋練連錬炉路露労廊朗楼浪漏老郎六録論和話賄惑枠湾腕", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "漢字", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "ひらがな", None, -1))
        self.lineEdit_17.setText(QtWidgets.QApplication.translate("MainWindow", "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん", None, -1))
        self.lineEdit_9.setText(QtWidgets.QApplication.translate("MainWindow", "ゐゑ", None, -1))
        self.lineEdit_18.setText(QtWidgets.QApplication.translate("MainWindow", "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ", None, -1))
        self.lineEdit_10.setText(QtWidgets.QApplication.translate("MainWindow", "ぁぃぅぇぉっゃゅょゎ", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "カタカナ", None, -1))
        self.lineEdit_19.setText(QtWidgets.QApplication.translate("MainWindow", "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン", None, -1))
        self.lineEdit_11.setText(QtWidgets.QApplication.translate("MainWindow", "ヰヱ", None, -1))
        self.lineEdit_20.setText(QtWidgets.QApplication.translate("MainWindow", "ヴガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ", None, -1))
        self.lineEdit_12.setText(QtWidgets.QApplication.translate("MainWindow", "ァィゥェォヵヶッャュョヮ", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "ひらがな カタカナ", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "小文字(半角)", None, -1))
        self.lineEdit_13.setText(QtWidgets.QApplication.translate("MainWindow", "abcdefghijklmnopqrstuvwxyz", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("MainWindow", "大文字(半角)", None, -1))
        self.lineEdit_14.setText(QtWidgets.QApplication.translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "小文字(全角)", None, -1))
        self.lineEdit_15.setText(QtWidgets.QApplication.translate("MainWindow", "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "大文字(全角)", None, -1))
        self.lineEdit_16.setText(QtWidgets.QApplication.translate("MainWindow", "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("MainWindow", "ギリシャ大文字", None, -1))
        self.lineEdit_21.setText(QtWidgets.QApplication.translate("MainWindow", "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("MainWindow", "ギリシャ小文字", None, -1))
        self.lineEdit_22.setText(QtWidgets.QApplication.translate("MainWindow", "αβγδεζηθικλμνξοπρστυφχψω", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("MainWindow", "ルーン文字", None, -1))
        self.lineEdit_23.setText(QtWidgets.QApplication.translate("MainWindow", "ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛟᛞ", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", "アルファベット等", None, -1))
