---
title: "PANS PRO Manager"
lang: zh
slug: "pans-pro-rtls/infrastructure/pans-pro-manager"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/infrastructure/pans-pro-manager/"
order: 99
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-manager">
<span id="id1"></span><h1>PANS PRO Manager</h1>
<p>本页概述了使用专为Android设备设计的PANS PRO Manager工具的基本步骤。它指导用户完成超宽带设备的配置、设置和管理，确保PANS PRO RTLS系统内的无缝集成和操作。</p>
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>允许对整个网络的设备进行管理和可视化。Allowing management and visualization of the devices for the whole network。</p></li>
<li><p>与设备的通信是通过BLE完成的，支持多达6个并发连接，以保持连接可靠性。</p></li>
<li><p>2D和3D网格提供网络中设备的实时位置更新和可视化。</p></li>
<li><p>其他有用的功能包括锚点自动定位、BLE固件更新、用户管理和位置记录。</p></li>
</ul>
<hr class="docutils">
<div class="section" id="system-environment">
<h3>系统环境</h3>
<p><a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 是基于Android API <strong>24级</strong> 及后续版本开发的。参见 <a class="reference external" href="https://apilevels.com">apilevels</a></p>
<ul class="simple">
<li><p>安卓最低版本:安卓7（API 24）</p></li>
<li><p>最小内存:100 MB（可用磁盘空间）</p></li>
<li><p>最低Bluetooth版本:4.2（建议5.0或更高版本）</p></li>
<li><p>建议使用android设备:谷歌Pixel 7（同等设备）</p></li>
</ul>
</div>
<div class="section" id="instruction">
<h3>用法说明</h3>
<p>要开始使用，请下载 <a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 应用程序(<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.panspro&amp;hl=en">可在Google Play中获得</a>)</p>
<blockquote>
<div><div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/panspro-manager-qr-code.png"><img alt="../../../_images/panspro-manager-qr-code.png" src="/docs-assets/zh-cn/_images/panspro-manager-qr-code.png" style="width: 344.4px; height: 344.4px;"></a>
</div>
</div></blockquote>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>开始</h2>
<p>要开始使用 <a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a>，需要登录。默认情况下，用户名为 <span class="red-text">admin</span>，密码为 <span class="red-text">admin</span>，前提是启用了用户管理设置。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-login.jpg"><img alt="login1" src="/docs-assets/zh-cn/_images/ppm-login.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-login-admin.jpg"><img alt="login2" src="/docs-assets/zh-cn/_images/ppm-login-admin.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<div class="section" id="menu">
<h3>菜单</h3>
<p>有关更多用户自定义选项和访问主要功能，请导航到菜单。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-menu.jpg"><img alt="../../../_images/ppm-menu.jpg" class="align-center" src="/docs-assets/zh-cn/_images/ppm-menu.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="devices-discovery">
<span id="id2"></span><h3>设备发现</h3>
<p>成功登录后，主页将如 <span class="red-text">左侧</span> 图片所示显示。为了快速检测区域内可用的网络和设备，请从主页点击 <span class="red-text">开始设备发现</span> 功能。请耐心等待设备发现与扫描过程完成，发现的网络和设备将如 <span class="red-text">右侧</span> 图片所示列出。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-home-page.jpg"><img alt="discovery1" src="/docs-assets/zh-cn/_images/ppm-home-page.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network1.jpg"><img alt="discovery2" src="/docs-assets/zh-cn/_images/ppm-assign-network1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="network-configuration">
<h3>网络配置</h3>
<ul>
<li><p>创建网络</p>
<blockquote>
<div><ul class="simple">
<li><p>选择要设置网络的设备。</p></li>
<li><p>将弹出一个对话框，提示您输入网络名称。</p></li>
<li><p>键入所需的网络名称。</p></li>
<li><p>然后，应用程序将创建网络。</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-assign-network5.jpg"><img alt="nt1" src="/docs-assets/zh-cn/_images/ppm-assign-network5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network6.jpg"><img alt="nt2" src="/docs-assets/zh-cn/_images/ppm-assign-network6.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network7.jpg"><img alt="nt3" src="/docs-assets/zh-cn/_images/ppm-assign-network7.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>分配多个设备</p>
<blockquote>
<div><ul class="simple">
<li><p>要将多个设备添加到网络中，请按住列表中的设备。</p></li>
<li><p>然后，应用程序将分配多个设备。</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-assign-network8.jpg"><img alt="as1" src="/docs-assets/zh-cn/_images/ppm-assign-network8.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network9.jpg"><img alt="as2" src="/docs-assets/zh-cn/_images/ppm-assign-network9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network11.jpg"><img alt="as3" src="/docs-assets/zh-cn/_images/ppm-assign-network11.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul class="simple">
<li><p>如果网络已经可用，请选择它。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-2.jpg"><img alt="nw1" src="/docs-assets/zh-cn/_images/ppm-network-2.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-network-1.jpg"><img alt="nw2" src="/docs-assets/zh-cn/_images/ppm-network-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>要查看所选设备的详细信息，请单击该设备。详细信息将显示在下面。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-network-3.jpg"><img alt="../../../_images/ppm-network-3.jpg" class="align-center" src="/docs-assets/zh-cn/_images/ppm-network-3.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
</li>
<li><p>要从网络中删除设备，请向右滑动设备。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-assign-network13.jpg"><img alt="../../../_images/ppm-assign-network13.jpg" class="align-center" src="/docs-assets/zh-cn/_images/ppm-assign-network13.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="device-configuration">
<h3>设备配置</h3>
<p>要配置节点，需要事先将节点分配到特定网络。</p>
<ul class="simple">
<li><p>选择具有指定节点的网络以查看网络详细信息。</p></li>
<li><p>滑动屏幕进行扫描，确保应用程序与设备之间有连接信号。</p></li>
<li><p>如果铅笔图标可用，您可以选择它来配置节点。If the pencil icon is available, you can select it to configure the node。</p></li>
</ul>
<p>以下两个示例说明了配置:</p>
<ul class="simple">
<li><p>左侧设备代表一个 <span class="red-text">标签节点</span>，其中 <span class="red-text">正常更新率</span> 和 <span class="red-text">静态更新率</span> 参数是可配置的。</p></li>
<li><p>右侧设备代表一个 <span class="red-text">锚节点</span>，其中 <span class="red-text">POSITION（M</span> 参数是可配置的。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-device-configure-a.jpg"><img alt="device1" src="/docs-assets/zh-cn/_images/ppm-device-configure-a.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-device-configure-b.jpg"><img alt="device2" src="/docs-assets/zh-cn/_images/ppm-device-configure-b.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="network-visualization">
<h3>网络可视化</h3>
<p><a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 工具的主要特征是它能够可视化网络的准确位置。以下示例说明了二维模式下的网络表示。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-grib-2d-1.jpg"><img alt="2d1" src="/docs-assets/zh-cn/_images/ppm-grib-2d-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-grib-2d-3.jpg"><img alt="2d2" src="/docs-assets/zh-cn/_images/ppm-grib-2d-3.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p>为了以3D显示网络，以下示例说明了3D模式下的网络表示。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-grib-3d-0.jpg"><img alt="3d1" src="/docs-assets/zh-cn/_images/ppm-grib-3d-0.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-grib-3d-1.jpg"><img alt="3d2" src="/docs-assets/zh-cn/_images/ppm-grib-3d-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="position-logs">
<h3>职位日志</h3>
<p>为了显示网络中每个设备的详细信息及其静态数据，以下示例说明了设备及其相应的位置。</p>
<a class="reference internal image-reference" href="../../../_images/ppm-positiong-logs.jpg"><img alt="../../../_images/ppm-positiong-logs.jpg" class="align-center" src="/docs-assets/zh-cn/_images/ppm-positiong-logs.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="auto-positioning">
<h3>自动定位</h3>
<p>另一个关键功能是自动定位，可帮助用户快速自动初始化网络。</p>
<p>访问 <span class="red-text">自动定位</span>。点击应用程序中的 <span class="red-text">选项菜单</span> （<em>表示为三个垂直点</em>）。</p>
<ul class="simple">
<li><p>以下示例说明了完成自动定位过程后的结果。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-menu.jpg"><img alt="am1" src="/docs-assets/zh-cn/_images/ppm-network-menu.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-1.jpg"><img alt="am2" src="/docs-assets/zh-cn/_images/ppm-auto-positioning-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-2.jpg"><img alt="am3" src="/docs-assets/zh-cn/_images/ppm-auto-positioning-2.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul class="simple">
<li><p>等待完成；您将收到节点的位置信息。然后按 <span class="red-text">保存</span> 保存结果。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-3.jpg"><img alt="au1" src="/docs-assets/zh-cn/_images/ppm-auto-positioning-3.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-4.jpg"><img alt="au2" src="/docs-assets/zh-cn/_images/ppm-auto-positioning-4.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-5.jpg"><img alt="au3" src="/docs-assets/zh-cn/_images/ppm-auto-positioning-5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="firmware-update-over-ble">
<span id="id3"></span><h3>通过BLE进行固件更新</h3>
<p>访问固件状态。点击应用程序中的 <span class="red-text">选项菜单</span> （<em>表示为三个垂直点</em>）。查找 <span class="red-text">固件状态</span> 选项并选择它。</p>
<p>选择要更新的设备。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-menu.jpg"><img alt="fw1" src="/docs-assets/zh-cn/_images/ppm-network-menu.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-firmware-update.jpg"><img alt="fw2" src="/docs-assets/zh-cn/_images/ppm-firmware-update.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
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
