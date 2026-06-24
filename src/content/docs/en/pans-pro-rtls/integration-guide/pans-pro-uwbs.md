---
title: "PANS PRO UWBS"
lang: en
slug: "pans-pro-rtls/integration-guide/pans-pro-uwbs"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/pans-pro-uwbs/"
order: 92
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-uwbs">
<span id="id1"></span><h1>PANS PRO UWBS</h1>
<p><a class="reference internal" href="#pans-pro-uwbs"><span class="std std-ref">PANS PRO UWBS</span></a> is a complete Real-Time Location System and network stack - configurable into anchor, tag or gateway nodes.</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>Utilizes the TWR (Two-Way Ranging) technique: Integrated location engines enable the device to operate independently in navigation mode using TWR.</p></li>
<li><p>Supports networking profile 0: Fully scalable <a class="footnote-reference brackets" href="#note-1" id="id2">1</a> with high capacity and low power consumption.</p></li>
<li><p>Network Visualization tool support: Compatible with PANS PRO Manager for Android, and LEAPS Center WebApp for Windows, Linux, and macOS platforms.</p></li>
<li><p>Firmware update and maintenance: Facilitates easy updates and ongoing maintenance.</p></li>
<li><p>Compatibility: Fully compatible with PANS RTLS (a freemium version) and includes long-term bug-fixing support.</p></li>
<li><p>Superior power management: Ensures extended battery life.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="used-terminology">
<h2>Used Terminology</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 86%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Term</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>Anchor</strong></p></td>
<td><p>Has a fixed location.</p></td>
</tr>
<tr class="row-odd"><td><p><strong>Tag</strong></p></td>
<td><p>Moving location determines dynamically it’s position with the help of anchors.</p></td>
</tr>
<tr class="row-even"><td><p><strong>Gateway</strong></p></td>
<td><p>Knows about all nodes in the network, provides stateful
information about network nodes (read/introspect), caches
this information (might even collect data and track
history) and provides it to the gateway client. It also
provides a means to interact with network elements (a.k.a. interaction proxy)</p></td>
</tr>
<tr class="row-odd"><td><p><strong>Node</strong></p></td>
<td><p>Network node (anchor, tag, gateway, …)</p></td>
</tr>
<tr class="row-even"><td><p><strong>LE</strong></p></td>
<td><p>Location engine</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<dl class="footnote brackets">
<dt class="label" id="note-1"><span class="brackets"><a class="fn-backref" href="#id2">1</a></span></dt>
<dd><p>Users must use the Industrial Gateway LC5 unit</p>
</dd>
</dl>
</div>
</div>


           </div>
