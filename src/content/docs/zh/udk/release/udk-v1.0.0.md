---
title: "版本 v1.0.0"
lang: zh
slug: "udk/release/udk-v1.0.0"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/release/udk-v1.0.0/"
order: 59
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v1-0-0">
<h1>版本 v1.0.0</h1>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p><strong>版本</strong>:  UDK v1.0.0</p></li>
<li><p><strong>发布日期</strong>: 2025年1月8日</p></li>
</ul>
</div>
<ul class="simple">
<li><p>LEAPS UWB 子系统</p>
<ul>
<li><p>基于客户和团队反馈的错误修正 + 改进</p></li>
<li><p>改进UL TDoA时间同步和多重迭代算法。</p></li>
<li><p>添加新的三边测量算法</p></li>
<li><p>功耗验证和优化</p></li>
<li><p>使用室外测试设置进行自动测试（系统测试, API测试, 不同模式和系统配置的测试）</p></li>
<li><p>作为网关功能的一部分，改进回程数据</p></li>
<li><p>将DW3000驱动程序更新到最新版本</p></li>
<li><p>确保使用任意数量的锚点进行自动定位测量</p></li>
<li><p>改进位置引擎过滤</p></li>
<li><p>添加与FiRa兼容的新射频配置文件</p></li>
<li><p>更改 CH9 的默认前导码</p></li>
<li><p>为shell API添加自动退出功能，以优化功耗</p></li>
<li><p>增加测量和位置指标</p></li>
<li><p>在 DWM3001, DWM1001, 村田 2AB 上验证</p></li>
<li><p>生产版本验证</p></li>
</ul>
</li>
<li><p>LEAPS Server</p>
<ul>
<li><p>根据客户和团队的反馈意见进行的 Bug 修正 + 改进</p></li>
<li><p>生产版本验证</p></li>
</ul>
</li>
<li><p>LEAPS Gateway</p>
<ul>
<li><p>错误修正</p></li>
<li><p>改进USB接口的处理</p></li>
<li><p>生产版本验证</p></li>
</ul>
</li>
<li><p>LEAPS Manager Android</p>
<ul>
<li><p>调试并修正部分 Android 设备的问题，提高Bluetooth稳定性</p></li>
<li><p>允许更改MQTT网络ID</p></li>
<li><p>改进用户管理和权限</p></li>
<li><p>改进节点列表和网格中的实时更新</p></li>
<li><p>代码重构和清理</p></li>
<li><p>生产版本验证</p></li>
</ul>
</li>
<li><p>LEAPS Manager iOS</p>
<ul>
<li><p>在App Store上发布</p></li>
<li><p>错误修正</p></li>
<li><p>向节点添加有用的属性</p></li>
<li><p>改进节点列表和网格中的实时更新</p></li>
<li><p>提高 FW 更新速度</p></li>
</ul>
</li>
<li><p>LEAPS Center</p>
<ul>
<li><p>错误修正</p></li>
<li><p>更新 Docker 支持</p></li>
<li><p>更新 VMWare 支持</p></li>
<li><p>生产版本验证</p></li>
</ul>
</li>
<li><p>UDK SDK</p>
<ul>
<li><p>错误修正</p></li>
<li><p>根据客户反馈改进文档</p></li>
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
