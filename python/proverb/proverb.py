"""Generate the 'horseshoe nail' proverb with a supplied list of items"""

def proverb(*items, qualifier=None):
    if not items:
        return []

    qualifier_pfx = f'{qualifier} ' if qualifier else ''
        
    lines = [
        f'For want of a {want} the {lost} was lost.'
        for want, lost in zip(items, items[1:])
    ]
        
    return lines + [f'And all for the want of a {qualifier_pfx}{items[0]}.']
    