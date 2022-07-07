# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_random_item(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sulfuras(self):
        sell_in, quality = 20, 30
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(sell_in, items[0].sell_in)
        self.assertEqual(quality, items[0].quality)

    def test_sellin_expired_quality(self):
        items = [Item("Foo", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(18, items[0].quality)

    def test_never_negative_quality(self):
        items = [Item("Foo", 20, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", 20, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_aged_brie_exipred_quality(self):
        items = [Item("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_never_above_50_quality(self):
        items = [Item("Aged Brie", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstagepasses_more_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(31, items[0].quality)

    def test_backstagepasses_more_than_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(32, items[0].quality)

    def test_backstagepasses_less_than_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(33, items[0].quality)

    def test_backstagepasses_past_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_items(self):
        items = [Item("Conjured Milk", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(28, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
