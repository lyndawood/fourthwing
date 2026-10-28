#!/usr/bin/env python3
import re

with open('index.html', 'r') as f:
    content = f.read()

# Find the :root section and enhance it
old_root = """  :root {
    --navh: 0px;
    --bg: #07080a;
    --panel: #11141a;
    --panel2: #0a0c10;
    --edge: rgba(190,202,218,.11);
    --edge-str: rgba(190,202,218,.26);
    --stone: #8d98a8;
    --bone: #e2dccf;
    --bone-dim: #a9a394;
    --amber: #c08a2e;
    --amber-b: #e3b662;
    --steel: #7d91a6;
    --ink: #dce2ea;
    --muted: #767f8c;
    --display: 'Cinzel', Georgia, serif;
    --body: 'Spectral', Georgia, serif;
    --label: 'Marcellus SC', Georgia, serif;
    font-size: 16px;
  }"""

new_root = """  :root {
    --navh: 0px;
    --bg: #07080a;
    --panel: #11141a;
    --panel2: #0a0c10;
    --edge: rgba(190,202,218,.11);
    --edge-str: rgba(190,202,218,.26);
    --stone: #8d98a8;
    --bone: #e2dccf;
    --bone-dim: #a9a394;
    --amber: #c08a2e;
    --amber-b: #e3b662;
    --steel: #7d91a6;
    --ink: #dce2ea;
    --muted: #767f8c;
    --crimson: #8b1a1a;
    --gold: #d4af37;
    --dragon-purple: #4a1a6f;
    --display: 'Cinzel', Georgia, serif;
    --body: 'Spectral', Georgia, serif;
    --label: 'Marcellus SC', Georgia, serif;
    font-size: 16px;
  }"""

content = content.replace(old_root, new_root)

# Enhance header styling with glow animation
old_header_h1 = """  header h1 {
    font-family: var(--display); font-weight: 700;
    font-size: clamp(2.3rem, 7vw, 4.4rem);
    letter-spacing: .13em; text-transform: uppercase;
    color: var(--bone); line-height: 1.05;
    text-shadow: 0 2px 30px rgba(0,0,0,.9), 0 0 48px rgba(170,185,205,.14);
  }"""

new_header_h1 = """  header h1 {
    font-family: var(--display); font-weight: 700;
    font-size: clamp(2.3rem, 7vw, 4.4rem);
    letter-spacing: .13em; text-transform: uppercase;
    color: var(--bone); line-height: 1.05;
    text-shadow: 0 2px 30px rgba(0,0,0,.9), 0 0 48px rgba(170,185,205,.14), 0 0 80px rgba(212,175,55,.2);
    animation: glow-pulse 3s ease-in-out infinite;
  }
  @keyframes glow-pulse {
    0%, 100% { text-shadow: 0 2px 30px rgba(0,0,0,.9), 0 0 48px rgba(170,185,205,.14), 0 0 80px rgba(212,175,55,.2); }
    50% { text-shadow: 0 2px 30px rgba(0,0,0,.9), 0 0 48px rgba(170,185,205,.14), 0 0 120px rgba(212,175,55,.35); }
  }"""

content = content.replace(old_header_h1, new_header_h1)

# Enhance card styling with more dramatic effects
old_card = """  .card {
    position: relative;
    background: linear-gradient(170deg, var(--panel), var(--panel2));
    border: 1px solid var(--edge); border-radius: 3px;
    padding: 2rem 1rem 1.5rem; text-align: center; cursor: pointer;
    transition: transform .18s, border-color .25s, box-shadow .25s;
  }
  .card::after { content: ""; position: absolute; top: 0; left: 0; width: 15px; height: 15px; border-top: 1px solid var(--amber); border-left: 1px solid var(--amber); opacity: .35; transition: opacity .25s; }
  .card:hover { transform: translateY(-4px); border-color: var(--edge-str); box-shadow: 0 18px 44px rgba(0,0,0,.7), 0 0 20px rgba(192,138,46,.1); }
  .card:hover::after { opacity: 1; }"""

new_card = """  .card {
    position: relative;
    background: linear-gradient(170deg, var(--panel), var(--panel2));
    border: 1px solid var(--edge); border-radius: 3px;
    padding: 2rem 1rem 1.5rem; text-align: center; cursor: pointer;
    transition: transform .18s, border-color .25s, box-shadow .25s, background .3s;
    overflow: hidden;
  }
  .card::before {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 0%, rgba(212,175,55,.1), transparent 70%);
    opacity: 0;
    transition: opacity .3s;
    pointer-events: none;
  }
  .card::after { content: ""; position: absolute; top: 0; left: 0; width: 15px; height: 15px; border-top: 1px solid var(--amber); border-left: 1px solid var(--amber); opacity: .35; transition: opacity .25s; }
  .card:hover { transform: translateY(-6px); border-color: var(--amber-b); box-shadow: 0 18px 44px rgba(0,0,0,.7), 0 0 30px rgba(212,175,55,.25), inset 0 0 20px rgba(212,175,55,.08); }
  .card:hover::before { opacity: 1; }
  .card:hover::after { opacity: 1; }"""

content = content.replace(old_card, new_card)

# Enhance pic-wrap with dragon scale effect
old_pic_wrap = """  .pic-wrap { display: block; width: fit-content; margin: 0 auto 1.15rem; position: relative; }
  .pic-wrap::before { content: ""; position: absolute; inset: -7px; border-radius: 50%; border: 1px solid rgba(192,138,46,.22); transition: border-color .25s; }
  .card:hover .pic-wrap::before { border-color: rgba(227,182,98,.6); }"""

new_pic_wrap = """  .pic-wrap { display: block; width: fit-content; margin: 0 auto 1.15rem; position: relative; }
  .pic-wrap::before { 
    content: ""; 
    position: absolute; 
    inset: -7px; 
    border-radius: 50%; 
    border: 2px solid rgba(192,138,46,.22); 
    transition: border-color .25s, box-shadow .25s;
    box-shadow: 0 0 0 1px rgba(212,175,55,.1);
  }
  .card:hover .pic-wrap::before { 
    border-color: rgba(227,182,98,.8); 
    box-shadow: 0 0 20px rgba(212,175,55,.4), inset 0 0 15px rgba(212,175,55,.15);
  }"""

content = content.replace(old_pic_wrap, new_pic_wrap)

with open('index.html', 'w') as f:
    f.write(content)

print("✨ Enhanced fantasy styling applied!")
