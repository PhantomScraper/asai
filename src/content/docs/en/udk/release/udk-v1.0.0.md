---
title: "Version v1.0.0"
lang: en
slug: "udk/release/udk-v1.0.0"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/release/udk-v1.0.0/"
order: 59
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v1-0-0">
<h1>Version v1.0.0</h1>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p><strong>Version</strong>: UDK v1.0.0</p></li>
<li><p><strong>Release Date</strong>: Jan 8, 2025</p></li>
</ul>
</div>
<ul class="simple">
<li><p>LEAPS UWB Subsystem</p>
<ul>
<li><p>Bugfixes + Improvements based on the feedback from the customers and team</p></li>
<li><p>Improve the UL-TDoA time synchronization and multileteration algorithms.</p></li>
<li><p>Add new trilateration algorithm</p></li>
<li><p>Power consumption validation and optimization</p></li>
<li><p>Use of the outdoor test setup for automated tests (system test, API tests, testing of different modes and configuration of the system)</p></li>
<li><p>Improve backhaul data as a part of the gateway functionality</p></li>
<li><p>Update the DW3000 drivers to the latest version</p></li>
<li><p>Ensure auto-positioning measurements is done with any amount of Anchors</p></li>
<li><p>Improve the location engine filtering</p></li>
<li><p>Add a new RF profile that is FiRa compatible</p></li>
<li><p>Change default preamble code for the CH9</p></li>
<li><p>Added autolog out for shell API to optimize the power consumption</p></li>
<li><p>Add measurement and position metrics</p></li>
<li><p>Validate on DWM3001, DWM1001, Murata 2AB</p></li>
<li><p>Production release validation</p></li>
</ul>
</li>
<li><p>LEAPS Server</p>
<ul>
<li><p>Bugfixes + Improvements based on the feedback from the customers and the team</p></li>
<li><p>Production release validation</p></li>
</ul>
</li>
<li><p>LEAPS Gateway</p>
<ul>
<li><p>Bugfixes</p></li>
<li><p>Improve handling of the USB interface</p></li>
<li><p>Production release validation</p></li>
</ul>
</li>
<li><p>LEAPS Manager Android</p>
<ul>
<li><p>Debug and bugfixes issues on some of the Android devices, improve Bluetooth stability</p></li>
<li><p>Allow changing MQTT network ID</p></li>
<li><p>Improve user management and permissons</p></li>
<li><p>Improve real-time updates of the node list and in the Grid</p></li>
<li><p>Code refactoring and clean up</p></li>
<li><p>Production release validation</p></li>
</ul>
</li>
<li><p>LEAPS Manager iOS</p>
<ul>
<li><p>Release on App Store</p></li>
<li><p>Bugfixes</p></li>
<li><p>Add useful properties to the nodes</p></li>
<li><p>Improve real-time updates of the node list and in the Grid</p></li>
<li><p>Improve the speed of FW update</p></li>
</ul>
</li>
<li><p>LEAPS Center</p>
<ul>
<li><p>Bugfixes</p></li>
<li><p>Update Docker support</p></li>
<li><p>Update VMWare support</p></li>
<li><p>Production release validation</p></li>
</ul>
</li>
<li><p>UDK SDK</p>
<ul>
<li><p>Bugfixes</p></li>
<li><p>Documentation improvements based on customers feedback</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<div class="section" id="known-limitations">
<h2>Known Limitations</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 53%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>No.</p></th>
<th class="head"><p>Summary</p></th>
<th class="head"><p>Affected</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>1</p></td>
<td><p><a class="reference internal" href="/docs/en/udk/known-limitation/limit-001#limitation-1"><span class="std std-ref">UWB Calibration of the devices is not supported.</span></a></p></td>
<td><p><a class="reference internal" href="/docs/en/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">Locate Device using Angle-of-Arrival (AoA) Demo</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p><a class="reference internal" href="/docs/en/udk/known-limitation/limit-002#limitation-2"><span class="std std-ref">Configuration of some device parameters is not supported.</span></a></p></td>
<td><p><a class="reference internal" href="/docs/en/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">Locate Device using Angle-of-Arrival (AoA) Demo</span></a></p></td>
</tr>
</tbody>
</table>
<div class="toctree-wrapper compound">
</div>
</div>
<hr class="docutils">
<div class="section" id="known-issues">
<h2>Known Issues</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 53%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>No.</p></th>
<th class="head"><p>Summary</p></th>
<th class="head"><p>Affected</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>1</p></td>
<td><p><a class="reference internal" href="/docs/en/udk/known-issue/issue-004#issue-1"><span class="std std-ref">Configuration of some of the FiRa parameters does not work reliably.</span></a></p></td>
<td><p><a class="reference internal" href="/docs/en/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">Locate Device using Angle-of-Arrival (AoA) Demo</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p><a class="reference internal" href="/docs/en/udk/known-issue/issue-005#issue-2"><span class="std std-ref">The device sometimes resets unexpectedly during starting or during stopping of the ranging.</span></a></p></td>
<td><p><a class="reference internal" href="/docs/en/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">Locate Device using Angle-of-Arrival (AoA) Demo</span></a></p></td>
</tr>
</tbody>
</table>
<div class="toctree-wrapper compound">
</div>
<hr class="docutils">
</div>
</div>


           </div>
