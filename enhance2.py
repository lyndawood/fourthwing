#!/usr/bin/env python3

with open('index.html', 'r') as f:
    content = f.read()

# Find the ornament section and enhance it with decorative elements
old_ornament = """  .ornament {
    margin: 1.9rem auto 0; width: min(360px, 70%); height: 1px;
    background: linear-gradient(90deg, transparent, var(--edge-str) 20%, var(--amber) 50%, var(--edge-str) 80%, transparent);
    position: relative;
  }
  .ornament .gem { display: none; }"""

new_ornament = """  .ornament {
    margin: 1.9rem auto 0; width: min(360px, 70%); height: 2px;
    background: linear-gradient(90deg, transparent, var(--edge-str) 20%, var(--amber) 50%, var(--edge-str) 80%, transparent);
    position: relative;
    box-shadow: 0 0 20px rgba(212,175,55,.3), 0 0 40px rgba(212,175,55,.1);
  }
  .ornament .gem { 
    display: block;
    position: absolute;
    width: 8px;
    height: 8px;
    background: var(--amber-b);
    border-radius: 50%;
    top: 50%;
    transform: translateY(-50%);
    box-shadow: 0 0 12px rgba(227,182,98,.8);
  }
  .ornament .gem:nth-child(1) { left: 15%; }
  .ornament .gem:nth-child(2) { left: 50%; transform: translateX(-50%) translateY(-50%); }
  .ornament .gem:nth-child(3) { right: 15%; }"""

content = content.replace(old_ornament, new_ornament)

# Enhance book-head styling
old_book_head = """  .book-head { display: flex; align-items: baseline; gap: 1.2rem; flex-wrap: wrap; border-bottom: 1px solid var(--edge); padding-bottom: 1rem; }"""

new_book_head = """  .book-head { 
    display: flex; 
    align-items: baseline; 
    gap: 1.2rem; 
    flex-wrap: wrap; 
    border-bottom: 2px solid var(--edge); 
    padding-bottom: 1rem;
    position: relative;
  }
  .book-head::after {
    content: "";
    position: absolute;
    bottom: -2px;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--amber) 20%, var(--amber) 80%, transparent);
    opacity: 0.6;
  }"""

content = content.replace(old_book_head, new_book_head)

# Enhance modal styling
old_modal = """  .modal {
    background: linear-gradient(172deg, #141821, #080a0e);
    border: 1px solid var(--edge-str); border-radius: 4px;
    max-width: 640px; width: 100%; padding: 2rem 1.9rem 2.1rem; position: relative;
    box-shadow: 0 28px 80px rgba(0,0,0,.85);
  }"""

new_modal = """  .modal {
    background: linear-gradient(172deg, #141821, #080a0e);
    border: 2px solid var(--edge-str); border-radius: 4px;
    max-width: 640px; width: 100%; padding: 2rem 1.9rem 2.1rem; position: relative;
    box-shadow: 0 28px 80px rgba(0,0,0,.85), 0 0 40px rgba(212,175,55,.15), inset 0 0 30px rgba(212,175,55,.05);
  }"""

content = content.replace(old_modal, new_modal)

# Add dragon scale pattern to controls
old_controls = """  .controls {
    position: sticky; top: var(--navh); z-index: 50;
    background: rgba(6,8,11,.97);
    border-top: 1px solid var(--edge); border-bottom: 1px solid var(--edge);
    padding: .95rem 1rem .85rem;
  }"""

new_controls = """  .controls {
    position: sticky; top: var(--navh); z-index: 50;
    background: rgba(6,8,11,.97);
    border-top: 1px solid var(--edge); 
    border-bottom: 2px solid var(--edge);
    padding: .95rem 1rem .85rem;
    box-shadow: 0 4px 12px rgba(0,0,0,.5), inset 0 1px 0 rgba(212,175,55,.1);
  }"""

content = content.replace(old_controls, new_controls)

# Enhance search and select focus states
old_search_focus = """  #search:focus { border-color: var(--amber); }"""
new_search_focus = """  #search:focus { 
    border-color: var(--amber); 
    box-shadow: 0 0 12px rgba(192,138,46,.3), inset 0 0 8px rgba(192,138,46,.1);
  }"""

content = content.replace(old_search_focus, new_search_focus)

old_select_focus = """  select#progress:focus { border-color: var(--amber); }"""
new_select_focus = """  select#progress:focus { 
    border-color: var(--amber); 
    box-shadow: 0 0 12px rgba(192,138,46,.3), inset 0 0 8px rgba(192,138,46,.1);
  }"""

content = content.replace(old_select_focus, new_select_focus)

# Add more dramatic book-synopsis styling
old_synopsis = """  .book-synopsis { max-width:72ch; margin:0 0 2rem; text-align:left; border:1px solid var(--edge); border-radius:3px; background:rgba(190,202,218,.025); overflow:hidden; }"""

new_synopsis = """  .book-synopsis { 
    max-width:72ch; 
    margin:0 0 2rem; 
    text-align:left; 
    border:1px solid var(--edge); 
    border-radius:3px; 
    background:rgba(190,202,218,.025); 
    overflow:hidden;
    transition: border-color .3s, box-shadow .3s;
  }
  .book-synopsis:hover {
    border-color: var(--amber);
    box-shadow: 0 0 20px rgba(192,138,46,.15), inset 0 0 15px rgba(192,138,46,.05);
  }"""

content = content.replace(old_synopsis, new_synopsis)

with open('index.html', 'w') as f:
    f.write(content)

print("✨ Added more fantasy decorative elements!")
