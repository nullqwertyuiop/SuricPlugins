import random
from datetime import datetime
import json
from pathlib import Path

from graia.ariadne import Ariadne
from graia.ariadne.event.message import  Friend, Member, GroupMessage, FriendMessage, MessageEvent
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
    dick_color = random.choice(COLOR_TEMPLATES)
    dick_outward = random.choice(OUTWARD_TEMPLATES)
    dick_comment_score = 0.0
    dick_comment_score_time = 6
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

    # 先判断boki
    if random.randint(0, 1) == 1:
        boki_status = "勃起"
        angle = f"{random.randint(90, 180)}度"
        angle_status = "boki"
        dick_comment_score += 10
    else:
        boki_status = "软掉"
        angle = f"{random.randint(0, 90)}度"
        angle_status = ""
        dick_color = ""
        dick_outward = ""


    rd_phimosis_status = random.randint(0, 2)
    if rd_phimosis_status == 0:
        phimosis_status = "包茎"
    elif rd_phimosis_status == 1:
        phimosis_status = "半包茎"
    else:
        phimosis_status = "非包茎"
    dick_comment_score += rd_phimosis_status * 5

    rd_dick_hardness = random.randint(1, 10)
    dick_hardness = f"莫氏硬度为{rd_dick_hardness}"
    dick_comment_score += rd_dick_hardness

    rd_egg_weight = random.randint(50, 1000)
    egg_weight = f"{rd_egg_weight}克"
    dick_comment_score += rd_egg_weight * 10 / 951.0

    dick_legth = random.randint(-10, 30)
    if dick_legth > 0:
        dick_comment_score += dick_legth / 3.0
    elif dick_legth != 0:
        dick_comment_score += abs(dick_legth)

    if dick_legth > 20:
        dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_0)
        dick_comment = random.choice(COMMENT_TEMPLATES_0)
    elif 15 < dick_legth <= 20:
        dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_1)
        dick_comment = random.choice(COMMENT_TEMPLATES_1)
    elif 10 <= dick_legth <= 15:
        dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_2)
        dick_comment = random.choice(COMMENT_TEMPLATES_2)
    elif 0 < dick_legth < 10:
        dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_3)
        dick_comment = random.choice(COMMENT_TEMPLATES_3)
    elif dick_legth == 0:
        dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_4)
        dick_comment = random.choice(COMMENT_TEMPLATES_4)
    else:
        dick_length_evaluate = random.choice(EVALUATE_TEMPLATES_5)
        dick_comment = random.choice(COMMENT_TEMPLATES_5)
    a = "\n"
    length_text = f"{dick_legth}cm的牛子，{a}{dick_length_evaluate}"


    # #######################################################################
    # 新功能
    # 牛子颜色
    cr = random.randint(0,255)
    cg = random.randint(0,255)
    cb = random.randint(0,255)
    black = "black"
    white = "white"
    if(cr+cg+cb>382):
        textcolor = black
    else:
        textcolor = white
    # RGB-to-Hex
    Hexcolor = ('{:02X}' * 3).format(cr, cg, cb)
    print (cr,cg,cb)
    print (Hexcolor)
    # #######################################################################

    await send_message(
        event.sender.group if isinstance(event, GroupMessage) else event.sender,
        MessageChain(f"你今天有一根{dick_enchant}{dick_color}{dick_outward}{boki_status}的，{angle_status}角度为{angle}的{phimosis_status}的{dick_hardness},并且蛋蛋{egg_weight}的{length_text}{a}大众点评：{round(dick_comment_score/dick_comment_score_time,1)}分，{dick_comment}"),
        app.account,
    )
    random.seed()


def RandomSeed(supplicant: Member | Friend):
    random.seed(int(f"{datetime.now().strftime('%Y%m%d')}{supplicant.id}"))
