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

    # logic error 1: Quality can never be negative
    def test_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # logic error 2: Quality can never exceed 50 (except Sulfuras)
    def test_quality_never_exceeds_fifty(self):
        items = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)  

    # logic error 3: Conjured items degrade twice as fast
    def test_conjured_items_degrade_twice(self):
        items = [
            Item("Normal Item", 5, 10),
            Item("Conjured", 5, 10)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)  
        self.assertEqual(8, items[1].quality)  

    # Syntax error
    def test_get_item_name(self):
        items = [Item("Random Item", 5, 10)]
        gilded_rose = GildedRose(items)
        self.assertEqual("Random Item", gilded_rose.get_item_name(0))

        
if __name__ == '__main__':
    unittest.main()
