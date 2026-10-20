#!/usr/bin/env python3
"""Render the public examples collection from its credited image records."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


def esc(value):
    return html.escape(str(value), quote=True)


GROUPS = [
    ("movement", "Movement & attention", {"moving", "becoming-with"},
     "Bodies, rhythms, orientations, and scales become ways to explore a world. These examples include Southern Devices and MuMu."),
    ("encounters", "Roleplay & encounters", {"encountering", "roleplay"},
     "A prototype, a robot, a setting, or a scenario gives participants something to meet and respond to. The encounter can change the world being rehearsed."),
    ("gathering", "Gathering & making", {"workshop", "making"},
     "Writing, drawing, cards, conversation, sound, and shared materials help a group give its ideas a form."),
    ("shared-worlds", "Worlds made together", {"worldbuilding"},
     "The Middle brings community contributions into a shared digital environment. These views show the resulting world, alongside the workshop practices documented elsewhere in this collection."),
    ("teaching", "Teaching through performance", {"teaching"},
     "Student work from Edgeland Futurism at UC San Diego shows how props, bodily action, and public encounters can make a speculative world available to others. Instructors: Ash Eliza Smith and Pepe Rojo."),
]


def card(item):
    source_url = item.get("source_url")
    source = (f'<a href="{esc(source_url)}" target="_blank" rel="noopener noreferrer">{esc(item["source_label"])} ↗</a>'
              if source_url else esc(item["source_label"]))
    project_credit = f'<p class="example-credit">{esc(item["project_credit"])}</p>' if item.get("project_credit") else ""
    return f'''<article class="example" id="{esc(item['id'])}">
      <figure>
        <a class="example-image" href="{esc(item['image'])}" target="_blank" rel="noopener" aria-label="Open full image: {esc(item['title'])}">
          <img src="{esc(item['image'])}" alt="{esc(item['alt'])}" width="{item['width']}" height="{item['height']}" loading="lazy" decoding="async">
        </a>
        <figcaption><h3>{esc(item['title'])}</h3><p>{esc(item['caption'])}</p>
          <p class="example-credit">{esc(item['credit'])}</p>{project_credit}
          <p class="example-source">{source}</p>
        </figcaption>
      </figure>
    </article>'''


def render(data):
    version = (ROOT / "VERSION").read_text().strip()
    anchor = "v" + version.replace(".", "-")
    entries = data["examples"]
    jump_links = ''.join(f'<a href="#{key}">{esc(title)}</a>' for key, title, _, _ in GROUPS)
    sections = []
    for key, title, practices, intro in GROUPS:
        selected = [x for x in entries if x['practice'] in practices]
        if not selected:
            continue
        sections.append(f'''<section class="examples-section" id="{key}" aria-labelledby="{key}-title">
          <div class="examples-section-heading"><p class="eyebrow">{len(selected):02d} images / In practice</p><h2 id="{key}-title">{esc(title)}</h2><p>{esc(intro)}</p></div>
          <div class="examples-grid">{''.join(card(x) for x in selected)}</div>
        </section>''')
    framework = next(x for x in entries if x['id'] == 'paper-framework')
    featured = next(x for x in entries if x['id'] == 'paper-drone-dance')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Images and examples of embodied worldbuilding through performance, play, workshops, and teaching. Explore the practice around Co-Constructing Multispecies Futures.">
<title>Examples — Co-Constructing Multispecies Futures</title><link rel="stylesheet" href="assets/toolkit.css"><link rel="stylesheet" href="assets/examples.css"></head>
<body class="examples-page"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header wrap"><a class="wordmark" href="index.html#start" aria-label="Co-Constructing Multispecies Futures home"><span class="mark" aria-hidden="true">✳</span> MULTISPECIES<br><span class="wordmark-second">FUTURES</span></a>
<nav aria-label="Main navigation"><a href="index.html#start">Start here</a><a href="interactive.html">Interactive Tool</a><a href="index.html#print">Print cards</a><a href="guide.html">Facilitate</a><a href="examples.html" aria-current="page">Examples</a><a href="paper.html">About &amp; cite</a></nav></header>
<main id="main" class="wrap"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html#start">Home</a><span aria-hidden="true">/</span><span aria-current="page">Examples</span></nav>
<section class="examples-intro">
  <div class="examples-intro-heading"><p class="eyebrow">Embodied worldbuilding / A growing collection</p><h1>Worlds take shape<br><em>between us.</em></h1><p class="hero-intro">Movement, roleplay, making, and collective imagining.</p></div>
  <figure class="examples-featured">
    <a href="#{esc(featured['id'])}" aria-label="Read the example: {esc(featured['title'])}"><img src="{esc(featured['image'])}" alt="{esc(featured['alt'])}" width="{featured['width']}" height="{featured['height']}" fetchpriority="high" decoding="async"></a>
    <figcaption><a href="#{esc(featured['id'])}">{esc(featured['title'])} ↓</a><p>{esc(featured['caption'])}</p><p class="example-credit">{esc(featured['credit'])}</p></figcaption>
  </figure>
  <div class="examples-intro-context"><p>Images shared by Ash Eliza Smith: the complete image set from <em>Performing the What-If</em>, alongside MuMu, The Middle, workshops, and teaching. Explore the practice that informs this toolkit, with each project’s context and credits.</p><p class="small">{len(entries)} images · Select a gallery image to view the full frame. For dates and development context, visit the <a href="workshops.html">workshop history</a>.</p></div>
</section>
<nav class="examples-jump" aria-label="Browse examples by practice">{jump_links}<a href="#framework">The framework</a><a href="#contribute">Share your practice</a></nav>
{''.join(sections)}
<section class="examples-section" id="framework" aria-labelledby="framework-title"><div class="examples-section-heading"><p class="eyebrow">From Performing the What-If</p><h2 id="framework-title">A vocabulary for trying things.</h2><p>Encountering, moving with, and becoming-with are overlapping modes of embodied practice. They can be explored through everyday materials as well as emerging technologies.</p></div>
<div class="framework-example">{card(framework)}</div>
<details class="framework-text"><summary>Read the table as text</summary><div class="table-scroll"><table><caption>Three modes of embodied encounter, from low-fi to emerging technologies. Bleed and attunement move across all three.</caption><thead><tr><th scope="col">Mode</th><th scope="col">Case</th><th scope="col">What the body approaches</th><th scope="col">Low-fi</th><th scope="col">With emerging technologies</th></tr></thead><tbody>
<tr><th scope="row">Encountering</th><td>LARRP, Speculative Robotics Lab Pop-Up</td><td>Sharing a scenario of care with a machine</td><td>A person voices a robot from behind a screen; others roleplay with a found object</td><td>Working robots voiced in real time (Wizard-of-Oz), green-screen compositing</td></tr>
<tr><th scope="row">Moving with</th><td><em>Southern Devices</em> drone dance</td><td>Being seen and tracked; where the body is free to go and where it is steered</td><td>Follow a partner with a phone camera, then swap; walk the sensors of a familiar street</td><td>Drone duet with an operator or in automated follow mode</td></tr>
<tr><th scope="row">Becoming-with</th><td><em>MuMu</em></td><td>Approaching a non-human umwelt and being reshaped by the relation</td><td>Draw two cards; move, or crawl, at that being’s scale and pace</td><td>In XR, crawling through a prairie dog burrow, stretching as an apple tree, or sowing seeds as a planting robot, with OZZI</td></tr>
</tbody></table></div></details><p class="section-note">These modes are distinct from the three interwoven phases of <em>Rehearsing Realities</em>: enter the magic circle; prototype with entangled bodies; rehearse transformation. <a href="paper.html">Read about the framework and its lineages.</a></p></section>
<section class="examples-contribute" id="contribute" aria-labelledby="contribute-title"><p class="eyebrow">Keep the collection growing</p><h2 id="contribute-title">What took shape<br>in your gathering?</h2><p>A photograph, a sketch, an object, a short performance, or a media link can help another group begin. Keep the prompts, a sentence about what happened, and the credit you want shown with the work.</p><p class="small">You can prepare a smaller image and keep its caption and credits together in the browser. The preparation preview sends nothing. Community uploads are not open on this page yet.</p><p>When sharing elsewhere, you can use <strong>#CoConstructingMultispeciesFutures</strong> and link to this toolkit.</p><div class="hero-actions"><a class="button primary" href="downloads/Co-Constructing_Multispecies_Futures_Community_Preparation_v0.1.0.html" target="_blank" rel="noopener">Prepare an image · preview ↗</a><a class="button secondary" href="guide.html">Lead a session ↗</a></div></section>
<p class="examples-credit-note">Images keep their source credits. Photo authorship is left unstated when the source does not name a photographer. New contributions will be displayed with the permission and credit agreed by their contributors.</p>
</main><footer class="site-footer"><div class="wrap footer-layout"><div class="footer-project"><span>CO-CONSTRUCTING MULTISPECIES FUTURES</span><a href="versions.html#{anchor}">Interactive Tool v{esc(version)} · Development edition</a><a href="index.html#start">Back to the homepage ↑</a></div><div class="footer-about"><strong>About &amp; cite</strong><nav aria-label="About and citation"><a href="paper.html#cite">How to cite</a><a href="paper.html">Paper &amp; lineage</a><a href="workshops.html">Workshop history</a><a href="examples.html" aria-current="page">Examples</a><a href="versions.html">Versions</a></nav></div></div></footer></body></html>
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((SITE / 'data/examples.json').read_text())
    entries = data['examples']
    assert len({x['id'] for x in entries}) == len(entries), 'Duplicate image IDs'
    for item in entries:
        assert (SITE / item['image']).is_file(), item['image']
        assert all(item.get(key) for key in ('caption', 'credit', 'alt', 'source_label'))
    output = render(data)
    destination = SITE / 'examples.html'
    if args.check:
        assert destination.read_text() == output, 'Examples page is out of date'
        print(f'Examples page matches {len(entries)} credited image records.')
    else:
        destination.write_text(output)
        print(f'Wrote examples.html with {len(entries)} credited image records.')


if __name__ == '__main__':
    main()
