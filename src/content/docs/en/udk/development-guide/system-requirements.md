---
title: "System Requirements"
lang: en
slug: "udk/development-guide/system-requirements"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/development-guide/system-requirements/"
order: 44
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="anchor-dev-sr"></span><h1>System Requirements</h1>
<p>The following sections provide details on necessary software and hardware before starting with SDK on UDK devices.</p>
<hr class="docutils">
<div class="section" id="hardware-software">
<h2>Hardware &amp; Software</h2>
<p>Please install below software tool before jump into development phase:</p>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 80%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Item</p></th>
<th class="head"><p>Version</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.14.2">Zephyr SDK</a></p></td>
<td><p>0.14.2</p></td>
<td><p>Mandatory. The RTOS includes a BSP package, supported for the UDK device.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference external" href="https://openocd.org/pages/getting-openocd.html">OpenOCD</a></p></td>
<td><p>–</p></td>
<td><p>Aim to provide firmware upgrades, debugging, programming in the system. For detailed installation, refer to the section <a class="reference internal" href="/docs/en/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">Programming/Upgrading firmware</span></a>.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference external" href="https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack">SEGGER J-Link</a></p></td>
<td><p>–</p></td>
<td><p>Aim to provide firmware upgrades, debugging, and programming in the system. For detail installation, refer to the section <a class="reference internal" href="/docs/en/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">Programming/Upgrading firmware</span></a>.</p></td>
</tr>
<tr class="row-odd"><td><p>Desktop Device</p></td>
<td><p>–</p></td>
<td><p>Mandatory, recommend: supports Linux environment to fit with guidelines.</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="environment-setup">
<h2>Environment Setup</h2>
<a class="reference internal image-reference" href="../../../_images/development_tools.png"><img alt="../../../_images/development_tools.png" class="align-right" src="/docs-assets/_images/development_tools.png" style="width: 339.25px; height: 203.75px;"></a>
<p>Each device is equipped with an onboard USB DAPLink, facilitating seamless programming and debugging of the target microcontroller.</p>
<p>The USB DAPLink must be connected to a PC to program the firmware into the boards.</p>
<p>The figure below depicts the isolated connection required for programming the firmware.</p>
</div>
</div>


           </div>
