# Avatar Collections

Generate collections of unique portrait avatars using Google's Gemini image generation API. Each collection has its own style prompt and 100 diverse character descriptions (50 male, 50 female).

## Collections

### VANGUARD — 100 Superhero Avatars
Semi-realistic superhero character portraits with unique powers, costumes, and weapons. Characters range from cosmic elders and asteroid miners to living paintings and probability surfers.

**[Browse the gallery](https://roidayan1.github.io/avatars/VANGUARD/)**

### DiverseFaces — 100 Diverse Portrait Avatars
Stylized painterly portraits of globally-inspired individuals. Rich variation in ethnicity, cultural clothing, accessories, and expressions — professional LinkedIn-style framing with vibrant abstract backgrounds.

**[Browse the gallery](https://roidayan1.github.io/avatars/DiverseFaces/)**

## Project Structure

```
collections/           # One .py file per collection (prompt + characters)
  vanguard.py
  diversefaces.py
generate-images.py     # Image generation script
VANGUARD/              # Generated: images + gallery page
DiverseFaces/          # Generated: images + gallery page
```

## Usage

1. Set your Gemini API key in `.env`:
   ```
   GEMINI_API_KEY=your_key_here
   ```

2. Generate a collection:
   ```bash
   python3 generate-images.py --collection vanguard
   python3 generate-images.py --collection diversefaces
   ```

3. Regenerate specific images:
   ```bash
   python3 generate-images.py --collection vanguard --regenerate 1 5 42
   ```

4. Regenerate only the gallery HTML:
   ```bash
   python3 generate-images.py --collection vanguard --gallery-only
   ```

## Adding a New Collection

Create `collections/<name>.py` with: `NAME`, `SUBTITLE`, `PROMPT_TEMPLATE`, `MALES` (50), and `FEMALES` (50). Then run the generator. Gallery pages auto-discover all collections and cross-link between them. See [CLAUDE.md](CLAUDE.md) for the full specification.

## Requirements

- Python 3 (standard library only, no third-party packages)
- Google Gemini API key
