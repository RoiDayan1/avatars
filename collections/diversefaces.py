"""DiverseFaces — 100 Diverse Portrait Avatars

Stylized semi-realistic portraits of diverse, globally-inspired individuals.
"""

NAME = "DiverseFaces"
SUBTITLE = "100 Diverse Portrait Avatars"

PROMPT_TEMPLATE = """\
A stylized semi-realistic portrait illustration of a different adult person, centered, upper body (chest-up), facing forward, soft friendly expression, clean modern look.

CHARACTER IDENTITY:
{character}

Art style: painterly digital illustration, soft brush strokes, subtle grain texture, smooth shading, slightly stylized facial features (not photorealistic), warm and inviting.

Composition:
- Square image (1:1)
- Head centered
- Chest-up framing (LinkedIn-style portrait)
- Slight tilt or relaxed posture allowed

Lighting:
- Soft, even studio lighting
- No harsh shadows
- Warm tone

Background:
- Abstract geometric or organic shapes
- Soft pastel gradients mixed with occasional vibrant accents
- Layered circles / shapes with subtle texture
- Slight vignette, smooth transitions

Mood:
- Professional, friendly, approachable, yet visually interesting and expressive

Quality:
- High resolution
- Clean edges
- Consistent style

--no photorealism, no harsh shadows, no busy background, no text, no watermark"""

# 50 Male characters (odd indices: 1, 3, 5, ... 99)
# 50 Female characters (even indices: 2, 4, 6, ... 100)

MALES = [
    # 1
    "Male, age 58, Nigerian, very dark skin, clean-shaved head, full grey beard neatly trimmed. Deep-set wise eyes, broad nose, strong jaw. Wearing a richly embroidered indigo agbada with gold thread patterns. Gold-rimmed reading glasses. Expression: warm, dignified authority.",
    # 3
    "Male, age 32, Japanese, light skin, sharp angular jaw, messy black hair with an undercut. Thin eyebrows, narrow dark eyes. Wearing a fitted charcoal turtleneck under a camel overcoat. Small silver hoop earring in left ear. Expression: calm confidence, slight smile.",
    # 5
    "Male, age 45, Indigenous Australian, deep brown skin, broad flat nose, strong brow, thick curly black hair with grey streaks. Traditional dot-paint markings on forehead in white ochre. Wearing a rust-colored linen shirt, rolled sleeves. Expression: grounded, steady gaze.",
    # 7
    "Male, age 27, Swedish, very pale skin, platinum blonde buzz cut, pale blue eyes, angular cheekbones, light stubble. Wearing an oversized moss-green hoodie with a white tee visible underneath. Small tattoo of a pine tree behind his ear. Expression: relaxed, easygoing.",
    # 9
    "Male, age 52, Moroccan, warm olive skin, salt-and-pepper beard, deep brown eyes with crow's feet, aquiline nose. Wearing a cream djellaba with intricate geometric embroidery at the collar. Leather-strap wristwatch. Expression: contemplative, gentle wisdom.",
    # 11
    "Male, age 35, Korean, pale skin, round face, soft features, thick black hair parted to one side. Wire-frame round glasses. Wearing a lavender button-down shirt with the top button open, navy blazer. Expression: friendly, approachable intellectual.",
    # 13
    "Male, age 41, Afro-Brazilian, medium brown skin, tight curly black hair faded on sides, full lips, broad nose, strong neck. Wearing a vibrant yellow linen camp-collar shirt with tropical leaf print. Gold chain necklace. Expression: bold, magnetic charisma.",
    # 15
    "Male, age 63, Sikh Indian, warm brown skin, long flowing white beard, white turban (dastar) wrapped neatly. Deep laugh lines, kind brown eyes. Wearing a deep maroon kurta with gold buttons. Expression: serene, paternal warmth.",
    # 17
    "Male, age 29, Cuban, light olive skin, wavy dark brown hair slicked back, strong jaw with stubble, hazel eyes. Wearing a fitted white guayabera with mother-of-pearl buttons. Thin gold bracelet. Expression: charming, confident smirk.",
    # 19
    "Male, age 38, Maasai-inspired, very dark skin, elongated earlobes with beaded ear ornaments, shaved head, tall and lean. Wearing a vibrant red and blue shuka (traditional cloth) draped over one shoulder. Beaded collar necklace in white, red, and blue. Expression: proud, dignified stillness.",
    # 21
    "Male, age 50, Polish, ruddy pale skin, thick salt-and-pepper mustache, deep-set grey eyes, square jaw, receding hairline. Wearing a worn brown leather jacket over a dark plaid flannel shirt. Expression: tough but kind, weathered resilience.",
    # 23
    "Male, age 26, Ethiopian, deep dark skin, high forehead, sharp cheekbones, close-cropped natural hair. Long elegant neck. Wearing a cream cable-knit sweater. Small nose stud in sterling silver. Expression: thoughtful, introspective calm.",
    # 25
    "Male, age 44, Mexican, warm brown skin, thick black hair with a few grey strands swept back, full mustache, deep brown eyes. Wearing a denim jacket over a white henley. Turquoise ring on right hand. Expression: steady, quiet strength.",
    # 27
    "Male, age 33, Filipino, warm tan skin, round friendly face, short black hair, flat nose, bright dark eyes. Wearing a salmon-pink polo shirt under a light grey cardigan. Expression: genuinely cheerful, open and approachable.",
    # 29
    "Male, age 55, Tuareg-inspired, dark brown skin, tall and lean, indigo-dyed tagelmust (turban/veil) covering lower face and head, only deep brown eyes visible. Wearing flowing indigo robes. Silver amulet visible at chest. Expression: mysterious, calm intensity in the eyes.",
    # 31
    "Male, age 37, mixed (Black/Irish), medium brown skin, wild curly auburn hair, green eyes, freckles across nose and cheeks, strong jaw. Wearing a forest-green corduroy jacket over a cream tee. Expression: artistic, warm rebelliousness.",
    # 33
    "Male, age 48, Turkish, olive skin, thick dark eyebrows, neatly trimmed black beard with silver threads, hooked nose, deep brown eyes. Wearing a tailored dark navy suit with a burgundy pocket square. Expression: refined, quietly powerful.",
    # 35
    "Male, age 30, Samoan, deep brown skin, large build, traditional pe'a (tatau) patterns visible on forearms, short black hair, wide nose, warm smile. Wearing a fitted black t-shirt, shell necklace. Expression: gentle giant, radiating warmth.",
    # 37
    "Male, age 65, Chinese, weathered tan skin, thin white hair combed back, deep wrinkles around eyes and mouth, wispy white goatee. Wearing a traditional dark blue mandarin-collar jacket (tangzhuang). Expression: serene wisdom, quiet humor in the eyes.",
    # 39
    "Male, age 28, Somali, dark brown skin, tall and lean, high cheekbones, trimmed goatee, short natural hair. Wearing a teal bomber jacket over a white crewneck. Gold-framed aviator sunglasses pushed up on forehead. Expression: cool confidence, easy smile.",
    # 41
    "Male, age 42, Greek, olive skin, thick black curly hair with silver at temples, strong jaw, five o'clock shadow, warm brown eyes. Wearing a white linen shirt unbuttoned at the collar, rolled sleeves. Leather cord necklace with a small blue evil-eye pendant. Expression: Mediterranean warmth, relaxed intensity.",
    # 43
    "Male, age 36, Jamaican, dark brown skin, long dreadlocks pulled back in a thick bundle, strong angular face, neat goatee. Wearing a burnt-orange dashiki-style shirt with intricate embroidery. Wooden bead bracelet. Expression: soulful, creative energy.",
    # 45
    "Male, age 53, Russian, pale skin, sharp features, short grey hair buzzed close, ice-blue eyes, prominent cheekbones, thin lips. Wearing a dark charcoal wool coat with a stand-up collar. Expression: stoic, intense focus softened by a hint of warmth.",
    # 47
    "Male, age 31, Navajo, warm reddish-brown skin, broad face, dark eyes, black hair in a traditional tsiiyéeł (hair bun) tied with white yarn. Wearing a turquoise-and-silver bolo tie over a denim western shirt. Expression: proud, calm centeredness.",
    # 49
    "Male, age 40, Ghanaian, very dark skin, shaved head, round face, wide nose, bright white smile. Wearing a kente-pattern vest over a crisp white shirt. Bold geometric wooden earrings. Expression: joyful, infectious energy.",
    # 51
    "Male, age 57, Scottish, ruddy pale skin with visible veins, wild grey-red eyebrows, bald on top with wispy ginger sides, full red-grey beard. Wearing a heavy dark green tweed jacket with elbow patches. Expression: gruff warmth, mischievous eyes.",
    # 53
    "Male, age 34, Vietnamese, pale-olive skin, angular face, straight black hair falling across forehead, delicate features, sharp dark eyes. Wearing an oversized vintage denim jacket covered in enamel pins over a black turtleneck. Expression: artistic, quietly intense.",
    # 55
    "Male, age 46, Berber (Amazigh), warm brown skin, close-cropped dark hair with grey at temples, strong nose, geometric henna-style tattoo on chin (traditional). Wearing a cream wool burnous (hooded cloak) over earth-toned clothes. Expression: weathered pride, quiet dignity.",
    # 57
    "Male, age 25, mixed (Korean/Nigerian), rich dark brown skin, high cheekbones, almond-shaped dark eyes, short tight curls with bleached blonde tips. Wearing a bold pattern-blocked streetwear jacket in orange and purple. Multiple ear piercings. Expression: vibrant, unapologetic confidence.",
    # 59
    "Male, age 60, Peruvian (Quechua), weathered deep brown skin, broad face, small dark eyes with deep laugh lines, short grey-black hair under a chullo (traditional knit hat with earflaps) in red and geometric patterns. Wearing a thick handwoven poncho in earth tones. Expression: ancient kindness, quiet joy.",
    # 61
    "Male, age 39, Iranian, olive skin, strong dark eyebrows, neatly trimmed beard, prominent nose, dark brown eyes. Hair swept back with a slight wave. Wearing a deep burgundy mock-neck sweater. Expression: intellectual warmth, focused.",
    # 63
    "Male, age 29, Aboriginal Australian (modern urban), dark brown skin, broad nose, curly black hair with shaved sides, bright brown eyes. Wearing a stylish black leather jacket over a graphic tee featuring indigenous dot-art design. Expression: modern pride, creative spark.",
    # 65
    "Male, age 47, Haitian, very dark skin, salt-and-pepper close-cropped hair, strong jaw, deep-set dark eyes, broad nose. Wearing a brightly patterned tropical shirt in turquoise and coral. Wooden cross pendant. Expression: warm resilience, quiet strength.",
    # 67
    "Male, age 33, Finnish, very pale skin, almost white-blonde hair in a messy top-knot, light grey eyes, high cheekbones, clean-shaven, angular jaw. Wearing a minimalist slate-blue Scandinavian-design wool pullover. Expression: calm, understated intelligence.",
    # 69
    "Male, age 51, Rajasthani Indian, warm brown skin, magnificent handlebar mustache waxed to points, bright turban in saffron orange, weathered face with strong features. Wearing a white cotton kurta with mirror-work embroidery at the collar. Expression: regal, flamboyant pride.",
    # 71
    "Male, age 36, Congolese, very dark skin, tall, lean angular face, high forehead, short natural hair. Wearing a sapeur-inspired outfit: bright pink suit jacket with matching pocket square, crisp white shirt, bold patterned bow tie. Expression: sharp, impeccable style.",
    # 73
    "Male, age 43, mixed (Native American/White), medium tan skin, long straight dark hair with grey streak, strong nose, hazel eyes, weathered features. Wearing a flannel shirt under a canvas work vest. Turquoise bracelet on left wrist. Expression: quiet observation, grounded calm.",
    # 75
    "Male, age 28, Senegalese, dark brown skin, tall, striking features, bright white teeth, short black hair with a sharp line-up. Wearing an immaculate white boubou (grand boubou) with delicate silver embroidery. Expression: elegant, effortless grace.",
    # 77
    "Male, age 54, Tibetan, weathered tan-brown skin, round face, deep wrinkles from sun and wind, small dark eyes, closely shaved grey hair. Wearing a deep maroon chuba (traditional robe) with one shoulder bare. Prayer beads around wrist. Expression: deep peace, weathered wisdom.",
    # 79
    "Male, age 31, Colombian, warm medium-brown skin, thick wavy dark hair, neatly trimmed short beard, bright brown eyes, wide nose. Wearing a colorful hand-knit ruana (poncho) over a simple grey tee. Expression: open, easygoing warmth.",
    # 81
    "Male, age 45, Māori (New Zealand), medium-brown skin, traditional tā moko (facial tattoo) with curvilinear patterns on chin and lower face, shaved head, strong brow, dark eyes. Wearing a dark blazer over a simple black tee, greenstone (pounamu) pendant. Expression: fierce pride, cultural strength.",
    # 83
    "Male, age 62, Bengali Indian, warm brown skin, thinning grey hair combed neatly, round glasses with thick frames, gentle round face. Wearing a cream-colored panjabi (kurta) with subtle gold embroidery. Expression: kindly professor, gentle curiosity.",
    # 85
    "Male, age 35, Puerto Rican, light brown skin, short curly dark hair with a fade, strong jaw, trimmed beard connecting to mustache, warm brown eyes. Wearing a guayabera-inspired modern shirt in pale blue, sleeves rolled. Gold stud earring. Expression: confident charm, easy smile.",
    # 87
    "Male, age 49, Mongolian, golden-brown skin, broad flat face, high cheekbones, narrow dark eyes, short black hair with grey at temples. Wearing a traditional deel (robe) in deep blue with orange sash, silver belt ornaments. Expression: nomadic pride, stoic calm.",
    # 89
    "Male, age 26, mixed (Afro-German), light brown skin, tight coils of dark hair with blonde highlights, green eyes, angular features, light stubble. Wearing an earth-toned patchwork jacket over a mustard sweater. Expression: artistic, gently rebellious.",
    # 91
    "Male, age 56, Thai, warm golden-brown skin, round friendly face, neat grey hair, kind dark eyes behind gold-rimmed bifocals. Wearing a deep purple silk nehru-collar shirt. Small gold Buddha pendant. Expression: gentle, paternal warmth.",
    # 93
    "Male, age 38, Iraqi Kurdish, olive skin, thick dark beard, strong nose, intense dark brown eyes, short dark hair. Wearing a traditional Kurdish vest with geometric embroidery over a white collarless shirt. Expression: fierce dignity, guarded warmth.",
    # 95
    "Male, age 30, Rwandan, very dark skin, tall lean build, narrow face, high cheekbones, short natural hair, clean-shaven. Wearing a tailored emerald-green blazer over a black mock-neck. Thin gold chain. Expression: modern elegance, ambitious focus.",
    # 97
    "Male, age 64, Inuit (Canadian), weathered brown skin, broad round face, small dark eyes almost hidden in deep smile lines, short grey hair, wispy chin whiskers. Wearing a thick cable-knit fisherman's sweater in heather grey. Expression: warm humor, eyes twinkling with stories.",
    # 99
    "Male, age 34, Egyptian, warm olive skin, short dark curly hair, strong jaw, prominent nose, well-groomed stubble, dark brown eyes. Wearing a deep teal linen shirt with gold cufflinks, collar open. Thin gold chain. Expression: suave, quietly magnetic.",
]

FEMALES = [
    # 2
    "Female, age 45, West African (Yoruba), very dark skin, elaborate gele (head wrap) in vibrant coral and gold fabric, round face, bold dark eyes, full lips. Wearing a flowing adire-dyed dress in deep indigo. Large gold hoop earrings. Expression: regal warmth, commanding presence.",
    # 4
    "Female, age 29, Japanese, pale skin, sharp elegant features, sleek black hair in a low bun with a single decorative kanzashi pin. Minimal makeup. Wearing a structured cream blazer over a silk black top. Expression: composed, quiet sophistication.",
    # 6
    "Female, age 55, Mexican (Oaxacan), warm brown skin, silver-streaked black hair in a thick braid over one shoulder, deep laugh lines, warm dark eyes. Wearing a hand-embroidered huipil blouse in bright florals on white cotton. Jade stud earrings. Expression: maternal strength, radiant kindness.",
    # 8
    "Female, age 33, mixed (Swedish/Ethiopian), light brown skin, voluminous curly dark hair, striking hazel eyes, high cheekbones, freckles. Wearing an oversized burnt-orange cardigan over a white tee, delicate gold layered necklaces. Expression: effortlessly cool, warm openness.",
    # 10
    "Female, age 62, Chinese, fair weathered skin, short silver-white hair styled in a chic pixie cut, gentle brown eyes, smile lines. Wearing a mandarin-collar silk jacket in deep plum with subtle floral brocade. Pearl drop earrings. Expression: elegant wisdom, quiet authority.",
    # 12
    "Female, age 38, Nigerian (Igbo), dark brown skin, intricate cornrow braids gathered into a high bun, angular face, sharp cheekbones, bold brows. Wearing a structured cobalt-blue wrap dress. Statement brass geometric necklace. Expression: fierce, unapologetic confidence.",
    # 14
    "Female, age 27, Finnish, very pale skin, straight platinum-blonde hair past shoulders, cool blue eyes, delicate features, light brows. Wearing a minimalist slate-grey knit sweater. Small silver stud in nostril. Expression: serene, introspective calm.",
    # 16
    "Female, age 50, Peruvian (Quechua), deep brown skin, round face, dark eyes, black hair streaked with grey under a traditional montera hat with colorful trim. Wearing a hand-woven manta (shawl) in red and orange geometric patterns over a dark blouse. Expression: resilient joy, earthy warmth.",
    # 18
    "Female, age 35, Somali, dark brown skin, long elegant neck, high cheekbones, large dark eyes, lightweight hijab in dusty rose draped loosely. Wearing a flowing olive-green dress with gold embroidery at the cuffs. Expression: graceful, quiet confidence.",
    # 20
    "Female, age 42, Greek, olive skin, thick dark curly hair loose around shoulders, strong nose, warm brown eyes, laugh lines. Wearing a white linen blouse with puffed sleeves, chunky turquoise pendant necklace. Expression: Mediterranean warmth, vivacious energy.",
    # 22
    "Female, age 31, Korean, pale skin, round face, soft features, blunt-cut black bob with micro-bangs, dark monolid eyes. Wearing an avant-garde asymmetric black top with architectural draping. Minimalist silver ear cuffs. Expression: creative edge, cool composure.",
    # 24
    "Female, age 58, Jamaican, dark brown skin, silver dreadlocks piled high in an elegant updo, wide nose, warm brown eyes, laugh lines. Wearing a vibrant wrap in sunshine yellow and green madras pattern. Large wooden disc earrings. Expression: joyful wisdom, infectious warmth.",
    # 26
    "Female, age 26, mixed (Indian/Brazilian), warm golden-brown skin, wavy dark hair with burgundy highlights, large expressive dark eyes, full lips. Wearing a cropped terracotta jacket over a sage-green silk top. Nose ring (small gold hoop). Stacked gold bangles. Expression: bold, spirited energy.",
    # 28
    "Female, age 47, Maori (New Zealand), medium-brown skin, traditional tā moko on chin (curvilinear patterns), dark eyes, thick dark hair with silver streaks pulled back. Wearing a dark structured jacket, greenstone (pounamu) pendant. Expression: ancestral strength, quiet authority.",
    # 30
    "Female, age 34, Ukrainian, pale skin, high cheekbones, bright green eyes, thick dark-blonde hair in a loose braid adorned with small wildflowers. Wearing an embroidered vyshyvanka blouse in white with red and black traditional patterns. Expression: folk warmth, gentle determination.",
    # 32
    "Female, age 40, Tuareg-inspired, dark brown skin, indigo-dyed headscarf partially covering hair, silver nose ring, dark kohl-lined eyes. Wearing layered indigo-blue robes and elaborate silver Tuareg cross pendant. Expression: desert mystery, quiet power.",
    # 34
    "Female, age 25, Filipina, warm tan skin, round face, bright dark eyes, long straight black hair with a middle part, wide smile. Wearing a modern terno-inspired blouse in soft pink with butterfly sleeves. Delicate gold chain with a small sun pendant. Expression: sunny optimism, youthful radiance.",
    # 36
    "Female, age 53, Iranian, olive skin, thick silver-streaked dark hair swept back, prominent nose, deep brown eyes, defined brows. Wearing a rich emerald-green silk shawl over dark clothing. Antique gold filigree earrings. Expression: intellectual elegance, measured strength.",
    # 38
    "Female, age 30, Rwandan, very dark skin, close-cropped natural hair, long elegant neck, high cheekbones, large dark eyes. Wearing a bright kitenge-print wrap dress in geometric orange and cobalt patterns. Bold beaded collar necklace. Expression: modern grace, confident poise.",
    # 40
    "Female, age 65, Navajo, warm reddish-brown skin, long silver hair loose over shoulders, deep wrinkles, dark eyes with weathered kindness. Wearing a handwoven Navajo blanket-style shawl in earth reds and turquoise, silver-and-turquoise squash blossom necklace. Expression: elder wisdom, deep peace.",
    # 42
    "Female, age 28, Dominican, warm medium-brown skin, voluminous tight curls, bright amber eyes, full lips, beauty mark above upper lip. Wearing a bold coral off-shoulder top and large gold bamboo earrings. Expression: vivacious, magnetic warmth.",
    # 44
    "Female, age 48, Tibetan, weathered tan skin, round face, small dark eyes with deep smile lines, black hair with grey streaks in a practical braid. Wearing a striped apron (pangden) over a dark chuba robe. Coral and turquoise bead necklace. Expression: resilient joy, mountain calm.",
    # 46
    "Female, age 36, Senegalese, dark brown skin, elaborate twisted updo with gold thread woven through, angular face, high forehead. Wearing a tailored jumpsuit in marigold yellow with wide legs. Statement brass cuff bracelet. Expression: fashion-forward confidence, regal bearing.",
    # 48
    "Female, age 52, Russian, pale skin, short wavy silver hair, striking ice-blue eyes, angular cheekbones, thin lips. Wearing a dark wool turtleneck, chunky amber pendant necklace. Expression: intellectual intensity, steely warmth.",
    # 50
    "Female, age 32, Thai, warm golden-brown skin, heart-shaped face, delicate features, straight black hair cut in a modern shag. Wearing a silk blouse in deep orchid purple, small gold temple-bell earrings. Expression: gentle, poised calm.",
    # 52
    "Female, age 43, mixed (Ghanaian/German), medium brown skin, natural hair in a large defined afro, green eyes, strong jaw, broad nose. Wearing a structured camel-colored coat, bold kente-inspired scarf. Thick-framed tortoiseshell glasses. Expression: academic confidence, approachable warmth.",
    # 54
    "Female, age 60, Mongolian, golden-brown skin, round face, narrow dark eyes, grey hair in a neat bun, weathered features. Wearing a traditional deel in deep crimson with gold embroidery, ornate silver and coral headdress. Expression: nomadic dignity, gentle fierceness.",
    # 56
    "Female, age 29, Colombian, warm olive skin, long wavy dark hair, bright brown eyes, dimples, arched brows. Wearing a colorful mochila-inspired woven vest over a white blouse. Beaded statement earrings in primary colors. Expression: lively energy, open warmth.",
    # 58
    "Female, age 39, Haitian, very dark skin, natural hair in thick twisted locs with golden cuffs, strong angular features, dark eyes. Wearing a structured white blazer and a bold printed headband. Large resin hoop earrings in red and black. Expression: creative power, unflinching gaze.",
    # 60
    "Female, age 46, Bengali Indian, warm brown skin, thick dark hair with a dramatic white streak at the temple, large expressive dark eyes, full face. Wearing a handloom cotton sari in deep mustard with red border, antique gold jhumka (bell) earrings. Expression: artistic soul, contemplative grace.",
    # 62
    "Female, age 27, mixed (Japanese/Mexican), light olive skin, dark brown hair in a short textured crop, wide dark eyes, soft round features. Wearing a vintage-style embroidered denim jacket covered in patches and pins, red bandana around neck. Expression: eclectic, adventurous spirit.",
    # 64
    "Female, age 56, Aboriginal Australian, deep dark brown skin, broad face, wide nose, grey-streaked curly hair, warm brown eyes. Wearing a vibrant art-print top featuring dot-painting inspired patterns in ochre and white. Wooden bead earrings. Expression: grounded wisdom, gentle humor.",
    # 66
    "Female, age 33, Kurdish (Iraqi), olive-tan skin, thick dark wavy hair, bold dark brows, hazel-green eyes, strong nose. Wearing traditional Kurdish dress with a sequined vest in gold and emerald over a flowing floral skirt, elaborate hair ornaments. Expression: spirited pride, fierce beauty.",
    # 68
    "Female, age 50, Inuit (Greenlandic), weathered brown skin, round face, small dark eyes, wide cheekbones, short grey-black hair. Wearing an anorak with traditional beadwork in bright colors, kamik-style boots visible. Expression: arctic resilience, humor in the eyes.",
    # 70
    "Female, age 24, Kenyan, dark brown skin, shaved head with a tiny geometric pattern buzzed in, long elegant neck, large dark eyes, high cheekbones. Wearing a draped asymmetric top in burnt sienna, multiple thin gold hoop earrings climbing both ears. Expression: bold minimalism, striking confidence.",
    # 72
    "Female, age 41, mixed (Polish/Vietnamese), light skin with warm undertones, dark hair in a sleek low ponytail, almond-shaped grey-green eyes, angular features. Wearing a deep olive silk blouse with a mandarin collar. Subtle jade stud earrings. Expression: measured sophistication, quiet intensity.",
    # 74
    "Female, age 63, Egyptian, warm olive skin, silver hair in a short elegant wave, dark eyes lined with subtle kohl, prominent nose, dignified bearing. Wearing a richly embroidered kaftan in deep burgundy and gold. Antique scarab pendant necklace. Expression: ancient grace, matriarchal presence.",
    # 76
    "Female, age 35, Afro-Latina (Brazilian), medium-brown skin, tight coils of dark hair with golden highlights, bright brown eyes, wide nose, full lips, dimple on left cheek. Wearing a bold geometric-print wrap top in teal and coral. Large wooden circle earrings. Expression: vibrant joy, magnetic personality.",
    # 78
    "Female, age 44, Afghan (Hazara), light brown skin, distinctive Central Asian features, high cheekbones, almond-shaped dark eyes, dark hair under a loosely draped silk scarf in deep teal. Wearing an embroidered chapan-style jacket in rich reds and blues. Expression: quiet resilience, soulful depth.",
    # 80
    "Female, age 28, Maasai-inspired, very dark skin, shaved head, elaborate beaded headband and cascading beaded collar necklace in red, white and blue. Long elegant neck, large dark eyes. Wearing a draped red shuka over one shoulder. Expression: timeless grace, proud beauty.",
    # 82
    "Female, age 37, mixed (Irish/Chinese), pale skin with warm undertones, wavy auburn hair with a single silver streak, bright green eyes, spattering of freckles, angular cheekbones. Wearing a peacock-blue silk blouse, antique locket necklace. Expression: enigmatic, warm curiosity.",
    # 84
    "Female, age 51, Indonesian (Javanese), warm brown skin, round gentle face, dark eyes, black hair pulled back with a decorative batik headband. Wearing a traditional kebaya blouse in ivory lace over a rich brown batik skirt. Gold filigree earrings. Expression: maternal serenity, cultural pride.",
    # 86
    "Female, age 26, Eritrean, dark brown skin, elaborate braided hairstyle (cornrows into an upswept crown), angular face, large dark eyes, full lips. Wearing a modern interpretation of a zuria (white cotton dress) with colorful embroidered borders, gold coffee-bean pendant. Expression: youthful elegance, spirited energy.",
    # 88
    "Female, age 59, Ainu (Japanese indigenous), tan skin, round face, deep-set brown eyes, thick wavy grey-black hair, faint traditional tattoo patterns around lips. Wearing layered robes in indigo with geometric attush (bark-cloth) patterns. Expression: ancestral warmth, gentle resilience.",
    # 90
    "Female, age 30, Lebanese, light olive skin, thick dark hair with loose waves, striking dark eyes, defined brows, strong nose, red lips. Wearing a fitted black blazer over a crimson silk top. Gold statement hoops. Expression: Mediterranean confidence, polished allure.",
    # 92
    "Female, age 47, Xhosa (South African), dark brown skin, elaborate beaded headpiece and face paint (white dots on cheeks), strong features, dark eyes. Wearing a traditional blanket wrap in ochre and black patterns. Heavy brass arm cuffs. Expression: ceremonial dignity, deep cultural roots.",
    # 94
    "Female, age 32, mixed (Samoan/Japanese), warm tan skin, thick wavy dark hair to shoulders, round face blending Pacific and East Asian features, dark eyes, wide nose. Wearing a modern structured top in deep plum with subtle tapa-cloth pattern. Frangipani flower tucked behind ear. Expression: island warmth, gentle strength.",
    # 96
    "Female, age 55, Amazigh (Berber), warm brown skin, dark eyes lined with kohl, silver-streaked dark hair covered loosely with a patterned headscarf, traditional chin tattoo (geometric lines). Wearing a layered dress with silver fibula brooch. Expression: desert wisdom, enduring pride.",
    # 98
    "Female, age 40, mixed (Nigerian/Norwegian), medium-dark skin, wild natural curly hair in a large afro, striking blue eyes, strong jaw, broad nose. Wearing a tailored mustard-yellow blazer over a black turtleneck. Bold resin geometric earrings. Expression: commanding presence, creative fire.",
    # 100
    "Female, age 34, Guatemalan (Maya), warm brown skin, round face, high cheekbones, dark eyes, black hair in a thick braid interwoven with colorful ribbons. Wearing a hand-woven huipil in brilliant blues and reds with bird and flower motifs. Jade ear studs. Expression: vibrant heritage, quiet determination.",
]
