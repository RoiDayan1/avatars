# VANGUARD

Generate 100 unique superhero portrait avatars using Google's Gemini image generation API.

**[Browse the gallery](https://roidayan1.github.io/avatars/VANGUARD/)**

## Overview

This project creates a diverse set of 100 superhero character portraits (50 male, 50 female) with detailed character descriptions covering a wide range of ethnicities, powers, and visual styles. Each character has a unique identity including age, ethnicity, costume, weapon, color palette, expression, and superpower.

Characters are interleaved by gender (odd indices = male, even indices = female) and range from cosmic elders and asteroid miners to living paintings and probability surfers.

## Project Structure

```
characters.py          # Character descriptions (MALES and FEMALES lists)
generate-images.py     # Image generation script using Gemini API
VANGUARD/              # Generated PNG portraits + gallery page
  index.html           # Web gallery with download ZIP button
  image_001–100.png    # Avatar images
```

## Usage

1. Set your Gemini API key in `.env`:
   ```
   GEMINI_API_KEY=your_key_here
   ```
2. Run the generator:
   ```bash
   python generate-images.py
   ```

Images are saved as `VANGUARD/image_001.png` through `image_100.png`.

To regenerate specific images, set the `REGENERATE` list in `generate-images.py` to the desired indices.

## Requirements

- Python 3 (standard library only, no third-party packages)
- Google Gemini API key
