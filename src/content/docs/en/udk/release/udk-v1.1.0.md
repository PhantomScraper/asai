---
title: "Version v1.1.0"
lang: en
slug: "udk/release/udk-v1.1.0"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/release/udk-v1.1.0/"
order: 20
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v1-1-0">
<h1>Version v1.1.0</h1>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p><strong>Version</strong>: UDK v1.1.0</p></li>
<li><p><strong>Release Date</strong>: Jun 16, 2025</p></li>
</ul>
</div>
<ul>
<li><p>LEAPS UWB Subsystem</p>
<blockquote>
<div><ul class="simple">
<li><p>Bugfixes</p></li>
<li><p>Power optimization using BLE activation</p></li>
<li><p>Optimize further the UWB capacity</p></li>
<li><p>Improve TWR Tag roaming capability between different networks</p></li>
<li><p>Add sniffer functionality</p></li>
<li><p>Make measurement data for the DL-TDoA available to the users</p></li>
<li><p>Add APIs in order to be able to validate the full capacity of the uplink and downlink user data when TWR is used</p></li>
<li><p>In-depth revalidation of the range</p></li>
<li><p>Add secure boot option</p></li>
<li><p>Further runtime optimization of the UWB routines</p></li>
<li><p>Memory optimization review</p></li>
<li><p>Review and optimize further the power consumption</p></li>
<li><p>Validate on DWM3001, DWM1001, Murata 2AB</p></li>
<li><p>Use of the outdoor test setup for automated tests (system test, API tests, testing of different modes and configuration of the system)</p></li>
<li><p>Ensure auto-positioning measurements is done with any amount of Anchors</p></li>
<li><p>Add new trilateration algorithm, added calculation time</p></li>
<li><p>Add coexisting networks</p></li>
<li><p>Add Zone-ID to improve the position estimation accuracy</p></li>
<li><p>Add network mask so a Tag can roam between networks that fits in the mask</p></li>
<li><p>Add support for InsightSIP ISP3080, power consumption optimization</p></li>
<li><p>Add support for the new accelerometer used by the ISP3080</p></li>
<li><p>Add sending of distances when location engine is disabled</p></li>
<li><p>Bugfixed/Improved the UL-TDOA slot timing, capacity, configuration</p></li>
<li><p>Added non-volatile counters for power and reset cycles</p></li>
<li><p>Add board voltage specific configuration, voltage measurement and battery status indication, improved battery protection</p></li>
<li><p>Add temperature measurement and data collection</p></li>
<li><p>Revalidate the antenna delay and applied correction for each of the RF setup</p></li>
<li><p>Add automatic Rx reception rate calculation</p></li>
<li><p>Add shell debug support via the SWD to debug platforms without UART (e.g. InsightSIP ISP3080)</p></li>
<li><p>Improve the data backhaul</p></li>
<li><p>Improve anchor selection strategy for the TWR RTLS</p></li>
<li><p>Various API improvements</p></li>
<li><p>Add support for the SPI flash memory</p></li>
<li><p>Implement measures to prepare for the new RED / CRA directives</p></li>
<li><p>Initial preparation for the QPG6200 support</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Server</p>
<blockquote>
<div><ul class="simple">
<li><p>Improving the time-synchronization for the UL-TDoA</p></li>
<li><p>Improving the multilateration algorithm for the UL-TDoA and DL-TDoA</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Gateway</p>
<blockquote>
<div><ul class="simple">
<li><p>Bugfixes</p></li>
<li><p>Optimize performance to handle higher capacity</p></li>
<li><p>Allow configuration of the UWB RF parameters, Tx power settings</p></li>
<li><p>Added support of overlay configuration file</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Manager Android</p>
<blockquote>
<div><ul class="simple">
<li><p>Bugfixes</p></li>
<li><p>Add dark mode</p></li>
<li><p>Allow auto-positioning with more than 6 anchors and not all in Bluetooth range</p></li>
<li><p>Demo configuration behavior improvements</p></li>
<li><p>Allows configure UWB properties</p></li>
<li><p>Add device filter feature</p></li>
<li><p>Add export device feature</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Manager iOS</p>
<blockquote>
<div><ul class="simple">
<li><p>Bugfixes</p></li>
<li><p>Add battery level display</p></li>
<li><p>Add tooltips</p></li>
<li><p>Network improvements</p></li>
<li><p>Heatmap improvements</p></li>
<li><p>Demo configuration behavior improvements</p></li>
<li><p>Improvements for the Bluetooth discovery and communication</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Center</p>
<blockquote>
<div><ul class="simple">
<li><p>Bugfixes + Improvements based on the feedback from the customers and the team</p></li>
<li><p>Improve the heatmap</p></li>
<li><p>Add flip functions for the floorplan</p></li>
<li><p>Add grid configuration</p></li>
<li><p>Add surrounding anchor signal map</p></li>
<li><p>Add zone alarm feature</p></li>
<li><p>Add different shapes of geofencing</p></li>
<li><p>Add logging feature</p></li>
<li><p>Add tools for validation of full-capacity of uplink/downlink user data when TWR is used</p></li>
<li><p>Investigate whether 3D objects can be imported to the map</p></li>
<li><p>Add tooltips</p></li>
<li><p>Add zoom in/out buttons in 2D/3D</p></li>
</ul>
</div></blockquote>
</li>
<li><p>UDK SDK</p>
<blockquote>
<div><ul class="simple">
<li><p>Bugfixes</p></li>
<li><p>Documentation improvements based on customers feedback</p></li>
<li><p>Release on Github</p></li>
</ul>
</div></blockquote>
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
