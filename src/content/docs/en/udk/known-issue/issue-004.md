---
title: "ISSUE004"
lang: en
slug: "udk/known-issue/issue-004"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/known-issue/issue-004/"
order: 85
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="issue004">
<span id="issue-1"></span><h1>ISSUE004</h1>
<hr class="docutils">
<p><strong>Summary</strong></p>
<blockquote>
<div><p>Configuration of some of the FiRa parameters does not work reliably.</p>
</div></blockquote>
<hr class="docutils">
<p><strong>Affected version</strong>:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">v0.16.2</span></code></p></li>
</ul>
<hr class="docutils">
<p><strong>How to impact users</strong>:</p>
<ul class="simple">
<li><p>Affected: <a class="reference internal" href="/docs/en/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">Locate Device using Angle-of-Arrival (AoA) Demo</span></a></p></li>
<li><p>Unexpected Behavior: Configuration of some FiRa parameters does not work reliably.</p>
<ul>
<li><p>The Report angle parameter cannot be turned off when the Measurement scheme is either SS-TWR non deferred or DS-TWR non deferred.</p></li>
<li><p>The Ranging does not work reliably when the parameter Ranging duration is configured to 1000 milliseconds.</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<p><strong>Steps to Reproduce</strong>:</p>
<ul class="simple">
<li><p>None</p></li>
</ul>
<hr class="docutils">
<p><strong>Workaround</strong>:</p>
<ul class="simple">
<li><p>None</p></li>
</ul>
</div>


           </div>
