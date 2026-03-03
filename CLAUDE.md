# Avatar Collections

Generate diverse avatar portrait collections using Google Gemini image generation.

## Project Structure

```
collections/           # Collection definitions (one .py file per collection)
  vanguard.py          # VANGUARD: 100 superhero avatars
  diversefaces.py      # DiverseFaces: 100 diverse portrait avatars
generate-images.py     # Image generation script (collection-agnostic)
VANGUARD/              # Generated output for VANGUARD
DiverseFaces/          # Generated output for DiverseFaces
```

## How to Add a New Collection

1. Create `collections/<name>.py` with these required exports:

```python
"""Short description of the collection."""

NAME = "DisplayName"           # Used as output directory name and gallery title
SUBTITLE = "100 ... Avatars"   # Gallery subtitle
PROMPT_TEMPLATE = """\
Your style prompt here...

CHARACTER IDENTITY:
{character}

... rest of prompt (composition, lighting, background, quality)...
"""

MALES = [
    # 50 male character descriptions (odd indices: 1, 3, 5, ... 99)
    "Male, age ..., description...",
    ...
]

FEMALES = [
    # 50 female character descriptions (even indices: 2, 4, 6, ... 100)
    "Female, age ..., description...",
    ...
]
```

2. Generate images:
```bash
python3 generate-images.py --collection <name>
```

3. Regenerate specific images:
```bash
python3 generate-images.py --collection <name> --regenerate 1 5 42
```

4. Regenerate only the gallery HTML:
```bash
python3 generate-images.py --collection <name> --gallery-only
```

## Collection Module Contract

Each collection module in `collections/` must define:

| Export | Type | Description |
|--------|------|-------------|
| `NAME` | `str` | Display name, used as output directory and gallery title |
| `SUBTITLE` | `str` | Gallery subtitle line |
| `PROMPT_TEMPLATE` | `str` | Prompt with `{character}` placeholder |
| `MALES` | `list[str]` | 50 male character descriptions |
| `FEMALES` | `list[str]` | 50 female character descriptions |

Characters are interleaved: Male[0]=index 1, Female[0]=index 2, Male[1]=index 3, etc.

## Writing Character Descriptions

- Each description is a single string injected into `{character}` in the prompt template
- Include: age, ethnicity/background, skin tone, facial features, hair, clothing, accessories, expression
- Aim for maximum diversity across the full set
- Avoid repetition — each character should feel unique
- The description should complement the style prompt (don't repeat style/lighting/composition instructions)

## Gallery

- Each collection gets a `<NAME>/index.html` gallery page, auto-generated after image generation or via `--gallery-only`
- Gallery pages auto-discover all other collections and add cross-navigation links (top-right corner)
- After adding a new collection, regenerate all galleries to update the nav links:
  ```bash
  python3 generate-images.py --collection vanguard --gallery-only
  python3 generate-images.py --collection diversefaces --gallery-only
  ```

## Environment

- `GEMINI_API_KEY` env var required (set in `.env` or export directly — `.env` is auto-loaded)
- Python 3, standard library only
- Output goes to `<NAME>/` directory (images + index.html gallery)
