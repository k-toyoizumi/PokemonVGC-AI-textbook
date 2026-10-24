"""Validate published chapter navigation, MathML, captions and table structure."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent.parent
pages={p.resolve():BeautifulSoup(p.read_text(), 'html.parser') for p in [ROOT/'index.html',*sorted((ROOT/'chapters').glob('*.html'))]}
assert len(pages)==8, 'Expected landing page plus chapters 1–7'
links=tables=figures=0
for path,soup in pages.items():
 ids=[e['id'] for e in soup.select('[id]')]
 assert len(ids)==len(set(ids)),(path,'duplicate ids')
 assert soup.select_one('header.site-header')
 assert '.header{' not in soup.style.get_text(),(path,'CSS collision')
 assert not soup.select('.citation'),(path,'unresolved references')
 for m in soup.select('.math'):
  assert m.find('math'),(path,'unconverted TeX',m.get_text())
 for table in soup.select('table'):
  tables+=1
  heads=table.select_one('thead tr').find_all(['th','td'],recursive=False)
  for row in table.select('tbody tr'):
   cells=row.find_all(['th','td'],recursive=False)
   assert len(cells)==len(heads),(path,'table columns')
   assert [c.get('style','') for c in cells]==[c.get('style','') for c in heads],(path,'table alignment')
 for figure in soup.select('figure'):
  figures+=1
  assert figure.img.get('alt') and figure.figcaption and figure.get('id'),(path,'incomplete figure')
 for a in soup.select('a[href]'):
  u=urlsplit(a['href'])
  if u.scheme or u.netloc:continue
  dest=(path.parent/unquote(u.path)).resolve() if u.path else path
  assert dest in pages,(path,'missing page',a['href'])
  if u.fragment:assert pages[dest].find(id=unquote(u.fragment)),(path,'missing anchor',a['href'])
  links+=1
 # All seven chapter destinations exist in the sidebar on every page.
 side=soup.select_one('aside.sidebar')
 assert len(side.select('a.side-link'))==8,(path,'missing chapter links')
 assert soup.select_one('.chapter-nav') and soup.select_one('aside.toc')
for n in [5,6,7]:
 p=(ROOT/f'chapters/chapter{n:02}.html').resolve();s=pages[p]
 assert len(s.select('article details.solution'))>=4,(n,'exercises')
 assert len(s.select('article math'))>=10,(n,'math')
 assert s.select_one('article figure figcaption').get_text().startswith(f'図{n}.1：')
print(f'PASS: {len(pages)} pages, {tables} tables, {figures} figures, {links} internal links; MathML/captions/navigation')
