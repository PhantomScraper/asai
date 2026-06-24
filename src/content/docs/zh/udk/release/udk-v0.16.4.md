---
title: "版本 v0.16.4"
lang: zh
slug: "udk/release/udk-v0.16.4"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/release/udk-v0.16.4/"
order: 58
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v0-16-4">
<h1>版本 v0.16.4</h1>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p><strong>版本</strong>： UDK v0.16.4</p></li>
<li><p><strong>发布日期</strong>： 2024 年 11 月 21 日</p></li>
</ul>
</div>
<ul class="simple">
<li><p>LEAPS UWB 子系统</p>
<ul>
<li><p>错误修正</p></li>
<li><p>增加 UL-TDoA 支持</p></li>
<li><p>修复 USB 和 SPI 接口的回程问题</p></li>
<li><p>改善功耗</p></li>
<li><p>安装室外测试设置</p></li>
<li><p>设置自动构建系统，创建相关工具以执行测试</p></li>
<li><p>向客户提供 UWB 认证和测试程序</p></li>
</ul>
</li>
<li><p>LEAPS Server</p>
<ul>
<li><p>错误修正</p></li>
<li><p>增加 UL-TDoA 支持</p></li>
<li><p>添加多方位定位算法和定位引擎相关组件</p></li>
<li><p>添加测量和定位指标</p></li>
</ul>
</li>
<li><p>LEAPS Gateway</p>
<ul>
<li><p>增加 UL-TDoA 支持</p></li>
<li><p>优化回程数据</p></li>
</ul>
</li>
<li><p>LEAPS Manager Android</p>
<ul>
<li><p>错误修正</p></li>
<li><p>增加UL-TDOA支持</p></li>
<li><p>添加测量和定位指标</p></li>
<li><p>增加节点列表和网格的实时更新</p></li>
<li><p>添加电池电量显示</p></li>
<li><p>优化平面布局配置流程</p></li>
<li><p>在固件更新窗口中添加支持的硬件列表</p></li>
<li><p>添加日志记录</p></li>
<li><p>添加 MQTT 接口</p></li>
<li><p>添加多节点选择和配置</p></li>
<li><p>改进UI/UX</p></li>
</ul>
</li>
<li><p>LEAPS Manager iOS</p>
<ul>
<li><p>通过试飞发布</p></li>
<li><p>错误修正</p></li>
<li><p>所有的演示都可以使用演示选择器进行配置，以及其他各种相关的改进。</p></li>
<li><p>增加UL-TDOA支持</p></li>
<li><p>添加测量和定位指标</p></li>
<li><p>增加节点列表和网格的实时更新</p></li>
<li><p>增加发现时间配置</p></li>
<li><p>改进自动定位（允许处理 BLE 范围之外的节点）</p></li>
<li><p>增加公制/英制单位配置</p></li>
<li><p>根据新设计更新静态/标称更新率配置</p></li>
<li><p>改进平面图</p></li>
<li><p>为发现添加倒计时计数器</p></li>
<li><p>改进二维网格</p></li>
<li><p>显示 UWBS 模式</p></li>
</ul>
</li>
<li><p>LEAPS Center</p>
<ul>
<li><p>新的UI/UX，有很多改进</p></li>
<li><p>添加360平面旋转，添加平面比例重置</p></li>
<li><p>添加支持页面</p></li>
<li><p>为区域添加可见功能，改进区域配置</p></li>
<li><p>添加测量和位置度量。</p></li>
<li><p>改进节点配置</p></li>
<li><p>更新spring框架</p></li>
<li><p>Docker支持</p></li>
</ul>
</li>
<li><p>UDK SDK</p>
<ul>
<li><p>DW3000 驱动程序已更新至最新版本</p></li>
<li><p>所有范例均已验证</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<div class="section" id="known-limitations">
<h2>已知限制</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 53%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>没有。</p></th>
<th class="head"><p>摘要</p></th>
<th class="head"><p>受影响</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>1</p></td>
<td><p><a class="reference internal" href="/docs/zh/udk/known-limitation/limit-001#limitation-1"><span class="std std-ref">不支持 UWB 校准设备.</span></a>。</p></td>
<td><p><a class="reference internal" href="/docs/zh/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">使用到达角(AoA)定位设备演示</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p><a class="reference internal" href="/docs/zh/udk/known-limitation/limit-002#limitation-2"><span class="std std-ref">不支持某些设备参数的配置.</span></a>。</p></td>
<td><p><a class="reference internal" href="/docs/zh/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">使用到达角(AoA)定位设备演示</span></a></p></td>
</tr>
</tbody>
</table>
<div class="toctree-wrapper compound">
</div>
</div>
<hr class="docutils">
<div class="section" id="known-issues">
<h2>已知问题</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 53%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>没有。</p></th>
<th class="head"><p>摘要</p></th>
<th class="head"><p>受影响</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>1</p></td>
<td><p><a class="reference internal" href="/docs/zh/udk/known-issue/issue-004#issue-1"><span class="std std-ref">某些 FiRa 参数的配置工作不稳定.</span></a></p></td>
<td><p><a class="reference internal" href="/docs/zh/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">使用到达角(AoA)定位设备演示</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p><a class="reference internal" href="/docs/zh/udk/known-issue/issue-005#issue-2"><span class="std std-ref">设备有时会在启动或停止测距时意外重置.</span></a></p></td>
<td><p><a class="reference internal" href="/docs/zh/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">使用到达角(AoA)定位设备演示</span></a></p></td>
</tr>
</tbody>
</table>
<div class="toctree-wrapper compound">
</div>
<hr class="docutils">
</div>
</div>


           </div>
