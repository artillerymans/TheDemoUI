from flet import Row, Icon, icons, colors, Text, Stack, Container
from flet.alignment import center


class TitleView(Row):

    def __init__(self, title_str,on_back = None):
        super().__init__(self)
        self.alignment = "spaceBetween"
        self.controls = [
            Container(
                Icon(
                    name=icons.ARROW_BACK_IOS_ROUNDED,
                    color=colors.BLACK,
                    size=20
                ),
                alignment=center,
                on_click=on_back
            ),
            Text(
                title_str,
                color=colors.BLACK,
                font_family="PingFang SC",
                weight="w700"
            ),
            Stack(
                width=20,
                height=20
            )
        ]



