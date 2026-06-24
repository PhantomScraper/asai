---
title: "BLE 接口"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/ble-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/ble-interface/"
order: 130
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="ble-interface">
<h1>BLE 接口</h1>
<div class="section" id="introduction">
<h2>简介</h2>
<p>本页描述了通过Bluetooth低功耗 (BLE) 链接提供的 LEAPS UWB 子系统应用程序接口 (UWBS)。</p>
<p>在 UWBS BLE API 设计中，UWBS 模块作为 BLE 外围设备，可通过 API 与 BLE 中央设备通信。 本文件将介绍 BLE 中央装置可用于通讯的 API。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>如果Linux上的Bluetooth完全停止运作，请使用以下指令重新启动Bluetooth:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">systemctl restart bluetooth.service</span>
</pre></div>
</div>
</div>
<hr class="docutils">
<div class="section" id="used-terminology">
<h3>使用术语</h3>
<ul class="simple">
<li><p><strong>UWBS</strong>: LEAPS UWB 子系统模块. UWBS 在 BLE 通讯中扮演 BLE 外围设备的角色。</p></li>
<li><p><strong>CDEV</strong>: 连接 UWBS 外围设备的 BLE 中央设备。</p></li>
<li><p><strong>ELDR</strong>: 扩展加载器。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="position-representation">
<h3>位置表示</h3>
<p>在实时定位系统中显示位置和距离时，有两件事需要考虑:</p>
<ul class="simple">
<li><p>准确性</p></li>
<li><p>精度</p></li>
</ul>
<p>精度是指节点报告的位置与实际位置之间的误差。 目前，本设计中使用的 UWBS 可提供约 10 厘米的精度。</p>
<p>精度是指最小有效位（LSB）的值。 在本系统的板载固件中，精度为 1 毫米，即 0.001 米。 位置以三维坐标（X, Y, Z）表示，其中 X, Y 和 Z 各为 32 位整数（4字节）。 每个 LSB 代表 1 毫米。 这样做是为了更容易解释数值和更容易计算所报告的数值。</p>
<p>在决定精度时，重要的是要结合准确度来选择，这样才能得到有意义的结果。 如果精度低，向用户显示精确值也是无用的。 就目前 10 厘米的精度而言，1 毫米的精度过于精细。 因此，在安卓应用程序中，使用的精度为 1 厘米，即 0.01 米。 只有当坐标/距离变化超过 1 厘米时，Android 应用程序才会显示更新值？这类似于将浮点数/二进制数值舍入到有意义的小数位数。</p>
<hr class="docutils">
</div>
</div>
<div class="section" id="ble-communication-with-uwbs">
<span id="blecommunicationwithuwbs"></span><h2>与 UWBS 进行 BLE 通信</h2>
<div class="line-block">
<div class="line">BLE 中央设备直接与 UWBS 连接，以设置和检索</div>
<div class="line">参数. 它需要单独连接到每个设备进行配置/控制. 与 UWBS 的通信是基于请求-响应模型(参见 <a class="reference internal" href="#ble-gatt-model"><span class="std std-ref">BLE GATT 模型</span></a>)。</div>
</div>
<div class="line-block">
<div class="line">UWBS 接受 TLV API 请求，并将 TLV API 响应通知中心。 BLE 中心必须在任何请求之前启用通知功能，以接收响应。 UWBS 一次只支持一个请求。 有关 UWBS 可识别的所有 TLV 框架的编码详情，请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api#leapsapi"><span class="std std-ref">LEAPS API</span></a>。 除了接受请求，UWBS 还会生成事件。 要启用事件:</div>
</div>
<ul class="simple">
<li><p>通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> 启用 UWBS 中的事件。</p></li>
<li><p>启用专用特性通知</p></li>
</ul>
<div class="line-block">
<div class="line">所有 API 请求, 响应和事件的有效载荷都以一个 2 字节长的 TLV 标头开始，其中第一个字节对应于帧的类型，第二个字节代表帧的长度。 在通过 BLE 特性进行流式传输时，长度应被用于检查帧是否完整。</div>
</div>
<hr class="docutils">
<div class="section" id="ble-lus-leaps-uart-service-interface">
<h3>BLE LUS（LEAPS UART 服务）接口</h3>
<p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a> 支持额外的 <strong>BLE LUS (LEAPS UART Service)</strong> 接口, 请按照以下步骤设置接口。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>如果正在开启 UART shell，将无法访问 BLE shell。</p>
</div>
<ol class="arabic">
<li><p>用下面的命令安装 python ble-serial 库:</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">python -m pip install ble-serial==2.7.1</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>如果使用的是 Windows 系统，请按照此链接 <a class="reference external" href="https://github.com/Jakeler/ble-serial">ble-serial</a> 中的 “Windows 附加步骤” 进行操作。</p>
</div>
</li>
<li><p>使用下面的命令查找设备。 LEAPS 显卡的名称应该是 “LEAPS。。。。”。</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">ble-scan</span>
</pre></div>
</div>
<p>以及成功扫描的结果：</p>
<a class="reference internal image-reference" href="../../../../_images/ble-lus-scan.png"><img alt="../../../../_images/ble-lus-scan.png" class="align-center" src="/docs-assets/zh-cn/_images/ble-lus-scan.png" style="width: 920.0px; height: 462.0px;"></a>
</li>
<li><p>要连接串行端口，请打开终端并运行以下命令，并输入在上述步骤中找到的</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">ble-serial -d CA:E5:56:1F:57:3D -r e8573d97-6758-11e9-8860-cb4385c24b83 -w e6bfa235-6758-11e9-979f-5b24c4603eb8 -t 10</span>
</pre></div>
</div>
</li>
<li><p>如果连接成功，将显示如下内容</p>
<img alt="../../../../_images/ble-lus-passed.png" class="align-center" src="/docs-assets/zh-cn/_images/ble-lus-passed.png">
</li>
<li><p>根据日志，脚本创建了一个名为 “/tmp/ttyBLE” 的串口，用于与 LEAPS 板上的串口通信。 运行该终端，打开另一个终端，使用 minicom 等工具访问该串口。</p></li>
<li><p>按双击回车键进入 shell。</p></li>
</ol>
<hr class="docutils">
</div>
<div class="section" id="autodisconnect">
<span id="id1"></span><h3>自动断开连接</h3>
<p>如果 CDEV 没有通过向 CCCD 写入 0x0001 来启用 “（<strong>API Response</strong>）” 或 “（<strong>API Events</strong>）” 特征的通知，UWBS 将在 15 秒后自动终止连接（参见 <a class="reference internal" href="#ble-gatt-model"><span class="std std-ref">BLE GATT 模型</span></a>）。</p>
</div>
<hr class="docutils">
<div class="section" id="ble-throughput">
<h3>BLE 吞吐量</h3>
<p>使用最大可能的 ATT MTU 和最高的连接优先级，以便在与 UWBS 之间进行数据流传输时，利用最大可能的吞吐量。 UWBS 支持的最大 MTU 为 150 字节。 节点首选的连接间隔为最小 10 毫秒到最大 40 毫秒，延迟为 0，超时 2 秒。 请注意，在Bluetooth v4.0 和 v4.1 中，无论 MTU 协商与否，最大数据长度都会保持默认值，因此与Bluetooth v4.2 及更高版本相比，这些Bluetooth版本的最大吞吐量会受到限制。</p>
</div>
<hr class="docutils">
<div class="section" id="security-encryption">
<h3>安全/加密</h3>
<div class="line-block">
<div class="line">系统支持两种 BLE 操作模式：无加密或仅加密 (AES-OFB)。 加密功能和操作将在下一节中说明：</div>
</div>
<ul class="simple">
<li><p>功能</p>
<ul>
<li><p>访问控制和信息完整性 (MIC/MAC - 信息完整性代码或信息验证码)</p></li>
<li><p>保密性</p></li>
<li><p>重放保护</p></li>
</ul>
</li>
<li><p>BLE 无线加密采用 AES OFB 128 密码。</p></li>
<li><p>在加密网络中，每个想要参与通讯的节点，都需要有一个由用户设置的128位对称密钥。</p>
<ul>
<li><p>在LEAPS Android Manager里:通过设置</p></li>
<li><p>On module:UART/SPI/UserApp/Shell API</p></li>
</ul>
</li>
<li><p>加密/解密是分块进行的，每个块的大小固定为 16字节。 因此，加密有效载荷的大小必须取整为 16 字节的倍数。 换句话说，如果启用了安全功能，信息的有效载荷必须对齐到 16 字节的倍数。 如果禁用加密，则有效载荷不得对齐到 16 字节。</p></li>
<li><p>每条信息将包含</p>
<ul>
<li><p>Nonce - 16 字节</p></li>
<li><p>MIC/MAC - 2 字节</p></li>
<li><p>有效载荷 (如果启用加密，对齐为 16 字节)</p></li>
<li><p>See also <a class="reference internal" href="#messageencoding"><span class="std std-ref">信息编码</span></a></p></li>
</ul>
</li>
<li><p>下图解释了如何使用AES加密数据</p>
<ul>
<li><p>In red: 密钥，必须保护</p></li>
<li><p>In blue: 公共数据 - 分布在每条 BLE 信息中</p></li>
<li><p>In grey: 加密加速器/控制器</p></li>
<li><p>In yellow: 计算/加密区块</p></li>
<li><p>In green: 明文/解密区块</p></li>
</ul>
</li>
</ul>
<img alt="../../../../_images/encryptedusingaes.png" class="align-center" src="/docs-assets/zh-cn/_images/encryptedusingaes.png">
<ul class="simple">
<li><p>下图解释了如何使用 AES OFB 对数据进行加密和链式处理</p></li>
</ul>
<img alt="../../../../_images/aes_ofb.png" class="align-center" src="/docs-assets/zh-cn/_images/aes_ofb.png">
<img alt="../../../../_images/aes_ofb_02.png" class="align-center" src="/docs-assets/zh-cn/_images/aes_ofb_02.png">
<ul class="simple">
<li><p>参与加密网络的节点要求</p>
<ul>
<li><p>使用正确的Nonce进行加密/解密</p></li>
<li><p>拥有 128 位 AES 密钥</p></li>
</ul>
</li>
<li><p>有两种nonce - 用于信息加密/解密的nonce和用于信息完整性检查的nonce。</p>
<ul>
<li><p>每个加密/解密nonce的长度为16字节。 发送方生成并在发送的信息中嵌入nonce。 在解密过程中，接收方会使用收到的nonce作为初始化向量（IV）。</p></li>
<li><p>每个完整性 nonce 长度为 16 字节. 它从接收到的信息 nonce 中提取，并将其 nonce 递增 1。</p></li>
</ul>
</li>
<li><p>为了抵御中继攻击，每个nonce都必须是唯一的，在网络中的任何时候，任何信息都不能重复使用nonce。</p></li>
</ul>
<hr class="docutils">
</div>
<div class="section" id="ble-gatt-model">
<span id="id2"></span><h3>BLE GATT 模型</h3>
<p><strong>UWBS服务</strong> 的UUID是 <strong>680c21d9-c946-4c1f-9c11-baa1c21329e7</strong>. 根据 BLE 规范的建议，所有特征值都以小字尾编码。</p>
<hr class="docutils">
<div class="section" id="uwbs-characteristics">
<h4>UWBS 特征</h4>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>UUID</p></th>
<th class="head"><p>名称</p></th>
<th class="head"><p>长度</p></th>
<th class="head"><p>价值</p></th>
<th class="head"><p>标志</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Std.GAP 服务，标签 <strong>0x2A00</strong></p></td>
<td><p>标签</p></td>
<td><p>Var</p></td>
<td><p>UTF-8 编码字符串</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>e6bfa234-
6758-11e9-
979f-5b2
4c4603eb8</strong></p></td>
<td><p>API 请求</p></td>
<td><p>最大变量 50 字节</p></td>
<td><p>信息头 + TLV 编码的 API 请求</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p><strong>e8573d96-
6758-11e9-
8860-cb4
385c24b83</strong></p></td>
<td><p>API 响应</p></td>
<td><p>最多 273 字节</p></td>
<td><p>信息头 + TLV 编码的 API 响应</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>003bbdf2-
c634-4b3d-
ab56-7ec889
b89a37</strong></p></td>
<td><p>API 事件</p></td>
<td><p>最多 273 字节</p></td>
<td><p>信息头 + TLV 编码的 API 事件</p></td>
<td><p>RO</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>标签特性是一个特殊特性。 它是标准 “名称” 特性（0x2A00）下标准强制 GAP 服务（0x1800）的一部分。</p>
</div>
<hr class="docutils">
</div>
<div class="section" id="message-encoding">
<span id="messageencoding"></span><h4>信息编码</h4>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 37%">
<col style="width: 26%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>项目</p></th>
<th class="head"><p>长度</p></th>
<th class="head"><p>有效载荷</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>传输头</strong></p></td>
<td><p>2字节</p></td>
<td><p>索引(1字节) 合计(1字节)</p></td>
</tr>
<tr class="row-odd"><td><p><strong>无</strong></p></td>
<td><p>16字节</p></td>
<td><p>无信息，如果关闭了安全机制，则与此无关</p></td>
</tr>
<tr class="row-even"><td><p><strong>mic/mac</strong></p></td>
<td><p>2字节</p></td>
<td><p>如果启用加密，则进行信息完整性检查；如果禁用加密，则进行有效载荷的简单字节总和检查</p></td>
</tr>
<tr class="row-odd"><td><p><strong>付费</strong></p></td>
<td><p>从 0 到 255 字节</p></td>
<td><p>值或 TLV 编码帧（取决于特定特性）</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="operation-mode">
<span id="operationmode"></span><h4>操作模式</h4>
<p>使用 API 请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-cfg-get#leaps-cfg-get"><span class="std std-ref">leaps_cfg_get</span></a> 读取当前配置. 使用 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set#leaps-cfg-anchor-set"><span class="std std-ref">leaps_cfg_anchor_set</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set#leaps-cfg-tag-set"><span class="std std-ref">leaps_cfg_tag_set</span></a> API 请求来设置 UWBS 配置。</p>
</div>
<hr class="docutils">
<div class="section" id="location-data">
<h4>位置数据</h4>
<p>使用 API 请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-loc-get#leaps-loc-get"><span class="std std-ref">leaps_loc_get</span></a> 来读取包含位置, 距离或两者的位置数据. 使用请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-pos-set#leaps-pos-set"><span class="std std-ref">leaps_pos_set</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-pos-get#leaps-pos-get"><span class="std std-ref">leaps_pos_get</span></a> 只操作 UWBS 位置。</p>
<p>通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> 启用 “位置数据就绪” 事件，并接收 “事件” 特征的通知，以自动从 UWBS 获取当前位置和距离。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 18%">
<col style="width: 18%">
<col style="width: 18%">
<col style="width: 18%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>位置数据编码，作为特征 “事件” 的 BLE 通知接收</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="4"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>int32_t- 小端序，是以毫米为单位的 x 坐标</p></td>
<td><p>int32_t- 小端序, 是以毫米为单位的 y 坐标</p></td>
<td><p>int32_t- 小端序, 是以毫米为单位的 z 坐标</p></td>
<td><p>uint8_t- 是位置质量因子，单位为百分比(0-100)</p></td>
</tr>
<tr class="row-even"><td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td colspan="4"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00
0x9c
0x0e
0x00
0x00
0x64</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示请求/命令状态</div>
<div class="line">类型0x41表示位置</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>上一表格中的残留帧</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td colspan="6"><p>价值</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><p>uint8_t - 值中编码的距离数</p></td>
<td><p>uint16_t - UWB 地址，小端序</p></td>
<td><p>uint32_t - 小端序中的距离（单位：毫米）</p></td>
<td><p>uint8_t - 距离品质因数，以百分比表示 (0-100)</p></td>
<td><p>标准13字节格式的位置(x,y,z,qf)</p></td>
<td><p>…</p></td>
</tr>
<tr class="row-even"><td><p>0x49</p></td>
<td><p>0x51</p></td>
<td><p>0x04</p></td>
<td colspan="4"><p>位置和距离 nr.2,3,4</p></td>
<td><p>nr. 2, 3, 4</p></td>
</tr>
</tbody>
</table>
<p>类型0x49表示测距锚的位置和距离</p>
<hr class="docutils">
</div>
<div class="section" id="user-data">
<span id="userdata"></span><h4>用户数据</h4>
<p>通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> 启用事件 “用户数据就绪”，并接收关于特征 “事件” 的通知，以自动从UWBS接收ble用户数据。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>BLE用户数据编码，作为特征 “事件” 的BLE通知接收</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>最大128字节</p></td>
</tr>
<tr class="row-even"><td><p>0x51</p></td>
<td><p>0x80</p></td>
<td><p>0x01 0x02 0x03 …
0x7F 0x80</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="node-id">
<span id="id3"></span><h4>节点 id</h4>
<p>使用请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-node-id-get#leaps-node-id-get"><span class="std std-ref">leaps_node_id_get</span></a> 来读取 UWBS 的地址。</p>
</div>
<div class="section" id="network-id">
<span id="networkid"></span><h4>网络id</h4>
<p>使用请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-panid-set#leaps-panid-set"><span class="std std-ref">leaps_panid_set</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-panid-get#leaps-panid-get"><span class="std std-ref">leaps_panid_get</span></a> 来操作网络 ID。</p>
</div>
<div class="section" id="reset-or-reboot">
<span id="id4"></span><h4>重置或重启</h4>
<p>重置 UWBS 的请求，如 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a> 或 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-factory-reset#leaps-factory-reset"><span class="std std-ref">leaps_factory_reset</span></a> 会在重置前断开 BLE 中央连接. 中心应等待 1 秒后再重新连接。</p>
</div>
<div class="section" id="anchor-list">
<span id="id5"></span><h4>锚点列表</h4>
<p>参见请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get#leaps-anchor-list-get"><span class="std std-ref">leaps_anchor_list_get</span></a>。</p>
</div>
<div class="section" id="device-info">
<span id="deviceinfo"></span><h4>设备信息</h4>
<p>请参阅请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get#leaps-dev-info-get"><span class="std std-ref">leaps_dev_info_get</span></a> 来读取固件, 硬件和配置的版本。</p>
</div>
<div class="section" id="update-rate">
<span id="updaterate"></span><h4>更新率</h4>
<p>请参阅请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-set#leaps-upd-rate-set"><span class="std std-ref">leaps_upd_rate_set</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-get#leaps-upd-rate-get"><span class="std std-ref">leaps_upd_rate_get</span></a> 来更改标签节点的更新率。</p>
<hr class="docutils">
</div>
</div>
<div class="section" id="auto-positioning">
<span id="autopositioning"></span><h3>自动定位</h3>
<p>BLE API 也能启动自动定位程序. 自动定位过程已在 CDEV 上完成（位置已计算）. BLE API 可启动距离测量和检索. 工作流程如下:</p>
<ol class="arabic">
<li><p>测量:</p>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>找到并验证启动器 (节点必须是 <em>真正的启动器</em>，而不仅仅是 <em>配置为启动器</em>，请参阅 <a class="reference internal" href="#operationmode"><span class="std std-ref">操作模式</span></a> 和 <a class="reference internal" href="#bleadvertisements"><span class="std std-ref">BLE 广告</span></a>)</p></li>
<li><p>连接到启动器。</p></li>
<li><p>如果尚未启用，通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> 启用 “位置就绪” 事件（不要忘记启用 BLE cccd 特性通知）。</p></li>
<li><p>通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-autopos-start#leaps-autopos-start"><span class="std std-ref">leaps_autopos_start</span></a> 请求启动自动定位。</p></li>
<li><p>从启动器接收到所有测得的距离，将测得的距离保存到矩阵中。</p></li>
<li><p>断开与启动器的连接。</p></li>
<li><p>获取所有其他（非启动器）节点的距离:</p></li>
</ol>
<blockquote>
<div><ol class="lowerroman simple">
<li><p>连接</p></li>
<li><p>使用 API 请求从 UWBS 获取位置数据 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-loc-get#leaps-loc-get"><span class="std std-ref">leaps_loc_get</span></a> 从 UWBS 获取位置数据，并将距离保存到矩阵中。</p></li>
<li><p>断开连接</p></li>
</ol>
</div></blockquote>
</div></blockquote>
</li>
<li><p>评估测量距离, 检查正交性并计算位置。</p></li>
<li><p>根据用户请求，将计算出的位置保存到节点上（使用 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-pos-set#leaps-pos-set"><span class="std std-ref">leaps_pos_set</span></a> 请求）。</p></li>
</ol>
<hr class="docutils">
</div>
<div class="section" id="ble-advertisements">
<span id="bleadvertisements"></span><h3>BLE 广告</h3>
<p>BLE 广告是外围设备让他人知道其存在的常用方式。 根据 BLE 规范，广播有效载荷由三连串组成，即 [长度, 类型, &lt;数据&gt;]。</p>
<p>UWBS 将广播关于其 <strong>存在和运行模式</strong> 的基本信息。 BLE 广告的长度不足以同时包含位置信息。</p>
<p>在BLE广告中，有31个字节需要使用:</p>
<ul class="simple">
<li><p>3 字节为强制标志（一个 AD 三字节）。</p></li>
<li><p>其余的 28 个字节可用于应用程序填写 AD 记录（每条记录有 2 个字节的长度+类型开销）。</p></li>
</ul>
<div class="section" id="presence-broadcast">
<h4>存在广播</h4>
<p>UWBS 模块上的 BLE 采用可连接的非定向模式工作。 它发布存在广播，其中包含服务可用性和一些服务数据。 存在广播遵循BLE广告帧结构，使用 28 个字节来呈现信息。 设备名称放在扫描响应中，需要主动扫描。</p>
<p>存在广播和扫描响应编码如下表所示。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>广告</strong></p></th>
<th class="head"><p><strong>价值</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x02</p></td>
</tr>
<tr class="row-odd"><td><p>类型</p></td>
<td><p>0x01 (标志)</p></td>
</tr>
<tr class="row-even"><td><p>价值</p></td>
<td><p>设备/广告标志 - 可连接</p></td>
</tr>
<tr class="row-odd"><td><p>LEN</p></td>
<td><p>0x19 (25 dec)</p></td>
</tr>
<tr class="row-even"><td><p>类型</p></td>
<td><p>0x21 (33 dec, 服务数据)</p></td>
</tr>
<tr class="row-odd"><td rowspan="8"><p>价值</p></td>
<td><p><strong>680c2 1d9-c946-4c1f-9c11-baa1c21329e7</strong> (16字节)</p></td>
</tr>
<tr class="row-even"><td><p>PAN ID (2 字节)</p></td>
</tr>
<tr class="row-odd"><td><p>节点 ID (2 字节)</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">标志（1 字节）</div>
<div class="line">Bit layout: OXSEIBUU O - 操作模式 (标记 0, 锚点 1)</div>
<div class="line">X - 保留</div>
<div class="line">S - security_enabled</div>
<div class="line">E - 错误提示</div>
<div class="line">I - initiator_enabled,</div>
<div class="line">B - gateway_enabled</div>
<div class="line">UU - UWB 模式:关闭 (0), 被动 (1), 主动 (2)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>变化计数器 (1 字节) - 每次 UWBS 的重要内部状态发生变化 (例如配置) 时，变化计数器也会随之变化</p></td>
</tr>
<tr class="row-even"><td><p>UWB 计数器（1 字节）–低功耗设备使用的倒计时计数器。 当低功耗设备上的此计数器达到 0 时，设备的 UWB 活动将被禁用。 当锚检测到设备上的计数器低于配置的低水位值时，锚会连接到设备并重置计数器，以保持设备的 UWB 活动。</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">UWBS 标志（1 字节）</div>
<div class="line">位布局: FUSR</div>
</div>
<div class="line-block">
<div class="line">F - 固件类型(2 bits, 0=BLDR, 1=ELDR, 2=MAIN)</div>
<div class="line">U - UWB系统(2 bits, 0=LEAPS RTLS, 1=FIRA)</div>
<div class="line">S - UWB 子系统 (2 bits, 0=UCI, 1=NIQ)</div>
<div class="line">R - 保留,</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>客户信息 (1 字节) 客户的具体信息</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>扫描响应</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x16 (22 dec)</p></td>
</tr>
<tr class="row-odd"><td><p>类型</p></td>
<td><p>0x09 (设备名称，放置在扫描响应数据包中，使用主动扫描来检测它)</p></td>
</tr>
<tr class="row-even"><td><p>价值</p></td>
<td><p>“LEAPS” 前缀 (5 个字符) + 十六进制格式的完整节点 ID（16 个字符）</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="section" id="firmware-update">
<span id="firmwareupdate"></span><h3>固件更新</h3>
<p>固件更新功能用于更新 UWBS 的固件. 本节描述 BLE 接口的控制和数据流. 有关固件更新过程的更多详情，请参阅 API 请求 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> 。</p>
<div class="section" id="updating-the-fw-binary">
<h4>更新 FW 二进制文件</h4>
<ol class="arabic simple">
<li><p>CDEV 连接到 UWBS。</p></li>
<li><p>CDEV 通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> 开始更新 FW。</p></li>
<li><p>如果 UWBS 响应状态为 “ok”，CDEV 可以跳过此步骤。 如果 UWBS 响应状态为 “really”，CDEV 将重置 UWBS，并在 UWBS 重启后重新连接，CDEV 将重新开始更新。 如果 UWBS 响应状态为 “不允许”，则无法进行 fw 更新。 UWBS 中可能禁用了 fw 更新。</p></li>
<li><p>CDEV 通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> 发送 FW 片段。</p></li>
<li><p>CDEV 在成功发送最后一个数据块后，会重置 UWBS。</p></li>
</ol>
</div>
<div class="section" id="updating-the-eldr-binary">
<h4>更新 ELDR二进制文件</h4>
<ol class="arabic simple">
<li><p>在 UWBS 重新启动后，CDEV 重新连接。</p></li>
<li><p>CDEV通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> 开始更新 ELDR。</p></li>
<li><p>CDEV 通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> 发送 ELDR 片段。</p></li>
<li><p>CDEV 在成功发送最后一个数据块后，会重置 UWBS。</p></li>
<li><p>CDEV 可以在 UWBS 重启后连接，并观察 FW 信息，以验证固件更新是否正在运行。</p></li>
</ol>
<p>CDEV 应该在每次连接到 UWBS 时，启用 <strong>API 响应</strong> 特性的通知，以防止 UWBS 自动断开连接 (参见 <a class="reference internal" href="#autodisconnect"><span class="std std-ref">自动断开连接</span></a>)。</p>
<p>在固件更新过程中，如果 UWBS 突然断开连接，可以根据当前的更新阶段，从步骤 7 或步骤 1 重新开始。</p>
</div>
<div class="section" id="transmitting-the-fw-binary">
<h4>传输 FW 二进制文件</h4>
<p>在 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> 启动固件更新后，数据会通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> 传输到 UWBS. UWBS 通过在响应中编码大小和偏移量，准确地告诉 CDEV 它需要哪个数据缓冲区. CDEV 开始使用写入（write）方式发送所请求的缓冲区块，而不做响应，因此不涉及整个往返. 请注意，如果 BLE 传输的 MTU 无法容纳所请求的缓冲区大小，则每个数据块可由多个 BLE 传输来传输. 数据块包括:</p>
<ul class="simple">
<li><p>Data: UWBS 要求的fw缓冲区大小(240)</p></li>
<li><p>相对偏移（从最开始）:4 字节。</p></li>
</ul>
<p>发送数据缓冲区后，CDEV 等待进一步的指令。 在传输过程中，UWBS 通常会一个接一个地按顺序请求数据缓冲区，以获得固件的连续字节序列。 如果出现异常，例如当前缓冲区传输失败，节点可能会请求一个意外的缓冲区。</p>
<p>如果出现错误，固件更新会停止，需要重新启动。</p>
</div>
<div class="section" id="finishing-the-transmission">
<h4>完成传输</h4>
<p>一旦成功接收到最后一个数据块，UWBS就会让 CDEV知道它已经接收到完整的二进制固件。 收到后</p>
<ol class="arabic simple">
<li><p>CDEV 通过 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a> 命令重置 UWBS，这将导致 UWBS 与 CDEV 断开连接。</p></li>
<li><p>CDEV 等待 1 秒。</p></li>
<li><p>CDEV 尝试再次连接 UWBS 并检查其固件状态（参见 <a class="reference internal" href="#deviceinfo"><span class="std std-ref">设备信息</span></a>）。</p></li>
</ol>
</div>
</div>
</div>
<div class="section" id="appendix-bibliography">
<h2>附录 - 参考书目</h2>
<ol class="arabic simple">
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/question/55309/connection-issues-with-android-60-marshmallow-and-nexus-6/">https://devzone.nordicsemi.com/question/55309/connection-issues-with-android-60-marshmallow-and-nexus-6/</a></p></li>
<li><p><a class="reference external" href="http://stackoverflow.com/questions/37151579/schemes-for-streaming-data-with-ble-gatt-characteristics">http://stackoverflow.com/questions/37151579/schemes-for-streaming-data-with-ble-gatt-characteristics</a></p></li>
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/nordic/nordic-blog/b/blog/posts/what-to-keep-in-mind-when-developing-your-ble-andr">开发 BLE Android 应用程序时应注意的事项</a></p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide#leaps-rtls-integration-guie"><span class="std std-ref">集成指南</span></a></p></li>
</ol>
</div>
<div class="section" id="appendix-migration-from-dwm-ble-api">
<h2>附录 - 迁移自 DWM BLE API</h2>
<p>下表总结了 LEAPS BLE API 与之前的 DWM BLE API 相比的变化. 这样做的目的是为了更容易过渡到 LEAPS BLE API. DWM BLE API 中使用的前 GATT 模型被请求/响应模型取代，该模型比前模型的特性更少，参见 <a class="reference internal" href="#blecommunicationwithuwbs"><span class="std std-ref">与 UWBS 进行 BLE 通信</span></a> 部分。</p>
<div class="section" id="former-ble-gatt-model">
<h3>前 BLE GATT 模型</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 37%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><div class="line-block">
<div class="line"><strong>名称</strong></div>
<div class="line"><strong>原关贸总协定特性</strong></div>
</div>
</th>
<th class="head"><p><strong>DWM和LEAPS比较</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>标签</p></td>
<td><div class="line-block">
<div class="line">DWM: <em>标准名称特性(0x2A00) 下的标准强制 GAP 服务(0x1800)</em></div>
<div class="line">LEAPS: 无变化，保持不变</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>操作模式</p></td>
<td><div class="line-block">
<div class="line">DWM: 当前的 UWBS 配置包含在特殊的</div>
<div class="line">特性</div>
<div class="line">LEAPS: see <a class="reference internal" href="#operationmode"><span class="std std-ref">操作模式</span></a> 读取/写入 UWBS 的配置, 参阅 <a class="reference internal" href="#firmwareupdate"><span class="std std-ref">固件更新</span></a> 在固件 1 和固件 2 之间切换。</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>更新率</p></td>
<td><p>DWM: 当前更新速率包含在特殊特性 LEAPS 中: 请参阅 <a class="reference internal" href="#updaterate"><span class="std std-ref">更新率</span></a> 部分以读取/写入当前更新速率配置</p></td>
</tr>
<tr class="row-odd"><td><p>网络 ID</p></td>
<td><p>DWM: 当前网络ID包含在特殊特征LEAPS中：请参阅 <a class="reference internal" href="#networkid"><span class="std std-ref">网络id</span></a> 部分读/写当前网络ID</p></td>
</tr>
<tr class="row-even"><td><p>位置数据模式</p></td>
<td><p>DWM: 用作 “位置数据” 这一特殊特性的设置. LEAPS：不再需要，请参阅 <a class="reference internal" href="#userdata"><span class="std std-ref">用户数据</span></a> 从 UWBS 获取位置，并参阅 <a class="reference internal" href="#autopositioning"><span class="std std-ref">自动定位</span></a> 部分获取自动定位程序时的距离。</p></td>
</tr>
<tr class="row-odd"><td><p>位置数据</p></td>
<td><p>DWM:UWBS 的当前位置（在执行自动定位程序时也包含距离）包含在一个特殊的特性中 LEAPS：请参阅 <em>位置数据</em> 一节获取位置和距离。</p></td>
</tr>
<tr class="row-even"><td><p>持续位置</p></td>
<td><div class="line-block">
<div class="line">DWM: 持久位置是通过特殊特性写入的</div>
<div class="line">LEAPS: 请参阅 <a class="reference internal" href="#userdata"><span class="std std-ref">用户数据</span></a> 部分，了解如何将持久位置写入 UWBS</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>设备信息</p></td>
<td><div class="line-block">
<div class="line">DWM: 设备信息，如配置, 节点 ID 和固件</div>
<div class="line">从特殊特性读取版本信息</div>
<div class="line">请参阅 <a class="reference internal" href="#deviceinfo"><span class="std std-ref">设备信息</span></a> 部分读取节点固件版本，请参阅 <a class="reference internal" href="#node-id"><span class="std std-ref">节点 id</span></a> 部分读取节点 ID，请参阅 <a class="reference internal" href="#operationmode"><span class="std std-ref">操作模式</span></a> 部分读取节点配置。</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>统计</p></td>
<td><p>DWM: 统计数据包含在一个特殊的特性中 LEAPS: 统计数据不再支持</p></td>
</tr>
<tr class="row-odd"><td><p>MAC 统计</p></td>
<td><p>DWM: MAC 统计数据包含在特殊特性 LEAPS 中: 不再支持 MAC 统计</p></td>
</tr>
<tr class="row-even"><td><p>集群信息</p></td>
<td><p>DWM: UWB 集群信息包含在一个特殊特性中 LEAPS: 不再支持集群信息</p></td>
</tr>
<tr class="row-odd"><td><p>锚点列表</p></td>
<td><div class="line-block">
<div class="line">DWM: 当前邻居锚节点列表包含在一个特殊属性中</div>
<div class="line">LEAPS：请参阅 <a class="reference internal" href="#anchor-list"><span class="std std-ref">锚点列表</span></a> 部分来读取当前的锚节点列表</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>FW 更新推送</p></td>
<td><div class="line-block">
<div class="line">DWM: 固件更新通过一个特殊的特性启动，该特性也用于将新固件传输到 UWBS 中。</div>
<div class="line">LEAPS: 请参阅 <a class="reference internal" href="#firmwareupdate"><span class="std std-ref">固件更新</span></a> 部分，了解如何启动固件更新以及如何将固件传输到节点中</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>FW更新投票</p></td>
<td><div class="line-block">
<div class="line">DWM: UWBS 在固件更新期间使用此特性的通知对 BLE 中心做出响应</div>
<div class="line">LEAPS: 请参阅 <a class="reference internal" href="#firmwareupdate"><span class="std std-ref">固件更新</span></a> 章节，了解如何执行固件更新</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>断开连接</p></td>
<td><div class="line-block">
<div class="line">DWM: BLE 中央断开连接通过一个特殊的特性，它是处理 API bug 的变通方法</div>
<div class="line">LEAPS: 错误修复后不支持</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
