import random
from datetime import datetime
import json
from pathlib import Path

from graia.ariadne import Ariadne
from graia.ariadne.event.message import (
    Friend,
    Member,
    GroupMessage,
    FriendMessage,
    MessageEvent,
)
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.twilight import (
    Twilight,
    FullMatch,
    RegexMatch,
    RegexResult,
)
from graia.ariadne.util.saya import listen, dispatch, decorate
from graia.saya import Channel

from library.decorator.blacklist import Blacklist
from library.decorator.distribute import Distribution
from library.decorator.switch import Switch
from library.util.dispatcher import PrefixMatch
from library.util.message import send_message

channel = Channel.current()
assets_path = Path(Path(__file__).parent, "assets")
settings_file = Path(assets_path / "news_settings.json")

with settings_file.open("r", encoding="UTF-8") as f:
    _data = json.loads(f.read())
    COLOR_TEMPLATES = _data["news_color"]
    OUTWARD_TEMPLATES = _data["outward"]
    EVALUATE_TEMPLATES_0 = _data["news_evaluate_0"]
    EVALUATE_TEMPLATES_1 = _data["news_evaluate_1"]
    EVALUATE_TEMPLATES_2 = _data["news_evaluate_2"]
    EVALUATE_TEMPLATES_3 = _data["news_evaluate_3"]
    EVALUATE_TEMPLATES_4 = _data["news_evaluate_4"]
    EVALUATE_TEMPLATES_5 = _data["news_evaluate_5"]
    COMMENT_TEMPLATES_0 = _data["public_comment_0"]
    COMMENT_TEMPLATES_1 = _data["public_comment_1"]
    COMMENT_TEMPLATES_2 = _data["public_comment_2"]
    COMMENT_TEMPLATES_3 = _data["public_comment_3"]
    COMMENT_TEMPLATES_4 = _data["public_comment_4"]
    COMMENT_TEMPLATES_5 = _data["public_comment_5"]
_data


@listen(GroupMessage, FriendMessage)
@dispatch(Twilight(PrefixMatch(), FullMatch("今日牛子")))
@decorate(Switch.check(channel.module), Distribution.distribute(), Blacklist.check())
async def daily_news(app: Ariadne, event: MessageEvent):
    RandomSeed(event.sender)
    # #######################################################################
    # TODO:PlayWright重构
    # #######################################################################
    # 需要首先判断牛子是否大于0
    news_length = random.randint(-10, 30)
    news_or_cloaca = ""
    a = "\n"
    if news_length > 0:

        # 确定拥有的生殖器类型
        news_or_cloaca = "牛子"

        # 确定是否勃起
        if random.randint(0, 1) == 1:
            boki_status = "勃起"
            angle_status = "勃起"
            angle = f"{random.randint(90, 180)}度"
        else:
            boki_status = "软掉"
            angle_status = ""
            angle = f"{random.randint(0, 90)}度"

        # 判断是否包茎
        rd_phimosis_status = random.randint(0, 2)
        if rd_phimosis_status == 0:
            phimosis_status = "包茎"
        elif rd_phimosis_status == 1:
            phimosis_status = "半包茎"
        else:
            phimosis_status = "非包茎"

        # 判断蛋蛋重量
        rd_egg_weight = random.randint(50, 500)
        egg_weight = f"{rd_egg_weight}克"

        # 生成牛子的系统评价 # 生成牛子的大众点评
        if news_length > 20:
            dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_0)
            dick_comment = random.choice(COMMENT_TEMPLATES_0)
            news_score = random.randint(60, 100)
        elif 15 < news_length <= 20:
            dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_1)
            dick_comment = random.choice(COMMENT_TEMPLATES_1)
            news_score = random.randint(40, 80)
        elif 10 <= news_length <= 15:
            dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_2)
            dick_comment = random.choice(COMMENT_TEMPLATES_2)
            news_score = random.randint(30, 60)
        else:
            dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_3)
            dick_comment = random.choice(COMMENT_TEMPLATES_3)
            news_score = random.randint(0, 30)

    elif news_length < 0:
        news_or_cloaca = "泄殖腔"
        # 生成泄殖腔的系统评价 # 生成泄殖腔的大众点评
        dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_5)
        dick_comment = random.choice(COMMENT_TEMPLATES_5)
        news_score = random.randint(0, 100)

    else:
        news_or_cloaca = "如履平地"
        # 生成独特的评价
        dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_4)
        dick_comment = random.choice(COMMENT_TEMPLATES_4)
        news_score = 0

    # 照搬旧版的附魔系统
    if random.randint(0, 4) == 0:
        enchant_lv = ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ"]
        enchant_list = [
            "附魔上了消失诅咒",
            "附魔上了经*修补",
            "附魔上了火焰附加",
            "附魔上了耐久",
            "附魔上了荆棘",
            "附魔上了力量",
        ]
        rd_enchant = random.randint(0, 5)
        dick_enchant = enchant_list[rd_enchant]
        dick_comment_score = 0
        if rd_enchant < 2:
            dick_comment_score += rd_enchant * 10
        else:
            if rd_enchant == 2:
                rd_lv = random.randint(0, 1)
                dick_comment_score += (rd_lv + 1) * 5
            elif rd_enchant < 5:
                rd_lv = random.randint(0, 2)
                dick_comment_score += (rd_lv + 1) * 10 / 3.0
            else:
                rd_lv = random.randint(0, 4)
                dick_comment_score += (rd_lv + 1) * 2
            dick_enchant += enchant_lv[rd_lv]
        dick_enchant += "的"
    else:
        dick_enchant = ""

    # 新功能
    # 牛子颜色
    # 定义三个数值来生成 RGB
    cr = random.randint(0, 255)
    cg = random.randint(0, 255)
    cb = random.randint(0, 255)
    # 没用的两个参数
    black = "black"
    white = "white"
    # 设想是如果r+g+b大于382就将覆盖层文字修改为黑色，否则为白色
    if cr + cg + cb > 382:
        textcolor = black
    else:
        textcolor = white
    # RGB-to-Hex 将RGB转换为Hex值，使其占用长度减少
    Hexcolor = ("{:02X}" * 3).format(cr, cg, cb)
    # print(cr, cg, cb)
    # print(Hexcolor)
    # #######################################################################
    # 先判断牛子是否大于0
    # >0 为正常牛子
    # <0 为腔
    # #######################################################################

    # 向PlayWright输出的参数内容
    # 生殖器类型
    News_or_cloaca_out = news_or_cloaca
    # 长度
    News_length_out = news_length
    # 系统评价
    System_comment_out = dick_length_evaluate
    # 颜色
    Hexcolor_out = f"#{Hexcolor}颜色的"
    # 大众点评分数
    Score_out = news_score / 10
    if news_or_cloaca == "牛子":
        news_message = f"你今天有一根{dick_enchant}{Hexcolor_out}{boki_status}的{News_length_out}CM长的，{angle_status}角度为{angle}的{phimosis_status}的,并且蛋蛋{egg_weight}的牛子{a}系统点评：{System_comment_out}{a}大众点评：{Score_out}分，{dick_comment}"
    else:
        news_message = f"你今天有一根{dick_enchant}{Hexcolor_out}的{News_length_out}CM深的泄殖腔{a}系统点评：{System_comment_out}{a}大众点评：{Score_out}分，{dick_comment}"

    await send_message(
        event.sender.group if isinstance(event, GroupMessage) else event.sender,
        MessageChain(news_message),
        app.account,
    )
    random.seed()

# Seed
def RandomSeed(supplicant: Member | Friend):
    random.seed(int(f"{datetime.now().strftime('%Y%m%d')}{supplicant.id}"))
