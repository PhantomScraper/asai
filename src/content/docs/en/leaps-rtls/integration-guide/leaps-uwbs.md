---
title: "LEAPS UWBS"
lang: en
slug: "leaps-rtls/integration-guide/leaps-uwbs"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-uwbs/"
order: 66
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwbs">
<span id="leapsuwbs"></span><h1>LEAPS UWBS</h1>
<p><a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> UWBS is a fully-embedded and advanced UWB Sub-System that covers a wide range of use cases. One UWB Sub-System is configurable in different modes and profiles. The UWBS can run as an Anchor, a Tag or a Gateway. The networking profiles are fully scalable with high capacity and low-power.</p>
<hr class="docutils">
<div class="section" id="software-architecture">
<h2>Software Architecture</h2>
<div class="figure align-center" id="id1">
<a class="reference internal image-reference" href="../../../_images/leaps_uwbs.png"><img alt="../../../_images/leaps_uwbs.png" src="/docs-assets/_images/leaps_uwbs.png" style="width: 730.8000000000001px; height: 657.9px;"></a>
<p class="caption"><span class="caption-text"><a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> UWBS Architecture</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>Versatility makes it easy to balance the system requirements, costs, deployment time and maintenance complexity. Applications range from simple distance proximity to high-speed tracking or navigation of an unlimited receiver.</p></li>
<li><p>It integrates a sophisticated UWBMAC that allows adaptive clustering of the infrastructure devices, air-time reuse, slot allocation, etc. A scalable, proven collision detection, collision avoidance and collision resolution allow the system to function robustly in complex environments.</p></li>
<li><p>Supported measurement techniques include TWR, DL-TDoA and UL-TDoA. Integrated location engines allow the device to operate independently in the navigation mode using DL-TDoA or TWR.</p></li>
<li><p>Superior power management provides a long battery lifetime for both TWR and TDoA modes.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="used-terminology">
<h2>Used terminology</h2>
<ul class="simple">
<li><p><strong>Anchor</strong>: Has fixed location.</p></li>
<li><p><strong>Tag</strong>: Changes location, determines position dynamically with the help of anchors.</p></li>
<li><p><strong>Gateway</strong>: Provides stateful information about network nodes (read/introspect), caches node information, might even collect data and track history, provides means for the application layer to interact with UWB network elements (a.k.a. <em>interaction proxy</em>).</p></li>
<li><p><strong>Node</strong>: Network node (anchor, tag, gateway, …).</p></li>
<li><p><strong>LE</strong>: Location engine.</p></li>
<li><p><strong>CORE_INT:</strong> GPIO pin reserved by firmware to inform users about new UART/SPI interface events.</p></li>
<li><p><strong>TLV:</strong> Type-Length-Value encoding.</p></li>
<li><p><strong>UWBS</strong> UWB sub-system.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="uwb-rf">
<h2>UWB RF</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 17%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"></th>
<th class="head"><p><a class="reference internal" href="/docs/en/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> ,
<a class="reference internal" href="/docs/en/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> ,
PANS v2.0</p></th>
<th class="head"><p><a class="reference internal" href="/docs/en/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a>,
<a class="reference internal" href="/docs/en/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
<th class="head"><p>Qorvo FiRa</p></th>
<th class="head"><p>Custom stack (DW3000 RF)</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Channel</p></td>
<td><p>5</p></td>
<td><p>5,9</p></td>
<td><p>9</p></td>
<td><p>5,9</p></td>
</tr>
<tr class="row-odd"><td><p>PRF</p></td>
<td><p>64M</p></td>
<td><p>64M</p></td>
<td><p>64M</p></td>
<td><p>16M, 64M</p></td>
</tr>
<tr class="row-even"><td><p>Preamble Length</p></td>
<td><p>128</p></td>
<td><p>128</p></td>
<td><p>64</p></td>
<td><p>32, 64, 72, 128, 256, 512, 1024, 1536, 2048, 4096</p></td>
</tr>
<tr class="row-odd"><td><p>PAC Size</p></td>
<td><p>8</p></td>
<td><p>8</p></td>
<td><p>8</p></td>
<td><p>4, 8, 16, 32</p></td>
</tr>
<tr class="row-even"><td><p>Rx code</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>1-29 (PRF16: 1-8; PRF64: 9-24)</p></td>
</tr>
<tr class="row-odd"><td><p>Tx code</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>1-29 (PRF16: 1-8; PRF64: 9-24)</p></td>
</tr>
<tr class="row-even"><td><p>SFD Type</p></td>
<td><p>IEEE 802.15.4 short 8-symbol</p></td>
<td><p>IEEE 802.15.4 short 8-symbol</p></td>
<td><p>IEEE 802.15.4z defined 8-symbol</p></td>
<td><p>IEEE 802.15.4 short 8-symbol, Decawave-defined 8-symbols,
Decawave-defined 16-symbols, IEEE 802.15.4z defined 8-symbol</p></td>
</tr>
<tr class="row-odd"><td><p>Data Rate</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8Mbit/s, 850kbits/s</p></td>
</tr>
<tr class="row-even"><td><p>PHR Mode</p></td>
<td><p>DW proprietary extended
frames PHR mode</p></td>
<td><p>DW proprietary extended
frames PHR mode</p></td>
<td><p>Standard</p></td>
<td><p>Standard, Extended (DW proprietary extended frames PHR mode)</p></td>
</tr>
<tr class="row-odd"><td><p>PHR Rate</p></td>
<td><p>Standard</p></td>
<td><p>Standard</p></td>
<td><p>Standard</p></td>
<td><p>Standard, PHR at data rate (6M81)</p></td>
</tr>
<tr class="row-even"><td><p>SFD Timeout</p></td>
<td><p>129</p></td>
<td><p>129</p></td>
<td><p>65</p></td>
<td><p>Configurable</p></td>
</tr>
<tr class="row-odd"><td><p>STS Mode</p></td>
<td><p><cite>-</cite></p></td>
<td><p>OFF</p></td>
<td><p>OFF</p></td>
<td><p>Off, 1, 2, No data, Super Deterministic Codes</p></td>
</tr>
<tr class="row-even"><td><p>STS Length</p></td>
<td><p><cite>-</cite></p></td>
<td><p>0</p></td>
<td><p>0</p></td>
<td><p>32, 64, 128, 256, 512, 1024, 2048</p></td>
</tr>
<tr class="row-odd"><td><p>PDOA Mode</p></td>
<td><p><cite>-</cite></p></td>
<td><p>M0</p></td>
<td><p>M1</p></td>
<td><p>M0, M1, M3</p></td>
</tr>
<tr class="row-even"><td rowspan="2"><p>Hardware supported</p></td>
<td><p><cite>UWB IC:</cite> DW1000</p></td>
<td><p><cite>UWB IC:</cite> DW3000 family, QM33 family</p></td>
<td><p><cite>UWB IC:</cite> DW3000 family, QM33 family</p></td>
<td><p><cite>UWB IC:</cite> DW3000 family, QM33 family</p></td>
</tr>
<tr class="row-odd"><td><p><cite>Modules:</cite> DWM1001C</p></td>
<td><p><cite>Modules:</cite> DWM3001C, Murata Type2AB</p></td>
<td><p><cite>Modules:</cite> DWM3001C, Murata Type2AB</p></td>
<td><p><cite>Modules:</cite> DWM3001C, Murata Type2AB</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="ble-rf">
<h2>BLE RF</h2>
<p>We are supporting 2M PHY, frequency band as 2.4GHz, 40 channels with 2MHz spacing (more detail can be found in BLE specification 5.3).</p>
</div>
</div>


           </div>
