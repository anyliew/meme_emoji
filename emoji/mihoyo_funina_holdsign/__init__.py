from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.exception import TextOverLength
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def mihoyo_funina_holdsign (images, texts: list[str], args):
    text = texts[0]
    frame = BuildImage.open(img_dir / "0.jpg")
    try:
        frame.draw_text(
            (275, 382, 639, 820),
            text,
            fill=(0, 0, 0),
            allow_wrap=True,
            max_fontsize=120,
            min_fontsize=20,
            lines_align="left",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(text)
    return frame.save_jpg()


add_meme(
    "mihoyo_funina_holdsign",
    mihoyo_funina_holdsign,
    min_texts=1,
    max_texts=1,
    default_texts=["当那古老的预言终结、一切落幕之后，我曾经陷入很长时间的消沉。站在舞台上的人受到观众的追捧，同时也承受着更多的注视与期待。但我很清楚，他们期待的并不是我，而是我扮演的那位「神明」...在这个过程中，我真正得到的只有孤独。所以我一度庆恶任何跟表演有关的事，把自己关在房间里，直到再次站上舞台、再次面对观众的时候，我才发现不知不觉我内心的不安已经消失了。现在的我可以坦然承受他们的目光,也许是因为…我终于开始「扮演」我自己了。"],
    keywords=["芙宁娜举牌","芙芙举牌","芙芙酱举牌"],
    tags=MemeTags.mihoyo,
    date_created=datetime(2025, 6, 1),
    date_modified=datetime(2025, 7, 4),
)