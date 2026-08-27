import os
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'output' / 'site'


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.lang = None
        self.title = []
        self.in_title = False
        self.classes = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'title':
            self.in_title = True
        if tag in ('a', 'link', 'script', 'img'):
            target = attrs.get('href') or attrs.get('src')
            if target:
                self.links.append((tag, target))
        if 'class' in attrs:
            self.classes.extend(attrs['class'].split())

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)


class GeneratedSiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not SITE.exists():
            raise AssertionError('Build the site before running generated-site tests')
        cls.pages = sorted(SITE.rglob('*.html'))

    def test_expected_language_pages_exist(self):
        self.assertGreaterEqual(len(self.pages), 80)
        self.assertTrue((SITE / 'index.html').is_file())
        self.assertTrue((SITE / 'tr' / 'index.html').is_file())
        self.assertTrue((SITE / 'pinout' / 'pwm.html').is_file())
        self.assertTrue((SITE / 'tr' / 'pinout' / 'pwm.html').is_file())
        self.assertTrue((SITE / 'pinout' / 'ardupilot.html').is_file())
        self.assertTrue((SITE / 'tr' / 'pinout' / 'ardupilot.html').is_file())

    def test_html_metadata_and_templates(self):
        for page in self.pages:
            content = page.read_text(encoding='utf-8')
            parser = PageParser()
            parser.feed(content)
            expected_lang = 'tr' if page.relative_to(SITE).parts[0] == 'tr' else 'en'
            with self.subTest(page=page):
                self.assertEqual(parser.lang, expected_lang)
                self.assertTrue(''.join(parser.title).strip())
                self.assertNotIn('{{', content)
                self.assertNotIn('translate-me', parser.classes)
                self.assertNotIn('gemstone-logo.png', content)

    def test_every_internal_link_and_asset_resolves(self):
        failures = []
        for page in self.pages:
            parser = PageParser()
            parser.feed(page.read_text(encoding='utf-8'))
            for tag, target in parser.links:
                split = urlsplit(target)
                if target.startswith('//') or split.scheme or target.startswith(('#', 'mailto:', 'tel:')):
                    continue

                path = unquote(split.path)
                candidate = SITE / path.lstrip('/') if path.startswith('/') else page.parent / path
                candidate = Path(os.path.normpath(candidate))
                if candidate.is_dir():
                    candidate = candidate / 'index.html'
                if not candidate.exists():
                    failures.append('{}: {} {}'.format(page.relative_to(SITE), tag, target))

                if tag == 'a' and 'pinout.t3gemstone.org' in target:
                    failures.append('{}: language link leaves the local site: {}'.format(
                        page.relative_to(SITE), target))

        self.assertEqual(failures, [], '\n' + '\n'.join(failures))


if __name__ == '__main__':
    unittest.main()
