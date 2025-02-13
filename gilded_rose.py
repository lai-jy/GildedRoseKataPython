# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemStrategy:
    def update(self, item):
        raise NotImplementedError("Subclasses must implement update method")

class NormalItem(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        quality_decrement = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - quality_decrement)

class AgedBrie(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        quality_increment = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + quality_increment)

class Sulfuras(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        item.quality = 80  

class BackstagePass(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        
        if item.sell_in < 0:
            item.quality = 0
            return
            
        if item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

class ConjuredItem(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        quality_decrement = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - quality_decrement)

class GildedRose(object):
    STRATEGY_MAP = {
        "Aged Brie": AgedBrie(),
        "Sulfuras": Sulfuras(),
        "Sulfuras, Hand of Ragnaros": Sulfuras(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePass(),
        "Conjured": ConjuredItem()
    }

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.STRATEGY_MAP.get(item.name, NormalItem())
            strategy.update(item)

    def get_item_names(self):
        return [item.name for item in self.items]
    
    def get_item_name(self, index):
        return self.items[index].name
    
    def get_item(self):
        return self.get_item_names()