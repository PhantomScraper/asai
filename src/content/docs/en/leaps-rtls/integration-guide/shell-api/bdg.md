---
title: "BDG"
lang: en
slug: "leaps-rtls/integration-guide/shell-api/bdg"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/shell-api/bdg/"
order: 144
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="bdg">
<h1>BDG</h1>
<hr class="docutils">
<div class="section" id="utlv">
<span id="id1"></span><h2>utlv</h2>
<p>Cmd as TLV frame for UWB Subsystem.</p>
<p>When executed on the ESP32, the <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#tlv"><span class="std std-ref">tlv</span></a> command reports ESP32-related values. In contrast, the utlv command retrieves values originating from the UWB module.</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; utlv</span>

<span class="go">Usage: utlv &lt;MSB&gt; &lt;MSB-1&gt; ...</span>
</pre></div>
</div>
<ul class="simple">
<li><p>&lt;MSB&gt; Most significant byte of the TLV frame payload.</p></li>
<li><p>&lt;MSB-1&gt; … Remaining bytes of the payload, listed in descending order of significance, ending with the least significant byte.</p></li>
</ul>
</div></blockquote>
<p>Example:</p>
<blockquote>
<div><p>Read node configuration:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; utlv 8 0</span>
<span class="go">CRC: 0x37</span>
<span class="go">OUTPUT(hex):</span>
<span class="go">40 01 00 06 46 03 1c 60 00 5f</span>
</pre></div>
</div>
</div></blockquote>
</div>
</div>


           </div>
