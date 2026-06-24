---
title: "システム要件"
lang: ja
slug: "udk/udk-start/system-requirements"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/system-requirements/"
order: 33
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="id1"></span><h1>システム要件</h1>
<hr class="docutils">
<div class="section" id="hardware">
<h2>ハードウェア</h2>
<p>次の表は、今後の各セクションのデモのセットアップに必要なハードウェアのリストです。一部のアイテムはオプションであり、すべてのデモに必須ではないことをご了承ください。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>アイテム</strong></p></th>
<th class="head"><p><strong>数量</strong></p></th>
<th class="head"><p><strong>必要量</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UDKキット</p></td>
<td><p>1+</p></td>
<td><p>必須</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/udk_kit_box.png"><img alt="../../../_images/udk_kit_box.png" class="align-right" src="/docs-assets/ja/_images/udk_kit_box.png" style="width: 167.4px; height: 98.1px;"></a>
</div></blockquote>
<p>各キットには、LC13デバイス1台（AoAアンテナ付き）、LC14デバイス5台（非AoAアンテナ付き）、USBタイプCデータケーブル2本が含まれます。</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">USB-C</div>
<div class="line">Data</div>
<div class="line">ケーブル</div>
</div>
</td>
<td><p>2+ (デモにより異なります)</p></td>
<td><p>オプション</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/usb-c-data-cable.png"><img alt="../../../_images/usb-c-data-cable.png" class="align-right" src="/docs-assets/ja/_images/usb-c-data-cable.png" style="width: 172.0px; height: 89.0px;"></a>
</div></blockquote>
<p>UDKデバイスへの電源供給、PCとのデータ交換、ファームウェアの再フラッシュ。注: USB-C データケーブル 2 本は、UDK の箱の中に入っています。ボードの再フラッシュはオプションです。デバイスは製品からプログラムされます。</p>
</td>
</tr>
<tr class="row-even"><td><p>バッテリー</p></td>
<td><p>6+ (デモにより異なります)</p></td>
<td><p>オプション</p></td>
<td><div class="line-block">
<div class="line">USB-Cケーブルを使用せずにUDKデバイスに給電する場合。</div>
<div class="line">推奨：</div>
</div>
<blockquote>
<div><ul class="simple">
<li><p>Fenix RCR123A (3.7V)</p></li>
<li><p>Keeppower RCR123A 3.7V (860 mAh &amp; 付属の充電器)</p></li>
</ul>
<p><a class="reference internal" href="../../../_images/battery-rcr123a.png"><img alt="Fenix" src="/docs-assets/ja/_images/battery-rcr123a.png" style="width: 150.25px; height: 149.0px;"></a>  <a class="reference internal" href="../../../_images/keeppower-rcr123a.jpg"><img alt="keeppower" src="/docs-assets/ja/_images/keeppower-rcr123a.jpg" style="width: 144.0px; height: 144.0px;"></a></p>
</div></blockquote>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">クランプまたは</div>
<div class="line">三脚</div>
<div class="line">カメラ</div>
<div class="line">マウント</div>
</div>
</td>
<td><p>4+</p></td>
<td><p>おすすめだ</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/super-clamp-mount.jpg"><img alt="../../../_images/super-clamp-mount.jpg" class="align-right" src="/docs-assets/ja/_images/super-clamp-mount.jpg" style="width: 160.0px; height: 160.0px;"></a>
</div></blockquote>
<div class="line-block">
<div class="line">RTLSデモのアンカー機器取り付け用。</div>
<div class="line">推奨： <a class="reference external" href="https://www.smallrig.com/clamp-mount-v1-w-ball-head-mount-and-coolclamp-1124.html">Super Clamp Mount</a></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">Phone</div>
<div class="line">Device <a class="footnote-reference brackets" href="#note" id="id2">1</a></div>
<div class="line"><br></div>
</div>
</td>
<td><p>1</p></td>
<td><p>おすすめだ</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/samsung-a7.png"><img alt="../../../_images/samsung-a7.png" class="align-right" src="/docs-assets/ja/_images/samsung-a7.png" style="width: 124.75px; height: 124.75px;"></a>
</div></blockquote>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> （BluetoothまたはMQTTを使用してデバイスの設定やネットワークの可視化に使用できるアプリケーション）の実行に使用します。</p>
<ul class="simple">
<li><p><cite>Android OSバージョン6.0以上が必要。</cite></p></li>
<li><p>` iOS バージョン 15 以降が必要。`</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">iOS</div>
<div class="line">デバイス</div>
</div>
</td>
<td><p>1</p></td>
<td><p>オプション</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/iso-device.jpeg"><img alt="../../../_images/iso-device.jpeg" class="align-right" src="/docs-assets/ja/_images/iso-device.jpeg" style="width: 120.0px; height: 120.0px;"></a>
</div></blockquote>
<p>Nearby Interactionアクセサリ(UDK)と通信し、距離や方向を表示するiOSアプリケーションである <a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo の近くのインタラクション</span></a> アプリケーションを実行するために使用します。U1チップを搭載したiPhoneとiOSバージョン16以降が必要です。</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">デスクトップ</div>
<div class="line">デバイス</div>
</div>
</td>
<td><p>1</p></td>
<td><p>オプション</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/desktop-device.png"><img alt="../../../_images/desktop-device.png" class="align-right" src="/docs-assets/ja/_images/desktop-device.png" style="width: 111.0px; height: 97.80000000000001px;"></a>
</div></blockquote>
<p>様々な用途に使用可能：ウェブサーバアプリケーション（<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a>、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>、MQTT Broker）を含む VirtualBox イメージを実行するためのもので、Windows、macOS、Linux オペレーティングシステムに対応しています。そのほか、USB/UART/Bluetoothを使用したデバイスのアップデート、USB/UARTを使用したデバイスとの通信、DAPLinkが統合されたUDKデバイスの再プログラミング、UDK SDKを使用したカスタムアプリケーションの開発にも使用できます。</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">ラズベリー</div>
<div class="line">Pi 3B</div>
<div class="line">または新しい</div>
</div>
</td>
<td><p>1</p></td>
<td><p>オプション</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ras-pi-device.jpg"><img alt="../../../_images/ras-pi-device.jpg" class="align-right" src="/docs-assets/ja/_images/ras-pi-device.jpg" style="width: 100.0px; height: 100.0px;"></a>
</div></blockquote>
<p>LEAPS Gateway、LEAPS Server、LEAPS Center、MQTT Broker などのウェブサーバアプリケーションを備えたゲートウェイの迅速なセットアップに使用します。そのほか、USB/UART/Bluetoothを使用したデバイスのアップデート、USB/UARTを使用したデバイスとの通信、DAPLinkが統合されたUDKデバイスの再プログラミングにも使用できます。</p>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="software">
<h2>ソフトウェア</h2>
<p>以下は、デモンストレーション目的および UDK での開発に不可欠なすべてのソフトウェア アプリケーションおよびツールのリストです。</p>
<hr class="docutils">
<div class="section" id="leaps-applications-and-tools">
<h3>LEAPS アプリケーションおよびツール</h3>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>アイテム</p></th>
<th class="head"><p>アイテム バージョン</p></th>
<th class="head"><p>バージョン 必要性</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>LEAPS Ultra-Wideband Sus-Systemファームウェア。UDKデバイスには、製造時からLEAPS UWBSがプリロードされています。ファームウェアが必要なのは、ファームウェアのアップデートまたはデバイスのリカバリーの場合のみです。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>BluetoothまたはMQTTを使用してデバイスの設定やネットワークの可視化に使用できるAndroidアプリケーション。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>LEAPS UWBSとLEAPS Server、ひいてはTCP/IPネットワーク間のゲートウェイとして機能するLinuxデーモンアプリケーション。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>UWBネットワークの中央データハブとして機能し、MQTTブローカーを介して外部システムとの間でデータの集約と送信を行うLinuxデーモンアプリケーション。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>UWB ネットワークの設定と可視化のための Web アプリケーション。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/udk/development-guide/udk-sdk-getting-started#udksdk"><span class="std std-ref">SDKで起動</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>Zephyr RTOSをベースとしたUDK SDK（ソフトウェア開発キット）は、カスタムUltra-Widebandアプリケーションの評価および開発に使用できます。</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="partner-applications-and-tools">
<h3>パートナー・アプリケーションおよびツール</h3>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>アイテム</p></th>
<th class="head"><p>アイテム バージョン</p></th>
<th class="head"><p>バージョン 必要性</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB レンジングおよび AoA デモ アプリ</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>Qorvo FiRa対応デバイスの機能をデモするQorvo®デスクトップアプリケーション。デスクトップ上でデバイスを設定し、双方向測距、到達角、位置データを可視化できます。このアプリケーションはWindows、macOS、Linuxオペレーティングシステムをサポートしています。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo の近くのインタラクション</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>Qorvo® Nearby Interaction および Qorvo® NI Background アプリケーションは、Apple Nearby Interaction フレームワークを使用して、Qorvo ウルトラワイドバンド技術を簡単に評価することができます。アプリケーションはApp Storeで入手できます。</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="third-party-applications-and-tools">
<h3>サードパーティのアプリケーションとツール</h3>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>アイテム</p></th>
<th class="head"><p>アイテム バージョン</p></th>
<th class="head"><p>バージョン 必要性</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://mosquitto.org/download/">モスキートMQTTブローカー</a></p></td>
<td><p>2.0.11</p></td>
<td><p>オプション</p></td>
<td><p>Mosquitto はMQTT v5.0/v3.1.1/v3.1ブローカーです。Mosquittoの推奨バージョンは2.0.11です。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<dl class="footnote brackets">
<dt class="label" id="note"><span class="brackets"><a class="fn-backref" href="#id2">1</a></span></dt>
<dd><p>テストしたデバイス SamSung A7、Samsung Galaxy A21S、Samsung Galaxy A22</p>
</dd>
</dl>
</div>
</div>
</div>


           </div>
