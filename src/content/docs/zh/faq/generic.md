---
title: "通用"
lang: zh
slug: "faq/generic"
section: "faq"
sourceUrl: "https://docs.leapslabs.com/zh-cn/faq/generic/"
order: 29
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="generic">
<span id="faq-generic"></span><h1>通用</h1>
<hr class="docutils">
<div class="line-block">
<div class="line">以下 FAQ（常见问题）涵盖了有关 Ultra-Wideband, <a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> 或 <a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> 的常见问题。</div>
</div>
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>我是实时定位系统的新手。 你有基本术语的列表吗？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>锚点</strong> - <strong>AN (锚节点)</strong> - 具有固定位置的基础设施节点 - 能够测量位置数据, 数据卸载和路由的参考节点。</p>
<ul>
<li><p class="sd-card-text">锚节点可以启用网关功能 - 它可以作为 UWB 子系统与其他接口（如以太网和 WiFi）之间的网关。 UWB 子系统通过 SPI 或 USB 接口与主机连接。</p></li>
</ul>
</li>
<li><p class="sd-card-text"><strong>定位引擎 (LE)</strong> - 一种使用测量值进行位置估计的算法. 主要分为两组</p></li>
</ul>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text"><strong>三维定位</strong> - 利用节点之间的距离来估计位置的定位引擎，尤其是在使用三维定位时。</p></li>
<li><p class="sd-card-text"><strong>多方位</strong> - 利用节点之间的时差来估计位置的定位引擎，尤其是在使用 TDoA 时。</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p class="sd-card-text"><strong>导航</strong> - 在移动对象一侧收集和使用位置数据的定位模式。 在 LEAPS RTLS 和 PANS PRO RTLS 的导航模式中，位置是在模块上计算的，数据可通过模块上的应用程序接口获取。 这种方法可在移动设备上提供极低延迟的定位数据，降低基础设施成本，并大大简化部署。 典型应用包括无人机, 机器人, 工具, 车辆和便携式设备的导航。</p></li>
<li><p class="sd-card-text"><strong>节点</strong> - 能够与其它设备（锚点, 标签。。。。。。）通信的网络设备。</p></li>
<li><p class="sd-card-text"><strong>标签</strong> - <strong>TN（标签节点）</strong> - 移动位置的移动节点 - 它使用锚点来测量, 定位自己的位置，并根据不同的模式，以指定的更新率交换数据。</p></li>
<li><p class="sd-card-text"><strong>到达时间差 (TDoA)</strong> - 这是一种测量技术，在已知的固定位置测量节点之间的时间差。 测量结果就是时差。 已知固定位置的节点通常需要同步。 TDoA 是一种双曲线定位方法，有两个主要子类别</p></li>
</ul>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text"><strong>上行链路 TDoA（UL-TDoA）</strong> - 是 TDoA 的一种**跟踪**模式，标签通常会在随机时间发送一条名为闪烁的短信息。 锚点接收到闪烁信息后，利用同步时间，采用双曲线定位法估算标签的位置。 这种定位方法至少需要 4 次测量，通常对锚点部署的形状更为敏感。 由于标签只需短暂闪烁，因此这种方法耗电量最低。 UL-TDoA 标签对硬件设计和电池的要求也较低。 与需要更复杂的时间调度和避免碰撞方案的 TWR 系统相比，这种方法更容易实现网络可扩展性和标签低功耗，因为它可以随机访问媒体。</p></li>
<li><p class="sd-card-text"><strong>下行链路TDoA（DL-TDoA）</strong> - 是TDoA的**导航**模式，标签只聆听来自锚点的包含时间和通常锚点位置的网络信息。 根据这些数据，标签可以计算出自己的位置。 这类似于室内使用的全球导航卫星系统（GNSS）。 由于标签只监听不发送，因此对标签的数量没有限制。 这种模式允许标签完全保密，因为它们不会发射信号。</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p class="sd-card-text"><strong>跟踪</strong> - 在中央服务器上收集位置和遥测数据的一种定位模式。 数据可通过 LEAPS Server API 获取。 这种模式适用于在一个地方（通常在服务器上）监控和处理大量设备的数据。 典型应用包括资产追踪, 区域违规检测, 运动员成绩监控和人员追踪等。</p></li>
<li><p class="sd-card-text"><strong>双向测距（TWR）</strong> - 是一组测量技术，通过双向交换信息来估计两个节点之间的距离。 测量结果就是距离。 标签位置计算不需要节点的时间同步。</p></li>
<li><p class="sd-card-text"><strong>超宽带（UWB）</strong> - 是一种无线电技术，可以使用非常低的能量水平，在大部分无线电频谱上进行短距离, 高带宽通信。 与Bluetooth, WIFI 或 GPS 等其他技术相比，UWB 对多径衰落具有很强的免疫力。 因此，它适用于精确定位，尤其是在室内。</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>DWM1001, PANS RTLS, PANS PRO RTLS 和 LEAPS RTLS 之间有什么区别？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>DWM1001</strong> 是基于 Decawave/Qorvo 的 DW1000 超宽带 (UWB) 收发器 IC 的硬件模块，它是 IEEE 802.15.4-2011 UWB 实现. 它集成了 UWB 和 Bluetooth® 天线, 所有射频电路, Nordic Semiconductor nRF52832 和运动传感器. 该模块最初由 LEAPS 设计，并以 Decawave 品牌销售。</p></li>
<li><p class="sd-card-text"><strong>PANS RTLS</strong> 是一个完整的实时定位系统和网络堆栈，以TWR测量技术为基础. UWB 子系统可配置为锚点, 标签或网关模式. 软件堆栈由 LEAPS 开发，以 Decawave/Qorvo 品牌销售。</p></li>
<li><p class="sd-card-text"><strong>PANS PRO RTLS</strong> 基于 PANS RTLS 协议栈。 它由 LEAPS 维护并提供给市场。 PANS PRO RTLS 中对许多软件进行了改进和错误修正，以提供可用于生产的堆栈。 一系列经过认证的产品已通过此软件栈推向市场。 与 PANS RTLS 协议栈一样，该协议栈以二进制代码的形式免费提供给市场。</p></li>
<li><p class="sd-card-text"><strong>LEAPS RTLS</strong> 是一个先进的实时定位系统，可涵盖广泛的导航和追踪使用案例。 其核心是一个嵌入式 UWB 子系统，可配置为不同的模式和配置文件。 该协议栈可在锚点, 标签或网关模式下运行。 网络配置文件完全可扩展，具有高容量和低功耗的特点。 其多功能性使系统要求, 成本, 部署时间和维护复杂性之间的平衡变得容易。 应用范围从简单的距离接近，到高速跟踪或导航无限量的接收器。 支持的测量技术包括 TWR（双向测距）, UL-TDoA（使用上行链路到达时间差进行跟踪）和 DL-TDoA（使用下行链路到达时间差进行导航）。 LEAPS 协议栈已整合到 LEAPS 以及第三方的产品中。</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>LEAPS如何参与DWM1001模块和PANS RTLS网络堆栈的开发？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>DWM1001模块</strong> 最初是由LEAPS设计的，LEAPS参与了设计, 模块调试, 验证，并以Decawave/Qorvo的品牌将设计投入生产。</p></li>
<li><p class="sd-card-text"><strong>LEAPS</strong> 设计并开发了PANS RTLS <strong>的</strong> 软件堆栈，包括一套广泛的嵌入式测试，用于生产中的模块校准和功能测试。</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>LEAPS RTLS 与 PANS PRO RTLS 在架构上有何不同？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<p class="sd-card-text">LEAPS RTLS（上）和 PANS PRO RTLS（下）的系统架构比较：</p>
<p class="sd-card-text"><strong>LEAPS RTLS 系统架构</strong></p>
<img alt="../../_images/leaps-architect-solution.png" class="align-center" src="/docs-assets/zh-cn/_images/leaps-architect-solution.png">
<p class="sd-card-text"><strong>PANS PRO RTLS 系统架构</strong></p>
<img alt="../../_images/pans_pro-sub-system.png" class="align-center" src="/docs-assets/zh-cn/_images/pans_pro-sub-system.png">
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>如何实现两个设备之间尽可能长的距离？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<p class="sd-card-text">这与 <a class="reference external" href="https://www.omnicalculator.com/physics/fresnel-zone">菲涅尔区</a> 有一定关系。 很久以前，我们曾在大约 1.2 米至 1.5 米的高度进行过一些测量，结果发现信号在一定距离内丢失，然后在 5 至 10 米处恢复一段时间。 后来，我们发现了菲涅尔区域，并将高度增加到 2 米，从那以后，我们就再也没有观察到这个问题了。</p>
<p class="sd-card-text">对于大多数无线电讯号，你只需要注意第一菲涅尔区，但对于超宽带无线电讯号，似乎其他区域也很重要。</p>
<p class="sd-card-text">实际例子:</p>
<p class="sd-card-text">天线间距 = 100米</p>
<ul class="simple">
<li><p class="sd-card-text">频率 = 6.5GHz</p></li>
<li><p class="sd-card-text">第一区域半径 = 1.07米</p></li>
<li><p class="sd-card-text">第2区半径 = 1.52米</p></li>
<li><p class="sd-card-text">第三区半径 = 1.86米</p></li>
</ul>
<p class="sd-card-text">天线间距 = 200 米</p>
<ul class="simple">
<li><p class="sd-card-text">频率 = 6.5GHz</p></li>
<li><p class="sd-card-text">第一区半径 = 1.52 米</p></li>
<li><p class="sd-card-text">第2区半径 = 2.15米</p></li>
<li><p class="sd-card-text">第3区半径 = 2.63米</p></li>
</ul>
<p class="sd-card-text">在线计算器在这里 <a class="reference external" href="https://www.omnicalculator.com/physics/fresnel-zone">菲涅尔区计算器</a></p>
</div>
</details></div>


           </div>
