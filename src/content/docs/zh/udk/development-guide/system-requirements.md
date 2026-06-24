---
title: "系统要求"
lang: zh
slug: "udk/development-guide/system-requirements"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/development-guide/system-requirements/"
order: 44
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="anchor-dev-sr"></span><h1>系统要求</h1>
<p>在开始在UDK设备上使用SDK之前，以下部分提供了有关必要软件和硬件的详细信息。</p>
<hr class="docutils">
<div class="section" id="hardware-software">
<h2>软硬件</h2>
<p>请在进入开发阶段之前安装以下软件工具:</p>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 80%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>项目</p></th>
<th class="head"><p>版本</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.14.2">Zephyr SDK</a></p></td>
<td><p>0.14.2</p></td>
<td><p>强制性的。RTOS包括一个BSP包，支持UDK设备。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference external" href="https://openocd.org/pages/getting-openocd.html">OpenOCD</a></p></td>
<td><p>–</p></td>
<td><p>旨在提供系统中的固件升级、调试、编程。有关详细的安装，请参阅一节 <a class="reference internal" href="/docs/zh/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">编程/升级固件</span></a>。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference external" href="https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack">SEGGER J-Link</a></p></td>
<td><p>–</p></td>
<td><p>旨在提供系统中的固件升级、调试和编程。有关安装的详细信息，请参阅一节 <a class="reference internal" href="/docs/zh/udk/development-guide/firmware-reflashing#flashingfirmware"><span class="std std-ref">编程/升级固件</span></a>。</p></td>
</tr>
<tr class="row-odd"><td><p>桌面设备</p></td>
<td><p>–</p></td>
<td><p>强制性，推荐:支持Linux环境以符合指导方针。</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="environment-setup">
<h2>环境设置</h2>
<a class="reference internal image-reference" href="../../../_images/development_tools.png"><img alt="../../../_images/development_tools.png" class="align-right" src="/docs-assets/zh-cn/_images/development_tools.png" style="width: 339.25px; height: 203.75px;"></a>
<p>每个设备都配备了一个板载USB DAPLink，便于对目标微控制器进行无缝编程和调试。</p>
<p>DAPLink必须连接到PC，才能将固件编程到板中。</p>
<p>下图描述了固件编程所需的隔离连接。</p>
</div>
</div>


           </div>
