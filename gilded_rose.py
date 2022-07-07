# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name == "Aged Brie":
                if item.quality < 50:
                    if item.sell_in < 0:
                        item.quality = min(50, item.quality + 2)
                    else:
                        item.quality = min(50, item.quality + 1)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    item.quality = 0
                else:
                    quality_increase = 1
                    if item.sell_in < 6:
                        quality_increase += 2
                    elif item.sell_in < 11:
                        quality_increase += 1
                    item.quality = min(50, item.quality + quality_increase)
            else:
                if item.sell_in < 0:
                    item.quality = max(0, item.quality - 2)
                else:
                    item.quality = max(0, item.quality - 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
