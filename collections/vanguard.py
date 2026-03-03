"""VANGUARD — 100 Superhero Avatars

Diverse superhero character portraits with unique powers, costumes, and weapons.
"""

NAME = "VANGUARD"
SUBTITLE = "100 Superhero Avatars"

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

# 50 Male characters (odd indices: 1, 3, 5, ... 99)
# 50 Female characters (even indices: 2, 4, 6, ... 100)

MALES = [
    # 1: Cosmic elder
    "Age 55, dark brown skin, shaved head with glowing constellation tattoos across skull. Deep-set wise eyes, heavy brow, broad nose. Flowing dark nebula cloak with embedded starlight particles. Carries an ancient ornate staff topped with a miniature rotating galaxy. Colors: deep purple + midnight blue + gold star accents. Expression: calm, all-knowing. Power: cosmic foresight — faint galaxy swirl in his eyes.",
    # 3: Asteroid miner
    "Age 40, olive skin, thick black curly hair with electric blue streaks. Strong square jaw, crooked nose, thick eyebrows. Bulky cosmic miner suit with asteroid fragments embedded in chest plate. Wields a massive reinforced pickaxe crackling with energy. Colors: charcoal + amber + deep teal. Expression: determined, rugged. Power: asteroid control — stone fragments orbit his fists.",
    # 5: Data hacker
    "Age 25, East Asian features, pale skin, jet black slicked-back hair, narrow sharp eyes. Lean build. Sleek matte black bodysuit with holographic data streams flowing across surface. Compact high-tech pistol holstered on thigh. Colors: matte black + neon cyan + electric white. Expression: intense focus. Power: data manipulation — digital code fragments surround him.",
    # 7: Earth-cosmic bridge
    "Age 50, Indigenous Australian features, deep brown skin with traditional-inspired geometric markings that glow orange. Broad face, strong jaw, kind eyes. Bare-chested with cosmic dust cloak and stone arm bracers. Carries a heavy stone war hammer etched with star patterns. Colors: burnt orange + deep red + dusty gold + charcoal. Expression: stoic, grounded. Power: dust and stars swirl together around him.",
    # 9: Cosmic viking
    "Age 45, Nordic features, very pale skin, long red beard braided with metal rings, bald on top. Ice-blue eyes, weathered face, large build. Heavy fur-lined cosmic viking armor with frozen energy core on chest. Wields a massive double-bladed battle axe with frost energy along the edges. Colors: ice blue + frost white + deep brown + silver. Expression: battle-ready, stern. Power: cosmic frost — ice crystals form on his armor.",
    # 11: Plant guardian
    "Age 30, African features, very dark skin that shifts to bark-like texture on forearms. Short natural hair with tiny green sprouts. Wide nose, strong neck, warm eyes. Living wood armor with moss and lichen. Carries a large curved machete with a vine-wrapped handle. Colors: deep brown + forest green + amber. Expression: gentle giant. Power: plant growth — vines curl from his shoulders.",
    # 13: Fire striker
    "Age 35, Latino features, warm brown skin, shaved sides with wild fire-red mohawk that flickers. Square jaw, stubble, scar across left cheek. Tactical vest over bare arms with glowing ember lines under skin. Dual semi-automatic pistols holstered in drop-leg holsters. Colors: crimson + orange + charcoal + bright yellow. Expression: cocky smirk. Power: flames dance along his forearms.",
    # 15: Lava warrior
    "Age 28, Pacific Islander (Samoan), deep brown skin with traditional-inspired tattoo patterns that glow with lava light. Massive broad build, warm round face. Volcanic stone gauntlets and shoulder pauldrons. Swings an enormous obsidian war hammer with a molten core. Colors: obsidian black + molten orange + deep red + ember gold. Expression: fierce war cry. Power: magma control — cracks of lava glow on his skin.",
    # 17: Crystal monk
    "Age 65, Chinese elder features, weathered tan skin, long thin white beard, deeply wrinkled wise face. Small eyes with ancient depth. Simple monk robe with mountain stone elements and crystal formations on shoulders. Leans on a tall crystal-tipped wooden staff. Colors: stone grey + jade green + earth brown + crystal white. Expression: serene wisdom. Power: small crystals grow from his palms.",
    # 19: Permafrost tank
    "Age 42, Russian features, pale ruddy skin, thick brown beard with ice crystals. Heavy brow, broad flat nose, barrel chest. Massive ice-crystal armor with fur underlayer. Carries a brutal ice axe in one hand, slung assault rifle on back. Colors: ice blue + bone white + dark fur brown + crystalline teal. Expression: grim determination. Power: deep cold radiates visibly from his armor.",
    # 21: Neon hacker
    "Age 33, Korean features, pale skin, sharp undercut with neon-lit hair implants. Angular jaw, narrow eyes behind sleek AR visor. Matte black techwear with exposed circuitry and soft blue LED seams. Compact submachine gun with integrated targeting system slung at side. Colors: matte black + electric blue + chrome. Expression: cold focus. Power: holographic data streams project from his fingertips.",
    # 23: Drone controller
    "Age 27, Indian features, brown skin, messy dark hair, thin face. Large round glasses with heads-up display. Oversized tech hoodie covered in patches and cables, small drone companions on shoulders. Multi-tool kit on belt and tablet controller in hand. Colors: dark grey + neon green + white + orange accents. Expression: nervous genius, slight grin. Power: tiny drones orbit him.",
    # 25: War-weary veteran
    "Age 58, Eastern European features, grey-white buzzcut, deeply lined face, mechanical left arm (full prosthetic, exposed gears). Heavy build, thick neck, tired fierce eyes. Worn military-industrial power suit, patched and battle-scarred. Heavy modified assault rifle held at rest, combat knife strapped to chest. Colors: army green + rust + gunmetal + faded yellow stripes. Expression: war-weary veteran. Power: mechanical arm sparks fly.",
    # 27: Kinetic king
    "Age 45, Nigerian features, dark skin, bald, strong angular face with geometric scarification. Broad shoulders. Sleek black power armor with vibrating kinetic energy panels that pulse gold. Wields a long ceremonial spear with a kinetic energy tip. Colors: matte black + vibrant gold + deep bronze + warm amber. Expression: regal authority. Power: golden pulse waves emanate from his armor.",
    # 29: Shield tactician
    "Age 38, mixed (Black/White), medium brown skin, dreadlocks pulled back, cybernetic visor covering both eyes, strong stubbled jaw. Modular tactical gear with deployable shield generators on forearms. Sidearm pistol in hip holster. Colors: dark teal + electric cyan + matte grey + orange. Expression: alert, scanning. Power: translucent cyan barriers form near his hands.",
    # 31: Rune sorcerer
    "Age 35, Moroccan features, warm brown skin, short dark beard with grey streaks, glowing henna-like markings on forehead and hands. Deep brown eyes with faint golden ring. Dark layered robes with embroidered arcane symbols. Ornate curved dagger with rune-etched blade at his belt. Colors: deep burgundy + gold + dark purple + black. Expression: brooding intensity. Power: glowing runes float around his hands.",
    # 33: Mandala monk
    "Age 70, Tibetan monk features, weathered tan skin, completely bald, round peaceful face. Simple orange and saffron robes with a single glowing mandala on chest. Colors: saffron + burnt orange + gold + deep red. Expression: total inner peace. Power: a large soft mandala glows behind him.",
    # 35: Sacred flame
    "Age 32, Persian features, olive skin, thick dark eyebrows, neatly trimmed beard, aquiline nose. Handsome sharp features. Ornate golden armor with flowing midnight-blue cape inscribed with fire symbols. Curved scimitar with a flame-pattern Damascus steel blade in hand. Colors: midnight blue + burnished gold + flame orange + deep black. Expression: noble, righteous. Power: controlled fire wraps around his forearms.",
    # 37: Golden fighter
    "Age 25, Thai features, golden-brown skin, shaved head with single long topknot, lean angular face. Bare-chested with traditional-inspired golden wraps that glow with spiritual energy. Heavy brass knuckle-wraps on both fists, knee and elbow guards. Colors: gold + saffron + deep red + bronze. Expression: focused calm before a strike. Power: golden energy wraps around his fists.",
    # 39: Ice spirit shaman
    "Age 48, Inuit features, weathered brown skin, broad flat face, small dark eyes, short black hair under a carved bone and ice crown. Thick build. Fur and carved ice armor with spirit animal engravings. Carries a bone-and-ice harpoon with spirit carvings. Colors: ice white + deep ocean blue + bone + charcoal fur. Expression: stoic, wind-bitten. Power: ghostly animal shapes form in frost around him.",
    # 41: Shadow stepper
    "Age 22, Black American features, dark skin, high-top fade with dyed gold tips, diamond stud earring. Young angular face, sharp jaw, intense brown eyes. Oversized bomber jacket with hidden armor panels, hood up. Butterfly knife in hand, compact pistol tucked in waistband. Colors: black + gold + red + dark grey. Expression: street-smart defiance. Power: wisps of darkness curl from his jacket.",
    # 43: Impact bruiser
    "Age 35, white British features, ruddy pale skin, shaved head with stubble, broken nose, cauliflower ear. Heavy build. Worn leather jacket with brass knuckle energy gauntlets. Carries a heavy iron crowbar resting on shoulder. Colors: brown leather + brass + faded black + dark red. Expression: bruiser, tough love. Power: shockwave rings around his fists.",
    # 45: Rooftop runner
    "Age 30, Somali features, dark brown skin, tall and lean, high cheekbones, trimmed goatee. Hooded sleek athletic suit with reflective strips. Set of balanced throwing knives strapped across chest. Colors: midnight blue + reflective silver + neon yellow + black. Expression: alert, scanning rooftops. Power: enhanced agility — motion blur trails behind him.",
    # 47: Tired protector
    "Age 55, Mexican features, weathered brown skin, thick salt-and-pepper mustache, deep wrinkles, kind haunted eyes. Broad shoulders. Worn denim and flannel over concealed armor with santo medallion. Sawed-off double-barrel shotgun held low at his side. Colors: faded blue denim + red flannel + bronze medallion + earth brown. Expression: weary resolve. Power: medallion glows with warm light.",
    # 49: Construction guardian
    "Age 40, Aboriginal Australian features, dark brown skin, thick curly black hair and full beard. Wide nose, warm brown eyes. Customized construction gear — hard hat, reinforced vest, heavy gloves with energy conduits. Wields a massive sledgehammer crackling with energy. Colors: high-vis orange + dark grey + dusty yellow + matte black. Expression: reliable, steady. Power: energy grids project from his hands.",
    # 51: Reality folder
    "Age 35, translucent pale skin showing faint geometric structures underneath. No hair — smooth head with fractal patterns. Calm neutral features. Suit of folded paper/origami armor. Colors: white + pale blue + gold line work + soft grey. Expression: eerily calm. Power: space bends subtly around him.",
    # 53: Kintsugi man
    "Age 40, East Asian features but skin has cracked porcelain quality with golden kintsugi repairs. Serene face, closed eyes, shaved head. Minimalist white robe with gold-filled crack patterns. Colors: porcelain white + gold kintsugi + deep black cracks + warm amber. Expression: peaceful acceptance. Power: cracks on his skin glow when using power.",
    # 55: Mercury split
    "Age 50, his entire left side is made of liquid mercury — half his face is reflective chrome that moves. Right side: weathered Black man with grey stubble and kind tired eye. Simple hospital gown. Colors: liquid silver + warm brown skin + hospital white + dark grey. Expression: conflicted. Power: mercury reshapes on command.",
    # 57: Cubist hero
    "Age 25, body appears made of stacked geometric shapes — cubist-inspired but recognizably human. Brown skin tones in angular facets. Short geometric hair. Outfit is part of his body. Colors: warm browns + terracotta + angular shadows of deep sienna + gold edges. Expression: determined through angular features. Power: objects near him fragment into shapes.",
    # 59: Living tree
    "Age 60, made of living wood — old tree that grew into human shape. Bark skin with visible grain, moss in beard-like branch growth. Deep knotholes for eyes with warm amber light inside. Carries a gnarled wooden staff twisted from his own body. Colors: dark bark brown + moss green + amber glow + deep earth tones. Expression: ancient patience. Power: small creatures and plants grow on him.",
    # 61: Desert gunslinger
    "Age 42, mixed (Native American/Black), deep weathered brown skin, sun-bleached short locs, squint lines around sharp amber eyes. Lean rangy build, stubbled jaw, scar along left temple. Dusty long leather duster coat over tactical vest, wide-brimmed hat with bullet band. Twin heavy revolvers in worn hip holsters, bandolier of shells across chest. Colors: desert sand + worn leather brown + gunmetal + sun-bleached tan + dusty red. Expression: quiet menace, calculating aim. Power: supernatural accuracy — faint golden sight-lines trace from his eyes to targets.",
    # 63: Forge master
    "Age 52, Eastern European (Serbian), ruddy pale skin covered in old burn scars on forearms, thick salt-and-pepper beard, shaved head glistening with sweat. Barrel-chested, massive forearms. Heavy blacksmith's leather apron over bare chest, soot-stained work pants, steel-toed boots. Wields an enormous forging hammer in one hand, holds a glowing freshly-forged broadsword in the other. Colors: forge-fire orange + soot black + molten steel white-hot + aged leather brown + ash grey. Expression: proud craftsman, fierce. Power: anything he forges becomes indestructible — sparks and embers orbit his hammer.",
    # 65: Norse berserker
    "Age 35, very pale skin, massive red beard with braided bone charms, wild eyes, bear-like build. Bare-chested with fur pelt, runic tattoos across chest glowing blue. Wields a massive Viking battle axe in one hand, round wooden shield in other. Colors: ice blue runes + pale skin + red-brown fur + bone + blood red. Expression: berserker trance, eyes wide. Power: ghostly bear aura overlays his silhouette.",
    # 67: Jaguar warrior
    "Age 45, Aztec-inspired, brown skin with jaguar spot face paint that glows supernaturally. Strong features, wide nose, intense dark eyes. Elaborate feathered headdress and jade-studded armor. Wields a macuahuitl (obsidian-bladed wooden sword) and a round feathered shield. Colors: jade green + gold + obsidian black + quetzal feather green-blue + blood red. Expression: predatory focus. Power: eyes slit like a cat, spots spread on his skin.",
    # 69: Smoke djinn
    "Age 55, deep olive skin with smoke-like wisps trailing from his lower body. Bald, thick dark beard, ornate golden earrings, wise ancient eyes. Upper body bare with calligraphy tattoos, lower body fades to smoke. Ornate curved jambiya dagger with jeweled handle tucked in sash. Colors: smoke grey + deep gold + desert sand + deep crimson + bronze. Expression: amused, enigmatic. Power: smoke swirls form shapes of desires.",
    # 71: Mirror crown
    "Age 30, surrounded by a permanent crown of floating broken mirrors. Normal handsome face, mixed race, medium brown skin, short curly hair. Simple white shirt. Colors: mirror silver + skin brown + white + fractured reflections. Expression: confused, searching. Power: each mirror shows a different reality.",
    # 73: Eternal blue flame
    "Age 35, perpetually on fire with translucent blue flames. Underneath: dark-skinned man, bald, calm face visible through flames. Simple dark clothes burning endlessly. Colors: blue flame + orange ember core + dark brown skin + charcoal. Expression: peaceful despite being on fire. Power: the fire IS him.",
    # 75: Street samurai
    "Age 30, Japanese-American, tan skin, sharp angular jaw, short messy black hair with bleached tips, thin scar through left eyebrow. Lean muscular build. Modern tactical streetwear — black fitted jacket with armored panels, cargo pants with knee guards, combat boots. Katana in a matte black scabbard strapped across back, compact 9mm pistol in shoulder holster. Colors: matte black + dark grey + steel silver + neon red accent stitching + worn denim blue. Expression: focused, streetwise, ready. Power: enhanced reflexes — faint afterimage trails when he moves.",
    # 77: Invisible body
    "Age 25, only his head is visible — body below neck is invisible. Young Latino features, curly dark hair, goatee, kind brown eyes. Floating collar and tie where body should be. Colors: warm brown skin + white collar + dark tie + background showing through. Expression: cheerful despite his condition. Power: selective invisibility.",
    # 79: Living painting
    "Age unknown, a living painting — visible brush strokes make up his entire form, slightly 2D looking. Impressionist style face. Colors: thick visible strokes of blue + yellow + green + orange + white. Expression: serene. Power: he can paint things into existence.",
    # 81: Exo-suit soldier
    "Age 38, heavy-set, Hispanic features, scarred face visible through open-face tactical helmet. Thick neck, broken nose, stubble. Massive industrial powered exoskeleton — welded plates, exposed hydraulics. Carries a belt-fed heavy machine gun with ammo belt draped across chest. Colors: olive drab + rust + faded yellow hazard stripes + gunmetal. Expression: grim, mission-focused. Power: hydraulics hiss with steam.",
    # 83: Desert tactician
    "Age 45, East Asian (Vietnamese), wiry lean build, thin weathered face, salt-and-pepper crew cut. Military dog tags. Lightweight modular armor with drone deployment pack, arm-mounted targeting. Scoped precision rifle slung across back. Colors: desert tan + dark olive + tech blue displays + matte black. Expression: veteran calm. Power: holographic targeting data projects from his arm.",
    # 85: Commander
    "Age 50, large African-American man, grey-streaked close-cropped hair, square jaw, faded scar across nose bridge. Heavy dark utilitarian commander armor, worn flag patch. Service pistol in worn leather holster, binoculars around neck. Colors: midnight navy + faded olive + worn bronze insignia + dark grey. Expression: leadership weight, tired but resolute. Power: faint holographic battle plans hover near him.",
    # 87: Aquatic soldier
    "Age 25, mixed (Pacific Islander/White), tan skin, youthful face, buzz cut, wide-set eyes, easy grin. Lean build. Amphibious tactical suit with aquatic design lines, gill-like vents on neck. Harpoon gun slung on back, dive knife strapped to thigh. Colors: deep ocean blue + seafoam + matte grey + coral orange. Expression: relaxed surfer in soldier gear. Power: water streams around his suit.",
    # 89: Energy absorber king
    "Age 42, Nigerian features, very dark skin, muscular, tribal scarification (three parallel lines each cheek). Bald. Advanced ceremonial battle armor with geometric African patterns. Holds a tall ceremonial spear with vibrating energy tip and a large round shield. Colors: deep black + vibrant purple energy lines + gold geometric patterns + bronze. Expression: stoic warrior king. Power: purple energy ripples across armor when struck.",
    # 91: Puppet master
    "Age 35, Mediterranean features, olive skin, thin artistic face, goatee, long nimble fingers. Theatrical black and red outfit, top hat at jaunty angle. Colors: theatrical black + blood red + gold string accents + white gloves. Expression: showman's grin, slightly sinister. Power: glowing threads extend from each finger.",
    # 93: Forbidden librarian
    "Age 60, thin elderly Indian man, round glasses, white hair, gentle face. Ancient book fused to his left hand, pages fluttering. Tweed jacket over mystical robes. Colors: old parchment + leather brown + mystical green glow + tweed grey + spectral gold text. Expression: curious, slightly worried. Power: glowing text floats from the open book.",
    # 95: Soul gardener
    "Age 45, East African features, dark skin, grey temples, calloused hands. Simple gardening clothes — suspenders, rolled sleeves. Worn garden shears in one hand, hand trowel in belt. Translucent glowing flowers float around him. Colors: earth brown + ghost-white flowers + soft spectral green + spirit blue. Expression: tender, nurturing. Power: luminous phantom plants grow where he touches.",
    # 97: Dimension mapper
    "Age 30, mixed (Latino/Arab) features, warm brown skin, messy dark hair, ink-stained hands. Leather adventurer gear covered in map fragments and compass tools. Holds a compass that doubles as a folding dagger. Colors: parchment tan + ink black + leather brown + compass brass + purple shimmer. Expression: fascinated, looking at something others can't see. Power: faint map lines project from his notebook.",
    # 99: Probability surfer
    "Age 28, mixed (Irish/Jamaican), light brown skin, wild curly auburn hair, freckles, gap-toothed grin. Casual graphic tee under lucky jacket covered in four-leaf clovers, dice, cards. Colors: lucky green + gold + chance-red + denim blue + playing card white. Expression: cocky, knowing something good is about to happen. Power: probability streams ripple around him.",
]

FEMALES = [
    # 2: Gravity queen
    "Age 28, pale porcelain skin with faint iridescent shimmer, platinum white hair in a sharp asymmetric bob. Large almond eyes with silver irises. Sleek chrome and glass armor with floating orbital rings around shoulders. Colors: silver + ice blue + white + pale pink. Expression: serene, detached. Power: gravity manipulation — objects float around her.",
    # 4: Solar grandmother
    "Age 60, very dark skin, silver-white natural afro glowing faintly. High cheekbones, deep laugh lines, piercing golden eyes. Elegant robe of woven starlight fabric. Carries a tall golden scepter crowned with a miniature sun. Colors: deep gold + royal purple + black. Expression: warm authority. Power: solar energy — warm golden aura radiates from her.",
    # 6: Moon warrior
    "Age 35, South Asian features, warm brown skin, long black hair braided with tiny glowing stars. Soft round face, full lips, large expressive dark eyes. Celestial silk armor with crescent moon shoulder pieces. Wields a curved crescent-bladed glaive. Colors: deep navy + silver + soft peach. Expression: compassionate, fierce. Power: soft moonlight from her hands.",
    # 8: Energy absorber
    "Age 22, mixed (Black/Korean), medium brown skin, voluminous curly dark hair with purple tips. Round face, button nose, mischievous grin. Light flexible space suit with glowing energy veins. Colors: electric purple + hot pink + black + chrome. Expression: playful, daring. Power: her hair crackles with captured energy.",
    # 10: Dimensional seer
    "Age 38, Middle Eastern features, olive skin, sharp hawk-like features, black hair in tight bun under translucent cosmic veil. Angular face, prominent cheekbones. Fitted dark suit with geometric star patterns etched in light. Ornate curved dagger with constellation patterns on blade. Colors: deep black + gold lines + dark teal. Expression: calculating, mysterious. Power: one eye glows with visible star map.",
    # 12: Water goddess
    "Age 45, Japanese features, pale skin with subtle blue-water shimmer. Sharp chin, thin elegant features, black hair flowing like liquid water. Robe that transitions from fabric to actual water at the hem. Holds an ornate trident made of coral and pearl. Colors: ocean blue + seafoam + pearl white + deep turquoise. Expression: composed, powerful stillness. Power: droplets float around her.",
    # 14: Storm caller
    "Age 55, Scandinavian features, sun-weathered pale skin, wild white hair like storm clouds. Strong broad face, ice-grey eyes, crow's feet. Heavy layered storm cloak crackling with static. Grips a short-handled war hammer that crackles with lightning. Colors: storm grey + electric white + deep violet + silver. Expression: fierce, commanding. Power: lightning arcs between her fingers.",
    # 16: Autumn witch
    "Age 32, Irish features, very pale freckled skin, wild curly copper-red hair full of autumn leaves. Upturned nose, green eyes, impish features. Living autumn foliage outfit and bark corset. Carries a sharp iron sickle with a wooden handle. Colors: copper + amber + deep green + burgundy + gold leaf. Expression: wild, free-spirited. Power: leaves swirl in a spiral around her.",
    # 18: Wind master
    "Age 25, Ethiopian features, deep dark skin, completely bald with wind-pattern scarification on scalp. Long elegant neck, high forehead. Sheer flowing garment moving as if perpetually windblown. Colors: sky blue + cloud white + pale lavender + soft grey. Expression: peaceful, eyes closed. Power: hair-thin air currents visible around her.",
    # 20: Jungle bioluminescent
    "Age 30, Brazilian features, warm golden-brown skin, thick wavy dark hair with bioluminescent streaks. Full cheeks, wide bright smile. Sleek suit of living jungle material — vines, flowers, phosphorescent moss. Machete with a vine-wrapped handle at her hip. Colors: neon green + electric blue bioluminescence + deep jungle green + violet. Expression: radiant joy. Power: glowing flowers bloom on her suit.",
    # 22: Exo-frame engineer
    "Age 40, West African features, dark brown skin, elaborate braids woven with fiber optic cables that glow. Round face, strong features, cybernetic eye patch over left eye. Heavy industrial exo-frame with exposed pistons. Massive wrench in one hand, welding torch holstered on belt. Colors: gunmetal + neon orange + matte black + copper. Expression: tough, no-nonsense. Power: her exo-frame hums with energy.",
    # 24: Nanotech operative
    "Age 35, mixed (Hispanic/Japanese), light tan skin, straight black hair with one side shaved revealing circuit-board tattoo. Sharp cheekbones, cybernetic jaw implant visible as chrome. Nano-fiber suit with modular armor plates. Dual compact pistols in magnetic holsters on thighs. Colors: pearl white + rose gold + matte black + soft pink LED. Expression: cool confidence. Power: her suit reshapes in real-time.",
    # 26: Holographic scout
    "Age 22, Scandinavian features, very pale, platinum pixie cut, wide blue eyes, youthful face. Slim build. Lightweight holographic bodysuit projecting shifting geometric patterns. Colors: holographic rainbow + white + soft blue + prismatic. Expression: wonder, curiosity. Power: prismatic fragments float around her.",
    # 28: Bio-scientist
    "Age 30, Chinese features, pale skin, long straight black hair in high ponytail, sharp calculating eyes. Minimalist white lab coat over tight dark bodysuit with embedded bio-monitors. Holds a precision surgical scalpel that glows with energy. Colors: clinical white + dark navy + subtle red heartbeat line + chrome. Expression: analytical, precise. Power: subtle data readouts hover near her temples.",
    # 30: Hidden genius
    "Age 50, Filipina features, warm tan skin, silver-streaked black hair in messy bun, laugh lines, reading glasses. Oversized cardigan over concealed micro-tech suit. Colors: warm brown + cream + hidden neon blue + copper. Expression: kind, deceptively harmless. Power: faint holographic blueprints near her hands.",
    # 32: Fae enchantress
    "Age 28, Celtic/Irish features, extremely pale skin with visible blue veins, wild red curly hair. Sharp fae-like features, pointed chin, green eyes. Tattered forest cloak over dress woven with living vines. Thorn-wrapped dagger of dark iron in hand. Colors: deep forest green + silver + mushroom brown + moonlight white. Expression: otherworldly, unsettling. Power: small wisps of light orbit her.",
    # 34: Spirit priestess
    "Age 40, Haitian features, deep dark skin, shaved head with painted voodoo-inspired symbols in white. Angular strong face, intense dark eyes, gap teeth. Layered ritual jewelry — bones, beads, feathers. Dark flowing dress with spirit motifs. Holds a ritual machete with bone-and-bead handle. Colors: deep black + bone white + deep purple + candle orange. Expression: powerful trance. Power: ghostly wisps rise around her.",
    # 36: Dream walker
    "Age 55, Native American (Navajo-inspired) features, warm reddish-brown skin, long silver hair with turquoise beads. Weathered kind face, deep-set dark eyes. Layered shawl of woven dreamcatcher patterns over deerskin. Colors: turquoise + earth red + sand + silver + sky blue. Expression: ancient knowing. Power: dreamcatcher pattern glows in her eyes.",
    # 38: Olympian warrior
    "Age 38, Greek features, olive skin, black curly hair piled high in ancient style, strong jaw, aquiline nose. Athletic build. Bronze and white draped armor inspired by ancient Olympian aesthetics. Wields a long spear in one hand and a round bronze Spartan shield in the other. Colors: bronze + marble white + olive green + deep sea blue. Expression: fierce warrior goddess. Power: faint golden shimmer on her skin.",
    # 40: Divine threads
    "Age 30, Indian (South) features, deep brown skin, extremely long black hair flowing with golden magical threads. Large kohl-lined dark eyes, glowing bindi. Elaborate silk sari-inspired costume with floating ornaments. Colors: deep magenta + gold + rich emerald + peacock blue. Expression: divine grace, mysterious smile. Power: golden threads flow from her fingertips.",
    # 42: Paint rebel
    "Age 27, Puerto Rican features, warm light-brown skin, long dark hair in high ponytail with neon pink streaks. Strong curved eyebrows, full lips. Tactical crop top and cargo pants with spray-can bandolier. Baseball bat wrapped in barbed wire slung over shoulder. Colors: hot pink + electric blue + concrete grey + black. Expression: rebellious grin. Power: her graffiti art comes alive as energy.",
    # 44: Kinetic detective
    "Age 45, Korean-American features, light skin, short black bob with grey streak, sharp tired eyes behind round glasses. Lean build. Dark trench coat hiding compressed kinetic armor. Snub-nosed revolver in shoulder holster under coat. Colors: dark navy + slate grey + hidden electric blue + black. Expression: quiet intensity, slight frown. Power: absorbs and returns force.",
    # 46: Signal hacker
    "Age 20, Vietnamese features, pale skin, choppy asymmetric black hair with one bleached white streak, wide curious eyes. Petite. Oversized vintage tech-modded hoodie with glowing circuitry patches. Colors: faded purple + neon green + washed black + white. Expression: curious hacker energy. Power: static electricity crackles around her devices.",
    # 48: Sonic assassin
    "Age 33, mixed (Nigerian/Swedish), medium brown skin, tall, close-cropped natural hair dyed platinum. High cheekbones, model-like features, cybernetic ear implant. Sleek dark streetwear with subtle bulletproof weave. Set of precision throwing blades in a chest harness. Colors: matte black + platinum + dark maroon + chrome. Expression: cold, professional. Power: sound wave visualizations near her ears.",
    # 50: Luck witch
    "Age 25, Roma (Romani) features, olive skin, wild long dark curly hair with gold coin accessories. Bright dark eyes, sharp features, hoop earrings. Layered colorful street-style clothes with hidden blades and mystic charms. Colors: deep red + gold + purple + forest green + black. Expression: untamed, unpredictable. Power: faint golden shimmer around her jewelry.",
    # 52: Space portal
    "Age 30, dark skin that transitions into deep space texture on one side of her face — stars and nebulae visible. One normal brown eye, one tiny galaxy eye. Asymmetric natural hair, half afro half dissolving into stardust. Colors: deep space black + cosmic purple + star white + warm brown. Expression: dual nature, half smile. Power: space warps near her body.",
    # 54: Identity mosaic
    "Age 28, features shift between ethnicities — face is a beautiful mosaic of different racial features blended seamlessly. Short hair changing color in sections. Clothes of overlapping cultural fabrics. Colors: multicolor mosaic + earth tones + vibrant accents of every hue. Expression: empathetic, warm. Power: her features shimmer and morph subtly.",
    # 56: Void walker
    "Age 35, pale skin, eyes entirely black — no whites, no iris, just void. Long straight white hair floating as if underwater. Gaunt angular face, high cheekbones, thin lips. Flowing black dress absorbing light at edges. Colors: void black + pale white skin + dark grey + faint purple glow. Expression: haunting, otherworldly. Power: darkness pools around her feet.",
    # 58: Glitch woman
    "Age 45, entire form is slightly glitched — like a character with rendering errors. Random pixel artifacts float around her. Normal East Asian features beneath the glitch. Casual clothes that stutter and duplicate. Colors: neon glitch cyan + magenta + yellow + muted clothing underneath. Expression: frustrated, trying to hold herself together. Power: she can corrupt physical space.",
    # 60: Living tattoo
    "Age 20, skin covered in living tattoos that move — dragons, waves, flowers, all animated. Pale skin, round youthful face, short messy black hair. Simple tank top to show the living ink. Colors: tattoo ink black + red + blue + green on pale skin + white clothing. Expression: punk energy, defiant smirk. Power: ink creatures peel off her skin.",
    # 62: Solar deity
    "Age 35, Egyptian-inspired, warm golden-brown skin, elaborate braided black hair with gold and lapis ornaments. Cat-like sharp features, lined eyes with gold. Golden and lapis armor inspired by ancient Egyptian aesthetics. Holds a khopesh (curved Egyptian sword) with a golden blade. Colors: gold + lapis lazuli blue + black eyeliner + warm sand + turquoise. Expression: regal, untouchable. Power: eye of Ra glows on her forehead.",
    # 64: Arctic huntress
    "Age 34, Mongolian features, wind-burned golden-brown skin, sharp high cheekbones, narrow focused dark eyes, black hair in a thick functional braid under a fur-lined hood. Athletic wiry build. Heavy arctic survival parka with bone toggles over layered armor, snow goggles pushed up on forehead. Recurve composite bow in hand, quiver of arrows on back, hunting knife at hip. Colors: arctic white + charcoal fur + bone + frostbitten blue + dark leather. Expression: patient hunter, eyes locked on prey. Power: ice arrows — frost trails behind each shot.",
    # 66: Storm orisha
    "Age 25, West African orisha-inspired, deep dark skin with gold dust markings across cheekbones. Regal posture, braided crown of hair with shells. Flowing white and gold ceremonial dress with storm energy at the hem. Wields a double-headed labrys axe crackling with electricity. Colors: pure white + gold + dark skin contrast + storm grey + electric blue. Expression: divine power, serene intensity. Power: lightning in her eyes.",
    # 68: Broken valkyrie
    "Age 38, tall athletic, pale skin with battle scars. Ash-blonde hair in warrior braids, steel-blue eyes, angular Nordic features. Winged silver and dark steel armor, partially damaged. One broken wing, one spread. Holds a battered but unbroken longsword. Colors: tarnished silver + dark steel + ash blonde + stormy blue-grey + blood red scratches. Expression: battle-exhausted but unbroken. Power: ghostly feathers fall around her.",
    # 70: Kitsune trickster
    "Age 30, Japanese features, pale skin, sharp vulpine features, amber fox-like eyes, long black hair with fox-ear styling. Nine subtle tail-like energy wisps behind her. Elegant dark kimono-inspired modern suit. Pair of folding iron war fans with razor edges. Colors: deep red + black + gold + white fox accents + amber. Expression: sly, dangerously charming. Power: faint mirror images flicker around her.",
    # 72: Film noir detective
    "Age 40, entirely monochrome — she exists in black and white and grey. Film-noir aesthetic. Sharp features, wavy dark hair, trench coat. The only color: bright red lipstick. Snub-nosed revolver in hand, cigarette smoke curling upward. Colors: black + white + grey + single red accent. Expression: world-weary detective. Power: she removes color from her surroundings.",
    # 74: Pirate captain
    "Age 38, Caribbean (Afro-Latina), rich dark brown skin, long thick black dreadlocks with gold rings and red beads, bold dark eyes, prominent scar across bridge of nose, gold tooth. Athletic curvy build. Weathered captain's longcoat over a corset with brass buckles, tricorn hat with a feather, tall boots. Flintlock pistol in one hand, curved cutlass in the other. Colors: deep ocean blue + weathered brown leather + gold trim + blood red sash + sea-foam teal. Expression: fearless, commanding grin. Power: controls ocean currents — saltwater swirls at her boots.",
    # 76: Split identity
    "Age 35, two people merged — visible seam line down middle of face. Left: dark skin, brown eye, curly black hair. Right: pale skin, blue eye, straight red hair. Two different outfit halves stitched together. Colors: warm earth tones (left) + cool blues (right) + visible merge line. Expression: left smiles, right frowns. Power: can split into two people.",
    # 78: Time split
    "Age 45, time moves differently around her — half her face is young (20s, smooth) and other half is ancient (80s, wrinkled, white-haired). One young eye, one clouded old eye. Robes shifting between new and tattered. Colors: young side vibrant warm + old side faded cool + temporal gold shimmer. Expression: young side hopeful, old side weary. Power: time manipulation.",
    # 80: Sound woman
    "Age 30, made of sound — visible sound waves form her silhouette. When she speaks, her form solidifies. Barely visible features (Black woman, natural hair) suggested through sonic wave patterns. Wears headphones. Colors: sound wave blue + frequency purple + bass deep red + white noise. Expression: lost in music. Power: her body IS sound.",
    # 82: Stealth operative
    "Age 32, tall athletic build, dark Black skin, high cheekbones, natural hair in tight braided rows. Full tactical stealth suit with active camo panels showing circuit patterns. Suppressed pistol in hand, combat knife strapped to shoulder. Colors: dark charcoal + teal circuit lines + matte black + subtle purple camo. Expression: silent professional, eyes on target. Power: edges of her suit shimmer.",
    # 84: Combat medic
    "Age 28, South Asian features, warm brown skin, dark hair in practical braid, sharp intelligent eyes. Sleek white and blue medic-combat armor with red cross, healing tech gauntlets. Compact sidearm pistol in thigh holster. Colors: white + medical blue + red cross + chrome + soft green glow. Expression: compassionate determination. Power: green energy flows from her gauntlets.",
    # 86: Energy blade warrior
    "Age 35, Middle Eastern features, olive skin, dark eyes, hijab integrated into high-tech helmet seamlessly. Strong jawline. Sleek dark armor with energy blade sheaths on forearms. Backup combat knife in boot sheath. Colors: deep midnight blue + silver edges + dark purple + matte black. Expression: disciplined warrior. Power: twin luminous blades from forearm guards.",
    # 88: Winter commander
    "Age 55, Russian features, pale skin, stern hawk-like face, silver hair in severe short cut. Cold blue eyes. Heavy winterized power armor with fur-lined collar, cracked visor pushed up. Many repair marks. Scoped heavy rifle slung across back. Colors: arctic white + faded red star + dark grey + frost + worn brass. Expression: cold iron will. Power: frost spreads from her armored gauntlets.",
    # 90: Supersonic pilot
    "Age 30, Japanese features, pale, black hair in tight practical bun, minimal makeup. Athletic slim build. Matte white and red pilot suit for aerial combat, lightweight wing pack folded on back. Colors: clean white + cherry red + matte grey + black visor + chrome. Expression: focused, pre-flight calm. Power: compressed air distortion around wing pack.",
    # 92: Chef hero
    "Age 40, stocky build, East Asian features, flour-dusted face, warm smile. Modified chef's whites with armored apron, meat cleaver and ladle holstered. Wok shield on her back. Colors: chef white + stainless steel + tomato red + herb green + flour dust. Expression: will feed you then fight for you. Power: ingredients float and transform around her.",
    # 94: Graffiti witch
    "Age 22, young Black woman, bright eyes, wide smile, paint-stained fingers. Covered in colorful paint splatters over dark streetwear, spray cans holstered like weapons. Aluminum baseball bat strapped to her back. Colors: neon pink + electric blue + toxic green + bright orange + black base. Expression: creative chaos, pure joy. Power: her painted symbols become real.",
    # 96: Battle conductor
    "Age 35, tall elegant, Eastern European features, pale skin, sharp cheekbones, dark hair in tight chignon. Formal conductor's tailcoat with golden musical note embroidery. Baton crackles with energy. Colors: formal black + gold embroidery + energy white + deep red lining. Expression: commanding, dramatic. Power: visible music notes follow her baton.",
    # 98: Memory keeper
    "Age 50, silver-haired Japanese woman, gentle lined face, calm eyes that flash with other people's experiences. Simple elegant dark clothes with single glowing crystal pendant. Colors: memory-flash gold for happy + cool blue for sad + dark clothes + crystal white + silver hair. Expression: compassionate, carrying weight of many lives. Power: ghostly scenes flicker around her pendant.",
    # 100: Emotion architect
    "Age 33, tall angular, Scandinavian features, very pale, short platinum hair, ice-blue eyes that shift color. Minimalist white outfit with geometric emotion-crystal formations growing from shoulders. Colors: deep orange crystals + cool blue eyes + white base + warm amber growth. Expression: intense concentration. Power: crystalline structures of pure emotion grow around her.",
]
