#!/usr/bin/env python3
"""
Dynamic Anti-Aliased Favicon Generator for AERO-SHED / SATTAL-PITCH
Draws a high-fidelity modern structural truss icon using Pillow and saves as multi-resolution .ico.
"""

import os
from PIL import Image, ImageDraw

def generate_favicon():
    # Draw high-res canvas (256x256) for crisp anti-aliasing
    size = 256
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0)) # transparent background
    draw = ImageDraw.Draw(img)

    # Color Palette: Neon Cyan (#00f2fe) to Electric Blue (#4facfe)
    cyan = (0, 242, 254, 255)
    blue = (79, 172, 254, 255)

    # Dimensions for high-res drawing
    margin_bottom = 200
    margin_left = 32
    margin_right = 224
    apex_y = 56
    apex_x = 128
    
    # Bottom Chord (horizontal tie)
    # Draw thick horizontal structural member
    draw.line([(margin_left, margin_bottom), (margin_right, margin_bottom)], fill=blue, width=16)
    
    # Left Rafter
    draw.line([(margin_left, margin_bottom), (apex_x, apex_y)], fill=cyan, width=16)
    
    # Right Rafter
    draw.line([(margin_right, margin_bottom), (apex_x, apex_y)], fill=cyan, width=16)
    
    # Vertical King Post
    draw.line([(apex_x, apex_y), (apex_x, margin_bottom)], fill=cyan, width=12)
    
    # Web Diagonals
    mid_left_x = (margin_left + apex_x) // 2
    mid_left_y = (margin_bottom + apex_y) // 2
    mid_right_x = (margin_right + apex_x) // 2
    mid_right_y = (margin_bottom + apex_y) // 2
    
    draw.line([(apex_x, margin_bottom), (mid_left_x, mid_left_y)], fill=blue, width=10)
    draw.line([(apex_x, margin_bottom), (mid_right_x, mid_right_y)], fill=blue, width=10)

    # Draw structural joints (nodes) as rounded caps
    node_radius = 12
    draw.ellipse([margin_left - node_radius, margin_bottom - node_radius, margin_left + node_radius, margin_bottom + node_radius], fill=blue)
    draw.ellipse([margin_right - node_radius, margin_bottom - node_radius, margin_right + node_radius, margin_bottom + node_radius], fill=blue)
    draw.ellipse([apex_x - node_radius, apex_y - node_radius, apex_x + node_radius, apex_y + node_radius], fill=cyan)
    draw.ellipse([apex_x - node_radius, margin_bottom - node_radius, apex_x + node_radius, margin_bottom + node_radius], fill=blue)

    # Output paths
    base_dir = r"C:\Users\rhlbh\.gemini\antigravity\scratch\sattal-pitch"
    
    # Resize down using high-quality LANCZOS interpolation
    img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    img_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    img_48 = img.resize((48, 48), Image.Resampling.LANCZOS)
    
    # Save as multi-resolution ICO file at the root
    ico_path = os.path.join(base_dir, "favicon.ico")
    img_32.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    
    # Also save a high-res PNG for modern browsers
    png_path = os.path.join(base_dir, "favicon.png")
    img.resize((192, 192), Image.Resampling.LANCZOS).save(png_path, "PNG")

    # Copy files inside the shed-design subfolder too
    shed_dir = os.path.join(base_dir, "shed-design")
    if os.path.exists(shed_dir):
        img_32.save(os.path.join(shed_dir, "favicon.ico"), format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
        img.resize((192, 192), Image.Resampling.LANCZOS).save(os.path.join(shed_dir, "favicon.png"), "PNG")
        
    print("======================================================================")
    print(" GORGEOUS MULTI-RESOLUTION FAVICON GENERATED ")
    print("======================================================================")
    print(f"  - Root Favicon (ICO)  : {ico_path}")
    print(f"  - High-res PNG (192px): {png_path}")
    print(f"  - Copied to subfolder : {os.path.join(shed_dir, 'favicon.ico')}")
    print("======================================================================")

if __name__ == '__main__':
    generate_favicon()
