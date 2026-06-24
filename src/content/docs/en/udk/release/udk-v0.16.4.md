---
title: "Version v0.16.4"
lang: en
slug: "udk/release/udk-v0.16.4"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/release/udk-v0.16.4/"
order: 58
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v0-16-4">
<h1>Version v0.16.4</h1>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p><strong>Version</strong>: UDK v0.16.4</p></li>
<li><p><strong>Release Date</strong>: Nov 21, 2024</p></li>
</ul>
</div>
<ul class="simple">
<li><p>LEAPS UWB Subsystem</p>
<ul>
<li><p>Bugfixes</p></li>
<li><p>Add UL-TDoA support</p></li>
<li><p>Bugfix of backhaul issues for USB and SPI interfaces</p></li>
<li><p>Improve power consumption</p></li>
<li><p>Installing an outdoor test setup</p></li>
<li><p>Set up an automatic build system, created related tools to perform the tests</p></li>
<li><p>Make the UWB certification and test routines to the customers</p></li>
</ul>
</li>
<li><p>LEAPS Server</p>
<ul>
<li><p>Bugfixes</p></li>
<li><p>Add UL-TDoA support</p></li>
<li><p>Add multilateration algorithm and location engine related components</p></li>
<li><p>Add measurement and position metrics</p></li>
</ul>
</li>
<li><p>LEAPS Gateway</p>
<ul>
<li><p>Add UL-TDoA support</p></li>
<li><p>Optimized backhaul data</p></li>
</ul>
</li>
<li><p>LEAPS Manager Android</p>
<ul>
<li><p>Bugfixes</p></li>
<li><p>Add UL-TDOA support</p></li>
<li><p>Add measurement and position metrics</p></li>
<li><p>Add real-time updates of the node list and in the Grid</p></li>
<li><p>Add battery level display</p></li>
<li><p>Improve floorplan configuration flow</p></li>
<li><p>Add list of supported HW in the FW update window</p></li>
<li><p>Add logging</p></li>
<li><p>Add MQTT interface</p></li>
<li><p>Add multiple nodes selection and configuration</p></li>
<li><p>Improve the UI/UX</p></li>
</ul>
</li>
<li><p>LEAPS Manager iOS</p>
<ul>
<li><p>Release via TestFlight</p></li>
<li><p>Bugfixes</p></li>
<li><p>All the demos can be configured using the Demo Selector and various other related improvements</p></li>
<li><p>Add UL-TDOA support</p></li>
<li><p>Add measurement and position metrics</p></li>
<li><p>Add real-time updates of the node list and in the Grid</p></li>
<li><p>Add discovery time configuration</p></li>
<li><p>Improve the auto-positioning (allow handling nodes outside of the BLE range)</p></li>
<li><p>Add metric/imperial units configuration</p></li>
<li><p>Update stationary/nominal update rate configuration according to the new design</p></li>
<li><p>Floorplan improvements</p></li>
<li><p>Add count down counter for the discovery</p></li>
<li><p>Improve the 2D Grid</p></li>
<li><p>Display the UWBS modes</p></li>
</ul>
</li>
<li><p>LEAPS Center</p>
<ul>
<li><p>New UI/UX with many improvements</p></li>
<li><p>Add 360 floorplan rotation, add ratio reset for floorplan</p></li>
<li><p>Add support page</p></li>
<li><p>Add visible features for zones, improve zone configuration</p></li>
<li><p>Add measurement and position metrics.</p></li>
<li><p>Improve node configuration</p></li>
<li><p>Update spring framework</p></li>
<li><p>Docker support</p></li>
</ul>
</li>
<li><p>UDK SDK</p>
<ul>
<li><p>The DW3000 drivers have been updated to the latest version</p></li>
<li><p>All examples have been validated</p></li>
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
