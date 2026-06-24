---
title: "API 通用数据类型"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/api-generic-data-types"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/api-generic-data-types/"
order: 144
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <section id="api-generic-data-types">
<h1>API 通用数据类型</h1>
<section id="id">
<h2>ID</h2>
<p>节点标识符。 这是一个唯一的 64 位数字。 它由固定前缀 0xDECA, MCU 唯一芯片 ID 和 DW1000/DW3000 唯一部件 ID 按以下格式导出： 0xDECA + 28 位 MCU 唯一芯片 ID + 20 位 DW1000 唯一部件 ID。</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text"><strong>id</strong> = 64 位整数</p>
</div>
</div>
<hr class="docutils">
</section>
<section id="status-code">
<span id="statuscode"></span><h2>状态码</h2>
<p>每条命令返回的状态码。</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text">‘0’ (<em>ok</em>)</p></li>
<li><p class="sd-card-text">‘1’ (<em>未知命令或 tlv 框架损坏</em>)</p></li>
<li><p class="sd-card-text">‘2’ (<em>内部错误</em>)</p></li>
<li><p class="sd-card-text">‘3’ (<em>无效参数</em>)</p></li>
<li><p class="sd-card-text">‘4’ (<em>忙</em>)</p></li>
<li><p class="sd-card-text">‘5’ (<em>不允许操作</em>)</p></li>
<li><p class="sd-card-text">‘6’ (<em>校验和值错误</em>)</p></li>
<li><p class="sd-card-text">‘7’ (<em>输入错误</em>)</p></li>
<li><p class="sd-card-text">‘8’ (<em>不支持</em>)</p></li>
<li><p class="sd-card-text">‘9’ (<em>需要重置并需要再次发送命令</em>)</p></li>
</ul>
</div>
</div>
<hr class="docutils">
</section>
<section id="position">
<span id="id1"></span><h2>位置</h2>
<p>节点（锚点或标签）的位置。</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>In CARTESIAN coordinate, position = x, y, z, pqf</strong> (<em>position coordinates</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>x</strong> = 32 位整数 (<em>单位：毫米</em>)</p></li>
<li><p class="sd-card-text"><strong>y</strong> = 32 位整数(<em>单位：毫米</em>)</p></li>
<li><p class="sd-card-text"><strong>z</strong> = 32 位整数(<em>单位：毫米</em>)</p></li>
<li><p class="sd-card-text"><strong>pqf</strong> = 8位整数(<em>位置质量因子，以百分比表示</em>)</p></li>
</ul>
</li>
<li><p class="sd-card-text"><strong>In WGS84 coordinate, position = lat, lon, 0, pqf</strong> (<em>position coordinates</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>lat</strong> = 32-bit integer (WGS84 latitude x10^7)</p></li>
<li><p class="sd-card-text"><strong>lon</strong> = 32-bit integer (WGS84 latitude x10^7)</p></li>
<li><p class="sd-card-text"><strong>0</strong></p></li>
<li><p class="sd-card-text"><strong>pqf</strong> = 8位整数(<em>位置质量因子，以百分比表示</em>)</p></li>
</ul>
</li>
</ul>
</div>
</div>
<hr class="docutils">
</section>
<section id="gpio-idx">
<span id="gpioidx"></span><h2>gpio_idx</h2>
<p>通过输入 PX。Y 向用户提供的 GPIO 引脚的索引，其中：</p>
<ul class="simple">
<li><p>X: 端口编号</p></li>
<li><p>Y: 引脚索引</p></li>
</ul>
<p>请参考下面列表中特定设备的编号/索引。</p>
<ul class="simple">
<li><p>DWM1001: P0.08, P0.12, P0.13, P0.15, P0.23, P0.27</p></li>
<li><p>DWM3001: P0.06, P0.12, P0.13, P0.17, P0.20, P0.21, P1.00, P1.01, P1.05, P1.09</p></li>
<li><p>LC13/LC14 (2AB): P0.11, P0.12, P0.13, P0.14, P1.7, P1.14</p></li>
</ul>
</section>
<hr class="docutils">
<section id="fw-version">
<h2>fw_version</h2>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>fw_version</strong> = <strong>maj</strong>, <strong>min, patch, ver</strong> (<em>固件版本</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>maj</strong> = 8位数(<em>MAJOR</em>)</p></li>
<li><p class="sd-card-text"><strong>min</strong> = 8位数(<em>MINOR</em>)</p></li>
<li><p class="sd-card-text"><strong>patch</strong> = 8位数(<em>PATCH</em>)</p></li>
<li><p class="sd-card-text"><strong>ver</strong> = res, var</p></li>
<li><p class="sd-card-text">: <strong>res</strong> = 4位数字(<em>RESERVED</em>)</p></li>
<li><p class="sd-card-text"><strong>var</strong> = 4位数字(<em>VARIANT</em>)</p></li>
</ul>
</li>
</ul>
</div>
</div>
</section>
</section>


           </div>
