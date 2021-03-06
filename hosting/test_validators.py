# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.exceptions import ValidationError

from .validators import validate_no_allcaps, validate_not_to_much_caps


class ValidatorTests(TestCase):
    def test_validate_no_allcaps(self):
        valid = ("ZAM", "Zam", "zim Zam zum", "McCoy", "鋭郎", "鋭郎 三好", "O'Hara", "O’Timmins")
        invalid = ("ZAMENHOF", "MC COY")
        for value in valid:
            self.assertEqual(validate_not_to_much_caps(value), None)
        for value in invalid:
            self.assertRaises(ValidationError, validate_no_allcaps, value)

    def test_validate_no_toomuchcaps(self):
        valid = ("ZAM", "Zam", "zim Zam zum", "McCoy", "鋭郎", "鋭郎 三好", "O'Hara", "O’Timmins")
        invalid = ("ZAMENHOF", "ZAm", "mcCOY", "mc COY")
        for value in valid:
            self.assertEqual(validate_not_to_much_caps(value), None)
        for value in invalid:
            self.assertRaises(ValidationError, validate_not_to_much_caps, value)
