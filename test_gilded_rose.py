# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)

    # logic error 1
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)  

    # logic error 2
    def test_backstage_passes_quality_increases(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].quality)  

    # logic error 3
    def test_normal_item_quality_degradation(self):
        items = [Item("Normal Item", -1, 10)]  
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)  

    # Syntax error
    def test_get_item_name(self):
        items = [Item("Random Item", 5, 10)]
        gilded_rose = GildedRose(items)
        self.assertEqual("Random Item", gilded_rose.get_item_name(0))

        
if __name__ == '__main__':
    unittest.main()
