---
title: "LEAPS RTLS"
lang: zh
slug: "udk/specification/system-architecture-overview"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/specification/system-architecture-overview/"
order: 53
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-rtls">
<h1>LEAPS RTLS</h1>
<p>节将提供对 LEAPS RTLS 系统更详细的了解，并概述其具体组件，这些组件将在下面的小节中进一步阐述。</p>
<hr class="docutils">
<div class="section" id="leaps-rtls-architecture">
<h2>LEAPS RTLS 架构</h2>
<p>下图概述了 LEAPS RTLS 系统的主要概念。 后续章节将提供每个组件的详细信息。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>The firmware for the UDK contains the LEAPS UWB Sub-System as well as Qorvo FiRa UWB Sub-System.</p>
</div>
<div class="figure align-default" id="id1">
<img alt="LEAPS RTLS 子系统" class="with-shadow float-center" src="/docs-assets/zh-cn/_images/leaps-architect-solution-for-udk.png">
<p class="caption"><span class="caption-text">LEAPS RTLS 架构。</span></p>
</div>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leaps-uwbs.png"><img alt="../../../_images/leaps-uwbs.png" class="align-right" src="/docs-assets/zh-cn/_images/leaps-uwbs.png" style="width: 91.80000000000001px; height: 75.8px;"></a>
</div>
<div class="section" id="leaps-uwbs">
<h2>LEAPS UWBS</h2>
<p>LEAPS UWBS 是一个完全嵌入式的 UWB 子系统，涵盖了广泛的使用案例。 一个 UWB 子系统可配置为不同的模式和配置文件。 UWBS 可以作为锚（Anchor）或标签（Tag）运行。 网关是 UWB 网络与上层之间的关梁。 网络配置文件具有高容量和低功耗的完全可扩展性。</p>
<ul class="simple">
<li><p>多功能性使系统需求, 成本, 部署时间和维护复杂性之间的平衡变得容易。 应用范围从简单的距离接近到无限接收器的高速跟踪或导航。</p></li>
<li><p>它整合了先进的UWBMAC，允许基础设施设备自适应集群, 空中时间重用, 时隙分配等。 可扩展的, 经过验证的碰撞检测, 碰撞避免和碰撞解决功能，使系统能够在复杂的环境中稳健运行。</p></li>
<li><p>支持的测量技术包括 TWR, DL-TDoA 和 UL-TDoA. 集成的定位引擎允许设备在导航模式下使用DL-TDoA或TWR独立运行。</p></li>
<li><p>卓越的电源管理为TWR和TDoA模式提供了较长的电池寿命。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsapi.png"><img alt="../../../_images/leapsapi.png" class="align-right" src="/docs-assets/zh-cn/_images/leapsapi.png" style="width: 87.3px; height: 144.6px;"></a>
</div>
<div class="section" id="leaps-api">
<h2>LEAPS API</h2>
<ul class="simple">
<li><p>LEAPS RTLS 软件栈提供应用程序接口，可轻松配置设备以适应定制应用. 用户可根据自己的特定需求，灵活地定制系统。</p></li>
<li><p>该 API 采用二进制类型-长度-值（TLV）帧格式，通过 UART, USB, SPI 和 BLE 接口连接外部设备。 当使用数据集中化时，高层应用程序可使用 JSON 通过 MQTT 进行通信。</p></li>
<li><p>通过 UART, USB 和 BLE 接口支持 API 命令行接口，并提供更友好, 更易读的格式。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsmanager.png"><img alt="../../../_images/leapsmanager.png" class="align-right" src="/docs-assets/zh-cn/_images/leapsmanager.png" style="width: 101.7px; height: 119.1px;"></a>
</div>
<div class="section" id="leaps-manager">
<h2>LEAPS Manager</h2>
<p>LEAPS Manager is a mobile application that provides device discovery, device configuration, network configuration, network management and location visualization.</p>
<ul class="simple">
<li><p>通过演示向导，可以方便快捷地使用预定义的演示设置来配置套件。</p></li>
<li><p>2D和3D网格提供实时位置更新，并将网络中的设备可视化。</p></li>
<li><p>与设备的通讯是通过 BLE 完成的，支持多达 6 个并发连接，以保持连接的可靠性。</p></li>
<li><p>使用数据集中时，可通过 MQTT 与 LEAPS Server通信，以管理和可视化整个网络的设备。</p></li>
<li><p>其他有用的功能还包括设备管理, 通过 BLE 进行固件更新, 锚点自动定位, 日志记录和调试控制台。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsgateway.png"><img alt="../../../_images/leapsgateway.png" class="align-right" src="/docs-assets/zh-cn/_images/leapsgateway.png" style="width: 90.3px; height: 63.599999999999994px;"></a>
</div>
<div class="section" id="leaps-gateway">
<h2>LEAPS Gateway</h2>
<p>LEAPS Gateway是UWB子系统与TCP/IP网络之间的关梁。</p>
<ul class="simple">
<li><p>LEAPS Gateway一侧通过通用LEAPS API、SPI或USB与LEAPS UWBS通信，另一侧通过TCP/IP与LEAPS Server通信。</p></li>
<li><p>根据LEAPS UWB网络配置文件，它提供了一个媒介，用于将锚点和标签的上行和下行位置及遥测数据，传输到LeapsServer，或从Leaps Server传输到锚点和标签。</p></li>
<li><p>与 UWBS 的互连，是通过专用LEAPS Gateway嵌入式装置上的 SPI 来完成的。 当通过 USB 与LEAPS UWBS互联时，例如 UDK 设备，LEAPS Gateway会以守护进程服务的方式运行在 Linux 平台上。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsserver.png"><img alt="../../../_images/leapsserver.png" class="align-right" src="/docs-assets/zh-cn/_images/leapsserver.png" style="width: 77.1px; height: 63.599999999999994px;"></a>
</div>
<div class="section" id="leaps-server">
<h2>LEAPS Server</h2>
<p>LEAPS Server是UWB网络的中央数据枢纽。 它通过MQTT Broker将所有LEAPS Gateway设备与世界互联。</p>
<ul class="simple">
<li><p>作为上行数据集中器, 下行数据路由器, 数据处理器, 定位引擎, 设备管理, 设备访问控制，并确保服务质量。</p></li>
<li><p>通过连接器与世界沟通。 目前支持的连接器是 MQTT，其中包括对 AWS 的支持。</p></li>
<li><p>在 Linux 平台上，LEAPS Server是作为一个守护进程服务运行的。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapscenter.png"><img alt="../../../_images/leapscenter.png" class="align-right" src="/docs-assets/zh-cn/_images/leapscenter.png" style="width: 85.5px; height: 121.0px;"></a>
</div>
<div class="section" id="leaps-center">
<h2>LEAPS Center</h2>
<p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 是一个网络应用程序，提供设备管理, 网络管理以及整个网络的位置和遥测数据的可视化。</p>
<ul class="simple">
<li><p>2D和3D网格提供实时位置更新，并将网络中的设备可视化。</p></li>
<li><p>其他有用的功能包括用户管理, 区域管理, 区域历史, 平面图管理, 位置历史和位置热图。</p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 通过 MQTT 与 LEAPS Server通信. 它在 Linux 或 Windows 平台上以服务形式运行。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsbroker.png"><img alt="../../../_images/leapsbroker.png" class="align-right" src="/docs-assets/zh-cn/_images/leapsbroker.png" style="width: 93.3px; height: 51.9px;"></a>
</div>
<div class="section" id="mqtt-broker">
<h2>MQTT代理商</h2>
<p>MQTT 代理商是一个服务器，它接收来自客户端的所有信息，然后将信息路由到适当的目标客户端。 MQTT 客户端是运行 MQTT 库并通过网络连接到 MQTT 代理的任何设备（从微控制器到完全成熟的服务器）。</p>
<hr class="docutils">
</div>
</div>


           </div>
