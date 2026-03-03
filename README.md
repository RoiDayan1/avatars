# avatars

Generate 100 unique superhero portrait avatars using Google's Gemini image generation API.

## Overview

This project creates a diverse set of 100 superhero character portraits (50 male, 50 female) with detailed character descriptions covering a wide range of ethnicities, powers, and visual styles. Each character has a unique identity including age, ethnicity, costume, weapon, color palette, expression, and superpower.

Characters are interleaved by gender (odd indices = male, even indices = female) and range from cosmic elders and asteroid miners to living paintings and probability surfers.

## Project Structure

```
characters.py          # Character descriptions (MALES and FEMALES lists)
generate-images.py     # Image generation script using Gemini API
generated_images/      # Output directory with generated PNG portraits
```

## Usage

1. Set your Gemini API key in `generate-images.py`
2. Run the generator:

```bash
python generate-images.py
```

Images are saved as `generated_images/image_001.png` through `image_100.png`.

To regenerate specific images, set the `REGENERATE` list in `generate-images.py` to the desired indices.

## Requirements

- Python 3 (standard library only, no third-party packages)
- Google Gemini API key
