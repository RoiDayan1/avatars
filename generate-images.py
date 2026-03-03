#!/usr/bin/env python3
"""Generate 100 unique superhero portrait images using Gemini Nano Banana.

No third-party packages required — uses only the Python standard library.
"""

import base64
import json
import os
import time
import urllib.request
import urllib.error
from pathlib import Path

from characters import MALES, FEMALES

API_KEY = os.environ["GEMINI_API_KEY"]

API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.5-flash-image:generateContent"
)

PROMPT_TEMPLATE = """\
A stylized semi-realistic portrait illustration of a superhero character in a square (1:1) format.

CHARACTER IDENTITY:
{character}

COMPOSITION:
- Square (1:1), chest-up portrait, high resolution
- Centered with slight dynamic pose allowed
- Character fills frame naturally, extends to bottom edge

ART STYLE (CONSISTENT ACROSS ALL):
- Semi-realistic digital illustration with high detail
- Realistic proportions, skin textures, and facial features
- Subtle painterly touches — soft brush strokes on background only
- Clean rendering with natural skin tones and believable lighting
- Closer to concept art realism than cartoon or stylized

LIGHTING:
- Soft diffused lighting with optional colored accent lighting matching the character theme

BACKGROUND:
- Abstract full-bleed background that complements the character's theme and colors

QUALITY:
- High detail, clean rendering
- No text, no logos, no borders, no watermarks"""

# Build interleaved list: Male[0], Female[0], Male[1], Female[1], ...
CHARACTERS = []
for m, f in zip(MALES, FEMALES):
    CHARACTERS.append(m)
    CHARACTERS.append(f)

TOTAL = len(CHARACTERS)
OUTPUT_DIR = "generated_images"
DELAY = 1.0
RETRIES = 2

# Set to a list of indices to regenerate only those, or empty to generate all.
REGENERATE = [
    61
]


def generate_image(api_key: str, index: int, output_dir: Path) -> bool:
    character = CHARACTERS[index - 1]
    prompt = PROMPT_TEMPLATE.format(character=character)
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
        print(f"[{index:3d}/{TOTAL}] HTTP {e.code}: {error_body[:200]}")
        return False
    except Exception as e:
        print(f"[{index:3d}/{TOTAL}] Error: {e}")
        return False

    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData")
            if inline and inline.get("data"):
                ext = "png" if "png" in inline.get("mimeType", "") else "jpg"
                filepath = output_dir / f"image_{index:03d}.{ext}"
                filepath.write_bytes(base64.b64decode(inline["data"]))
                print(f"[{index:3d}/{TOTAL}] Saved {filepath.name}")
                return True

    print(f"[{index:3d}/{TOTAL}] No image returned by the model")
    return False


def main():
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    indices = REGENERATE if REGENERATE else list(range(1, TOTAL + 1))

    print(f"Output:  {output_dir.resolve()}")
    print(f"Delay:   {DELAY}s between requests")
    print(f"Model:   gemini-2.5-flash-image (Nano Banana)")
    print(f"Images:  {len(indices)}" + (f" (regenerating)" if REGENERATE else ""))
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
            ok = generate_image(API_KEY, i, output_dir)
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


if __name__ == "__main__":
    main()
