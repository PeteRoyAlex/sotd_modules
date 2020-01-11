def colour_filter(colour):

        # Yellow, Red, Blue, Purple, Green, Pink, Silver,
        # Orange, White, Black, Grey, Gold, Multi, Brown
        this = colour

        viariants = ['Yellow', 'lemon']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Red', 'berry', 'rose']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Blue', 'Navy', 'teal']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Purple']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Green', 'Khaki','Turquoise', 'mint']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Pink', 'fuschia', 'magenta']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Silver']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Orange', 'coral']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['White', 'Ivory', 'cream', 'stone']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Black','blk']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Grey']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Gold']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Multi', 'various']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]
        viariants = ['Brown', 'bronze', 'rust']
        if any(x.lower() in colour.lower() for x in viariants):
            colour = viariants[0]

        if this == colour:
            colour = ""

        return colour
