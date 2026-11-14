---
permalink: /
title: ""
excerpt: "Huanyu Li — underwater intelligent vision, image enhancement, vision-language understanding, and efficient deep learning."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<section class="intro-section" id="about-me" aria-labelledby="intro-title">
  <p class="eyebrow">UNDERWATER VISION · VISION & LANGUAGE</p>
  <h1 id="intro-title">Huanyu Li <span lang="zh">李环宇</span></h1>
  <p class="intro-lead">Understanding the underwater world through vision and language.</p>
  <p>I received my Ph.D. degree in Marine Resources and Information Engineering from China University of Petroleum (East China). My research interests focus on underwater intelligent vision, image enhancement, vision-language understanding, and efficient deep learning.</p>
  <div class="intro-actions">
    <a class="primary-link" href="#publications">Explore publications <span aria-hidden="true">↗</span></a>
    <a href="{{ site.author.googlescholar }}">Google Scholar <span aria-hidden="true">↗</span></a>
    <a href="mailto:{{ site.author.email }}">Get in touch <span aria-hidden="true">↗</span></a>
  </div>
</section>

<section id="research" aria-labelledby="research-title">
  <h2 id="research-title"><span class="section-number" aria-hidden="true">01</span> Research Interests</h2>
  <ul class="research-grid">
    <li><span aria-hidden="true">01 /</span><h3>Underwater Intelligent Vision</h3></li>
    <li><span aria-hidden="true">02 /</span><h3>Image Enhancement and Restoration</h3></li>
    <li><span aria-hidden="true">03 /</span><h3>Vision-Language Understanding</h3></li>
    <li><span aria-hidden="true">04 /</span><h3>Efficient Deep Learning and Model Compression</h3></li>
  </ul>
</section>

<section id="highlights" aria-labelledby="highlights-title">
  <h2 id="highlights-title"><span class="section-number" aria-hidden="true">02</span> Highlights</h2>
  <ul class="highlight-list">
    <li><strong>Top Reviewer 2026</strong><span>IEEE TGRS</span></li>
    <li><strong>Excellence in Review 2025</strong><span>IEEE JOE</span></li>
    <li><strong>ESI Hot Paper</strong><span>Multiple ESI Highly Cited Papers</span></li>
    <li><strong>Featured Article</strong><span>ISPRS JPRS</span></li>
  </ul>
</section>

<section id="news" aria-labelledby="news-title">
  <h2 id="news-title"><span class="section-number" aria-hidden="true">03</span> News</h2>
<ul class="news-list"><li><span class="news-date">Sep. 2026</span><div><strong>3 collaborative papers</strong> have been <strong>published</strong> in the <strong><i>2026 IEEE International Conference on Image Processing (ICIP)</i></strong> (CCF-C)!</div></li><li><span class="news-date">Aug. 2026</span><div>Awarded the <strong>Top Reviewer 2026</strong> by <em>IEEE Transactions on Geoscience and Remote Sensing</em>.</div></li><li><span class="news-date">Jul. 2026</span><div>Our work "<a href="https://ieeexplore.ieee.org/document/11598958">Joint Underwater Image Enhancement and Captioning through Multi-Supervised Chained Task Learning</a>" (<strong><i>IEEE Transactions on Geoscience and Remote Sensing</i></strong>) has been <strong>published</strong>!</div></li></ul>
<details class="news-archive"><summary>Earlier news</summary><ul class="news-list"><li><span class="news-date">Jul. 2026</span><div>Our work "<a href="https://link.springer.com/article/10.1007/s11263-025-02650-w">Large Foundation Model Empowered Region-aware Underwater Image Captioning</a>" (<strong><i>International Journal of Computer Vision</i></strong>) has been newly selected as an <strong>ESI Highly Cited Paper</strong>!</div></li><li><span class="news-date">Apr. 2026</span><div>Awarded the <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11493606">Excellence in Review 2025</a> by <strong><i>IEEE Journal of Oceanic Engineering</i></strong>.</div></li><li><span class="news-date">Jan. 2026</span><div>Our works "<a href="https://ieeexplore.ieee.org/document/11062881">Underwater Image Captioning With AquaSketch-Enhanced Cross-Scale Information Fusion</a>" (<strong><i>IEEE Transactions on Geoscience and Remote Sensing</i></strong>) and "<a href="https://www.sciencedirect.com/science/article/abs/pii/S1566253525003422">Underwater image captioning via attention mechanism based fusion of visual and textual information</a>" (<strong><i>Information Fusion</i></strong>) have been newly selected as <strong>ESI Highly Cited Papers</strong>!</div></li><li><span class="news-date">May. 2025</span><div>Our work "<a href="https://www.sciencedirect.com/science/article/pii/S0924271624004726">Underwater image captioning: Challenges, models, and datasets</a>" (<strong><i>ISPRS Journal of Photogrammetry and Remote Sensing</i></strong>) has been newly selected as an <strong>ESI Hot Paper</strong>!</div></li></ul></details>
</section>

<section id="publications" aria-labelledby="publications-title">
  <div class="section-heading">
    <h2 id="publications-title"><span class="section-number" aria-hidden="true">04</span> Selected Publications</h2>
    <a class="scholar-link" href="{{ site.author.googlescholar }}">All publications ↗</a>
  </div>
  <p class="section-note">* Corresponding author. My name is highlighted in bold.</p>
  <a class="citation-badge" href="{{ site.author.googlescholar }}"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FLiHuanyu-PhD%2FLihuanyu-PhD.github.io%2Fgoogle-scholar-stats%2Fgs_data_shieldsio.json" alt="Google Scholar citations" loading="lazy"></a>
  <div class="publication-filters" role="group" aria-label="Filter publications" hidden>
    <button type="button" data-filter="all" aria-pressed="true">All papers</button>
    <button type="button" data-filter="lead" aria-pressed="false">First / corresponding author</button>
    <button type="button" data-filter="collaborative" aria-pressed="false">Collaborative works</button>
  </div>
  <p class="publication-count" aria-live="polite" hidden></p>
  <ol class="publication-list">
    {% for paper in site.data.publications %}
    <li class="publication" data-role="{{ paper.role }}">
      <div class="publication-year">{{ paper.year }}</div>
      <div class="publication-body">
        <h3><a href="{{ paper.url }}">{{ paper.title }} <span class="paper-arrow" aria-hidden="true">↗</span></a></h3>
        <p class="publication-authors">{{ paper.authors }}</p>
        <p class="publication-venue">{{ paper.venue }}</p>
        {% if paper.badges.size > 0 %}<div class="paper-badges">{% for badge in paper.badges %}<span>{{ badge }}</span>{% endfor %}</div>{% endif %}
      </div>
    </li>
    {% endfor %}
  </ol>
</section>

## Honors and Awards
{: #honors}

- Aug. 2026:  Awarded the **Top Reviewer 2026** by *IEEE Transactions on Geoscience and Remote Sensing*.

- Apr. 2026:  Awarded the <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11493606">Excellence in Review 2025</a> by *IEEE Journal of Oceanic Engineering*.

- Feb. 2025:  Our paper <a href="https://www.sciencedirect.com/science/article/pii/S0924271624004726">Underwater image captioning: Challenges, models, and datasets</a> was selected as a <a href="https://www.sciencedirect.com/journal/isprs-journal-of-photogrammetry-and-remote-sensing/about/featured-articles/2025-featured-article">Featured Article</a> of *ISPRS Journal of Photogrammetry and Remote Sensing*. (**Only 12 out of 364 papers selected.**)

- Oct. 2023:  Awarded the <a href="http://m.jyt.henan.gov.cn/2023/08-12/2795956.html">Outstanding Master's Thesis</a> of Henan Province.


## Education
{: #education}

- **2022 – 2026**, Ph.D. in Marine Resources and Information Engineering, China University of Petroleum (East China), China.

- **2019 – 2022**, M.Eng. in Signal and Information Processing, Zhongyuan University of Technology, China.  
  MS Thesis: *Research on Structured Pruning Method and Hardware Acceleration of Convolutional Neural Networks*

- **2015 – 2019**, B.Eng. in Automation, Zhongyuan University of Technology, China.


## Academic Services
{: #service}

### Editorial Service

- **Lead Guest Editor**, Special Issue *[Advances in Underwater Image Processing and Analysis](https://www.mdpi.com/journal/jimaging/special_issues/LUG5F450XG)*, *[Journal of Imaging](https://www.mdpi.com/journal/jimaging)*, 2026–present.

### Peer Review Experience

Reviewed **200+ manuscripts** for more than **30 academic journals and conferences**.

#### Reviewer for:

<ul class="reviewer-list"><li>IEEE Transactions on Geoscience and Remote Sensing</li><li>IEEE Transactions on Circuits and Systems for Video Technology</li><li>IEEE Journal of Oceanic Engineering</li><li>Pattern Recognition</li><li>Engineering Applications of Artificial Intelligence</li><li>Neural Networks</li><li>Applied Soft Computing</li><li>IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing</li><li>IEEE International Conference on Image Processing</li><li>Neural Computing and Applications</li><li>The Visual Computer</li><li>Signal, Image and Video Processing</li><li>...and more.</li></ul>

<footer class="homepage-footer">Huanyu Li · Underwater Vision &amp; Vision-Language Understanding <a href="#about-me">Back to top ↑</a></footer>
