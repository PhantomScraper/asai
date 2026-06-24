---
title: "LEAPS Manager"
lang: zh
slug: "leaps-rtls/infrastructure/leaps-manager"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/infrastructure/leaps-manager/"
order: 69
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-manager">
<span id="leapsmanager"></span><h1>LEAPS Manager</h1>
<p><a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 是一个重要的工具，为UDK（<a class="reference external" href="https://docs.leapslabs.com/UDK/">All-in-One超宽带演示套件</a>）提供设备发现、设备配置、网络配置、网络管理和位置可视化 以及LEAPS RTLS（一种先进的超宽带实时定位系统）。</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>演示向导允许用户以简单, 超快的方式配置套件的预定义演示设置。</p></li>
<li><p>2D和3D网格提供实时位置更新，并将网络中的设备可视化。</p></li>
<li><p>与设备的通信是通过BLE完成的，支持多达6个并发连接，以保持连接可靠性。</p></li>
<li><p>当使用数据集中时，可以通过MQTT与 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> 进行通信，从而对整个网络的设备进行管理和可视化。</p></li>
<li><p>其他有用的功能还包括用户管理, 通过 BLE 更新固件, 锚自动定位, 位置记录和调试控制台。</p></li>
</ul>
<hr class="docutils">
<div class="section" id="system-environment">
<h3>系统环境</h3>
<p><a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 是基于Android API 24级及后续版本开发的。参见 <a class="reference external" href="https://apilevels.com">apilevels</a></p>
<ul class="simple">
<li><p>安卓最低版本:安卓7（API 24）</p></li>
<li><p>最小内存:100 MB（可用磁盘空间）</p></li>
<li><p>最低Bluetooth版本:4.2（建议5.0或更高版本）</p></li>
<li><p>建议使用android设备:谷歌Pixel 7（同等设备）</p></li>
</ul>
<p><strong>不推荐的设备是三星Galaxy Tab A8</strong>，请参阅已知问题列表:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/f/nordic-q-a/88557/samsung-galaxy-tab-a8-does-not-work-with-nrf-mesh-android-app">设备不适用于nrf mesh安卓应用程序</a></p></li>
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/f/nordic-q-a/89631/galaxy-tab-a8-sm-x200-connection-issues-with-gatt-error-133-after-multiple-connecting-failures">多次连接失败后出现133次连接错误</a></p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="instruction">
<h3>用法说明</h3>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
安卓</label><div class="sd-tab-content docutils">
<p>要开始使用，请下载 <a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序 (<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.leaps&amp;hl=en_GB&amp;gl=US">可在Google Play中获得</a>)</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-qr-code.png"><img alt="../../../_images/leaps-manager-qr-code.png" src="/docs-assets/zh-cn/_images/leaps-manager-qr-code.png" style="width: 337.5px; height: 337.5px;"></a>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
iOS</label><div class="sd-tab-content docutils">
<p>要开始使用，请下载 <a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序 (<a class="reference external" href="https://apps.apple.com/vn/app/leaps-manager/id6737454926">可在App Store中获得</a>)</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-ios-qr-code.png"><img alt="../../../_images/leaps-manager-ios-qr-code.png" src="/docs-assets/zh-cn/_images/leaps-manager-ios-qr-code.png" style="width: 344.09999999999997px; height: 344.09999999999997px;"></a>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="getting-started">
<h2>开始</h2>
<p>打开应用程序，然后选择 <span class="red-text">admin</span> （如果没有分配的网络）。如果网络已经存在。导航到 <span class="red-text">admin</span>。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-android-login.jpg"><img alt="../../../_images/leaps-manager-android-login.jpg" src="/docs-assets/zh-cn/_images/leaps-manager-android-login.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div>
<div class="section" id="network-configuration">
<h3>网络配置</h3>
<p>打开应用程序，然后选择 <span class="red-text">开始设备发现</span> （如果没有分配的网络）。如果网络已经存在。导航到 <span class="red-text">现有网络</span>。</p>
<p>在这里，应用程序开始发现和扫描所有可用的网络和设备。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-home.jpg"><img alt="lm1" src="/docs-assets/zh-cn/_images/leaps-manager-android-home.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-tab-create-network.jpg"><img alt="lm2" src="/docs-assets/zh-cn/_images/leaps-manager-android-tab-create-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-create-network.jpg"><img alt="lm3" src="/docs-assets/zh-cn/_images/leaps-manager-android-create-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p>等待发现和扫描过程完成。如果网络可用但未分配，则可以指定网络。您可以选择并创建设备，然后将它们分配到指定的网络。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-assign-devices.jpg"><img alt="lm4" src="/docs-assets/zh-cn/_images/leaps-manager-android-assign-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-assigning-devices.jpg"><img alt="lm5" src="/docs-assets/zh-cn/_images/leaps-manager-android-assigning-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-created-network.jpg"><img alt="lm6" src="/docs-assets/zh-cn/_images/leaps-manager-android-created-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="node-configuration">
<h3>节点配置</h3>
<p>要配置节点，您需要提前将节点分配给特定的网络。选择具有指定节点的网络以查看网络详细信息。</p>
<p>滑动屏幕进行扫描，确保应用程序与设备之间有连接信号。</p>
<p>如果铅笔图标可用，您可以选择它来配置节点。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-leaps-demo-network.jpg"><img alt="lm7" src="/docs-assets/zh-cn/_images/leaps-manager-android-leaps-demo-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-edit-anchor.jpg"><img alt="lm8" src="/docs-assets/zh-cn/_images/leaps-manager-android-edit-anchor.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-edit-tag.jpg"><img alt="lm9" src="/docs-assets/zh-cn/_images/leaps-manager-android-edit-tag.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="demo-selector">
<h3>演示选择器</h3>
<p>导航到演示选择器，然后选择要配置的演示:</p>
<ul class="simple">
<li><p>与 iPhone 的附近交互演示</p></li>
<li><p>使用到达角(AoA)定位设备演示</p></li>
<li><p>无基础设施的邻近性演示</p></li>
<li><p>下行 TDoA RTLS 演示</p></li>
<li><p>高速下行TDoA RTLS演示</p></li>
<li><p>TWR RTLS和数据遥测演示</p></li>
</ul>
<p>示例:TWR RTLS和数据遥测演示</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-demo-selector.jpg"><img alt="lm10" src="/docs-assets/zh-cn/_images/leaps-manager-android-demo-selector.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-twr-rtls.jpg"><img alt="lm11" src="/docs-assets/zh-cn/_images/leaps-manager-android-twr-rtls.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-config-auto.jpg"><img alt="lm12" src="/docs-assets/zh-cn/_images/leaps-manager-android-config-auto.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning.jpg"><img alt="lm13" src="/docs-assets/zh-cn/_images/leaps-manager-android-auto-positioning.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning-measuring.jpg"><img alt="lm14" src="/docs-assets/zh-cn/_images/leaps-manager-android-auto-positioning-measuring.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning-save.jpg"><img alt="lm15" src="/docs-assets/zh-cn/_images/leaps-manager-android-auto-positioning-save.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-leaps-demo-network.jpg"><img alt="lm16" src="/docs-assets/zh-cn/_images/leaps-manager-android-leaps-demo-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-network-on-2D-grid.jpg"><img alt="lm17" src="/docs-assets/zh-cn/_images/leaps-manager-android-network-on-2D-grid.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="configuration-information-for-10db-lna-pa-settings">
<h3>+10dB、LNA/PA设置的配置信息</h3>
<p>在演示中，您将找到有关+10dB低噪声放大器（LNA）/功率放大器（PA）设置的详细信息。此配置旨在为您的特定应用优化信号强度和质量。</p>
<p>配置:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">FCC/ETSI频道5</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">信道5上的ETSI+10</span> <span class="pre">dB</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">FCC/ETSI频道9</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">频道9上的ETSI+10</span> <span class="pre">dB</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">日本ARIB</span> <span class="pre">9频道</span></code></p></li>
</ul>
<p>演示中可用:</p>
<ul class="simple">
<li><p>无基础设施的邻近性演示</p></li>
<li><p>下行 TDoA RTLS 演示</p></li>
<li><p>高速下行TDoA RTLS演示</p></li>
<li><p>TWR RTLS和数据遥测演示</p></li>
</ul>
<p>如何配置:</p>
<ol class="arabic simple">
<li><p>导航到演示屏幕的右上角。</p></li>
<li><p>单击3点图标（菜单图标）。</p></li>
<li><p>选择相应的配置选项以查看或选择设置。</p></li>
</ol>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-fcc-etsi-ch9.jpg"><img alt="lm18" src="/docs-assets/zh-cn/_images/leaps-manager-android-fcc-etsi-ch9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-10dB-lna-pa-settings.jpg"><img alt="lm19" src="/docs-assets/zh-cn/_images/leaps-manager-android-10dB-lna-pa-settings.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="firmware-update-over-ble">
<span id="leaps-manager-fup-over-ble"></span><h3>通过BLE进行固件更新</h3>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-2" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Default Package</label><div class="sd-tab-content docutils">
<p>导航到 <span class="red-text">演示选择器</span>。此外，您可以导航到创建的网络以更新网络中的设备。</p>
<p>访问固件状态。点击应用程序中的 <span class="red-text">选项菜单</span> （<em>表示为三个垂直点</em>）。查找 <span class="red-text">固件状态</span> 选项并选择它。</p>
<p>选择要更新的设备。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-network.jpg"><img alt="lm20" src="/docs-assets/zh-cn/_images/leaps-manager-android-firmware-update-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-demo-selector-firmware-update.jpg"><img alt="lm21" src="/docs-assets/zh-cn/_images/leaps-manager-android-demo-selector-firmware-update.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-status.jpg"><img alt="lm22" src="/docs-assets/zh-cn/_images/leaps-manager-android-firmware-status.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>固件速度超过BLE，约为1.6kBps</p>
</div>
<p>应用程序将提供可视化指标或进度条，显示更新的进行情况. 请耐心等待更新过程。</p>
<p>更新完成后，您将看到 <span class="red-text">状态已完成</span>。此外，设备将发出两声蜂鸣声，表示更新成功。作为该过程的一部分，该板将自动重置。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-eldr.jpg"><img alt="lm23" src="/docs-assets/zh-cn/_images/leaps-manager-android-firmware-update-eldr.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-main.jpg"><img alt="lm24" src="/docs-assets/zh-cn/_images/leaps-manager-android-firmware-update-main.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-completed.jpg"><img alt="lm25" src="/docs-assets/zh-cn/_images/leaps-manager-android-firmware-update-completed.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Selectable Package</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Download the <a class="reference external" href="https://drive.google.com/file/d/12XES6qiCJDZ16JSx841OqcZfqSdy4OIJ/view">LEAPS-UWBS-Firmware-v1.1.0-package.zip</a> file to your PC. Use a program like WinZip or 7-Zip to extract the contents of the downloaded file.</p></li>
<li><p>Open the LM and navigate to the <span class="red-text">Demo Selector</span>. Additionally, you can navigate to the created network to update the devices in the network. Access firmware status. Tap the <span class="red-text">options menu</span> (<em>represented as three vertical dots</em>) within the application. Look for the <span class="red-text">Firmware status</span> option and select it.</p></li>
<li><p>In the top-right corner, click button to select the firmware Package.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-home-page.jpg"><img alt="lm37" src="/docs-assets/zh-cn/_images/leaps-manager-home-page.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-package.jpg"><img alt="lm38" src="/docs-assets/zh-cn/_images/leaps-manager-selecting-package.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-package_001.jpg"><img alt="lm39" src="/docs-assets/zh-cn/_images/leaps-manager-selecting-package_001.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</li>
<li><p>After successfully selecting the package, choose the devices to update.</p>
<blockquote>
<div><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-devices.jpg"><img alt="lm40" src="/docs-assets/zh-cn/_images/leaps-manager-selecting-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p>
</div></blockquote>
</li>
</ol>
<p>应用程序将提供可视化指标或进度条，显示更新的进行情况. 请耐心等待更新过程。</p>
<p>更新完成后，您将看到 <span class="red-text">状态已完成</span>。此外，设备将发出两声蜂鸣声，表示更新成功。作为该过程的一部分，该板将自动重置。</p>
</div>
</div>
</div></blockquote>
</div>
<div class="section" id="auto-positioning">
<h3>自动定位</h3>
<p><strong>1。 导言</strong></p>
<p>本指南将帮助您了解如何在应用程序上有效地使用此工具。</p>
<p>自动定位功能允许您根据所选锚点准确定位节点。正确的设置对于最佳性能至关重要。</p>
<ul class="simple">
<li><p>简介</p></li>
<li><p>访问自动定位</p></li>
<li><p>选择锚点</p></li>
<li><p>配置计算模式</p></li>
<li><p>Starting measurements</p></li>
<li><p>重新计算职位</p></li>
<li><p>查看和调整地图上的节点位置</p></li>
<li><p>保存配置</p></li>
<li><p>常见问题解答</p></li>
</ul>
<p><strong>2.访问自动定位</strong></p>
<p>要访问自动定位功能，请根据您的网络状态执行以下方法之一:</p>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>菜单访问</p></li>
</ol>
<ul class="simple">
<li><p>点击菜单图标:找到并点击屏幕 <code class="docutils literal notranslate"><span class="pre">右下角</span></code> 的菜单图标。</p></li>
<li><p>从菜单中选择 <code class="docutils literal notranslate"><span class="pre">自动定位</span></code> 功能。</p></li>
</ul>
<ol class="upperalpha simple" start="2">
<li><p>选择自动定位</p></li>
</ol>
<ul class="simple">
<li><p>访问 <code class="docutils literal notranslate"><span class="pre">演示选择器</span></code>。</p></li>
<li><p>从那里选择 <code class="docutils literal notranslate"><span class="pre">自动定位</span></code> 选项。</p></li>
</ul>
</div></blockquote>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-0.jpg"><img alt="lm26" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-0.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-1.jpg"><img alt="lm27" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>3。选择锚点</strong></p>
<a class="reference internal image-reference" href="../../../_images/leaps-manager-auto-positioning-2.jpg"><img alt="../../../_images/leaps-manager-auto-positioning-2.jpg" class="align-right" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-2.jpg" style="width: 237.60000000000002px; height: 528.0px;"></a>
<p>应用程序将显示锚点列表。</p>
<p>选择锚点:</p>
<blockquote>
<div><ul class="simple">
<li><p>勾选至少“2个锚点”旁边的复选框。</p></li>
<li><p>确保 <code class="docutils literal notranslate"><span class="pre">一个锚点</span></code> 被指定为 <code class="docutils literal notranslate"><span class="pre">发起者</span></code>。</p></li>
<li><p>锚必须 <code class="docutils literal notranslate"><span class="pre">站立</span></code> 并相互面对，以便准确定位。</p></li>
</ul>
</div></blockquote>
<p><strong>4。配置计算模式**（**可选</strong>）</p>
<ul class="simple">
<li><p>计算模式:如果所有配置都设置为 <code class="docutils literal notranslate"><span class="pre">计算</span></code>，应用程序将自动计算节点位置。</p></li>
<li><p>手动模式:如果设置为 <code class="docutils literal notranslate"><span class="pre">手动</span></code>，则位置将保持基本固定，直到您手动调整或重新计算为止。</p></li>
</ul>
<p><strong>5。开始测量</strong></p>
<p>选择锚点后，单击 <code class="docutils literal notranslate"><span class="pre">测量</span></code> 按钮开始定位过程。</p>
<ul class="simple">
<li><p>等待完成:让流程完成；您将收到所选节点的位置信息。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-4.jpg"><img alt="lm28" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-4.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-5.jpg"><img alt="lm29" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-6.jpg"><img alt="lm30" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-6.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>6。重新计算职位**（**可选</strong>）</p>
<ul class="simple">
<li><p>如果需要进行调整，只需按 <code class="docutils literal notranslate"><span class="pre">重新计算</span></code> 按钮即可重新计算。</p></li>
</ul>
<p><strong>7。查看和调整二维网格上的节点位置**（**可选</strong>）</p>
<ol class="arabic simple">
<li><p>访问地图:</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>点击 <code class="docutils literal notranslate"><span class="pre">右上角</span></code> 的地图图标，查看节点的实时位置。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>调整节点位置:</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">使用旋转功能旋转</span></code> 节点。</p></li>
<li><p>根据需要为每个节点设置一个 <code class="docutils literal notranslate"><span class="pre">特定位置</span></code>。</p></li>
<li><p>按下 <code class="docutils literal notranslate"><span class="pre">按住</span></code> 节点可将节点自由移动到任何所需的位置。</p></li>
<li><p>您还可以从该界面执行自动定位或重新计算。</p></li>
</ul>
</div></blockquote>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-8.jpg"><img alt="lm31" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-8.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-7.jpg"><img alt="lm32" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-7.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-9.jpg"><img alt="lm33" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>8.保存配置</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>一旦您对调整感到满意，请按2D网格 <code class="docutils literal notranslate"><span class="pre">顶部工具栏</span></code> 中的 <code class="docutils literal notranslate"><span class="pre">保存</span></code> 按钮或保存图标。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-10.jpg"><img alt="lm34" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-10.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-11.jpg"><img alt="lm35" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-11.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-12.jpg"><img alt="lm36" src="/docs-assets/zh-cn/_images/leaps-manager-auto-positioning-12.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div></blockquote>
<p>回到二维网格继续进行网络设置。</p>
<p><strong>常见问题解答</strong></p>
<ol class="arabic">
<li><div class="line-block">
<div class="line"><strong>Q:</strong> 如果列表中没有出现锚点怎么办？</div>
<div class="line"><strong>A:</strong> 确保您的网络处于活动状态，并且锚点在环境中配置正确。</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><strong>Q:</strong> 我可以使用单个锚点进行定位吗？</div>
<div class="line"><strong>A:</strong> 否，您必须至少选择两个锚点才能获得准确的结果。</div>
</div>
</li>
</ol>
</div>
</div>
<hr class="docutils">
<div class="section" id="troubleshooting">
<h2>故障排除</h2>
<ul class="simple">
<li><p>始终确保BLE连接稳定，设备在覆盖范围内。</p></li>
</ul>
</div>
</div>


           </div>
