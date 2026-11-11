import os
import math
from PIL import Image, ImageDraw

output_dir = r"C:\Users\Jafet_BaGo\Desktop\TestMCP\Assets\_Game\Sprites"
os.makedirs(output_dir, exist_ok=True)

# 1. Firefly (32x32)
def generate_firefly():
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Wings (translucent cyan/white)
    # Left wing
    draw.polygon([(16, 14), (8, 6), (13, 5), (18, 12)], fill=(200, 245, 255, 180))
    # Right wing
    draw.polygon([(16, 14), (24, 6), (19, 5), (14, 12)], fill=(200, 245, 255, 180))

    # Dark body thorax & head
    draw.ellipse([(13, 10), (19, 16)], fill=(45, 35, 45, 255))
    draw.ellipse([(14, 7), (18, 11)], fill=(30, 20, 30, 255))

    # Antennae
    draw.line([(15, 7), (12, 3)], fill=(45, 35, 45, 255), width=1)
    draw.line([(17, 7), (20, 3)], fill=(45, 35, 45, 255), width=1)

    # Eyes
    draw.point([(15, 8), (17, 8)], fill=(120, 255, 200, 255))

    # Glowing lantern abdomen (the light bulb!)
    # Outer glow
    draw.ellipse([(11, 15), (21, 27)], fill=(255, 240, 100, 200))
    # Inner bright core
    draw.ellipse([(13, 17), (19, 25)], fill=(255, 255, 200, 255))
    draw.point([(15, 19), (16, 19), (15, 20), (16, 20)], fill=(255, 255, 255, 255))

    img.save(os.path.join(output_dir, "spr_firefly.png"))
    print("Created spr_firefly.png")

# 2. Light Crystal (32x32)
def generate_crystal():
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Outer soft halo
    draw.polygon([(16, 2), (28, 16), (16, 30), (4, 16)], fill=(100, 230, 255, 60))

    # Diamond crystal main
    draw.polygon([(16, 4), (26, 16), (16, 28), (6, 16)], fill=(0, 190, 240, 255))
    # Inner facets
    draw.polygon([(16, 4), (16, 28), (6, 16)], fill=(0, 150, 210, 255))
    draw.polygon([(16, 6), (23, 16), (16, 26)], fill=(120, 230, 255, 255))
    # Highlight
    draw.polygon([(16, 6), (18, 16), (16, 22), (14, 16)], fill=(220, 255, 255, 255))

    img.save(os.path.join(output_dir, "spr_crystal.png"))
    print("Created spr_crystal.png")

# 3. Bat Enemy (32x32)
def generate_bat():
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Wings spread
    # Left wing
    draw.polygon([(14, 16), (3, 8), (5, 18), (9, 21), (13, 19)], fill=(40, 30, 48, 255))
    draw.polygon([(5, 18), (1, 14), (3, 8)], fill=(60, 45, 75, 255))
    # Right wing
    draw.polygon([(18, 16), (29, 8), (27, 18), (23, 21), (19, 19)], fill=(40, 30, 48, 255))
    draw.polygon([(27, 18), (31, 14), (29, 8)], fill=(60, 45, 75, 255))

    # Body
    draw.ellipse([(12, 12), (20, 23)], fill=(30, 22, 38, 255))
    # Head & ears
    draw.ellipse([(13, 9), (19, 15)], fill=(35, 25, 45, 255))
    draw.polygon([(13, 10), (12, 6), (15, 9)], fill=(45, 30, 55, 255))
    draw.polygon([(17, 9), (20, 6), (19, 10)], fill=(45, 30, 55, 255))

    # Glowing predatory red eyes
    draw.point([(15, 12), (17, 12)], fill=(255, 50, 70, 255))
    # Tiny fangs
    draw.point([(15, 15), (17, 15)], fill=(240, 240, 255, 255))

    img.save(os.path.join(output_dir, "spr_bat.png"))
    print("Created spr_bat.png")

# 4. Spikes (32x32)
def generate_spikes():
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 3 sharp spikes / stalagmites
    # Middle spike (tallest)
    draw.polygon([(16, 4), (11, 31), (21, 31)], fill=(80, 85, 95, 255))
    draw.polygon([(16, 4), (16, 31), (21, 31)], fill=(55, 60, 70, 255))
    draw.line([(16, 4), (16, 31)], fill=(120, 130, 145, 255))

    # Left spike
    draw.polygon([(8, 12), (3, 31), (13, 31)], fill=(75, 80, 90, 255))
    draw.polygon([(8, 12), (8, 31), (13, 31)], fill=(50, 55, 65, 255))

    # Right spike
    draw.polygon([(24, 10), (19, 31), (29, 31)], fill=(85, 90, 100, 255))
    draw.polygon([(24, 10), (24, 31), (29, 31)], fill=(55, 60, 70, 255))

    img.save(os.path.join(output_dir, "spr_spikes.png"))
    print("Created spr_spikes.png")

# 5. Platform Tile (48x16)
def generate_platform():
    img = Image.new("RGBA", (48, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Base stone slab
    draw.rounded_rectangle([(0, 0), (47, 15)], radius=3, fill=(35, 40, 50, 255), outline=(60, 70, 85, 255))
    # Top highlight / grass-moss layer
    draw.line([(2, 1), (45, 1)], fill=(80, 130, 120, 255))
    draw.line([(2, 2), (45, 2)], fill=(50, 90, 80, 255))
    # Stone texture cracks
    draw.line([(14, 5), (18, 9)], fill=(25, 28, 35, 255))
    draw.line([(32, 7), (36, 12)], fill=(25, 28, 35, 255))

    img.save(os.path.join(output_dir, "spr_platform.png"))
    print("Created spr_platform.png")

# 6. Exit Portal / Altar (48x48)
def generate_portal():
    img = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Stone arch pillars
    draw.rectangle([(6, 16), (12, 47)], fill=(45, 50, 60, 255), outline=(70, 78, 92, 255))
    draw.rectangle([(36, 16), (42, 47)], fill=(45, 50, 60, 255), outline=(70, 78, 92, 255))
    # Top arch
    draw.ellipse([(8, 4), (40, 24)], fill=(45, 50, 60, 255), outline=(70, 78, 92, 255))

    # Inner swirling magical portal void / light
    draw.ellipse([(14, 10), (34, 45)], fill=(20, 60, 75, 230))
    draw.ellipse([(17, 15), (31, 40)], fill=(40, 140, 170, 240))
    draw.ellipse([(20, 20), (28, 35)], fill=(120, 235, 255, 255))
    draw.ellipse([(22, 24), (26, 31)], fill=(255, 255, 255, 255))

    img.save(os.path.join(output_dir, "spr_portal.png"))
    print("Created spr_portal.png")

# 7. Light Radial Texture (128x128)
def generate_radial_light():
    img = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    center = 64.0
    max_r = 62.0
    for y in range(128):
        for x in range(128):
            dx = x - center
            dy = y - center
            dist = math.sqrt(dx*dx + dy*dy)
            if dist <= max_r:
                factor = 1.0 - (dist / max_r)
                alpha = int(255 * (factor ** 2.2))
                img.putpixel((x, y), (255, 255, 255, alpha))
            else:
                img.putpixel((x, y), (0, 0, 0, 0))
    img.save(os.path.join(output_dir, "spr_light_circle.png"))
    print("Created spr_light_circle.png")

# 8. UI Elements
def generate_ui():
    # Light Bar BG (128x16)
    bg = Image.new("RGBA", (128, 16), (0, 0, 0, 0))
    d_bg = ImageDraw.Draw(bg)
    d_bg.rounded_rectangle([(0, 0), (127, 15)], radius=4, fill=(18, 20, 26, 230), outline=(60, 68, 80, 255), width=2)
    bg.save(os.path.join(output_dir, "spr_ui_bar_bg.png"))

    # Light Bar Fill (128x16)
    fill = Image.new("RGBA", (128, 16), (0, 0, 0, 0))
    d_fill = ImageDraw.Draw(fill)
    d_fill.rounded_rectangle([(2, 2), (125, 13)], radius=3, fill=(255, 220, 60, 255))
    d_fill.line([(4, 4), (123, 4)], fill=(255, 255, 180, 255))
    fill.save(os.path.join(output_dir, "spr_ui_bar_fill.png"))

    # UI Crystal Icon (24x24)
    c_icon = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    d_c = ImageDraw.Draw(c_icon)
    d_c.polygon([(12, 2), (21, 12), (12, 22), (3, 12)], fill=(0, 210, 255, 255), outline=(200, 255, 255, 255))
    d_c.polygon([(12, 5), (17, 12), (12, 19), (7, 12)], fill=(120, 240, 255, 255))
    c_icon.save(os.path.join(output_dir, "spr_ui_crystal.png"))
    print("Created UI sprites")

generate_firefly()
generate_crystal()
generate_bat()
generate_spikes()
generate_platform()
generate_portal()
generate_radial_light()
generate_ui()
