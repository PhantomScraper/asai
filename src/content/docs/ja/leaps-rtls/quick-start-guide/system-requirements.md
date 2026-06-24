---
title: "システム要件"
lang: ja
slug: "leaps-rtls/quick-start-guide/system-requirements"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/quick-start-guide/system-requirements/"
order: 60
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="leaps-qsg-system-requirements"></span><h1>システム要件</h1>
<p>以下のセクションでは <a class="reference internal" href="/docs/ja/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> のRTLS（リアルタイムロケーションシステム）デモを始める前に必要なソフトウェアとハードウェアの詳細を説明します。一部の項目はオプションであり、全てのデモで必須ではないことをご了承ください。</p>
<div class="section" id="hardware">
<h2>ハードウェア</h2>
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
<tr class="row-even"><td><p>UWBデバイス</p></td>
<td><p>5+</p></td>
<td><p>必須</p></td>
<td><ul class="simple">
<li><p>少なくとも3つのアンカーノード</p></li>
<li><p>少なくとも1つのタグノード</p></li>
<li><p>ゲートウェイノード</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">マイクロUSB</div>
<div class="line">ケーブル</div>
</div>
</td>
<td><p>6+</p></td>
<td><p>オプション</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/micro-usb.webp"><img alt="../../../_images/micro-usb.webp" class="align-right" src="/docs-assets/ja/_images/micro-usb.webp" style="width: 119.92px; height: 119.92px;"></a>
</div></blockquote>
<p>デバイスへの電源供給、PCとのデータ交換、ファームウェアの再フラッシュを行います。ボードの再フラッシュはオプションです。</p>
</td>
</tr>
<tr class="row-even"><td><p>バッテリー</p></td>
<td><p>6+</p></td>
<td><p>オプション</p></td>
<td><div class="line-block">
<div class="line">マイクロUSBケーブルを使用せずにUWBデバイスに電力を供給する。</div>
<div class="line">推奨：</div>
</div>
<blockquote>
<div><ul class="simple">
<li><p>Fenix RCR123A (3.7V)</p></li>
<li><p>Keeppower RCR123A 3.7V (860 mAh &amp; 付属の充電器)</p></li>
</ul>
<p><a class="reference internal" href="../../../_images/battery-rcr123a.png"><img alt="Fenix" src="/docs-assets/ja/_images/battery-rcr123a.png" style="width: 120.2px; height: 119.2px;"></a>  <a class="reference internal" href="../../../_images/keeppower-rcr123a.jpg"><img alt="keeppower" src="/docs-assets/ja/_images/keeppower-rcr123a.jpg" style="width: 120.0px; height: 120.0px;"></a></p>
</div></blockquote>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Phone</div>
<div class="line">デバイス</div>
<div class="line"><br></div>
</div>
</td>
<td><p>1</p></td>
<td><p>おすすめだ</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/samsung-a7.png"><img alt="../../../_images/samsung-a7.png" class="align-right" src="/docs-assets/ja/_images/samsung-a7.png" style="width: 124.75px; height: 124.75px;"></a>
</div></blockquote>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> （BluetoothまたはMQTTを使用してデバイスを設定し、ネットワークを可視化するために使用できるアプリケーション）を実行するために使用します。</p>
<ul class="simple">
<li><p><cite>Android OSバージョン6.0以上が必要です。</cite></p></li>
<li><p>` iOS バージョン 15 以降が必要。`</p></li>
</ul>
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
<p>Windows、macOS、Linux オペレーティングシステムをサポートし、ウェブサーバアプリケーション（<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a>、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>、MQTT Broker）を含む VirtualBox イメージを実行する。そのほか、USB/UART/Bluetoothを使用したデバイスのアップデート、USB/UARTを使用したデバイスとの通信、DAPLinkが統合されたUDKデバイスの再プログラミング、UDK SDKを使用したカスタムアプリケーションの開発にも使用できます。</p>
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
<p>LEAPS Server、LEAPS Center、MQTTブローカーを含むウェブサーバーアプリケーションとゲートウェイの迅速なセットアップに使用します。また、USB/UART/Bluetoothを使用したデバイスのアップデートにも使用できます。</p>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="software">
<h2>ソフトウェア</h2>
<p>以下は、デモに必要なソフトウェア・アプリケーションとツールの一覧です。</p>
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
<td><p>LEAPS Ultra-Wideband Sus-Systemファームウェア。UDKデバイスには、製造時からLEAPS UWBSがプリロードされています。ファームウェアは、ファームウェアのアップデートまたはデバイスのリカバリーの場合にのみ必要です。</p></td>
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
<td><p>UWB ネットワークの中央データハブとして機能する Linux デーモンアプリケーションで、MQTT Broker を介して外部システムとの間でデータの集約と送信を行います。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a></p></td>
<td><p>-</p></td>
<td><p>オプション</p></td>
<td><p>UWB ネットワークの設定と可視化のための Web アプリケーション。</p></td>
</tr>
</tbody>
</table>
</div>
</div>


           </div>
