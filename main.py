from flet import *
from flet import colors, padding, margin, icons

from TitleView import TitleView


def main(page: Page):
    page.window_width = 375
    page.window_height = 812
    page.padding = padding.all(0)
    page.window_center()

    def onFish(e):
        page.window_close()

    m_column = Column(
        [
            Column(
                [
                    Container(
                        TitleView(title_str="个人信息", on_back=onFish),
                        padding=padding.symmetric(horizontal=10)
                    ),
                    Container(
                        content=Row(
                            [
                                Text(
                                    "联系人手机号",
                                    color='#000018',
                                    size=14,
                                    weight="w400"
                                ),
                                Text(
                                    value="177000000000",
                                    color='#666666',
                                    size=12,
                                    weight="w400"
                                )
                            ],
                            alignment="spaceBetween",
                        ),
                        padding=padding.symmetric(19, 15)
                    ),
                    Divider(
                        height=5,
                        thickness=5,
                        color='#F5F5F5'
                    ),
                    Container(
                        content=Row(
                            [
                                Text(
                                    "请提供法人证件照",
                                    color='#000018',
                                    size=14,
                                    weight="w400"
                                ),
                                Text(
                                    "身份证",
                                    color='#666666',
                                    size=14,
                                    weight="w400"
                                )
                            ],
                            alignment="spaceBetween",
                        ),
                        padding=padding.symmetric(horizontal=15, vertical=10)
                    ),
                    Container(
                        content=Row(
                            [
                                Column(
                                    [
                                        Image(
                                            src=f"/images/icon_sfz_zm.png",

                                        ),
                                        Text(
                                            "正面",
                                            weight="w400",
                                            color='#000018'
                                        )
                                    ],
                                    horizontal_alignment="center"
                                ),
                                Column(
                                    [
                                        Image(
                                            src=f"/images/icon_sfz_fm.png",

                                        ),
                                        Text(
                                            "反面",
                                            weight="w400",
                                            color='#000018'
                                        )
                                    ],
                                    horizontal_alignment="center"
                                )
                            ],
                            alignment="spaceEvenly"
                        ),
                        padding=padding.symmetric(horizontal=15, vertical=14),
                    ),
                    Container(
                        content=Divider(
                            height=0.5,
                            thickness=0.5
                        ),
                        padding=padding.symmetric(horizontal=20)
                    ),
                    Container(
                        content=Row(
                            [
                                Text(
                                    "证件号",
                                    weight="w400",
                                    color='#000018',
                                    size=14
                                ),
                                TextField(
                                    text_align="end",
                                    border="none",
                                    hint_text="身份证号",
                                    hint_style=TextStyle(12, "w400", color='#999999'),
                                    expand=True
                                )
                            ],
                            alignment="spaceBetween",
                        ),
                        padding=padding.symmetric(horizontal=20)
                    ),
                    Container(
                        content=Divider(
                            height=0.5,
                            thickness=0.5
                        ),
                        padding=padding.symmetric(horizontal=20)
                    ),
                    Container(
                        content=Row(
                            [
                                Text(
                                    "证件姓名",
                                    weight="w400",
                                    color='#000018',
                                    size=14
                                ),
                                TextField(
                                    text_align="end",
                                    border="none",
                                    hint_text="身份证姓名",
                                    hint_style=TextStyle(12, "w400", color='#999999'),
                                    expand=True
                                )
                            ],
                            alignment="spaceBetween",
                        ),
                        padding=padding.symmetric(horizontal=20)
                    ),
                    Container(
                        content=Divider(
                            height=0.5,
                            thickness=0.5
                        ),
                        padding=padding.symmetric(horizontal=20)
                    ),
                    Container(
                        content=Row(
                            [
                                Text(
                                    "身份证地址",
                                    weight="w400",
                                    color='#000018',
                                    size=14
                                ),
                                TextField(
                                    text_align="end",
                                    border="none",
                                    hint_text="地址",
                                    hint_style=TextStyle(12, "w400", color='#999999'),
                                    expand=True
                                )
                            ],
                            alignment="spaceBetween",
                        ),
                        padding=padding.symmetric(horizontal=20)
                    ),
                    Container(
                        content=Divider(
                            height=0.5,
                            thickness=0.5
                        ),
                        padding=padding.symmetric(horizontal=20)
                    )
                ],
                alignment="spaceBetween",
            ),
            Container(
                content=Column(
                    [
                        Row(
                            [
                                Checkbox(
                                    width=14,
                                    height=14,
                                    value=False,
                                ),
                                Text(
                                    "勾选即代表您同意",
                                    color='#000018',
                                    size=12,
                                    weight="w400"
                                ),
                                Text(
                                    "《服务协议》",
                                    color='#1777FE',
                                    size=12,
                                    weight="w400"
                                )
                            ],
                            alignment="center"
                        ),
                        Container(
                            Row(
                                [
                                    ElevatedButton(
                                        "提交",
                                        bgcolor='#1777FE',
                                        color='#FFFFFF',
                                        expand=True,
                                        on_click=lambda e: print("提交"),
                                        style=ButtonStyle(padding=padding.symmetric(vertical=13))
                                    )
                                ]
                            ),
                            margin=margin.symmetric(horizontal=20)
                        )

                    ],
                    spacing=13
                ),
                margin=margin.only(bottom=20)
            )
        ],
        alignment="spaceBetween",
        expand=True
    )

    page.add(
        m_column
    )


flet.app(target=main, assets_dir="assets")
