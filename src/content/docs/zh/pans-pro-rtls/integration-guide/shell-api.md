---
title: "壳牌API"
lang: zh
slug: "pans-pro-rtls/integration-guide/shell-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/shell-api/"
order: 122
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="shell-api">
<h1>壳牌API</h1>
<p>Shell 使用 UART 接口，也可以二进制模式工作. 二进制模式用于读取 TLV 格式的 API 命令. 复位后，DWM 默认以二进制模式启动. 在 1 秒钟内按两次 ENTER 键即可切换到 shell 模式. 在 shell 模式下执行 “quit”（退出）命令可切换到二进制模式. shell 模式和二进制模式可以来回切换. 在 shell 模式下按 Enter 键可重复上一条命令. 下文将概述 shell 命令。</p>
<hr class="docutils">
<p>下表概述了以太网网关和边缘节点上可用的 shell 命令。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 46%">
<col style="width: 13%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>命令</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
<th class="head"><p><strong>DWM1001</strong></p></th>
<th class="head"><p><strong>网关</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/base#pp-helpm"><span class="std std-ref">?</span></a></p></td>
<td><p>此帮助</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/base#pp-help"><span class="std std-ref">帮助</span></a></p></td>
<td><p>此帮助</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/base#pp-quit"><span class="std std-ref">退出</span></a></p></td>
<td><p>退出</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gc"><span class="std std-ref">gc</span></a></p></td>
<td><p>GPIO 清除</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gg"><span class="std std-ref">gg</span></a></p></td>
<td><p>GPIO 获取</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gs"><span class="std std-ref">gs</span></a></p></td>
<td><p>GPIO 设置</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gt"><span class="std std-ref">gt</span></a></p></td>
<td><p>GPIO toggle</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sys#pp-f"><span class="std std-ref">f</span></a></p></td>
<td><p>显示堆上的可用内存</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sys#pp-reset"><span class="std std-ref">重置</span></a></p></td>
<td><p>重启系统</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sys#pp-si"><span class="std std-ref">si</span></a></p></td>
<td><p>系统信息</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sys#pp-ut"><span class="std std-ref">ut</span></a></p></td>
<td><p>显示设备运行时间</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sys#pp-sbl"><span class="std std-ref">sbl</span></a></p></td>
<td><p>Set the battery voltage level</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sys#pp-frst"><span class="std std-ref">frst</span></a></p></td>
<td><p>出厂重置</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sens#pp-twi"><span class="std std-ref">twi</span></a></p></td>
<td><p>通用 TWI 读取</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sens#pp-aid"><span class="std std-ref">aid</span></a></p></td>
<td><p>读取 ACC 设备 ID</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sens#pp-av"><span class="std std-ref">av</span></a></p></td>
<td><p>读取 ACC 值</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sens#pp-scs"><span class="std std-ref">scs</span></a></p></td>
<td><p>固定配置集</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/sens#pp-scg"><span class="std std-ref">scg</span></a></p></td>
<td><p>获取固定配置</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/le#pp-les"><span class="std std-ref">les</span></a></p></td>
<td><p>Show meas. and pos.</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/le#pp-lec"><span class="std std-ref">lec</span></a></p></td>
<td><p>Show meas. and pos. in CSV</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/le#pp-lep"><span class="std std-ref">lep</span></a></p></td>
<td><p>Show pos. in CSV</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwb#pp-utpg"><span class="std std-ref">utpg</span></a></p></td>
<td><p>获取 TxPwr</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwb#pp-utps"><span class="std std-ref">utps</span></a></p></td>
<td><p>设置 TxPwr</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmp"><span class="std std-ref">nmp</span></a></p></td>
<td><p>设置UWB模式为无源</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmo"><span class="std std-ref">nmo</span></a></p></td>
<td><p>设置UWB模式为关闭</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nma"><span class="std std-ref">nma</span></a></p></td>
<td><p>设置模式为 AN</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmi"><span class="std std-ref">nmi</span></a></p></td>
<td><p>将模式设置为 ANI</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmt"><span class="std std-ref">nmt</span></a></p></td>
<td><p>设置模式为 TN</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmtl"><span class="std std-ref">nmtl</span></a></p></td>
<td><p>设置模式为 TN-LP</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmg"><span class="std std-ref">nmg</span></a></p></td>
<td><p>设置模式为 GN</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-la"><span class="std std-ref">la</span></a></p></td>
<td><p>显示 AN 列表</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-lg"><span class="std std-ref">lg</span></a></p></td>
<td><p>显示 GN 列表</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nis"><span class="std std-ref">nis</span></a></p></td>
<td><p>设置网络ID</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nls"><span class="std std-ref">nls</span></a></p></td>
<td><p>设置节点标签</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-udi"><span class="std std-ref">udi</span></a></p></td>
<td><p>显示传入的物联网数据</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-uui"><span class="std std-ref">uui</span></a></p></td>
<td><p>发送物联网数据</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-stg"><span class="std std-ref">stg</span></a></p></td>
<td><p>获取统计数据</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-stc"><span class="std std-ref">stc</span></a></p></td>
<td><p>清除统计数据</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-tlv"><span class="std std-ref">tlv</span></a></p></td>
<td><p>发送 TLV 帧</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-aurs"><span class="std std-ref">aurs</span></a></p></td>
<td><p>设置更新率</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-aurg"><span class="std std-ref">aurg</span></a></p></td>
<td><p>获取更新率</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-apg"><span class="std std-ref">apg</span></a></p></td>
<td><p>获取位置</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-aps"><span class="std std-ref">aps</span></a></p></td>
<td><p>设置位置</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-acas"><span class="std std-ref">acas</span></a></p></td>
<td><p>设置锚点配置</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-acts"><span class="std std-ref">acts</span></a></p></td>
<td><p>设置标签配置</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-aks"><span class="std std-ref">aks</span></a></p></td>
<td><p>设置加密密钥</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-akc"><span class="std std-ref">akc</span></a></p></td>
<td><p>清除加密密钥</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-ans"><span class="std std-ref">ans</span></a></p></td>
<td><p>设置 NVM usr 数据</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p>anc (未找到示例)</p></td>
<td><p>清除 NVM usr 数据</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/api#pp-ang"><span class="std std-ref">ang</span></a></p></td>
<td><p>获取 NVM usr 数据</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gateway#pp-amls"><span class="std std-ref">amls</span></a></p></td>
<td><p>设置一次 MAC 地址列表</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gateway#pp-amlg"><span class="std std-ref">amlg</span></a></p></td>
<td><p>获取 MAC 地址列表</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ahs"><span class="std std-ref">ahs</span></a></p></td>
<td><p>设置一次 HW 版本</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ana"><span class="std std-ref">ana</span></a></p></td>
<td><p>设置 MAC 地址</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gateway#pp-acs"><span class="std std-ref">acs</span></a></p></td>
<td><p>配置节点</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ums"><span class="std std-ref">ums</span></a></p></td>
<td><p>设置默认 UART 模式</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ipv4"><span class="std std-ref">ipv4</span></a></p></td>
<td><p>设置本地 IPv4</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/shell-api/gateway#pp-dns"><span class="std std-ref">dns</span></a></p></td>
<td><p>设置 DNS 服务器 IP 地址列表</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<div class="toctree-wrapper compound">
</div>
</div>


           </div>
