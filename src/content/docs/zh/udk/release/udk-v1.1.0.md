---
title: "版本 v1.1.0"
lang: zh
slug: "udk/release/udk-v1.1.0"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/release/udk-v1.1.0/"
order: 20
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v1-1-0">
<h1>版本 v1.1.0</h1>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p><strong>版本</strong>:  UDK v1.1.0</p></li>
<li><p><strong>发布日期</strong>: 2025年6月16日</p></li>
</ul>
</div>
<ul>
<li><p>LEAPS UWB 子系统</p>
<blockquote>
<div><ul class="simple">
<li><p>错误修正</p></li>
<li><p>使用BLE激活进行电源优化</p></li>
<li><p>进一步优化UWB容量</p></li>
<li><p>提高不同网络之间的TWR标签漫游能力</p></li>
<li><p>添加嗅探器功能</p></li>
<li><p>为用户提供DL TDoA的测量数据</p></li>
<li><p>添加API，以便在使用TWR时能够验证上行链路和下行链路用户数据的全部容量</p></li>
<li><p>深度重新验证范围</p></li>
<li><p>添加安全启动选项</p></li>
<li><p>UWB例程的进一步运行时优化</p></li>
<li><p>内存优化审查</p></li>
<li><p>进一步审查和优化功耗</p></li>
<li><p>Validate on DWM3001, DWM1001, Murata 2AB</p></li>
<li><p>使用室外测试设置进行自动化测试（系统测试、API测试、不同模式和系统配置的测试）</p></li>
<li><p>确保使用任意数量的锚进行自动定位测量</p></li>
<li><p>添加新的三边测量算法，增加计算时间</p></li>
<li><p>添加共存网络</p></li>
<li><p>添加区域ID以提高位置估计精度</p></li>
<li><p>添加网络掩码，以便标签可以在适合掩码的网络之间漫游</p></li>
<li><p>添加对InsightSIP ISP3080的支持，功耗优化</p></li>
<li><p>添加对ISP3080使用的新加速计的支持</p></li>
<li><p>在位置引擎禁用时添加距离发送</p></li>
<li><p>修复了错误/改进了UL-TDOA时隙定时、容量和配置</p></li>
<li><p>为电源和重置周期添加了非易失性计数器</p></li>
<li><p>添加板电压特定配置、电压测量和电池状态指示，改善电池保护</p></li>
<li><p>增加温度测量和数据收集</p></li>
<li><p>重新验证天线延迟，并对每个射频设置进行校正</p></li>
<li><p>添加自动Rx接收速率计算</p></li>
<li><p>通过SWD添加shell调试支持，以调试没有UART的平台（例如InsightSIP ISP3080）</p></li>
<li><p>改善数据回程</p></li>
<li><p>改进TWR RTLS的锚点选择策略</p></li>
<li><p>API的各种改进</p></li>
<li><p>添加对SPI闪存的支持</p></li>
<li><p>实施措施，为新的RED/CRA指令做好准备</p></li>
<li><p>QPG6200支持的初步准备</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS服务器</p>
<blockquote>
<div><ul class="simple">
<li><p>改进UL-TDoA的时间同步</p></li>
<li><p>改进UL-TDoA和DL-TDoA的多点定位算法</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Gateway</p>
<blockquote>
<div><ul class="simple">
<li><p>错误修正</p></li>
<li><p>优化性能以处理更高的容量</p></li>
<li><p>允许配置UWB RF参数、Tx功率设置</p></li>
<li><p>增加了对覆盖配置文件的支持</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Manager Android</p>
<blockquote>
<div><ul class="simple">
<li><p>错误修正</p></li>
<li><p>添加暗模式</p></li>
<li><p>允许使用6个以上锚点进行自动定位，但并非所有锚点都在Bluetooth范围内</p></li>
<li><p>演示配置行为改进</p></li>
<li><p>允许配置UWB属性</p></li>
<li><p>添加设备筛选器功能</p></li>
<li><p>添加导出设备功能</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Manager iOS</p>
<blockquote>
<div><ul class="simple">
<li><p>错误修正</p></li>
<li><p>添加电池电量显示</p></li>
<li><p>添加工具提示</p></li>
<li><p>网络改进</p></li>
<li><p>热图改进</p></li>
<li><p>演示配置行为改进</p></li>
<li><p>Bluetooth发现和通信的改进</p></li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Center</p>
<blockquote>
<div><ul class="simple">
<li><p>基于客户和团队反馈的Bug修复+改进</p></li>
<li><p>优化热图</p></li>
<li><p>为平面图添加翻转功能</p></li>
<li><p>添加网格配置</p></li>
<li><p>添加周围锚信号图</p></li>
<li><p>添加区域报警功能</p></li>
<li><p>添加不同形状的地理围栏</p></li>
<li><p>添加日志记录功能</p></li>
<li><p>添加工具，用于在使用TWR时验证上行链路/下行链路用户数据的满容量</p></li>
<li><p>调查三维对象是否可以导入到地图中</p></li>
<li><p>添加工具提示</p></li>
<li><p>在2D/3D中添加放大/缩小按钮</p></li>
</ul>
</div></blockquote>
</li>
<li><p>UDK SDK</p>
<blockquote>
<div><ul class="simple">
<li><p>错误修正</p></li>
<li><p>根据客户反馈改进文档</p></li>
<li><p>在Github上发布</p></li>
</ul>
</div></blockquote>
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
