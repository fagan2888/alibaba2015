## 派森队初赛
中国科大派森队初赛代码。 F1>10%

运行god.py可以运行整个流程，并得到一个baseline，即模型0.
默认是开10个进程运行的，机器不给力的慎重！！可以在com.py里面改变量n_process的值。

## 流程说明

1. user_action_data_split.py 首先将用户行为数据按照时间分为18号的，和非18号的。
生成user_action_train.csv和user_action_test.csv 。
2. createFeature.py [train|submit] 将第一个文件生成特征文件，如果用多个生成特征文件，最终用merge.py将特征文件融合到feature.merge.csv
gen_label_data.py 将第二个文件生成标签文件
3. gen_data.py 将特征和标签文件融合到data.csv中
4. data_sample.py 将data.csv划分为训练data.train.csv和测试文件data.test.csv，其中训练数据对付样本进行下采样。
5. model0.py 模型训练文件，不解释
6. gen_rec_data.py 利用模型和提交数据用的特征进行预测，生成提交文件

## 工具
summary.py 对已训练模型进行评价


File: data.csv

0 user_id
1 item_id
2 user_action_count
3 user_lastday_count
4 user_buy_count
5 item_click_count
6 item_lastday_count
7 item_buy_count
8 cat_click_count
9 cat_buy_count
10 user_cat_count
11 user_cat_lastday_count
12 user_item_count
13 user_item_lastday_count
14 user_add_car
15 user_add_star
16 item_added_car
17 item_added_start
18 user_item_lasttime
19 cat_add_car
20 cat_add_star
21 usergeo_item_lastday_click
22 usergeo_item_lastday_star
23 usergeo_item_lastday_cart
24 usergeo_item_lastday_buy
25 usergeo_item_before_lastday_click
26 usergeo_item_before_lastday_star
27 usergeo_item_before_lastday_cart
28 usergeo_item_before_lastday_buy
29 geo_users_number
30 user_item_geo_distance
31 user_item_buy
32 user_item_lastweek_click
33 user_item_lastweek_star
34 user_item_lastweek_add_car
35 user_item_lastweek_buy
36 user_item_halfmonth_click
37 user_item_halfmonth_star
38 user_item_halfmonth_add_car
39 user_item_halfmonth_buy
40 user_item_before_halfmonth_click
41 user_item_before_halfmonth_star
42 user_item_before_halfmonth_add_car
43 user_item_before_halfmonth_buy
44 user_cat_lastweek_click
45 user_cat_lastweek_star
46 user_cat_lastweek_add_car
47 user_cat_lastweek_buy
48 user_cat_halfmonth_click
49 user_cat_halfmonth_star
50 user_cat_halfmonth_add_car
51 user_cat_halfmonth_buy
52 user_cat_before_halfmonth_click
53 user_cat_before_halfmonth_star
54 user_cat_before_halfmonth_add_car
55 user_cat_before_halfmonth_buy
56 user_lastday_add_star
57 user_item_lastday_add_star
58 user_cat_lastday_add_star
59 user_lastday_add_cart
60 user_item_lastday_add_cart
61 user_cat_lastday_add_cart
62 user_lastday_buy
63 user_item_lastday_buy
64 user_cat_lastday_buy
65 user_item_click_nobuy
66 user_item_star_nobuy
67 user_item_cart_nobuy
68 user_item_buy_again
69 user_geo_b
70 user_geo_f
71 user_geo_i
72 user_geo_m
73 user_geo_o
74 user_geo_5
75 user_geo_4
76 user_geo_v
77 user_geo_9
78 user_geo_t
79 user_cat_aveThreeDayDelta_click
80 user_cat_aveThreeDayDelta_star
81 user_cat_aveThreeDayDelta_add_car
82 user_cat_aveThreeDayDelta_buy
83 user_item_aveThreeDayDelta_click
84 user_item_aveThreeDayDelta_star
85 user_item_aveThreeDayDelta_add_car
86 user_item_aveThreeDayDelta_buy
87 item_geo_9
88 item_geo_4
89 item_geo_m
90 item_geo_t
91 item_geo_f
92 buy
