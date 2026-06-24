---
title: "TLV API"
lang: zh
slug: "pans-pro-rtls/integration-guide/tlv-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/tlv-api/"
order: 121
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="tlv-api">
<h1>TLV API</h1>
<p>DWM 模块 API 中使用 TLV（类型-长度-值）格式。 TLV 格式的数据总是以类型字节开始，长度字节紧随其后，然后是由长度字节指定的可变数量的值字节（从 0 到 253 不等）。 表 1 显示了 TLV 格式数据的一个示例，其中类型字节为 0x28，长度字节为 0x02，根据长度字节的声明，值字段由两个字节组成：0x0D 和 0x01。</p>
<p>在 DWM1001 固件中，SPI 和 UART API 都使用 TLV 格式来传输数据。 用户应参考 TLV 类型列表，了解类型字节的含义。 对于每个特定命令或响应，值字段都有不同的长度，以提供相应的信息。</p>
<p><strong>TLV 格式数据示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 63%">
<col style="width: 11%">
<col style="width: 13%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="2"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>引脚索引</p></td>
<td><p><strong>引脚值</strong></p></td>
</tr>
<tr class="row-even"><td><p>0x28</p></td>
<td><p>0x02</p></td>
<td><p>0x0D</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>有关每个 API 的详细信息，请阅读以下页面：</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information">通用 API 信息</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-command-list">API 命令列表</a></li>
</ul>
</div>
</div>


           </div>
