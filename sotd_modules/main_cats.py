def category_filter(name):
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
