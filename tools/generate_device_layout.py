from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "images"
PNG_OUT = OUT_DIR / "device-layout-sketch.png"
SVG_OUT = OUT_DIR / "device-layout-sketch.svg"
FRONT_OUT = OUT_DIR / "device-layout-front-sketch.png"
LEFT_OUT = OUT_DIR / "device-layout-left-sketch.png"
BACK_OUT = OUT_DIR / "device-layout-back-sketch.png"
PNG_OUT_EN = OUT_DIR / "device-layout-sketch-en.png"
SVG_OUT_EN = OUT_DIR / "device-layout-sketch-en.svg"
FRONT_OUT_EN = OUT_DIR / "device-layout-front-sketch-en.png"
LEFT_OUT_EN = OUT_DIR / "device-layout-left-sketch-en.png"
BACK_OUT_EN = OUT_DIR / "device-layout-back-sketch-en.png"

WIDTH = 1600
HEIGHT = 2500
SCALE = 2

INK = "#555555"
LIGHT_INK = "#8d8d8d"
DASH = "#aaaaaa"
FILL = "#fbfbfb"
BLACK = "#222222"
WHITE = "#ffffff"

LABELS_ZH = {
    "title": "设备布局",
    "front_view": "正面视图",
    "left_view": "左侧视图",
    "back_view": "背面视图",
    "screen_line1": "2.8 寸 TFT",
    "screen_line2": "触摸屏",
    "screen_label": "2.8 寸 TFT 触摸屏",
    "main_mic": "主 mic（5孔）",
    "secondary_mic": "副 mic（5孔）",
    "rgb": "RGB",
    "power_button": ["电源按键"],
    "boot_button": ["BOOT 按键"],
    "custom_button": ["用户自定义", "按键"],
    "usb": "USB Type-C 接口",
    "sd": "SD 卡槽",
    "camera": "GC0308 摄像头",
    "speaker": "扬声器孔位",
}

LABELS_EN = {
    "title": "Device Layout",
    "front_view": "Front View",
    "left_view": "Left View",
    "back_view": "Back View",
    "screen_line1": '2.8" TFT',
    "screen_line2": "Touchscreen",
    "screen_label": '2.8" TFT Touchscreen',
    "main_mic": "Primary mic (5 holes)",
    "secondary_mic": "Secondary mic (5 holes)",
    "rgb": "RGB",
    "power_button": ["Power", "Button"],
    "boot_button": ["BOOT", "Button"],
    "custom_button": ["User-defined", "Button"],
    "usb": "USB Type-C Port",
    "sd": "SD Card Slot",
    "camera": "GC0308 Camera",
    "speaker": "Speaker Holes",
}


def font_path() -> str:
    candidates = [
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("C:/Windows/Fonts/simsun.ttc"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return ""


FONT_PATH = font_path()


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if FONT_PATH:
        return ImageFont.truetype(FONT_PATH, size * SCALE)
    return ImageFont.load_default()


def s(value: float) -> int:
    return int(round(value * SCALE))


def box(coords: tuple[float, float, float, float]) -> tuple[int, int, int, int]:
    return tuple(s(v) for v in coords)


def point(coords: tuple[float, float]) -> tuple[int, int]:
    return s(coords[0]), s(coords[1])


def draw_dashed_line(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    fill: str = DASH,
    width: int = 2,
    dash: int = 12,
    gap: int = 10,
) -> None:
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    length = (dx * dx + dy * dy) ** 0.5
    if length == 0:
        return
    ux = dx / length
    uy = dy / length
    pos = 0.0
    while pos < length:
        seg_end = min(pos + dash, length)
        p1 = (x1 + ux * pos, y1 + uy * pos)
        p2 = (x1 + ux * seg_end, y1 + uy * seg_end)
        draw.line([point(p1), point(p2)], fill=fill, width=s(width))
        pos += dash + gap


def draw_poly_dashed(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[float, float]],
    fill: str = DASH,
    width: int = 2,
) -> None:
    for first, second in zip(points, points[1:]):
        draw_dashed_line(draw, first, second, fill=fill, width=width)


def text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    value: str,
    size: int = 34,
    fill: str = INK,
    anchor: str = "lm",
) -> None:
    draw.text(point(xy), value, font=load_font(size), fill=fill, anchor=anchor)


def label_left(
    draw: ImageDraw.ImageDraw,
    y: float,
    value: str,
    target: tuple[float, float],
    x_text: float = 95,
    x_line: float = 520,
) -> None:
    text(draw, (x_text, y), value, 34, LIGHT_INK, "lm")
    draw_poly_dashed(draw, [(x_line, y), (target[0] - 18, y), target])


def label_right(
    draw: ImageDraw.ImageDraw,
    y: float,
    value: str,
    target: tuple[float, float],
    x_text: float = 1505,
    x_line: float = 1265,
) -> None:
    text(draw, (x_text, y), value, 34, LIGHT_INK, "rm")
    draw_poly_dashed(draw, [(x_line, y), (target[0] + 18, y), target])


def button_label(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    label_xy: tuple[float, float],
    lines: list[str],
) -> None:
    line_end = (label_xy[0], label_xy[1] - 36)
    draw_poly_dashed(draw, [start, line_end])
    for index, line in enumerate(lines):
        text(draw, (label_xy[0], label_xy[1] + index * 32), line, 28, LIGHT_INK, "mm")


def rounded(
    draw: ImageDraw.ImageDraw,
    coords: tuple[float, float, float, float],
    radius: float,
    outline: str = INK,
    fill: str = FILL,
    width: int = 4,
) -> None:
    draw.rounded_rectangle(box(coords), radius=s(radius), outline=outline, fill=fill, width=s(width))


def circle(
    draw: ImageDraw.ImageDraw,
    center: tuple[float, float],
    radius: float,
    outline: str = INK,
    fill: str | None = WHITE,
    width: int = 3,
) -> None:
    x, y = center
    draw.ellipse(box((x - radius, y - radius, x + radius, y + radius)), outline=outline, fill=fill, width=s(width))


def filled_circle(draw: ImageDraw.ImageDraw, center: tuple[float, float], radius: float, fill: str = BLACK) -> None:
    x, y = center
    draw.ellipse(box((x - radius, y - radius, x + radius, y + radius)), fill=fill)


def mic_cluster(draw: ImageDraw.ImageDraw, center: tuple[float, float]) -> None:
    cx, cy = center
    for dx, dy in [(0, 0), (-26, 0), (26, 0), (0, -26), (0, 26)]:
        filled_circle(draw, (cx + dx, cy + dy), 10)


def draw_front(draw: ImageDraw.ImageDraw, labels: dict[str, str | list[str]]) -> None:
    text(draw, (800, 155), str(labels["front_view"]), 30, INK, "mm")
    rounded(draw, (405, 195, 1195, 820), 70, width=5)
    rounded(draw, (535, 300, 1065, 620), 10, outline=BLACK, fill=WHITE, width=6)
    rounded(draw, (565, 330, 1035, 590), 4, outline="#777777", fill="#f6f6f6", width=2)
    text(draw, (800, 460), str(labels["screen_line1"]), 42, "#777777", "mm")
    text(draw, (800, 510), str(labels["screen_line2"]), 38, "#777777", "mm")

    mic_cluster(draw, (565, 715))
    mic_cluster(draw, (1035, 715))
    filled_circle(draw, (1135, 715), 8, BLACK)
    circle(draw, (1135, 715), 15, outline="#777777", fill=None, width=2)

    for cx in (695, 800, 905):
        circle(draw, (cx, 730), 32, outline=INK, fill=WHITE, width=4)
        filled_circle(draw, (cx, 730), 24, BLACK)

    label_left(draw, 430, str(labels["screen_label"]), (535, 430))
    label_left(draw, 715, str(labels["main_mic"]), (565, 715))
    button_label(draw, (695, 766), (655, 875), list(labels["power_button"]))
    button_label(draw, (800, 766), (800, 875), list(labels["boot_button"]))
    button_label(draw, (905, 766), (960, 860), list(labels["custom_button"]))

    label_right(draw, 650, str(labels["rgb"]), (1135, 715))
    label_right(draw, 760, str(labels["secondary_mic"]), (1035, 715), x_line=1065)


def draw_left_side(draw: ImageDraw.ImageDraw, labels: dict[str, str | list[str]]) -> None:
    offset = 175
    text(draw, (800, 925 + offset), str(labels["left_view"]), 30, INK, "mm")
    rounded(draw, (690, 980 + offset, 910, 1505 + offset), 38, width=5)
    draw.line(
        [
            point((690, 1010 + offset)),
            point((650, 1055 + offset)),
            point((650, 1430 + offset)),
            point((690, 1480 + offset)),
        ],
        fill=INK,
        width=s(4),
    )
    draw.line([point((715, 1015 + offset)), point((715, 1470 + offset))], fill="#cfcfcf", width=s(2))

    rounded(draw, (764, 1070 + offset, 836, 1190 + offset), 24, outline=BLACK, fill=WHITE, width=5)
    rounded(draw, (788, 1100 + offset, 812, 1160 + offset), 9, outline="#777777", fill="#eeeeee", width=2)
    filled_circle(draw, (800, 1280 + offset), 10, BLACK)
    rounded(draw, (756, 1370 + offset, 844, 1482 + offset), 14, outline=BLACK, fill=WHITE, width=5)
    rounded(draw, (775, 1395 + offset, 825, 1456 + offset), 8, outline="#777777", fill="#eeeeee", width=2)

    label_right(draw, 1128 + offset, str(labels["usb"]), (836, 1130 + offset), x_line=1095)
    label_right(draw, 1425 + offset, str(labels["sd"]), (844, 1425 + offset), x_line=1095)


def speaker_grid(draw: ImageDraw.ImageDraw) -> None:
    origin_x = 925
    origin_y = 2100
    spacing = 38
    rows = [4, 5, 6, 6, 5, 4]
    for row, count in enumerate(rows):
        y = origin_y + row * spacing
        row_width = (count - 1) * spacing
        x0 = origin_x - row_width / 2
        for col in range(count):
            filled_circle(draw, (x0 + col * spacing, y), 8, BLACK)


def draw_back(draw: ImageDraw.ImageDraw, labels: dict[str, str | list[str]]) -> None:
    offset = 255
    text(draw, (800, 1585 + offset), str(labels["back_view"]), 30, INK, "mm")
    rounded(draw, (405, 1630 + offset, 1195, 2075 + offset), 62, width=5)
    circle(draw, (800, 1718 + offset), 40, outline=BLACK, fill=WHITE, width=5)
    circle(draw, (800, 1718 + offset), 20, outline="#555555", fill="#eeeeee", width=3)
    filled_circle(draw, (808, 1710 + offset), 6, "#777777")
    speaker_grid(draw)

    label_left(draw, 1718 + offset, str(labels["camera"]), (800, 1718 + offset))
    label_right(draw, 1940 + offset, str(labels["speaker"]), (1015, 1940 + offset))


def draw_png(
    labels: dict[str, str | list[str]],
    png_out: Path,
    front_out: Path,
    left_out: Path,
    back_out: Path,
) -> None:
    image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), WHITE)
    draw = ImageDraw.Draw(image)
    text(draw, (95, 85), str(labels["title"]), 50, BLACK, "lm")
    draw.line([point((95, 125)), point((1505, 125))], fill="#e6e6e6", width=s(2))
    draw_front(draw, labels)
    draw_left_side(draw, labels)
    draw_back(draw, labels)
    image = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    image.save(png_out)
    image.crop((0, 135, WIDTH, 1035)).save(front_out)
    image.crop((0, 1040, WIDTH, 1815)).save(left_out)
    image.crop((0, 1815, WIDTH, HEIGHT)).save(back_out)


def svg_text(x: float, y: float, value: str, size: int = 34, anchor: str = "start", fill: str = INK) -> str:
    return (
        f'<text x="{x}" y="{y}" font-family="Microsoft YaHei, SimHei, Arial, sans-serif" '
        f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" dominant-baseline="middle">{value}</text>'
    )


def svg_line(x1: float, y1: float, x2: float, y2: float, stroke: str = INK, width: int = 3, dash: bool = False) -> str:
    dash_attr = ' stroke-dasharray="12 10"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}" fill="none"{dash_attr}/>'


def svg_label_left(y: float, value: str, tx: float, ty: float, x_text: float = 95, x_line: float = 520) -> list[str]:
    return [
        svg_text(x_text, y, value, 34, "start", LIGHT_INK),
        svg_line(x_line, y, tx - 18, y, DASH, 2, True),
        svg_line(tx - 18, y, tx, ty, DASH, 2, True),
    ]


def svg_label_right(y: float, value: str, tx: float, ty: float, x_text: float = 1505, x_line: float = 1265) -> list[str]:
    return [
        svg_text(x_text, y, value, 34, "end", LIGHT_INK),
        svg_line(x_line, y, tx + 18, y, DASH, 2, True),
        svg_line(tx + 18, y, tx, ty, DASH, 2, True),
    ]


def svg_button_label(start_x: float, start_y: float, label_x: float, label_y: float, lines: list[str]) -> list[str]:
    parts = [svg_line(start_x, start_y, label_x, label_y - 36, DASH, 2, True)]
    for index, line in enumerate(lines):
        parts.append(svg_text(label_x, label_y + index * 32, line, 28, "middle", LIGHT_INK))
    return parts


def svg_mic(cx: float, cy: float) -> list[str]:
    return [
        f'<circle cx="{cx + dx}" cy="{cy + dy}" r="10" fill="{BLACK}"/>'
        for dx, dy in [(0, 0), (-26, 0), (26, 0), (0, -26), (0, 26)]
    ]


def build_svg(labels: dict[str, str | list[str]]) -> str:
    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{WHITE}"/>',
        svg_text(95, 85, str(labels["title"]), 50, "start", BLACK),
        svg_line(95, 125, 1505, 125, "#e6e6e6", 2),
        svg_text(800, 155, str(labels["front_view"]), 30, "middle", INK),
        f'<rect x="405" y="195" width="790" height="625" rx="70" fill="{FILL}" stroke="{INK}" stroke-width="5"/>',
        f'<rect x="535" y="300" width="530" height="320" rx="10" fill="{WHITE}" stroke="{BLACK}" stroke-width="6"/>',
        f'<rect x="565" y="330" width="470" height="260" rx="4" fill="#f6f6f6" stroke="#777777" stroke-width="2"/>',
        svg_text(800, 460, str(labels["screen_line1"]), 42, "middle", "#777777"),
        svg_text(800, 510, str(labels["screen_line2"]), 38, "middle", "#777777"),
    ]
    parts.extend(svg_mic(565, 715))
    parts.extend(svg_mic(1035, 715))
    parts.append(f'<circle cx="1135" cy="715" r="8" fill="{BLACK}"/>')
    parts.append(f'<circle cx="1135" cy="715" r="15" fill="none" stroke="#777777" stroke-width="2"/>')
    for cx in (695, 800, 905):
        parts.append(f'<circle cx="{cx}" cy="730" r="32" fill="{WHITE}" stroke="{INK}" stroke-width="4"/>')
        parts.append(f'<circle cx="{cx}" cy="730" r="24" fill="{BLACK}"/>')
    parts.extend(svg_label_left(430, str(labels["screen_label"]), 535, 430))
    parts.extend(svg_label_left(715, str(labels["main_mic"]), 565, 715))
    parts.extend(svg_button_label(695, 766, 655, 875, list(labels["power_button"])))
    parts.extend(svg_button_label(800, 766, 800, 875, list(labels["boot_button"])))
    parts.extend(svg_button_label(905, 766, 960, 860, list(labels["custom_button"])))
    parts.extend(svg_label_right(650, str(labels["rgb"]), 1135, 715))
    parts.extend(svg_label_right(760, str(labels["secondary_mic"]), 1035, 715, x_line=1065))

    left_offset = 175
    parts.extend(
        [
            svg_text(800, 925 + left_offset, str(labels["left_view"]), 30, "middle", INK),
            f'<rect x="690" y="{980 + left_offset}" width="220" height="525" rx="38" fill="{FILL}" stroke="{INK}" stroke-width="5"/>',
            f'<polyline points="690,{1010 + left_offset} 650,{1055 + left_offset} 650,{1430 + left_offset} 690,{1480 + left_offset}" fill="none" stroke="{INK}" stroke-width="4"/>',
            svg_line(715, 1015 + left_offset, 715, 1470 + left_offset, "#cfcfcf", 2),
            f'<rect x="764" y="{1070 + left_offset}" width="72" height="120" rx="24" fill="{WHITE}" stroke="{BLACK}" stroke-width="5"/>',
            f'<rect x="788" y="{1100 + left_offset}" width="24" height="60" rx="9" fill="#eeeeee" stroke="#777777" stroke-width="2"/>',
            f'<circle cx="800" cy="{1280 + left_offset}" r="10" fill="{BLACK}"/>',
            f'<rect x="756" y="{1370 + left_offset}" width="88" height="112" rx="14" fill="{WHITE}" stroke="{BLACK}" stroke-width="5"/>',
            f'<rect x="775" y="{1395 + left_offset}" width="50" height="61" rx="8" fill="#eeeeee" stroke="#777777" stroke-width="2"/>',
        ]
    )
    parts.extend(svg_label_right(1128 + left_offset, str(labels["usb"]), 836, 1130 + left_offset, x_line=1095))
    parts.extend(svg_label_right(1425 + left_offset, str(labels["sd"]), 844, 1425 + left_offset, x_line=1095))

    back_offset = 255
    parts.extend(
        [
            svg_text(800, 1585 + back_offset, str(labels["back_view"]), 30, "middle", INK),
            f'<rect x="405" y="{1630 + back_offset}" width="790" height="445" rx="62" fill="{FILL}" stroke="{INK}" stroke-width="5"/>',
            f'<circle cx="800" cy="{1718 + back_offset}" r="40" fill="{WHITE}" stroke="{BLACK}" stroke-width="5"/>',
            f'<circle cx="800" cy="{1718 + back_offset}" r="20" fill="#eeeeee" stroke="#555555" stroke-width="3"/>',
            f'<circle cx="808" cy="{1710 + back_offset}" r="6" fill="#777777"/>',
        ]
    )
    origin_x = 925
    origin_y = 2100
    spacing = 38
    for row, count in enumerate([4, 5, 6, 6, 5, 4]):
        y = origin_y + row * spacing
        row_width = (count - 1) * spacing
        x0 = origin_x - row_width / 2
        for col in range(count):
            parts.append(f'<circle cx="{x0 + col * spacing}" cy="{y}" r="8" fill="{BLACK}"/>')
    parts.extend(svg_label_left(1718 + back_offset, str(labels["camera"]), 800, 1718 + back_offset))
    parts.extend(svg_label_right(1940 + back_offset, str(labels["speaker"]), 1015, 1940 + back_offset))
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SVG_OUT.write_text(build_svg(LABELS_ZH), encoding="utf-8")
    draw_png(LABELS_ZH, PNG_OUT, FRONT_OUT, LEFT_OUT, BACK_OUT)
    SVG_OUT_EN.write_text(build_svg(LABELS_EN), encoding="utf-8")
    draw_png(LABELS_EN, PNG_OUT_EN, FRONT_OUT_EN, LEFT_OUT_EN, BACK_OUT_EN)
    print(f"Wrote {SVG_OUT}")
    print(f"Wrote {PNG_OUT}")
    print(f"Wrote {FRONT_OUT}")
    print(f"Wrote {LEFT_OUT}")
    print(f"Wrote {BACK_OUT}")
    print(f"Wrote {SVG_OUT_EN}")
    print(f"Wrote {PNG_OUT_EN}")
    print(f"Wrote {FRONT_OUT_EN}")
    print(f"Wrote {LEFT_OUT_EN}")
    print(f"Wrote {BACK_OUT_EN}")


if __name__ == "__main__":
    main()
