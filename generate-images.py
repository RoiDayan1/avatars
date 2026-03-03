#!/usr/bin/env python3
"""Generate avatar images for a collection using Gemini image generation.

Usage:
    python3 generate-images.py --collection vanguard
    python3 generate-images.py --collection diversefaces

No third-party packages required — uses only the Python standard library.
"""

import argparse
import base64
import importlib.util
import json
import os
import time
import urllib.request
import urllib.error
from pathlib import Path

# Load .env file if present (stdlib-only, no dotenv dependency)
_env_path = Path(__file__).parent / ".env"
if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.5-flash-image:generateContent"
)

DELAY = 1.0
RETRIES = 2


def load_collection(name: str):
    """Load a collection module from the collections/ directory."""
    path = Path(__file__).parent / "collections" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    characters = []
    for m, f in zip(mod.MALES, mod.FEMALES):
        characters.append(m)
        characters.append(f)
    return mod, characters


def generate_image(api_key: str, prompt_template: str, character: str,
                   index: int, total: int, output_dir: Path) -> bool:
    prompt = prompt_template.format(character=character)
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }).encode()

    req = urllib.request.Request(
        f"{API_URL}?key={api_key}",
        data=body,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode(errors="replace")
        print(f"[{index:3d}/{total}] HTTP {e.code}: {error_body[:200]}")
        return False
    except Exception as e:
        print(f"[{index:3d}/{total}] Error: {e}")
        return False

    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData")
            if inline and inline.get("data"):
                ext = "png" if "png" in inline.get("mimeType", "") else "jpg"
                filepath = output_dir / f"image_{index:03d}.{ext}"
                filepath.write_bytes(base64.b64decode(inline["data"]))
                print(f"[{index:3d}/{total}] Saved {filepath.name}")
                return True

    print(f"[{index:3d}/{total}] No image returned by the model")
    return False


def discover_collections(current_name: str):
    """Find all other collections and return list of (NAME, module_filename)."""
    collections_dir = Path(__file__).parent / "collections"
    others = []
    for p in sorted(collections_dir.glob("*.py")):
        if p.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(p.stem, p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        if getattr(m, "NAME", None) and m.NAME != current_name:
            others.append(m.NAME)
    return others


def generate_gallery(mod, output_dir: Path):
    """Generate index.html gallery page for a collection."""
    name = mod.NAME
    subtitle = mod.SUBTITLE
    total = len(mod.MALES) + len(mod.FEMALES)
    other_collections = discover_collections(name)

    nav_links = " ".join(
        f'<a href="../{c}/">{c}</a>' for c in other_collections
    )

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} - {subtitle}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #0a0a0a; color: #eee; font-family: system-ui, sans-serif; padding: 2rem; }}
  h1 {{ text-align: center; font-size: 2rem; margin-bottom: 0.5rem; letter-spacing: 0.1em; }}
  p.subtitle {{ text-align: center; color: #888; margin-bottom: 1rem; }}
  .github-link {{
    position: absolute;
    top: 1.5rem;
    left: 1.5rem;
  }}
  .github-link a {{
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.5rem 1rem;
    background: #2a2a2a;
    color: #eee;
    text-decoration: none;
    border-radius: 6px;
    font-size: 0.85rem;
    transition: background 0.2s;
  }}
  .github-link a:hover {{ background: #3a3a3a; }}
  .github-link svg {{ fill: #eee; }}
  .nav-links {{
    position: absolute;
    top: 1.5rem;
    right: 1.5rem;
    display: flex;
    gap: 0.5rem;
  }}
  .nav-links a {{
    display: inline-block;
    padding: 0.5rem 1rem;
    background: #2a2a2a;
    color: #eee;
    text-decoration: none;
    border-radius: 6px;
    font-size: 0.85rem;
    transition: background 0.2s;
  }}
  .nav-links a:hover {{ background: #3a3a3a; }}
  .download {{ text-align: center; margin-bottom: 2rem; }}
  .download a {{
    display: inline-block;
    padding: 0.6rem 1.5rem;
    background: #2a2a2a;
    color: #eee;
    text-decoration: none;
    border-radius: 6px;
    font-size: 0.9rem;
    transition: background 0.2s;
  }}
  .download a:hover {{ background: #3a3a3a; }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 1rem;
    max-width: 1400px;
    margin: 0 auto;
  }}
  .card {{
    position: relative;
    border-radius: 8px;
    overflow: hidden;
    background: #1a1a1a;
    transition: transform 0.2s;
  }}
  .card:hover {{ transform: scale(1.03); }}
  .card img {{
    width: 100%;
    display: block;
  }}
  .card .label {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 0.4rem;
    background: rgba(0,0,0,0.7);
    text-align: center;
    font-size: 0.8rem;
    color: #ccc;
  }}
</style>
</head>
<body>
<div class="github-link"><a href="https://github.com/RoiDayan1/avatars" ><svg width="20" height="20" viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>GitHub</a></div>
<div class="nav-links">{nav_links}</div>
<h1>{name}</h1>
<p class="subtitle">{subtitle}</p>
<div class="download"><a href="#" id="downloadBtn">Download All (ZIP)</a></div>
<div class="grid" id="grid"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
<script>
  const grid = document.getElementById('grid');
  const total = {total};
  for (let i = 1; i <= total; i++) {{
    const num = String(i).padStart(3, '0');
    const gender = i % 2 === 1 ? 'M' : 'F';
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <a href="image_${{num}}.png" >
        <img src="image_${{num}}.png" alt="Character ${{i}}" loading="lazy">
      </a>
      <div class="label">#${{i}} (${{gender}})</div>`;
    grid.appendChild(card);
  }}

  document.getElementById('downloadBtn').addEventListener('click', async (e) => {{
    e.preventDefault();
    const btn = e.target;
    const orig = btn.textContent;
    btn.textContent = `Downloading 0/${{total}}...`;
    btn.style.pointerEvents = 'none';

    const zip = new JSZip();
    for (let i = 1; i <= total; i++) {{
      const num = String(i).padStart(3, '0');
      const resp = await fetch(`image_${{num}}.png`);
      zip.file(`image_${{num}}.png`, await resp.blob());
      btn.textContent = `Downloading ${{i}}/${{total}}...`;
    }}

    btn.textContent = 'Building ZIP...';
    const blob = await zip.generateAsync({{ type: 'blob' }});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = '{name}.zip';
    a.click();
    URL.revokeObjectURL(a.href);

    btn.textContent = orig;
    btn.style.pointerEvents = '';
  }});
</script>
</body>
</html>
"""
    gallery_path = output_dir / "index.html"
    gallery_path.write_text(html)
    print(f"Gallery saved: {gallery_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate avatar images for a collection")
    parser.add_argument("--collection", required=True,
                        help="Collection module name (e.g. vanguard, diversefaces)")
    parser.add_argument("--regenerate", type=int, nargs="*", default=[],
                        help="Regenerate only specific indices (e.g. --regenerate 1 5 42)")
    parser.add_argument("--gallery-only", action="store_true",
                        help="Only regenerate the gallery HTML, skip image generation")
    args = parser.parse_args()

    mod, characters = load_collection(args.collection)
    total = len(characters)
    output_dir = Path(mod.NAME)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.gallery_only:
        generate_gallery(mod, output_dir)
        return

    api_key = os.environ["GEMINI_API_KEY"]
    indices = args.regenerate if args.regenerate else list(range(1, total + 1))

    print(f"Collection: {mod.NAME} — {mod.SUBTITLE}")
    print(f"Output:     {output_dir.resolve()}")
    print(f"Delay:      {DELAY}s between requests")
    print(f"Model:      gemini-2.5-flash-image")
    print(f"Images:     {len(indices)}" + (" (regenerating)" if args.regenerate else ""))
    print("-" * 50)

    success = 0
    failed = 0

    for idx, i in enumerate(indices):
        ok = False
        for attempt in range(1 + RETRIES):
            if attempt > 0:
                wait = 2 ** attempt
                print(f"         Retry {attempt}/{RETRIES} after {wait}s...")
                time.sleep(wait)
            ok = generate_image(api_key, mod.PROMPT_TEMPLATE, characters[i - 1],
                                i, total, output_dir)
            if ok:
                break

        if ok:
            success += 1
        else:
            failed += 1

        if idx < len(indices) - 1:
            time.sleep(DELAY)

    print("-" * 50)
    print(f"Done! {success} succeeded, {failed} failed.")
    print(f"Images saved in: {output_dir.resolve()}")

    generate_gallery(mod, output_dir)


if __name__ == "__main__":
    main()
