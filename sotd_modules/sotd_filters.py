def main_cat(name):
    Category = ""

    jeans_names = ['jean','jeans']
    jeans_negatives = ['potato','shirt']
    if any(x.lower() in name.lower() for x in jeans_names) and not any(x.lower() in name.lower() for x in jeans_negatives):
        Category = "Jeans"

    knitwear_names = ['KNIT','JUMPER','SWEATER','CREW','RAGLAN SWEAT','HOODIE','SWEATSHIRT','HIGH NECK KNIT','TEXTURED KNIT','Cardigan','turtleneck','poncho']
    knitwear_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in knitwear_names) and not any(x.lower() in name.lower() for x in knitwear_negatives):
        Category = "Knitwear"

    jacket_names = ['COAT','JACKET','BLAZER','PEACOAT','COATIGAN','GILET','CAPE','PONCHO','KIMONO',' MAC','PARKA','biker']
    jacket_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in jacket_names) and not any(x.lower() in name.lower() for x in jacket_negatives):
        Category = "Jackets"

    shorts_names = ['Shorts']
    shorts_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in shorts_names) and not any(x.lower() in name.lower() for x in shorts_negatives):
        Category = "Shorts"

    shirts_names = ['Shirt','Polo']
    shirts_negatives = ['Tee','T-']
    if any(x.lower() in name.lower() for x in shirts_names) and not any(x.lower() in name.lower() for x in shirts_negatives):
        Category = "Shirts"

    top_names = [' TOP','T-SHIRT','TEE','VEST ','CAMISOLE','CAMI','SPARKLY TOP',' tops','blouse','shirt','tanktop','tank top','tunic']
    top_negatives = ['bikini','test']
    if any(x.lower() in name.lower() for x in top_names) and not any(x.lower() in name.lower() for x in top_negatives):
        Category = "Tops"

    tshirt_names = ['T-SHIRT','TEE',"T Shirt"]
    tshirt_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in tshirt_names) and not any(x.lower() in name.lower() for x in tshirt_negatives):
        Category = "T-Shirts"

    trouser_names = ['TROUSERS','trouser','DUNGAREES','HOT PANTS','LEGGINGS','JOGGERS','CULOTTES','TRACK PANTS','FLARES','CHINO','cargo','harem','bottoms','jog pants']
    trouser_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in trouser_names) and not any(x.lower() in name.lower() for x in trouser_negatives):
        Category = "Trousers"

    activewear_names = ['hoodie','jogging','sweatshirt','sweatshort','tracksuit','track pants','hoody','track top']
    activewear_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in activewear_names) and not any(x.lower() in name.lower() for x in activewear_negatives):
        Category = "Activewear"

    suit_names = ['suit','suits','tuxedo']
    suit_negatives = ['track','sweat']
    if any(x.lower() in name.lower() for x in suit_names) and not any(x.lower() in name.lower() for x in suit_negatives):
        Category = "Suits"

    underwear_names = ['boxers','breifs','socks','vest','undershirt','underwear']
    underwear_negatives = ['test','testing']
    if any(x.lower() in name.lower() for x in underwear_names) and not any(x.lower() in name.lower() for x in underwear_negatives):
        Category = "Underwear"

    beachwear_names = ['beach','boardshorts','trunks','bikini','kaftan','monokini','swimsuit','sarong']
    beachwear_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in beachwear_names) and not any(x.lower() in name.lower() for x in beachwear_negatives):
        Category = "Beachwear"

    nightwear_names = ['dressing gown','robe','pyjama','nightgown','sleepshirt',' pj','Nightie']
    nightwear_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in nightwear_names) and not any(x.lower() in name.lower() for x in nightwear_negatives):
        Category = "Nightwear"

    accessories_names = ['wallet','belt','scarf','handkerchief','hat',' tie','sunglasses','watch','cufflink','glove','case','hair','purse','umbrella','hat']
    accessories_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in accessories_names) and not any(x.lower() in name.lower() for x in accessories_negatives):
        Category = "Accessories"

    jewellery_names = ['ring','bracelet','necklace','brooch','earring','ear ring']
    jewellery_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in jewellery_names) and not any(x.lower() in name.lower() for x in jewellery_negatives):
        Category = "Jewellery"

    bags_names = ['bag','case','luggage','suitcase','backpack','breifcase','messenger bag','holdall','shoulder bag','clutch','work bag','tote','shopper bag']
    bags_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in bags_names) and not any(x.lower() in name.lower() for x in bags_negatives):
        Category = "Bags"

    dresses_names = ['dress','ballgown','tunic']
    dresses_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in dresses_names) and not any(x.lower() in name.lower() for x in dresses_negatives):
        Category = "Dresses"

    skirt_names = ['skirt']
    skirt_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in skirt_names) and not any(x.lower() in name.lower() for x in skirt_negatives):
        Category = "Skirts"

    lingerie_names = ['basque','bustier','corset','bodysuit','bra','brief','camisole']
    lingerie_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in lingerie_names) and not any(x.lower() in name.lower() for x in lingerie_negatives):
        Category = "Lingerie"

    hosiery_names = ['socks','stockings','tights']
    hosiery_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in hosiery_names) and not any(x.lower() in name.lower() for x in hosiery_negatives):
        Category = "Hosiery"

    jumpsuit_names = ['jumpsuit','playsuit']
    jumpsuit_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in jumpsuit_names) and not any(x.lower() in name.lower() for x in jumpsuit_negatives):
        Category = "Jumpsuits"

    boots_names = ['boot']
    boots_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in boots_names) and not any(x.lower() in name.lower() for x in boots_negatives):
        Category = "Boots"

    trainers_names = ['trainers']
    trainers_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in trainers_names) and not any(x.lower() in name.lower() for x in trainers_negatives):
        Category = "Trainers"

    heels_names = ['clogs','wedge court','mules','platform','stilettos','wedge sandals','heels']
    heels_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in heels_names) and not any(x.lower() in name.lower() for x in heels_negatives):
        Category = "Heels"

    flats_names = ['pump','sandal','ballet flat','espadrilles','sandals','flip-flops','flip flops','loafers','moccasins','slipper','pumps']
    flats_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in flats_names) and not any(x.lower() in name.lower() for x in flats_negatives):
        Category = "Flats"

    slipons_names = ['slip ons','slip-ons','slipons','deck shoes','boat shoes','espadrilles','loafers','monk shoes','slippers']
    slipons_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in slipons_names) and not any(x.lower() in name.lower() for x in slipons_negatives):
        Category = "Slip-Ons"

    laceups_names = ['brogues','derbies','oxford','lace-ups','lace ups']
    laceups_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in laceups_names) and not any(x.lower() in name.lower() for x in laceups_negatives):
        Category = "Lace-Ups"

    sandals_names = ['flip flops','flip-flops','leather sandals','sandals']
    sandals_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in sandals_names) and not any(x.lower() in name.lower() for x in sandals_negatives):
        Category = "Sandals"

    shoes_names = ['shoe']
    shoes_negatives = ['testing','test']
    if any(x.lower() in name.lower() for x in shoes_names) and not any(x.lower() in name.lower() for x in shoes_negatives):
        Category = "Shoes"

    return Category

def sub_cat(name):
    Category = ""
    # General Jeans Category
    jeans_names = ['jean','jeans']
    jeans_negatives = ['potato','shirt']
    filtering_jeans = any(x.lower() in name.lower() for x in jeans_names) and not any(x.lower() in name.lower() for x in jeans_negatives)
    if filtering_jeans and "bootcut" in name.lower():
        Category = "Bootcut Fit"
    elif filtering_jeans and "relaxed" in name.lower():
        Category = "Relaxed Fit"
    elif filtering_jeans and "straight" in name.lower():
        Category = "Straight-leg Fit"
    elif filtering_jeans and "tapered" in name.lower():
        Category = "Tapered Fit"
    elif filtering_jeans and "crop" in name.lower():
        Category = "Cropped"
    elif filtering_jeans and "boyfriend" in name.lower():
        Category = "Boyfriend"
    elif filtering_jeans and "flare" in name.lower():
        Category = "Flared"
    elif filtering_jeans and "wide" in name.lower():
        Category = "Wide Fit"
    elif filtering_jeans and "lose" in name.lower():
        Category = "Loose Fit"
    elif filtering_jeans and "stretched" in name.lower():
        Category = "Stretched Fit"
    elif filtering_jeans and "loose" in name.lower():
        Category = "First Category"
    # Attribute which can be both and above category and a stand alone
    if filtering_jeans and "skinny" in name.lower():
        if not Category:
            Category = "Skinny Fit"
    # Attribute which can be both and above category and a stand alone
    if filtering_jeans and "slim" in name.lower():
        if not Category:
            Category = "Slim Fit"
    # Final generalisation to catch non-matching sub-category jeans
    if not Category and filtering_jeans:
            Category = "Jeans"
    # Seperate Mens/Women's/boys/girls if gender specific


# SWEATERS AND KNITWEAR
# cardigans
# crew neck jumpers
# sleeveless jumpers
# turtlenecks
# v-neck jumpers
# zipped sweaters
#
# KNITWEAR
# cardigans
# jumpers
# ponchos
# sleeveless jumpers
# turtlenecks
# zipped sweaters

    # General Knitwear Category
    knitwear_names = ['KNIT','JUMPER','SWEATER','CREW','RAGLAN SWEAT','HOODIE','SWEATSHIRT','HIGH NECK KNIT','TEXTURED KNIT','Cardigan','turtleneck','poncho']
    knitwear_negatives = ['testing','test']
    filtering_knitwear = any(x.lower() in name.lower() for x in knitwear_names) and not any(x.lower() in name.lower() for x in knitwear_negatives)
    if filtering_knitwear and "cardigan" in name.lower():
        Category = "Cardigans"
    elif filtering_knitwear and "crew" in name.lower() and "jumper" in name.lower():
        Category = "Crew Neck Jumpers"
    elif filtering_knitwear and "sleeveless" in name.lower() and "jumper" in name.lower():
        Category = "Sleeveless Jumpers"
    elif filtering_knitwear and "turtleneck" in name.lower():
        Category = "Turtlenecks"
    elif filtering_knitwear and "v-neck" in name.lower() and "jumper" in name.lower():
        Category = "V-Neck Jumpers"
    elif filtering_knitwear and "poncho" in name.lower():
        Category = "Ponchos"
    # Attribute which can be both and above category and a stand alone
    if filtering_knitwear and "zip" in name.lower() and ("jumper" in name.lower() or "sweater" in name.lower()):
        if not Category:
            Category = "Zipped Jumpers"
    # Final generalisation to catch non-matching sub-category Knitwear
    if not Category and filtering_knitwear and "jumper" in name.lower():
        Category = "Jumpers"
    if not Category and filtering_knitwear:
        Category = "Knitwear"
    # Seperate Mens/Women's/boys/girls if gender specific


# JACKETS
# blazers
# casual jackets
# leather jackets
# parka jackets
# waistcoats and gilets
#
# JACKETS
# blazers and suit jackets
# casual jackets
# denim jackets
# fur jackets
# leather jackets
# padded and down jackets
# waistcoats and gilets
#
# COATS
# long coats
# parka coats
# raincoats and trench coats
# short coats
#
# COATS
# capes
# fur coats
# long coats
# parka coats
# raincoats and trench coats
# short coats

    # General Jackets Category
    jacket_names = ['COAT','JACKET','BLAZER','PEACOAT','COATIGAN','GILET','CAPE','PONCHO','KIMONO',' MAC','PARKA','biker']
    jacket_negatives = ['testing','test']
    filtering_jacket = any(x.lower() in name.lower() for x in jacket_names) and not any(x.lower() in name.lower() for x in jacket_negatives)
    if filtering_jacket and "blazer" in name.lower():
        Category = "Blazers"
    elif filtering_jacket and "bomber" in name.lower():
        Category = "Casual Jackets"
    elif filtering_jacket and "leather" in name.lower() and ("jacket" in name.lower() or"coat" in name.lower()):
        Category = "Leather Jackets"
    elif filtering_jacket and "parka" in name.lower():
        Category = "Parka Jackets"
    elif filtering_jacket and ("waistcoat" in name.lower() or "gilets" in name.lower()):
        Category = "Waistcoats & Gilets"
    elif filtering_jacket and "suit" in name.lower() and "jacket" in name.lower():
        Category = "Suit Jackets"
    elif filtering_jacket and "denim" in name.lower() and "jacket" in name.lower():
        Category = "Denim Jackets"
    elif filtering_jacket and "cape" in name.lower():
        Category = "Capes"
    elif filtering_jacket and "fur" in name.lower() and ("jacket" in name.lower() or"coat" in name.lower()):
        Category = "Fur Jackets"
    elif filtering_jacket and ("raincoat" in name.lower() or "trench" in name.lower()):
        Category = "Raincoats & Trenchcoats"
    elif filtering_jacket and "padded" in name.lower() and "down" in name.lower():
        Category = "Padded & Down Jackets"
    # Final generalisation to catch non-matching sub-category Jackets
    if not Category and filtering_jacket and "jacket" in name.lower():
        Category = "Jackets"
    # Seperate Mens/Women's/boys/girls if gender specific

# SHORTS
# bermuda shorts
# cargo shorts
# denim shorts
# formal shorts
# long and knee-length shorts
# mini shorts
#
# SHORTS
# bermuda shorts
# cargo shorts
# casual shorts
# chino shorts

    # General Shorts Category
    shorts_names = ['Shorts']
    shorts_negatives = ['testing','test']
    filtering_shorts = any(x.lower() in name.lower() for x in shorts_names) and not any(x.lower() in name.lower() for x in shorts_negatives)
    if filtering_shorts and "bermuda" in name.lower():
        Category = "Bermuda Shorts"
    elif filtering_shorts and "cargo" in name.lower():
        Category = "Cargo Shorts"
    elif filtering_shorts and "denim" in name.lower():
        Category = "Denim Shorts"
    elif filtering_shorts and "formal" in name.lower():
        Category = "Formal Shorts"
    elif filtering_shorts and ("long" in name.lower() or "knee" in name.lower()):
        Category = "Kneelength Shorts"
    elif filtering_shorts and "mini" in name.lower():
        Category = "Mini Shorts"
    elif filtering_shorts and "chino" in name.lower():
        Category = "Chino Shorts"
    # Final generalisation to catch non-matching sub-category Shorts
    if not Category and filtering_shorts:
        Category = "Shorts"
    # Seperate Mens/Women's/boys/girls if gender specific

# SHIRTS
# casual shirts
# formal shirts

    # Mens Shirts Category
    shirts_names = ['Shirt','Polo']
    shirts_negatives = ['Tee','T-']
    filtering_shirts = any(x.lower() in name.lower() for x in shirts_names) and not any(x.lower() in name.lower() for x in shirts_negatives)
    if filtering_shirts and 'formal' in name.lower():
        Category = "Formal Shirts"
    elif filtering_shirts and 'polo' in name.lower():
        Category = "Polo Shirts"
    # Final generalisation to catch non-matching sub-category Shirts
    if not Category and filtering_shirts:
        Category = "Shirts"
    # Seperate Mens/Women's/boys/girls if gender specific

# TOPS
# blouses
# long-sleeved tops
# shirts
# short-sleeve tops
# sleeveless and tank tops
# t-shirts

    # Womens Tops Category
    top_names = [' TOP','T-SHIRT','TEE','VEST ','CAMISOLE','CAMI','SPARKLY TOP',' tops','blouse','shirt','tanktop','tank top','tunic']
    top_negatives = ['bikini','test']
    filtering_top = any(x.lower() in name.lower() for x in top_names) and not any(x.lower() in name.lower() for x in top_negatives)
    if filtering_top and "blouse" in name.lower():
        Category = "Blouses"
    elif filtering_top and "shirt" in name.lower() and not "t-" in name.lower() and not "tee shirt" in name.lower() and not "t shirt" in name.lower():
        Category = "Shirts"
    elif filtering_top and ("t-shirt" in name.lower() or "tee" in name.lower() or "t shirt" in name.lower()):
        Category = "T-Shirts"
    elif filtering_top and ("tanktop" in name.lower() or "tank top" in name.lower()):
        Category = "Tank tops"
    elif filtering_top and "tunic" in name.lower():
        Category = "Tunic tops"
    # Attribute which can be both and above category and a stand alone
    if filtering_top and "long sleeve" in name.lower() and ("top" in name.lower() or "shirt" in name.lower()):
        if not Category:
            Category = "Long Sleeved"
        else:
            Category = Category + "," + "Long Sleeved"
    if filtering_top and "short sleeve" in name.lower() and ("top" in name.lower() or "shirt" in name.lower()):
        if not Category:
            Category = "Short Sleeved"
        else:
            Category = Category + "," + "Short Sleeved"
    if filtering_top and "sleeveless" in name.lower() and ("top" in name.lower() or "shirt" in name.lower()):
        if not Category:
            Category = "Sleeveless"
    # Final generalisation to catch non-matching sub-category Tops
    if not Category and filtering_top and "top" in name.lower():
        Category = "Tops"
    # Seperate Mens/Women's/boys/girls if gender specific

# T-SHIRTS
# long-sleeve t-shirts
# polo shirts
# short sleeve t-shirts
# sleeveless t-shirts

    # Mens T-Shirts Category
    tshirt_names = ['T-SHIRT','TEE',"T Shirt"]
    tshirt_negatives = ['testing','test']
    filtering_tshirt = any(x.lower() in name.lower() for x in tshirt_names) and not any(x.lower() in name.lower() for x in tshirt_negatives)
    # Attribute which can be both and above category and a stand alone
    if filtering_tshirt and "long sleeve" in name.lower() and ("top" in name.lower() or "shirt" in name.lower()):
        if not Category:
            Category = "T-Long Sleeved"
        else:
            Category = Category + "," + "T-Long Sleeved"
    if filtering_tshirt and "short sleeve" in name.lower() and ("top" in name.lower() or "shirt" in name.lower()):
        if not Category:
            Category = "T-Short Sleeved"
        else:
            Category = Category + "," + "T-Short Sleeved"
    if filtering_tshirt and "sleeveless" in name.lower() and ("top" in name.lower() or "shirt" in name.lower()):
        if not Category:
            Category = "T-Sleeveless"
        else:
            Category = Category + "," + "T-Sleeveless"
    # Final generalisation to catch non-matching sub-category T-Shirts
    if not Category and filtering_tshirt:
        Category = "T-Shirts"
    # Seperate Mens/Men's/boys/girls if gender specific

# TROUSERS
# casual trousers
# formal trousers
#
# TROUSERS
# cargo trousers
# cropped trousers
# full-length trousers
# harem pants
# leggings
# skinny trousers
# straight-leg trousers
# wide-leg and palazzo trousers

    # General Trousers Category
    trouser_names = ['TROUSERS','trouser','DUNGAREES','HOT PANTS','LEGGINGS','JOGGERS','CULOTTES','TRACK PANTS','FLARES','CHINO','cargo','harem','bottoms','jog pants']
    trouser_negatives = ['testing','test']
    filtering_trouser = any(x.lower() in name.lower() for x in trouser_names) and not any(x.lower() in name.lower() for x in trouser_negatives)
    if filtering_trouser and "formal" in name.lower():
        Category = "Fromal Trousers"
    elif filtering_trouser and "cargo" in name.lower() and ("pants" in name.lower() or "trousers" in name.lower()):
        Category = "Cargo Pants"
    elif filtering_trouser and "harem" in name.lower() and "pants" in name.lower():
        Category = "Harem Pants"
    elif filtering_trouser and "leggings" in name.lower():
        Category = "Leggings"
    elif filtering_trouser and "wide" in name.lower() or "palazzo" in name.lower():
        Category = "Wide Leg Trousers"
    elif filtering_trouser and "casual" in name.lower():
        Category = "Casual Trousers"
    elif filtering_trouser and ("jog" in name.lower() or "bottoms" in name.lower()):
        Category = "Jogging Bottoms"
    # Attribute which can be both and above category and a stand alone
    if filtering_trouser and "skinny" in name.lower():
        if not Category:
            Category = "Skinny Fit"
    # Attribute which can be both and above category and a stand alone
    if filtering_trouser and "slim" in name.lower():
        if not Category:
            Category = "Slim Fit"
    # Final generalisation to catch non-matching sub-category jeans
    if not Category and filtering_trouser:
            Category = "Trousers"
    # Seperate Mens/Women's/boys/girls if gender specific

# ACTIVEWEAR
# hoodies
# jogging bottoms
# sweatshirts
# sweatshorts
# tracksuits
#
# ACTIVEWEAR
# hoodies
# sweatshirts
# track pants and jogging bottoms
# tracksuits

    # General Activewear Category
    activewear_names = ['hoodie','jogging','sweatshirt','sweatshort','tracksuit','track pants','hoody','track top']
    activewear_negatives = ['testing','test']
    filtering_activewear = any(x.lower() in name.lower() for x in activewear_names) and not any(x.lower() in name.lower() for x in activewear_negatives)
    if filtering_activewear and "hood" in name.lower():
        Category = "Hoodies"
    elif filtering_activewear and "jogging" in name.lower() and ("pants" in name.lower() or "bottom" in name.lower()):
        Category = "Jogging Pants"
    elif filtering_activewear and "sweat" in name.lower() and ("shirt" in name.lower() or "top" in name.lower()):
        Category = "Sweatshirts"
    elif filtering_activewear and "sweatshorts" in name.lower():
        Category = "Sweatshorts"
    elif filtering_activewear and "track" in name.lower() and ("suit" in name.lower() or "top" in name.lower()):
        Category = "Tracksuits"
    # Final generalisation to catch non-matching sub-category jeans
    if not Category and filtering_activewear:
            Category = "Activewear"
    # Seperate Mens/Women's/boys/girls if gender specific

# SUITS
# skirt suits
# trouser suits
#
# SUITS
# three-piece suits
# tuxedos and evening suits
# two-piece suits

    # General Suits Category
    suit_names = ['suit','suits','tuxedo']
    suit_negatives = ['track','sweat']
    filtering_suit = any(x.lower() in name.lower() for x in suit_names) and not any(x.lower() in name.lower() for x in suit_negatives)
    if filtering_suit and "skirt" in name.lower():
        Category = "Skirt Suits"
    elif filtering_suit and "trouser" in name.lower():
        Category = "Trouser Suits"
    elif filtering_suit and "three" in name.lower() and ("piece" in name.lower() or "-piece" in name.lower()):
        Category = "Three-Piece Suits"
    elif filtering_suit and "two" in name.lower() and "piece" in name.lower():
        Category = "Two-Piece Suits"
    elif filtering_suit and "tuxedo" in name.lower() or ("evening" in name.lower() and "suit" in name.lower()):
        Category = "Tuxedos & Evening Suits"
    # Final generalisation to catch non-matching sub-category jeans
    if not Category and filtering_suit:
            Category = "Suits"
    # Seperate Mens/Women's/boys/girls if gender specific

# UNDERWEAR
# boxers
# briefs
# socks
# undershirts and vests

    # Men's Underwear Category
    underwear_names = ['boxers','breifs','socks','vest','undershirt','underwear']
    underwear_negatives = ['test','testing']
    filtering_underwear = any(x.lower() in name.lower() for x in underwear_names) and not any(x.lower() in name.lower() for x in underwear_negatives)
    if filtering_underwear and "boxers" in name.lower():
        Category = "Boxer Shorts"
    elif filtering_underwear and "briefs" in name.lower():
        Category = "Briefs"
    elif filtering_underwear and "socks" in name.lower():
        Category = "Socks"
    elif filtering_underwear and ("undershirt" in name.lower() or "vest" in name.lower()):
        Category = "Undershirts & Vests"
    # Final generalisation to catch non-matching sub-category jeans
    if not Category and filtering_underwear:
            Category = "Underwear"
    # Seperate Mens/Women's/boys/girls if gender specific

# BEACHWEAR
# beach towels
# boardshorts
# trunks
#
# BEACHWEAR
# beach towels
# bikinis
# kaftans
# monokinis and one-piece swimsuits
# sarongs

    # General Jewellery Category
    beachwear_names = ['beach','boardshorts','trunks','bikini','kaftan','monokini','swimsuit','sarong']
    beachwear_negatives = ['testing','test']
    filtering_beachwear = any(x.lower() in name.lower() for x in beachwear_names) and not any(x.lower() in name.lower() for x in beachwear_negatives)
    if filtering_beachwear and "towel" in name.lower():
        Category = "Beach Towels"
    elif filtering_beachwear and "board" in name.lower() and "shorts" in name.lower():
        Category = "Boardshorts"
    elif filtering_beachwear and "trunks" in name.lower():
        Category = "Trunks"
    elif filtering_beachwear and "sweatshorts" in name.lower():
        Category = "Sweatshorts"
    elif filtering_beachwear and "bikini" in name.lower():
        Category = "Bikinis"
    elif filtering_beachwear and "kaftan" in name.lower():
        Category = "Kaftans"
    elif filtering_beachwear and "sarongs" in name.lower():
        Category = "Sarongs"
    elif filtering_beachwear and ("monokin" in name.lower() or "one-piece" in name.lower()):
        Category = "Monokinis & One-Piece Swimsuits"
    # Final generalisation to catch non-matching sub-category Jewellery
    if not Category and filtering_beachwear:
            Category = "Jewellery"
    # Seperate Mens/Women's/boys/girls if gender specific

# NIGHTWEAR
# dressing gowns and robes
# pyjamas
#
# NIGHTWEAR
# nightgowns and sleepshirts
# pyjamas
# robes

    # General Nightwear Category
    nightwear_names = ['dressing gown','robe','pyjama','nightgown','sleepshirt',' pj','Nightie']
    nightwear_negatives = ['testing','test']
    filtering_nightwear = any(x.lower() in name.lower() for x in nightwear_names) and not any(x.lower() in name.lower() for x in nightwear_negatives)
    if filtering_nightwear and "dressing gown" in name.lower():
        Category = "Dressing Gowns & Robes"
    elif filtering_nightwear and ("pyjama" in name.lower() or "pj" in name.lower()):
        Category = "Pyjamas"
    elif filtering_nightwear and ("nightgown" in name.lower() or 'sleepshirt' in name.lower() or 'nightie' in name.lower()):
        Category = "Nightgowns & Sleepshirts"
    # Final generalisation to catch non-matching sub-category Nightwear
    if not Category and filtering_nightwear:
            Category = "Nightwear"
    # Seperate Mens/Women's/boys/girls if gender specific


# men’s accessories
# wallets
# belts
# scarves and handkerchiefs
# hats
# ties
# sunglasses
# watches
# cufflinks
# gloves
#
# women’s accessories
# cases
# sunglasses
# belts
# gloves
# hair
# scarves
# coin purses and wallets
# watches
# hats
# umbrellas

    # General Accessories Category
    accessories_names = ['wallet','belt','scarf','handkerchief','hat',' tie','sunglasses','watch','cufflink','glove','case','hair','purse','umbrella','hat']
    accessories_negatives = ['testing','test']
    filtering_accessories = any(x.lower() in name.lower() for x in accessories_names) and not any(x.lower() in name.lower() for x in accessories_negatives)
    if filtering_accessories and "wallet" in name.lower():
        Category = "Wallets"
    elif filtering_accessories and ("wallet" in name.lower() or "purse" in name.lower()):
        Category = "Purses and Wallets"
    elif filtering_accessories and ("hat" in name.lower() or 'cap' in name.lower()):
        Category = "Hats"
    elif filtering_accessories and "sunglasses" in name.lower():
        Category = "Sunglasses"
    elif filtering_accessories and "belts" in name.lower():
        Category = "Belts"
    elif filtering_accessories and "gloves" in name.lower():
        Category = "Gloves"
    elif filtering_accessories and "watch" in name.lower():
        Category = "Watches"
    elif filtering_accessories and ("scarf" in name.lower() or "handkerchief" in name.lower()):
        Category = "Scarves and Handkerchiefs"
    elif filtering_accessories and "scraf" in name.lower():
        Category = "Scarf"
    elif filtering_accessories and "tie" in name.lower():
        Category = "Ties"
    elif filtering_accessories and "cufflink" in name.lower():
        Category = "Cufflinks"
    elif filtering_accessories and "umbrella" in name.lower():
        Category = "Umbrellas"
    elif filtering_accessories and "case" in name.lower():
        Category = "Cases"
    elif filtering_accessories and "hair" in name.lower():
        Category = "Hair Accessories"
    # Final generalisation to catch non-matching sub-category Accessories
    if not Category and filtering_accessories:
            Category = "Accessories"
    # Seperate Mens/Women's/boys/girls if gender specific

# men’s jewellery
# rings
# bracelets
# necklaces
#
# women’s jewellery
# brooches
# bracelets
# earrings
# necklaces
# rings

    # General Jewellery Category
    jewellery_names = ['ring','bracelet','necklace','brooch','earring','ear ring']
    jewellery_negatives = ['testing','test']
    filtering_jewellery = any(x.lower() in name.lower() for x in jewellery_names) and not any(x.lower() in name.lower() for x in jewellery_negatives)
    if filtering_jewellery and "ring" in name.lower() and not "ear" in name.lower() and not "nose" in name.lower():
        Category = "Rings"
    elif filtering_jewellery and "bracelet" in name.lower():
        Category = "Bracelets"
    elif filtering_jewellery and "necklace" in name.lower():
        Category = "Necklaces"
    elif filtering_jewellery and "brooch" in name.lower():
        Category = "Brooches"
    elif filtering_jewellery and "ear" in name.lower():
        Category = "Earrings"
    # Final generalisation to catch non-matching sub-category Jewellery
    if not Category and filtering_jewellery:
            Category = "Jewellery"
    # Seperate Mens/Women's/boys/girls if gender specific

# men’s bags
# cases
# luggage and suitcases
# backpacks
# briefcases and work bags
# messenger
# holdalls
#
# women’s bags
# shoulder bags
# backpacks
# clutches
# luggage and suitcases
# briefcases and work bags
# totes and shopper bags

    # General Bags Category
    bags_names = ['bag','case','luggage','suitcase','backpack','breifcase','messenger bag','holdall','shoulder bag','clutch','work bag','tote','shopper bag']
    bags_negatives = ['testing','test']
    filtering_bags = any(x.lower() in name.lower() for x in bags_names) and not any(x.lower() in name.lower() for x in bags_negatives)
    if filtering_bags and "case" in name.lower():
        Category = "Cases"
    elif filtering_bags and ("luggage" in name.lower() or "suitcase" in name.lower()):
        Category = "Luggage & Suitcases"
    elif filtering_bags and "backpack" in name.lower():
        Category = "Backpacks"
    elif filtering_bags and ("breifcase" in name.lower() or "work" in name.lower()):
        Category = "Breifcases & Work Bags"
    elif filtering_bags and "messenger" in name.lower():
        Category = "Messenger Bags"
    elif filtering_bags and "holdall" in name.lower():
        Category = "Holdalls"
    elif filtering_bags and "shoulder" in name.lower():
        Category = "Shoulder Bags"
    elif filtering_bags and "clutch" in name.lower():
        Category = "Clutch Bags"
    elif filtering_bags and ("tote" in name.lower() or "shopper" in name.lower()):
        Category = "Tote & Shopper Bags"
    # Final generalisation to catch non-matching sub-category Bags
    if not Category and filtering_bags:
            Category = "Bags"
    # Seperate Mens/Women's/boys/girls if gender specific

# women’s clothing
#
# DRESSES
# casual and day dresses
# cocktail dresses
# gowns
# maxi and long dresses
# mini and short dresses
# prom and formal dresses

    # Women's Dresses Category
    dresses_names = ['dress','ballgown','tunic']
    dresses_negatives = ['testing','test']
    filtering_dresses = any(x.lower() in name.lower() for x in dresses_names) and not any(x.lower() in name.lower() for x in dresses_negatives)
    if filtering_dresses and "cocktail" in name.lower():
        Category = "Cocktail Dresses"
    elif filtering_dresses and ("pencil" in name.lower() or "flare" in name.lower()):
        Category = "Casual & Day Dresses"
    elif filtering_dresses and "gown" in name.lower():
        Category = "Gowns"
    elif filtering_dresses and ("maxi" in name.lower() or "long" in name.lower()):
        Category = "Maxi & Long Dresses"
    elif filtering_dresses and "tunic" in name.lower() and "dress" in name.lower():
        Category = "Tunic Dresses"
    elif filtering_dresses and ("mini" in name.lower() or "short" in name.lower()):
        Category = "Mini & Short Dresses"
    elif filtering_dresses and ("prom" in name.lower() or "formal" in name.lower()):
        Category = "Prom & Formal Dresses"
    # Final generalisation to catch non-matching sub-category Dresses
    if not Category and filtering_dresses:
            Category = "Dresses"
    # Seperate Mens/Women's/boys/girls if gender specific

# SKIRTS
# knee-length skirts
# maxi skirts
# mid-length skirts
# mini skirts

    # Women's Skirts Category
    skirt_names = ['skirt']
    skirt_negatives = ['testing','test']
    filtering_skirt = any(x.lower() in name.lower() for x in skirt_names) and not any(x.lower() in name.lower() for x in skirt_negatives)
    if filtering_skirt and "knee" in name.lower():
        Category = "Knee Length Skirts"
    elif filtering_skirt and "maxi" in name.lower():
        Category = "Maxi Skirts"
    elif filtering_skirt and "midi" in name.lower():
        Category = "Mid0Length Skirts"
    elif filtering_skirt and "mini" in name.lower():
        Category = "Mini Skirts"
    # Final generalisation to catch non-matching sub-category Skirts
    if not Category and filtering_skirt:
            Category = "Skirts"
    # Seperate Mens/Women's/boys/girls if gender specific

# LINGERIE
# basques, bustiers and corsets
# bodysuits
# bras
# briefs
# camisoles
# lingerie sets

    # Women's Lingerie Category
    lingerie_names = ['basque','bustier','corset','bodysuit','bra','brief','camisole']
    lingerie_negatives = ['testing','test']
    filtering_lingerie = any(x.lower() in name.lower() for x in lingerie_names) and not any(x.lower() in name.lower() for x in lingerie_negatives)
    if filtering_lingerie and "basque" in name.lower() or "bustier" in name.lower() or "corset" in name.lower():
        Category = "Basques, Bustiers & Corsets"
    elif filtering_lingerie and "bodysuit" in name.lower():
        Category = "Bodysuits"
    elif filtering_lingerie and "bra" in name.lower():
        Category = "Bras"
    elif filtering_lingerie and "briefs" in name.lower():
        Category = "Briefs"
    elif filtering_lingerie and "camisole" in name.lower():
        Category = "Camisoles"
    elif filtering_lingerie and " set" in name.lower():
        Category = "Lingerie Sets"
    # Final generalisation to catch non-matching sub-category Lingerie
    if not Category and filtering_lingerie:
            Category = "Lingerie"
    # Seperate Mens/Women's/boys/girls if gender specific

# HOSIERY
# socks
# stockings
# tights

    # Women's Hosiery Category
    hosiery_names = ['socks','stockings','tights']
    hosiery_negatives = ['testing','test']
    filtering_hosiery = any(x.lower() in name.lower() for x in hosiery_names) and not any(x.lower() in name.lower() for x in hosiery_negatives)
    if filtering_hosiery and "socks" in name.lower():
        Category = "Socks"
    elif filtering_hosiery and "stockings" in name.lower():
        Category = "Stockings"
    elif filtering_hosiery and "tights" in name.lower():
        Category = "Tights"
    # Final generalisation to catch non-matching sub-category Hosiery
    if not Category and filtering_hosiery:
            Category = "Hosiery"
    # Seperate Mens/Women's/boys/girls if gender specific

# JUMPSUITS
# full-length jumpsuits
# playsuits

    # Women's Jumpsuits Category
    jumpsuit_names = ['jumpsuit','playsuit']
    jumpsuit_negatives = ['testing','test']
    filtering_jumpsuit = any(x.lower() in name.lower() for x in jumpsuit_names) and not any(x.lower() in name.lower() for x in jumpsuit_negatives)
    if filtering_jumpsuit and "jumpsuit" in name.lower():
        Category = "Jumpsuits"
    elif filtering_jumpsuit and "playsuit" in name.lower():
        Category = "JumpPlaysuit"
    # Final generalisation to catch non-matching sub-category Jumpsuits
    if not Category and filtering_jumpsuit:
            Category = "Jumpsuits"
    # Seperate Mens/Women's/boys/girls if gender specific

# BOOTS
# ankle boots
# flat boots
# heel and high heel boots
# knee boots
# mid-calf boots
# over-the-knee boots
# rain boots
# sandal boots
# wedge boots
#
# BOOTS
# casual boots
# desert boots
# formal and smart boots
# rain boots

    # General Boots Category
    boots_names = ['boot']
    boots_negatives = ['testing','test']
    filtering_boots = any(x.lower() in name.lower() for x in boots_names) and not any(x.lower() in name.lower() for x in boots_negatives)
    if filtering_boots and "high" in name.lower() and "heel" in name.lower():
        Category = "Heel and High Heel Boots"
    elif filtering_boots and "ankle" in name.lower():
        Category = "Ankle Boots"
    elif filtering_boots and "flat" in name.lower():
        Category = "Flat Boots"
    elif filtering_boots and "mid" in name.lower() and "calf" in name.lower():
        Category = "Mid-Calf Boots"
    elif filtering_boots and "over" in name.lower() and "knee" in name.lower():
        Category = "Over the Knee Boots"
    elif filtering_boots and "knee" in name.lower():
        Category = "Knee Boots"
    elif filtering_boots and "rain" in name.lower():
        Category = "Rain Boots"
    elif filtering_boots and "sandal" in name.lower():
        Category = "Sandal Boots"
    elif filtering_boots and "wedge" in name.lower():
        Category = "Wedge Boots"
    elif filtering_boots and 'casual' in name.lower():
        Category = "Casual Boots"
    elif filtering_boots and "desert" in name.lower():
        Category = "Desert Boots"
    elif filtering_boots and ("formal" in name.lower() or "smart" in name.lower() or "work" in name.lower()):
        Category = "Formal & Smart Boots"
    # Final generalisation to catch non-matching sub-category Boots
    if not Category and filtering_boots:
            Category = "Boots"
    # Seperate Mens/Women's/boys/girls if gender specific

# TRAINERS
# high-top trainers
# low-top trainers
#
# TRAINERS
# high-top trainers
# low-top trainers

    # General Trainers Category
    trainers_names = ['trainers']
    trainers_negatives = ['testing','test']
    filtering_trainers = any(x.lower() in name.lower() for x in trainers_names) and not any(x.lower() in name.lower() for x in trainers_negatives)
    if filtering_trainers and "high" in name.lower() and "top" in name.lower():
        Category = "High Top Trainers"
    elif filtering_trainers and "low" in name.lower() and "top" in name.lower():
        Category = "Low Top Trainers"
    # Final generalisation to catch non-matching sub-category Jumpsuits
    if not Category and filtering_trainers:
            Category = "Trainers"
    # Seperate Mens/Women's/boys/girls if gender specific

# HEELS
# clogs
# court shoes
# low and mid heels
# mules
# platform heels
# sandal heels
# stilettos and high heels
# wedge court shoes
# wedge sandals

    # Women's Heels Category
    heels_names = ['clogs','wedge court','mules','platform','stilettos','wedge sandals','heels']
    heels_negatives = ['testing','test']
    filtering_heels = any(x.lower() in name.lower() for x in heels_names) and not any(x.lower() in name.lower() for x in heels_negatives)
    if filtering_heels and "clogs" in name.lower():
        Category = "Clogs"
    elif filtering_heels and "wedge court" in name.lower():
        Category = "Wedge Court"
    elif filtering_heels and "mules" in name.lower():
        Category = "Mules"
    elif filtering_heels and "platform" in name.lower():
        Category = "Platform Heels"
    elif filtering_heels and "sandal" in name.lower() and "court" in name.lower():
        Category = "Sandal Court Heels"
    elif filtering_heels and "sandal" in name.lower():
        Category = "Sandal Heels"
    elif filtering_heels and ("stilettos" in name.lower() or "high heels" in name.lower()):
        Category = "Stilettos & High Heels"
    # Final generalisation to catch non-matching sub-category Heels
    if not Category and filtering_heels:
            Category = "Heels"
    # Seperate Mens/Women's/boys/girls if gender specific

# FLATS
# ballet flats and pumps
# espadrilles
# flat sandals
# flip-flops
# lace-ups
# loafers and moccasins
# slippers

    # Women's Flats Category
    flats_names = ['pump','sandal','ballet flat','espadrilles','sandals','flip-flops','flip flops','loafers','moccasins','slipper','pumps']
    flats_negatives = ['testing','test']
    filtering_flats = any(x.lower() in name.lower() for x in flats_names) and not any(x.lower() in name.lower() for x in flats_negatives)
    if filtering_flats and "ballet flat" in name.lower():
        Category = "Ballet Flats"
    elif filtering_flats and "espadrilles" in name.lower():
        Category = "Espadrilles"
    elif filtering_flats and "sandals" in name.lower():
        Category = "Flat Sandals"
    elif filtering_flats and "flip" in name.lower() and 'flops' in name.lower():
        Category = "Flip-Flops"
    elif filtering_flats and "loafers" in name.lower():
        Category = "Loafers"
    elif filtering_flats and "moccasins" in name.lower():
        Category = "Moccasins"
    elif filtering_flats and "slippers" in name.lower():
        Category = "Slippers"
    # Final generalisation to catch non-matching sub-category Flats
    if not Category and filtering_flats:
            Category = "Flats"
    # Seperate Mens/Women's/boys/girls if gender specific

# SLIP-ONS
# boat and deck shoes
# espadrilles
# loafers
# monk shoes
# slippers

    # Men's Slip-Ons Category
    slipons_names = ['slip ons','slip-ons','slipons','deck shoes','boat shoes','espadrilles','loafers','monk shoes','slippers']
    slipons_negatives = ['testing','test']
    filtering_slipons = any(x.lower() in name.lower() for x in slipons_names) and not any(x.lower() in name.lower() for x in slipons_negatives)
    if filtering_slipons and ("boat" in name.lower() or "deck" in name.lower()):
        Category = "Boat & Deck Shoes"
    elif filtering_slipons and "espadrilles" in name.lower():
        Category = "Espadrilles"
    elif filtering_slipons and "monk" in name.lower():
        Category = "Monk Shoes"
    elif filtering_slipons and "loafers" in name.lower():
        Category = "Loafers"
    elif filtering_slipons and "moccasins" in name.lower():
        Category = "Moccasins"
    elif filtering_slipons and "slippers" in name.lower():
        Category = "Slippers"
    # Final generalisation to catch non-matching sub-category Slip-Ons
    if not Category and filtering_slipons:
            Category = "Slip-Ons"
    # Seperate Mens/Women's/boys/girls if gender specific

# LACE-UPS
# brogues
# derbies
# oxfords

    # Men's Lace-Ups Category
    laceups_names = ['brogues','derbies','oxford','lace-ups','lace ups']
    laceups_negatives = ['testing','test']
    filtering_laceups = any(x.lower() in name.lower() for x in laceups_names) and not any(x.lower() in name.lower() for x in laceups_negatives)
    if filtering_laceups and "brogues" in name.lower():
        Category = "Brogues"
    elif filtering_laceups and "derbies" in name.lower():
        Category = "Derbies"
    elif filtering_laceups and "oxfords" in name.lower():
        Category = "Oxfords"
    # Final generalisation to catch non-matching sub-category Lace-Ups
    if not Category and filtering_laceups:
            Category = "Lace-Ups"
    # Seperate Mens/Women's/boys/girls if gender specific

# SANDALS
# flip-flops
# leather sandals

    # Men's Sandals Category
    sandals_names = ['flip flops','flip-flops','leather sandals','sandals']
    sandals_negatives = ['testing','test']
    filtering_sandals = any(x.lower() in name.lower() for x in sandals_names) and not any(x.lower() in name.lower() for x in sandals_negatives)
    if filtering_sandals and "flops" in name.lower():
        Category = "Flip Flops"
    elif filtering_sandals and "leather" in name.lower():
        Category = "Leather Sandals"
    # Final generalisation to catch non-matching sub-category Sandals
    if not Category and filtering_sandals:
            Category = "Sandals"
    # Seperate Mens/Women's/boys/girls if gender specific

#Shoes Catchment

    # Men's Shoes Category
    shoes_names = ['shoe']
    shoes_negatives = ['testing','test']
    filtering_shoes = any(x.lower() in name.lower() for x in shoes_names) and not any(x.lower() in name.lower() for x in shoes_negatives)
    if not Category and filtering_shoes:
        Category = "Shoes"

    return Category

def colour(colour):

        # Yellow, Red, Blue, Purple, Green, Pink, Silver,
        # Orange, White, Black, Grey, Gold, Multi, Brown
        this = colour

        viariants = ['Yellow', 'lemon']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = [' Red',' Red ','berry','rose','Crimson','chilli']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = 'Red'
        viariants = ['Blue', 'Navy', 'teal', 'sky', 'ultramarine','Cornflower','Aqua']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Purple','plum','Indigo','Lilac','Grape']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Green', 'Khaki','Turquoise', 'mint']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Pink', 'fuschia', 'magenta','Fuchsia','Peony']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Silver']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Orange', 'coral','flame','Papaya']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['White', 'Ivory', 'cream', 'stone','latte','Vanilla']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Black','blk']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Grey','slate','charcoal']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Gold']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Multi', 'various']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Brown', 'bronze', 'rust','nude','tan','Neutral']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]

        if this == colour:
            colour = ""

        return colour

def sizes(sizes):
    sizes_final = sizes
    wrong = ""
    return sizes_final, wrong

    # wrong = []
    # sizes_final = []
    # for thing in sizes:
    #     start = thing
    #     if "8" in thing:
    #         thing = 8
    #     elif "10" in thing:
    #         thing = 10
    #     elif "12" in thing:
    #         thing = 12
    #     elif "14" in thing:
    #         thing = 14
    #     elif "16" in thing:
    #         thing = 16
    #     elif "18" in thing:
    #         thing = 18
    #     elif "XL" in thing.upper():
    #         thing = "1XL"
    #     elif "M" in thing:
    #         thing = "Medium"
    #
    #     if thing == start:
    #         wrong.append(thing)
    #     else:
    #         sizes_final.append(str(thing))
    #
    # return sizes_final, wrong


def gender(name):
    gender = ""
    if "women" in name.lower():
        gender = "Women"
    elif " men" in name.lower():
        gender = "Men"
    elif name.lower().startswith( "men" ):
        gender = "Men"
    else:
        gender = ""

    return gender

def perc_group(price, rrp):
    percentage_group = ""
    num = price / rrp
    if num < 0.1:
        percentage_group = "Over 90% Off"
    elif num < 0.2:
        percentage_group = "Over 80% Off"
    elif num < 0.3:
        percentage_group = "Over 70% Off"
    elif num < 0.4:
        percentage_group = "Over 60% Off"
    elif num < 0.5:
        percentage_group = "Over 50% Off"
    else:
        percentage_group = ""

    return percentage_group

def hot_deals(price, rrp, discount):
    hot_deal = ""
    if price / rrp < discount:
        hot_deal = "Hot Deal"
    return hot_deal

def price_cat(price):
    price_category = ""
    if price <= 5:
        price_category = "Under £5"
    elif price <= 10:
        price_category = "Under £10"
    elif price <= 20:
        price_category = "Under £20"

    return price_category

def discount_perc(price, rrp):

    perc = round((1 - (float(price) / float(rrp))) * 100)

    return perc
