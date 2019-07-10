import os
import random
import time
from time import sleep

from selenium.webdriver.support.select import Select

from SC.testSC.handle.IsElementExist import isElementExist


class Parameters:
    def __init__(self,driver):
        self.driver = driver
    # ==========================================添加作品===========================================================
    #首页到立即报名界面
    def test_activityAccessPage(self,activity_name):
        sleep(8)
        self.driver.find_element_by_xpath('//a[contains(text(),"双创活动")]').click()  # 双创活动
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="navigation"]/div[1]/ul/li[3]').click()  # 点击赛事支撑
        sleep(4)
        self.driver.find_element_by_xpath('//span[@title="' + activity_name + '"]').click()  # 点击需要添加作品的活动
        sleep(8)
    # 点击作品提交及作品录入
    def ZPAdd(self,NUM_ZP):
        filepath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        # TODO 判断是否有立即报名和题目抽选的选项
        if isElementExist(self.driver, '//img[@src="/web/static/img/apply.aa218d8.png"]'):  # 立即报名是否存在--存在
            self.driver.find_element_by_xpath('//img[@src="/web/static/img/apply.aa218d8.png"]').click()  # 点击立即报名
            sleep(3)
            # TODO 通过状态来判断
            try:
                self.driver.find_element_by_xpath('//div[7]/*[@id="model-frame"]/div[2]/div/div[@class="SuccessMsgs"]')
                self.driver.find_element_by_xpath('//div[7]/div[@id="model-frame"]/div[1]/span').click()  # 点击叉号
            except:
                self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/input').click()  # 勾选同意
                sleep(1)
                self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[3]/span/button/span').click()  # 点击确定
                sleep(1)
                self.driver.find_element_by_xpath('//*[@id="arr"]/div[1]/div[1]/p/span/a[2]').click()  # 返回活动详情页
        else:
            pass
        sleep(2)
        if isElementExist(self.driver, '//img[@src="/web/static/img/drawQuestions.720ef4a.png"]'):  # 题目抽选是否存在--存在
            self.driver.find_element_by_xpath(
                '//img[@src="/web/static/img/drawQuestions.720ef4a.png"]').click()  # 点击题目抽选
            sleep(2)
            try:
                self.driver.find_element_by_xpath(
                    '//div[7]/*[@id="model-frame"]/div[2]/div/div[@class="SuccessMsgs"]').click()
                self.driver.find_element_by_xpath('//div[7]/div[@id="model-frame"]/div[1]/span').click()  # 点击右上角叉号
            except:
                self.driver.find_element_by_xpath('//*[@id="game-detail"]/div[3]/div/div[2]/div[1]/p').click()  # 点击抽选题目
                sleep(1)
                self.driver.find_element_by_xpath(
                    '//*[@id="game-detail"]/div[3]/div/div[2]/div[2]/p/button[2]').click()  # 点击确定
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="arr"]/div[1]/div[1]/p[2]/a[2]').click()  # 返回活动详情页
        else:
            pass
        sleep(2)
        if isElementExist(self.driver, '//img[@src="/web/static/img/subWorks.ceb7c37.png"]'):  # 提交作品是否存在--存在
            self.driver.find_element_by_xpath('//img[@src="/web/static/img/subWorks.ceb7c37.png"]').click()  # 点击提交作品
            sleep(4)
            for i in range(int(NUM_ZP)):
                self.driver.find_element_by_xpath(
                    '//*[@id="model-frame"]/div[2]/div/div[1]/div[2]/button[1]').click()  # 点击新建
                sleep(4)
                # 作品内容录入
                # TODO 出生日期有问题，'/html/body/div[5]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[6]'第一个5的地方一直变
                # ========================================项目基本情况=====================================
                project_name = "内网作品名称" + time.strftime('%m%d%H%M', time.localtime(time.time()))
                print('参加活动的作品名称为：'+ project_name)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[1]/input').send_keys(
                    project_name)  # 录入项目名称
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[2]/input').send_keys(
                    "企业名称" + time.strftime('%m%d%H%M', time.localtime(time.time())))  # 录入申报单位
                # 添加合作单位1、合作单位2
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[5]/input[' + str(
                        random.randint(1, 2)) + ']').click()  # 项目来源
                TJDW = random.randint(1, 2)
                if TJDW == 2:
                    self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[6]/input[' + str(
                            TJDW) + ']').click()  # 推荐单位
                    self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[6]/div/input').send_keys(
                        "推荐国网二级单位")  # 录入推荐国网二级单位
                else:
                    self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[6]/input[' + str(
                            TJDW) + ']').click()  # 推荐单位
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[7]/input[' + str(
                        random.randint(1, 4)) + ']').click()  # 项目领域
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[7]/textarea').send_keys(
                    "所在领域具体方向描述")  # 录入所在领域具体方向描述
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[8]/input[1]').click()  # 专业方向-生产
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[8]/input[2]').click()  # 专业方向-营销
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[8]/input[3]').click()  # 专业方向-物资
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[8]/input[4]').click()  # 专业方向-基建
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[8]/input[5]').click()  # 专业方向-互联网新技术
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[8]/input[6]').click()  # 专业方向-综合
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[9]/input[' + str(
                        random.randint(1, 6)) + ']').click()  # 技术状态
                syfw = random.randint(1, 3)
                if syfw == 3:
                    self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[10]/input[' + str(
                            syfw) + ']').click()  # 适用范围
                    self.driver.find_element_by_xpath('//*[@placeholder="详细描述"]').send_keys("适用范围详细描述")  # 录入适用范围详细描述
                else:
                    self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[10]/input[' + str(
                            syfw) + ']').click()  # 适用范围
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[1]/div[1]/input').send_keys(
                    "项目负责人姓名")  # 录入项目负责人姓名

                Select(self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[1]/select[1]')).select_by_visible_text(
                    "男")  # 录入项目负责人性别
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[1]/div[2]/div/input').click()  # 打开出生年月
                sleep(2)
                self.driver.find_element_by_xpath(
                    '/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[6]').click()  # 选择出生年月
                sleep(1)
                Select(self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[1]/select[2]')).select_by_visible_text(
                    "博士")  # 录入项目负责人学历
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[2]/div[1]/input').send_keys(
                    "工作单位")  # 录入项目负责人工作单位
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[2]/div[2]/input').send_keys('职务')
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[2]/div[3]/input').send_keys(
                    "职位职称技术等级")  # 录入项目负责人职称技术等级
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[3]/div[1]/input').send_keys(
                    "15210328827")  # 录入项目负责人联系方式
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[3]/div[2]/input').send_keys(
                    "15210328827@126.com")  # 录入项目负责人电子邮箱
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[4]/div[1]/input').send_keys(
                    "130426199010231917")  # 录入项目负责人身份证号
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[4]/div[2]/input').send_keys(
                    "联系地址")  # 录入项目负责人联系地址
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[5]/div/textarea').send_keys(
                    "项目负责人简介")  # 录入项目负责人项目负责人简介
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[11]/div[6]/textarea').send_keys('团队优势')
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[12]/div[1]/div[1]/input').send_keys(
                    "项目参与人姓名")  # 录入项目参与人姓名
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[12]/div[1]/div[2]/input').click()  # 打开出生年月
                sleep(3)
                self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[6]').click()  # 选择出生年月
                sleep(1)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[12]/div[1]/div[3]/input').send_keys(
                    "职位职称技术等级")  # 录入项目参与人职位
                Select(self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[12]/div[1]/select')).select_by_visible_text(
                    "博士")  # 录入项目参与人学历
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[12]/div[2]/div[1]/input').send_keys(
                    "15210328828")  # 录入项目参与人联系方式
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[12]/div[2]/div[2]/input').send_keys(
                    "15210328828@126.com")  # 录入项目参与人电子邮箱
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[12]/div[2]/div[3]/input').send_keys('单位')
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[12]/div[3]/div/input').send_keys(
                    "备注")  # 录入项目参与人备注

                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[14]/div/div[1]/input').send_keys(
                    "获奖名称")  # 录入获奖名称
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[14]/div/div[2]/input').click()  # 打开获奖日期
                sleep(3)
                self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[6]').click()  # 选择获奖日期
                sleep(1)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[14]/div/div[3]/input').send_keys(
                    "奖励等级")  # 录入奖励等级
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[14]/div/div[4]/input').send_keys(
                    "授奖单位")  # 录入授奖单位

                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[16]/div/div[1]/input').send_keys(
                    "专利名称")  # 录入专利名称
                '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[16]/div/div[1]/input'
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[16]/div/div[2]/input').click()  # 打开公告日
                sleep(1)
                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[6]').click()  # 选择公告日
                sleep(1)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[16]/div/div[3]/input').send_keys(
                    "1234567890")  # 录入专利号/申请号
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[16]/div/div[4]/input').send_keys(
                    "0987654321")  # 录入专利类别
                sleep(1)
                self.driver.find_element_by_xpath('//div[18]/div/*[@id="fileUpload_test"]/form/input').send_keys(
                    filepath + "\data\Penguins.jpg")  # 项目基本情况附件
                sleep(5)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[1]/div/div[19]/div/input').click()  # 点击下一页
                sleep(2)
                # ========================================商业计划书=====================================
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[1]').send_keys(
                    "项目简介")  # 录入项目简介
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]').send_keys(
                    "录入项目创新点")  # 录入项目创新点
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]').send_keys(
                    "项目成效或预期成效")  # 录入项目成效或预期成效
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[4]/div/div/div[2]/div[1]').send_keys(
                    "市场分析")  # 录入市场分析
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[5]/div/div/div[2]/div[1]').send_keys(
                    "核心竞争力")  # 录入核心竞争力
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[6]/div/div/div[2]/div[1]').send_keys(
                    "商业模式")  # 录入商业模式
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[7]/div/div/div[2]/div[1]').send_keys(
                    "实施计划")  # 录入实施计划
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[8]/div/div/div[2]/div[1]').send_keys(
                    "安全、风险与对策")  # 录入安全、风险与对策
                self.driver.find_element_by_xpath('//div[9]/div/*[@id="fileUpload_test"]/form/input').send_keys(
                    filepath + "\data\Koala.jpg")  # 商业计划书附件
                self.driver.find_element_by_xpath('//div[9]/div/*[@id="fileUpload_test"]/form/input').send_keys(
                    filepath + "\data\Koala.jpg")  # 商业计划书附件
                sleep(5)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[10]/div/input').click()  # 点击下一步

                sleep(2)
                # ========================================服务需求=====================================
                NUM = '1'  # NUM可以输入1-6  参赛目的：寻求合作机会、宣传展示、寻求股权融资机会、寻求债权融资机会、寻求国家电网资源支持、寻求学习交流机会       可以做成随机数
                # 合作方式：技术转让、许可使用、合作开发、技术服务、融资需求、产品推广
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[1]/input[' + NUM + ']').click()  # 录入参赛    目的
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[2]/input[' + NUM + ']').click()  # 录入合作方式
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[3]/div/div[1]/input').click()  # 点击股权融资需求
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[3]/div/div[2]/div[1]/input').send_keys(
                    "100")  # 录入股权融资金额
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/input').send_keys(
                    "200")  # 录入股权比例
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[3]/div/div[2]/div[3]/textarea').send_keys(
                    "资金使用计划书1")  # 录入资金使用计划书
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[3]/div/div[3]/input').click()  # 点击债券融资需求
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[3]/div/div[4]/div[1]/input').send_keys(
                    "100")  # 录入债券融资金额
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[3]/div/div[4]/div[2]/input').send_keys(
                    "200")  # 录入ttach债券比例
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[3]/div/div[4]/div[3]/textarea').send_keys(
                    "资金使用计划书2")  # 录入资金使用计划书
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[4]/textarea').send_keys("资源需求")  # 录入资源需求
                self.driver.find_element_by_xpath('//div[5]/div/*[@id="fileUpload_test"]/form/input').send_keys(
                    filepath + "\data\Desert.jpg")  # 申报单位意见
                sleep(7)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div[3]/div[3]/div[2]/div[3]/div/div[6]/div/button').click()  # 点击保存
                sleep(5)
                self.driver.find_element_by_xpath(
                    '//*[@id="model-frame"]/div[2]/div/div[2]/div/div[1]/ul[1]/li[1]/input[1]').click()  # 选中要提交的作品
                sleep(1)
                self.driver.find_element_by_xpath(
                    '//*[@id="model-frame"]/div[2]/div/div[1]/div[2]/button[2]').click()  # 点击提交
                sleep(2)
                self.driver.find_element_by_xpath('//*[@id="raisePrice"]').click()  # 点击确定提交
                sleep(2)
        else:
            pass
    #==========================================添加活动=========================================================
    #首页到录入赛事支撑活动内容的界面
    def test_accessToAccBasciInfo(self):
        sleep(8)
        #####通过双创活动创建活动
        # driver.find_element_by_xpath('//*[@id="menu"]/span[5]/a').click()#双创活动
        # sleep(4)
        # driver.find_element_by_xpath('//*[@id="navigation"]/div[1]/ul/li[3]').click()#赛事支撑
        # sleep(4)
        # driver.find_element_by_xpath('//*[@id="navigation"]/div[1]/p').click()#发布活动
        #############企业中心创建活动
        self.driver.find_element_by_xpath('//*[@id="public-header"]/div[1]/div[2]/ul/li[4]').click()#企业中心
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="informationPage"]/section/aside/div/div[6]/div/span[2]').click()#点击活动
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="informationPage"]/section/aside/div/div[6]/div[2]/div[1]/div/span[2]').click()#点击我发起的活动
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="listactivitieslaunched"]/div[2]/div[3]/button[2]').click()#点击新建
        sleep(1)
        Select(self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div[2]/p/select')).select_by_visible_text("赛事支撑")#活动类型选择赛事支撑
        sleep(1)
        self.driver.find_element_by_xpath('//div[7]/*[@id="model-frame"]/div[3]/button[2]').click()#点击确定
    # 赛事支撑活动详情录入
    def test_activity_info_write(self,acc_name,acc_start_time_row,acc_start_time_col):
        #基本信息
        print('创建的活动为：' + acc_name)
        sleep(4)
        ###############基本信息
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[1]/p/input').send_keys(acc_name)
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[3]/p/input').send_keys('活动副标题')
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[7]/div').click()#活动范围的...
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="contact-frame"]/div[2]/div/div[1]/div/div/div/span[2]').click()#活动范围选择全活动
        self.driver.find_element_by_xpath('//*[@id="checkboxName"]').click()#勾选是否含子单位
        self.driver.find_element_by_xpath('//*[@id="contact-frame"]/div[3]/button[2]').click()#点击确定
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[9]/div').click()#主办方的...
        sleep(1)
        self.driver.find_element_by_xpath('//div[3]/div[@id="contact-frame"]/div[2]/div[2]/ul/li[1]/span').click()#主办方选择全社会
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[9]/input').send_keys('主办部门')#录入主办部门
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[11]/div/div').click()#承办方的...
        sleep(2)
        self.driver.find_element_by_xpath('//div[4]/div[@id="contact-frame"]/div[2]/div[2]/ul/li[1]/span').click()#承办方选择全社会
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[11]/div/input').send_keys('承办部门')#录入承办部门
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[2]/div[14]/div[1]/input').click()  # 打开活动开始时间控件
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                acc_start_time_col) + ']').click()  # 录入开始时间,第五行第二列 20
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/button[2]/span').click()  # 点击确定按钮

        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[2]/div[14]/div[2]/input').click()  # 打开活动结束时间控件
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div/div[3]/table[1]/tbody/tr[7]/td[7]').click()  # 录入结束时间(当前日期控件可展示的最后一天，非当月最后一天)

        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]/span').click()  # 点击确定
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[16]/div[2]/textarea').send_keys('活动简介')
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[18]/div[2]/textarea').send_keys('活动要求')
        sleep(1)
        #活动海报
        filepath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        # os.path.split(path)[0]获取文件的父级路径
        # os.path.dirname(path)获取路径去掉文件名的路径(只要文件夹)
        # os.path.abspath(__file__)获取__file__绝对路径
        self.driver.find_element_by_id('FileUpload').send_keys(filepath + "\data\Penguins.jpg")#活动海报上传
        sleep(6)
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[2]/div[22]/div/button').click()#点击下一步
        sleep(2)
        ###############活动配置
        #######活动报名
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[2]/div[1]/div[1]/input').click()  # 打开活动报名开始时间控件
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                acc_start_time_col) + ']').click()  # 录入活动报名开始时间,第五行第二列 20
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/button[2]/span').click()
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[2]/div[1]/div[2]/input').click()  # 打开活动报名结束时间控件
        sleep(1)
        if acc_start_time_col == 7:
            # 录入活动报名结束时间(若活动开始时间为日期控件最后一列，则结束日期为下一行的第一列)
            self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(
                acc_start_time_row + 1) + ']/td[1]').click()
        else:
            # 录入活动报名结束时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加一)
            self.driver.find_element_by_xpath(
                '/html/body/div[5]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                    acc_start_time_col + 1) + ']').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[2]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="zizhu"]').click()#活动报名-自主报名
        self.driver.find_element_by_xpath('//*[@id="zihuodong"]').click()#活动报名-子活动上报
        sleep(1)
        #######题目抽选
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[4]/div[1]/div[1]/input').click()  # 打开题目抽选开始时间控件
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[6]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                acc_start_time_col) + ']').click()  # 录入题目抽选开始时间,与活动报名时间一样
        self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/button[2]/span').click()  # 点击确定
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[4]/div[1]/div[2]/input').click()  # 打开题目抽选结束时间控件
        sleep(1)
        if acc_start_time_col == 7:
            # 录入题目抽选结束时间(若活动开始时间为日期控件最后一列，则结束日期为下一行的第一列)
            self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(
                acc_start_time_row + 1) + ']/td[1]').click()
        else:
            # 录入题目抽选结束时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加一)
            self.driver.find_element_by_xpath(
                '/html/body/div[7]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                    acc_start_time_col + 1) + ']').click()
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/button[2]/span').click()  # 点击确定
        sleep(1)
        self.driver.find_element_by_xpath('//div[@class="fileW1"]/div[@id="fileUpload_test"]/form/input').send_keys(filepath + "\data\zuopin.zip")#题目抽选上传题目点击上传
        sleep(7)
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[4]/div[4]/div[2]/div[3]/button').click()# 点击上传
        self.driver.find_element_by_xpath('//*[@id="suiji"]').click()#抽取规则-随机抽取
        # driver.find_element_by_xpath('//*[@id="ziyou"]"]').click()#抽取规则-自由选择

        ########作品申报
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[6]/div[1]/div[1]/input').click()  # 打开作品申报开始时间控件
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[8]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                acc_start_time_col) + ']').click()  # 录入作品申报开始时间,与活动报名时间一样
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/button[2]/span').click()  # 点击确定
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[6]/div[1]/div[2]/input').click()  # 打开作品申报结束时间控件
        sleep(2)
        if acc_start_time_col == 7:
            # 录入作品申报结束时间(若活动开始时间为日期控件最后一列，则结束日期为下一行的第一列)
            self.driver.find_element_by_xpath('/html/body/div[9]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(
                acc_start_time_row + 1) + ']/td[1]').click()
        else:
            # 录入作品申报结束时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加一)
            self.driver.find_element_by_xpath(
                '/html/body/div[9]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                    acc_start_time_col + 1) + ']').click()
            # '//*[@id="gameActivityForm"]/div[1]/div[3]/div[4]/div[1]/div[2]/input'
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/button[2]/span').click()  # 点击确定
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[7]/button').click()#作品申报-申报上限-未设置
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[2]/input').clear()#作品申报-申报上线限-个人内部项目-清空
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[2]/input').send_keys("100")#作品申报-申报上线限-个人内部项目
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[3]/input').clear()#作品申报-申报上线限-个人外部项目--清空
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[3]/input').send_keys("100")#作品申报-申报上线限-个人外部项目
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[4]/input').clear()#作品申报-申报上线限-企业内部项目--清空
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[4]/input').clear()#作品申报-申报上线限-企业外部项目--清空
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[4]/input').send_keys("100")#作品申报-申报上线限-企业内部项目
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[5]/input').clear()#作品申报-申报上线限-企业外部项目--清空
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[5]/input').clear()#作品申报-申报上线限-企业外部项目--清空
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[2]/div/div/div[2]/ul/li/div[5]/input').send_keys("100")#作品申报-申报上线限-企业外部项目
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="model-frame"]/div[3]/div/button').click()#作品申报-申报上线限-确定
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="youthGame"]').click()#作品申报-选择申报表-青创赛申请表
        # driver.find_element_by_xpath('//*[@id="commonExal"]').click()#作品申报-选择申报表-普通申请表
        #########比赛评审
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[9]/div[2]/div[1]/input').click()  # 打开比赛评审开始时间控件
        sleep(1)
        if acc_start_time_col >= 6:
            # 录入比赛评审开始时间(若比赛评审时间为作品提交结束时间加一,活动开始时间加二；若活动开始时间列号>=6，行号加一，列号+2-7)
            self.driver.find_element_by_xpath(
                '/html/body/div[10]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row + 1) + ']/td[' + str(
                    acc_start_time_col - 5) + ']').click()
        else:
            sleep(1)
            # 录入比赛评审开始时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加一)
            self.driver.find_element_by_xpath(
                '/html/body/div[10]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                    acc_start_time_col + 2) + ']').click()
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/button[2]/span').click()  # 点击确定
        # sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[9]/div[2]/div[2]/input').click()  # 打开比赛评审结束时间控件
        sleep(1)
        if acc_start_time_col >= 5:
            # 录入比赛评审结束时间(比赛评审时间为作品提交结束时间加二,活动开始时间加三；若活动开始时间列号>=5，行号加一，列号+3-7)
            self.driver.find_element_by_xpath(
                '/html/body/div[11]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row + 1) + ']/td[' + str(
                    acc_start_time_col - 4) + ']').click()
        else:
            # 录入比赛评审开始时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加3)
            self.driver.find_element_by_xpath(
                '/html/body/div[11]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                    acc_start_time_col + 3) + ']').click()
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/button[2]/span').click()  # 点击确定
        sleep(1)
        ########获奖公示
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[10]/div[2]/div[1]/div[1]/input').click()  # 打开获奖公示开始时间控件
        sleep(1)
        if acc_start_time_col >= 4:
            # 录入获奖公示开始时间(若获奖公示时间为作品提交结束时间加3,活动开始时间加4；若活动开始时间列号>=4，行号加一，列号+5-7)
            self.driver.find_element_by_xpath(
                '/html/body/div[12]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row + 1) + ']/td[' + str(
                    acc_start_time_col - 3) + ']').click()

        else:
            # 录入获奖公示开始时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加4)
            self.driver.find_element_by_xpath(
                '/html/body/div[12]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                    acc_start_time_col + 4) + ']').click()
        self.driver.find_element_by_xpath('/html/body/div[12]/div[2]/button[2]/span').click()  # 点击确定
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="gameActivityForm"]/div[1]/div[3]/div[10]/div[2]/div[1]/div[2]/input').click()  # 打开获奖公示结束时间控件
        sleep(1)
        if acc_start_time_col >= 3:
            # 录入获奖公示结束时间(获奖公示时间为作品提交时间加二,活动开始时间加三；若活动开始时间列号>=5，行号加一，列号+5-7)
            self.driver.find_element_by_xpath(
                '/html/body/div[13]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row + 1) + ']/td[' + str(
                    acc_start_time_col - 2) + ']').click()
        else:
            # 录入获奖公示结束时间(若活动开始时间不是日期控件最后一列，则结束日期行号不变，列数加3)
            self.driver.find_element_by_xpath(
                '/html/body/div[13]/div[1]/div/div[3]/table[1]/tbody/tr[' + str(acc_start_time_row) + ']/td[' + str(
                    acc_start_time_col + 5) + ']').click()
        self.driver.find_element_by_xpath('/html/body/div[13]/div[2]/button[2]/span').click()  # 点击确定
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[10]/div[3]/div').click()#获奖公示-通知范围的...
        sleep(2)
        self.driver.find_element_by_xpath('//div[5]/div[@id="contact-frame"]/div[2]/div/div[1]/div/div/div[1]/span[2]').click()#获奖公示-通知范围-全社会
        sleep(1)
        self.driver.find_element_by_xpath('//div[5]/div/div[2]/div/div[2]/ul/li/span[2]/input[@id="checkboxName"]').click()#勾选是否含子单位
        sleep(1)
        self.driver.find_element_by_xpath('//div[5]/*[@id="contact-frame"]/div[3]/button[2]').click()#点击确定
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[3]/div[11]/input[2]').click()#点击下一步
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="gameActivityForm"]/div[1]/div[4]/div[2]/div/input[2]').click()#点击发起活动
        sleep(1)
        self.driver.find_element_by_xpath('//div[1]/div[@id="model-frame"]/div[3]/button[2]').click()#确定发起活动
        sleep(2)
    def test_activityShenHe(self,acc_name):
        #################################################进行活动审核

        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/div/li/div/span').click()#点击审核管理
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/div/li/ul/a[3]/li/span').click()#点击活动审核
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[1]/div/div/input').clear()#清空活动名称
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[1]/div[1]/div/div/input').send_keys(acc_name)#查询活动名称
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/button[1]/span').click()#点击查询
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()#勾选活动
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[2]/div[3]/div/button[2]/span').click()#点击同意

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]/span').click()#点击确定
        sleep(2)
        self.driver.quit()
    def save_activity_name(self,acc_name):
        basepath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        # 打开文件
        f = open(basepath + "\\data\\activity_name", 'w')
        # 读取文件内容
        f.write(acc_name)
        # 关闭文件
        f.close()
    def get_activity_name(self):
        basepath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        # 打开文件
        f = open(basepath + '\data\\activity_name', 'r')
        # 读取文件内容
        acc_name = f.readline()
        return acc_name
        # 关闭文件
        f.close()
        # with open(basepath + '\data\\activity_name','r') as file:
        #     return file.readlines()

