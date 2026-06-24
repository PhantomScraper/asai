---
title: "Comparison"
lang: en
slug: "leaps-solutions/comparison"
section: "leaps-solutions"
sourceUrl: "https://docs.leapslabs.com/leaps-solutions/comparison/"
order: 8
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="comparison">
<span id="comparision"></span><h1>Comparison</h1>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 19%">
<col style="width: 32%">
<col style="width: 25%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Item</p></th>
<th class="head"><p><a class="reference internal" href="/docs/en/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a></p></th>
<th class="head"><p><a class="reference internal" href="/docs/en/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
<th class="head"><p>PANS RTLS</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Supported
profiles</p></td>
<td><p>Profile 2, 3, 4, 5</p></td>
<td><p>Profile 0</p></td>
<td><p>Profile 0</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Firmware update</div>
<div class="line">and maintenance</div>
</div>
</td>
<td><p>Yes</p></td>
<td><p>Limited</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">Use in production</div>
<div class="line">deployment</div>
</div>
</td>
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Limited</p></td>
</tr>
<tr class="row-odd"><td><p>Scalability</p></td>
<td><p>Fully scalable</p></td>
<td><p>Fully scalable  <a class="footnote-reference brackets" href="#note-0" id="id1">1</a></p></td>
<td><p>Fully scalable <a class="footnote-reference brackets" href="#note-1" id="id2">2</a></p></td>
</tr>
<tr class="row-even"><td><p>Location capability</p></td>
<td><div class="line-block">
<div class="line">TWR <a class="footnote-reference brackets" href="#note-2" id="id3">3</a>,</div>
<div class="line">UL-TDoA <a class="footnote-reference brackets" href="#note-3" id="id4">4</a>,</div>
<div class="line">DL-TDoA <a class="footnote-reference brackets" href="#note-4" id="id5">5</a></div>
</div>
</td>
<td><p>TWR only</p></td>
<td><p>TWR only</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Max. update rate</div>
<div class="line">per tag <a class="footnote-reference brackets" href="#note-5" id="id6">6</a></div>
</div>
</td>
<td><div class="line-block">
<div class="line">Up to 10 Hz for TWR</div>
<div class="line">Up to 50 Hz for UL-TDoA</div>
<div class="line">Up to 50 Hz for DL-TDoA</div>
</div>
</td>
<td><p>Up to 10 Hz for TWR</p></td>
<td><p>Up to 10 Hz for TWR</p></td>
</tr>
<tr class="row-even"><td><p>Total update capacity
<a class="footnote-reference brackets" href="#note-5" id="id7">6</a></p></td>
<td><div class="line-block">
<div class="line">Up to 320 Hz for TWR</div>
<div class="line">Up to 700 Hz for UL-TDoA</div>
<div class="line">Unlimited for DL-TDoA</div>
</div>
</td>
<td><p>Up to 150 Hz for TWR</p></td>
<td><p>Up to 150 Hz for TWR</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Max. measurements</div>
<div class="line">per update</div>
</div>
</td>
<td><p>Up to 30 <a class="footnote-reference brackets" href="#note-5" id="id8">6</a></p></td>
<td><p>4</p></td>
<td><p>4</p></td>
</tr>
<tr class="row-even"><td><p>Data server</p></td>
<td><p>Advanced</p></td>
<td><p>Advanced</p></td>
<td><p>Basic (duplicity filtration)</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Data latency</div>
<div class="line">on server</div>
</div>
</td>
<td><p>50 ms <a class="footnote-reference brackets" href="#note-5" id="id9">6</a></p></td>
<td><p>update rate + 50 ms</p></td>
<td><p>update rate + 50 ms</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">Data latency</div>
<div class="line">on the device</div>
</div>
</td>
<td><p>&lt; 10ms</p></td>
<td><p>&lt; 10ms</p></td>
<td><p>&lt; 10ms</p></td>
</tr>
<tr class="row-odd"><td><p>Server API</p></td>
<td><p>MQTT</p></td>
<td><p>MQTT</p></td>
<td><p>MQTT</p></td>
</tr>
<tr class="row-even"><td><p>Device API</p></td>
<td><p>UART, SPI, USB, Bluetooth</p></td>
<td><p>UART, SPI, Bluetooth</p></td>
<td><p>UART, SPI, Bluetooth</p></td>
</tr>
<tr class="row-odd"><td><p>Bluetooth API</p></td>
<td><p>Advanced (unified API)</p></td>
<td><p>Legacy</p></td>
<td><p>Legacy</p></td>
</tr>
<tr class="row-even"><td><p>Bluetooth Security</p></td>
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-odd"><td><p>Tools</p></td>
<td><p>LEAPS Manager for Android and iOS.
<a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> WebApp for
Windows/Linux/macOS.</p></td>
<td><p>PANS PRO Manager for Android.
LEAPS Center WebApp for
Windows/Linux/macOS.</p></td>
<td><p>DRTLS Manager for Android.
Basic WebApp for
Windows/Linux/macOS.</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">Compatible with</div>
<div class="line">PANS RTLS</div>
</div>
</td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>System updates</p></td>
<td><p>Yes</p></td>
<td><p>Bugfixes</p></td>
<td><p>No</p></td>
</tr>
<tr class="row-even"><td><p>Long term support</p></td>
<td><p>Yes</p></td>
<td><p>Bugfixes</p></td>
<td><p>No</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<dl class="footnote brackets">
<dt class="label" id="note-0"><span class="brackets"><a class="fn-backref" href="#id1">1</a></span></dt>
<dd><p>When LC5A Industrial Gateway is used</p>
</dd>
<dt class="label" id="note-1"><span class="brackets"><a class="fn-backref" href="#id2">2</a></span></dt>
<dd><p>Users must use the Raspberry Pi 3B as a Gateway device</p>
</dd>
<dt class="label" id="note-2"><span class="brackets"><a class="fn-backref" href="#id3">3</a></span></dt>
<dd><p>Two-Way Ranging</p>
</dd>
<dt class="label" id="note-3"><span class="brackets"><a class="fn-backref" href="#id4">4</a></span></dt>
<dd><p>Uplink Time Difference of Arrival</p>
</dd>
<dt class="label" id="note-4"><span class="brackets"><a class="fn-backref" href="#id5">5</a></span></dt>
<dd><p>Downlink Time Difference of Arrival</p>
</dd>
<dt class="label" id="note-5"><span class="brackets">6</span><span class="fn-backref">(<a href="#id6">1</a>,<a href="#id7">2</a>,<a href="#id8">3</a>,<a href="#id9">4</a>)</span></dt>
<dd><p>Depending on network profile and measurement mode</p>
</dd>
</dl>
<hr class="docutils">
</div>


           </div>
