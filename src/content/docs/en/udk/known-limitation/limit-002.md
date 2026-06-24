---
title: "LIMIT002"
lang: en
slug: "udk/known-limitation/limit-002"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/known-limitation/limit-002/"
order: 81
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="limit002">
<span id="limitation-2"></span><h1>LIMIT002</h1>
<p><strong>Summary</strong></p>
<p>Configuration of some device parameters is not supported.</p>
<hr class="docutils">
<p><strong>How to impact users</strong></p>
<ul class="simple">
<li><p>None</p></li>
</ul>
<hr class="docutils">
<p><strong>Steps to Reproduce</strong></p>
<ul class="simple">
<li><p>Affected: <a class="reference internal" href="/docs/en/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">Locate Device using Angle-of-Arrival (AoA) Demo</span></a></p></li>
<li><p>Configure the <strong>Qorvo UCI mode</strong> of the <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a></p></li>
<li><p>Unexpected Behavior: The configuration of some device parameters are not supported.</p>
<ul>
<li><p>Transmit Power</p></li>
<li><p>Antenna Delay</p></li>
<li><p>Pulse Shape.</p></li>
<li><p>LNA Activation</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<p><strong>Workaround</strong></p>
<ul class="simple">
<li><p>None</p></li>
</ul>
</div>


           </div>
