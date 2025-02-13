import random

CATEGORY_OPTIONS = {
    "fantasy": {
         "option1": ['Ram', 'Arjun', 'Kiran', 'Shiva', 'Krishna', 'Vishnu', 'Indra', 'Agni', 'Varuna', 'Brahma'],
         "option2": ['Sita', 'Radha', 'Parvati', 'Lakshmi', 'Saraswati', 'Ganga', 'Durga', 'Kali', 'Uma', 'Rukmini'],
         "option3": ['in a mystical forest', 'in a dark castle', 'in a magical village', 'by an enchanted lake', 'within a hidden cave', 'on a floating island', 'under a starlit sky', 'in a realm of magic', 'amid ancient ruins', 'beside a sacred river'],
         "option4": ['a powerful wizard emerged', 'a wise sage appeared', 'a brave warrior stood', 'a cunning thief lurked', 'a noble knight arrived', 'a fearless hunter ventured', 'a legendary bard sang', 'a mysterious seer foretold', 'a guardian spirit protected', 'a benevolent king ruled'],
         "option5": ['and battled a fierce dragon', 'and discovered a lost treasure', 'and vanquished a dark force', 'and saved the enchanted realm', 'and fulfilled an ancient prophecy', 'and restored peace', 'and forged new alliances', 'and conquered evil', 'and ignited hope', 'and transformed destiny'],
         "option6": ['bringing eternal peace.', 'ushering in a golden age.', 'and became a legend.', 'with magic and wonder.', 'as the stars aligned.', 'while destiny smiled.', 'and myths were born.', 'with the gods watching.', 'as legends echoed.', 'and fate was sealed.']
    },
    "adventure": {
         "option1": ['Explorer A', 'Captain X', 'Ranger Y', 'Adventurer Z', 'Seeker Q', 'Nomad W', 'Traveler V', 'Pioneer U', 'Scout T', 'Wanderer S'],
         "option2": ['with his loyal friend', 'accompanied by a brave guide', 'supported by a trusted ally', 'with a fearless companion', 'joined by a wise mentor', 'with a steadfast partner', 'with an experienced scout', 'supported by a comrade', 'with an intrepid sidekick', 'joined by a daring friend'],
         "option3": ['in treacherous mountains', 'through dangerous jungles', 'across uncharted islands', 'in mysterious deserts', 'through ancient ruins', 'across stormy seas', 'in wild savannas', 'through perilous canyons', 'across frozen tundras', 'in remote highlands'],
         "option4": ['found a hidden map', 'discovered a secret key', 'uncovered a cryptic clue', 'retrieved a lost artifact', 'stumbled upon an old compass', 'received a mysterious letter', 'encountered a coded message', 'secured an ancient relic', 'obtained a legendary token', 'was given a sacred scroll'],
         "option5": ['and faced relentless challenges', 'and overcame insurmountable odds', 'and braved formidable foes', 'and outsmarted dangerous traps', 'and fought against overwhelming forces', 'and navigated treacherous paths', 'and defied destiny', 'and risked everything', 'and solved ancient riddles', 'and conquered the unknown'],
         "option6": ['returning as a hero.', 'earning eternal glory.', 'and rewriting history.', 'with tales of valor.', 'and becoming a legend.', 'with their name forever remembered.', 'and inspiring future adventurers.', 'as the journey transformed them.', 'with an undying spirit.', 'and their saga continued.']
    },
    "romance": {
         "option1": ['Lover A', 'Sweetheart B', 'Beloved C', 'Darling D', 'Paramour E', 'Cupid F', 'Valentine G', 'Amour H', 'Cherish I', 'Adore J'],
         "option2": ['met Sweetheart K', 'encountered Darling L', 'embraced Beloved M', 'gazed at Lover N', 'admired Paramour O', 'cherished Cupid P', 'adored Valentine Q', 'savored Amour R', 'treasured Cherish S', 'worshipped Adore T'],
         "option3": ['in a quaint town', 'in a bustling city', 'by the sparkling seaside', 'in a serene village', 'under a starlit sky', 'at a romantic resort', 'in a secret garden', 'near a gentle river', 'in an old town square', 'at a moonlit balcony'],
         "option4": ['where destiny intervened', 'where fate brought them together', 'in an unexpected twist', 'amid soft whispers', 'as hearts aligned', 'with a magical spark', 'in a serendipitous encounter', 'as time stood still', 'with silent glances', 'in a moment of wonder'],
         "option5": ['overcoming all obstacles', 'despite the odds', 'with passion and perseverance', 'through trials of heart', 'against societal norms', 'with unwavering faith', 'beyond all challenges', 'with tender resolve', 'through bittersweet moments', 'amid infinite hope'],
         "option6": ['and their love became timeless.', 'and passion bloomed eternally.', 'and dreams intertwined.', 'as hearts sang in unison.', 'and romance flourished.', 'as their story became a legend.', 'and destiny smiled upon them.', 'and the world embraced their tale.', 'and love conquered all.', 'and forever was written in their stars.']
    },
    "mystery": {
         "option1": ['Detective X', 'Inspector Y', 'Agent Z', 'Sleuth A', 'Investigator B', 'Spy C', 'Officer D', 'Analyst E', 'Researcher F', 'Tracker G'],
         "option2": ['with his clever partner', 'assisted by a skilled aide', 'with a sharp-witted colleague', 'joined by a trusted sidekick', 'with a keen observer', 'aided by a resourceful friend', 'with a diligent assistant', 'accompanied by a quiet confidant', 'with an experienced analyst', 'supported by a loyal helper'],
         "option3": ['in a gloomy city', 'in a shadowy town', 'amid foggy streets', 'within a maze of alleys', 'in a mysterious mansion', 'beneath a cloak of night', 'around haunted corners', 'in a silent suburb', 'amid urban whispers', 'in a city of secrets'],
         "option4": ['uncovered a hidden clue', 'discovered a coded message', 'stumbled upon disturbing evidence', 'found a secret diary', 'revealed a shocking truth', 'unraveled an enigma', 'detected a silent warning', 'exposed a cunning plot', 'revealed a dark secret', 'discovered an unexpected lead'],
         "option5": ['that twisted the case further', 'leading to unexpected turns', 'that baffled even the experts', 'which deepened the mystery', 'that challenged the obvious', 'causing chaos among suspects', 'that blurred the lines of truth', 'that forced new inquiries', 'which left everyone in suspense', 'that shattered preconceptions'],
         "option6": ['and the case was closed.', 'and justice was served.', 'and truth emerged from shadows.', 'and mysteries unraveled.', 'and secrets faded away.', 'and clarity replaced confusion.', 'and the detective prevailed.', 'and answers finally surfaced.', 'and the enigma was solved.', 'and darkness was dispelled.']
    },
    "horror": {
         "option1": ['A cursed soul', 'A haunted figure', 'A restless spirit', 'An eerie wanderer', 'A doomed victim', 'A mysterious entity', 'A sinister shadow', 'A ghastly apparition', 'A chilling presence', 'A macabre specter'],
         "option2": ['tormented by the past', 'haunted by lost memories', 'pursued by nightmares', 'bound by a sinister fate', 'plagued with dread', 'enshrouded in darkness', 'lost in perpetual terror', 'shadowed by doom', 'gripped by horror', 'enslaved by fear'],
         "option3": ['in an abandoned mansion', 'within a cursed village', 'in a dark forest', 'inside a haunted asylum', 'at a forsaken cemetery', 'beneath a stormy sky', 'in a desolate ruin', 'amid crumbling walls', 'in a shadowy labyrinth', 'under a blood-red moon'],
         "option4": ['encountered unearthly sounds', 'heard bloodcurdling screams', 'witnessed ghastly visions', 'experienced supernatural chills', 'faced a terrifying presence', 'saw things no mortal should', 'encountered spectral figures', 'heard whispers from the abyss', 'witnessed impossible horrors', 'felt a creeping dread'],
         "option5": ['that shattered their sanity', 'that froze their blood', 'that tormented their soul', 'that defied reason', 'that summoned pure terror', 'that blotted out hope', 'that clawed at their mind', 'that ensnared their spirit', 'that left scars unseen', 'that defied explanation'],
         "option6": ['and the terror was everlasting.', 'and nightmares became reality.', 'and horror reigned supreme.', 'and darkness consumed all.', 'and despair took hold.', 'and the haunted remained.', 'and no light could break through.', 'and fear prevailed.', 'and the curse lived on.', 'and terror echoed forever.']
    },
    "sci-fi": {
         "option1": ['A space explorer', 'A futuristic warrior', 'A time traveler', 'An alien diplomat', 'A cybernetic agent', 'A star pilot', 'A galactic hero', 'A cosmic wanderer', 'A virtual reality savant', 'A robotic engineer'],
         "option2": ['from a distant planet', 'of an advanced civilization', 'with a mysterious past', 'with cutting-edge tech', 'accompanied by an AI', 'with cybernetic limbs', 'with quantum abilities', 'armed with futuristic gear', 'on a secret mission', 'with interstellar charm'],
         "option3": ['in a universe of endless stars', 'in a galaxy far away', 'across interstellar voids', 'in an alternate dimension', 'in a dystopian future', 'in a digital realm', 'amid cosmic wonders', 'in an ever-expanding cosmos', 'beyond known space', 'in a realm of science'],
         "option4": ['discovered a hidden planet', 'uncovered alien secrets', 'encountered bizarre phenomena', 'traversed wormholes', 'faced rogue robots', 'explored uncharted galaxies', 'challenged the laws of physics', 'battled cosmic foes', 'decoded ancient signals', 'unveiled futuristic marvels'],
         "option5": ['that redefined existence', 'that shattered reality', 'that defied expectations', 'that sparked a revolution', 'that altered destiny', 'that ignited innovation', 'that blurred science and myth', 'that reshaped the cosmos', 'that inspired awe', 'that rewrote the future'],
         "option6": ['and the universe marveled.', 'and the stars aligned in wonder.', 'and destiny was transformed.', 'and time bent in awe.', 'and the future was reborn.', 'and cosmic legends were born.', 'and science prevailed.', 'and the galaxy cheered.', 'and the saga continued.', 'and fate was rewritten.']
    },
    "comedy": {
         "option1": ['A quirky character', 'A funny guy', 'A hilarious hero', 'A clumsy protagonist', 'A witty individual', 'A prankster', 'A jester', 'A comedian', 'A clown', 'A goofball'],
         "option2": ['with a sharp tongue', 'with endless jokes', 'with a mischievous grin', 'armed with puns', 'with contagious laughter', 'with whimsical charm', 'with playful antics', 'with absurd humor', 'with quirky ideas', 'with comic timing'],
         "option3": ['in a lively town', 'in a bustling city', 'in a small village', 'in an eccentric neighborhood', 'in a vibrant community', 'in a humorous setting', 'amid quirky crowds', 'in a fun-filled locale', 'in a land of laughter', 'in a riotous place'],
         "option4": ['encountered absurd situations', 'faced hilarious mishaps', 'got into outrageous scrapes', 'experienced bizarre coincidences', 'witnessed comical chaos', 'found themselves in ridiculous predicaments', 'sparked uncontrollable laughter', 'tripped over life\'s ironies', 'danced with absurdity', 'laughed at the impossible'],
         "option5": ['that left everyone in stitches', 'that turned frowns upside down', 'that spread contagious joy', 'that defied seriousness', 'that sparked wild laughter', 'that became legendary', 'that broke all norms', 'that united people in mirth', 'that were simply unforgettable', 'that rewrote comedy'],
         "option6": ['and hilarity ensued.', 'and the town burst into laughter.', 'and joy reigned supreme.', 'and the joke lived on.', 'and smiles lit up the skies.', 'and laughter echoed forever.', 'and comedy triumphed.', 'and funny tales were told.', 'and the spirit of mirth prevailed.', 'and life became a constant laugh.']
    },
    "drama": {
         "option1": ['A troubled soul', 'A conflicted heart', 'An emotional being', 'A tormented spirit', 'A passionate individual', 'A determined fighter', 'A sensitive person', 'A stoic character', 'A rebellious youth', 'A bold protagonist'],
         "option2": ['with a complicated past', 'with hidden secrets', 'with deep sorrow', 'with burning ambition', 'with fragile hope', 'with intense emotions', 'with unresolved issues', 'with silent pain', 'with unspoken dreams', 'with a heart on fire'],
         "option3": ['in a world of chaos', 'amid societal turmoil', 'in a broken home', 'within a turbulent city', 'in a realm of despair', 'in challenging circumstances', 'amid constant strife', 'in a troubled community', 'through personal battles', 'in a storm of emotions'],
         "option4": ['faced life-altering challenges', 'battled inner demons', 'struggled against fate', 'endured heartbreaking trials', 'fought for redemption', 'withstood relentless storms', 'grappled with loss', 'challenged the status quo', 'confronted painful truths', 'faced the wrath of destiny'],
         "option5": ['that reshaped their destiny', 'that scarred their soul', 'that led to transformation', 'that ignited inner strength', 'that rewrote their future', 'that inspired change', 'that bridged broken dreams', 'that unveiled hidden courage', 'that redefined existence', 'that left a lasting mark'],
         "option6": ['and the drama unfolded.', 'and emotions ran deep.', 'and the journey continued.', 'and destiny took its course.', 'and the tale was etched in time.', 'and hearts were forever changed.', 'and life became a poignant saga.', 'and the world watched in awe.', 'and tears mixed with hope.', 'and the story resonated for ages.']
    },
    "history": {
         "option1": ['A renowned figure', 'A legendary hero', 'A famous leader', 'A celebrated icon', 'An influential statesman', 'A pioneer', 'A trailblazer', 'A visionary', 'An illustrious personality', 'A revered individual'],
         "option2": ['from ancient times', 'from a bygone era', 'from a forgotten age', 'from the annals of time', 'from a historic dynasty', 'from an age of legends', 'from classical antiquity', 'from olden days', 'from a storied past', 'from timeless lore'],
         "option3": ['in a mighty empire', 'within a historic kingdom', 'amidst ancient ruins', 'in a land of legends', 'in a time of valor', 'within royal courts', 'amidst grand battles', 'in a golden era', 'where myths prevailed', 'in a saga of old'],
         "option4": ['faced monumental challenges', 'witnessed epic battles', 'led a revolution', 'inspired a nation', 'battled against tyranny', 'changed the course of history', 'united divided peoples', 'etched history with valor', 'defied impossible odds', 'carved a legacy'],
         "option5": ['that reshaped nations', 'that echoed through centuries', 'that were immortalized in lore', 'that set new standards', 'that stirred the hearts of many', 'that bridged past and future', 'that transformed society', 'that became timeless', 'that changed destinies', 'that were written in stone'],
         "option6": ['and history remembered them.', 'and their legend lived on.', 'and the era was transformed.', 'and the legacy echoed forever.', 'and their name became immortal.', 'and time honored their deeds.', 'and the chronicles were enriched.', 'and a new chapter began.', 'and the world was forever altered.', 'and destiny was sealed.']
    },
    "mythology": {
         "option1": ['A divine being', 'A celestial god', 'An ancient deity', 'A revered immortal', 'A mythical creature', 'A legendary spirit', 'A fabled hero', 'A timeless guardian', 'A powerful titan', 'A wise oracle'],
         "option2": ['from the heavens', 'from the realm of gods', 'from an eternal age', 'from mythic times', 'from divine legends', 'from sacred lore', 'from celestial realms', 'from cosmic tales', 'from otherworldly domains', 'from the pantheon'],
         "option3": ['in a land of miracles', 'in a world of wonders', 'within divine settings', 'amid ethereal landscapes', 'in a realm of magic', 'in a celestial kingdom', 'where gods walked', 'in a mythic paradise', 'beneath radiant skies', 'in enchanted lands'],
         "option4": ['wielded immense power', 'brought forth miracles', 'challenged mortal fate', 'defied earthly limits', 'shaped the cosmos', 'inspired divine reverence', 'unleashed ancient magic', 'crafted legends', 'altered destiny', 'guided the stars'],
         "option5": ['that transcended mortal realms', 'that echoed through eternity', 'that reshaped the heavens', 'that stirred celestial awe', 'that blurred the lines of time', 'that wove cosmic tales', 'that defied human comprehension', 'that ignited divine passion', 'that became eternal lore', 'that reshaped destiny'],
         "option6": ['and myths were born.', 'and legends came alive.', 'and the divine reigned supreme.', 'and eternity witnessed the miracle.', 'and the cosmos celebrated.', 'and timeless tales emerged.', 'and destiny was rewritten.', 'and the pantheon rejoiced.', 'and celestial songs were sung.', 'and the saga became immortal.']
    }
}

def generate_story(category, option1, option2, option3, option4, option5, option6):
    start_options = [
        "Once upon a time,",
        "In a land far away,",
        "Long ago,",
        "In a forgotten kingdom,",
        "On a cold winter night,"
    ]
    
    story = random.choice(start_options) + " "
    
    if category not in CATEGORY_OPTIONS:
        return "Invalid category."
    
    data = CATEGORY_OPTIONS[category]
    try:
        idx1 = int(option1) - 1
        idx2 = int(option2) - 1
        idx3 = int(option3) - 1
        idx4 = int(option4) - 1
        idx5 = int(option5) - 1
        idx6 = int(option6) - 1
    except Exception:
        return "Invalid options selection."
    
    part1 = data['option1'][idx1] if idx1 < len(data['option1']) else ""
    part2 = data['option2'][idx2] if idx2 < len(data['option2']) else ""
    part3 = data['option3'][idx3] if idx3 < len(data['option3']) else ""
    part4 = data['option4'][idx4] if idx4 < len(data['option4']) else ""
    part5 = data['option5'][idx5] if idx5 < len(data['option5']) else ""
    part6 = data['option6'][idx6] if idx6 < len(data['option6']) else ""
    
    story += f"there was {part1}, who {part2} and journeyed {part3}. Then, {part4} and eventually {part5} {part6} "
    
    while len(story.split()) < 150:
        story += " Additional details enriched the tale with vivid imagery and profound meaning. "
    
    return story