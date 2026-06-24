---
title: "PANS PRO Manager"
lang: ja
slug: "pans-pro-rtls/infrastructure/pans-pro-manager"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/infrastructure/pans-pro-manager/"
order: 99
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-manager">
<span id="id1"></span><h1>PANS PRO Manager</h1>
<p>このページでは、Androidデバイス向けに特別に設計されたPANS PRO Managerツールの使用に必要な手順について説明します。超広帯域デバイスの設定、セットアップ、管理をガイドし、PANS PRO RTLSシステム内でのシームレスな統合と運用を実現します。</p>
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>ネットワーク全体のデバイスの管理と可視化を可能にします。</p></li>
<li><p>デバイスとの通信はBLE経由で行われ、最大6つの同時接続をサポートすることで接続の信頼性を維持します。</p></li>
<li><p>2Dおよび3Dグリッドは、ネットワーク内のデバイスのリアルタイム位置更新と可視化を提供します。</p></li>
<li><p>その他の便利な機能としては、アンカー自動配置、BLE経由のファームウェアアップデート、ユーザー管理、位置情報の記録などがあります。</p></li>
</ul>
<hr class="docutils">
<div class="section" id="system-environment">
<h3>システム環境</h3>
<p><a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> は、Android API <strong>レベル24</strong> 以降のバージョンに基づいて開発されています。 <a class="reference external" href="https://apilevels.com">apilevels</a> を参照してください。</p>
<ul class="simple">
<li><p>Android の最小バージョン: Android 7 (API 24)</p></li>
<li><p>メモリ: 100 MB (空きディスク容量)</p></li>
<li><p>Bluetooth の最小バージョン: 4.2 (5.0 以上を推奨)</p></li>
<li><p>Android デバイスの推奨機種: Google Pixel 7 (同等の機種)</p></li>
</ul>
</div>
<div class="section" id="instruction">
<h3>手順</h3>
<p>は、<a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> アプリケーション (<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.panspro&amp;hl=en">Google Play</a> から入手可能) をダウンロードしてください。</p>
<blockquote>
<div><div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/panspro-manager-qr-code.png"><img alt="../../../_images/panspro-manager-qr-code.png" src="/docs-assets/ja/_images/panspro-manager-qr-code.png" style="width: 344.4px; height: 344.4px;"></a>
</div>
</div></blockquote>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>使用開始</h2>
<p><a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> を使用するには、ログインが必要です。ユーザー管理設定が有効になっている場合、デフォルトのユーザー名は <span class="red-text">admin</span>、パスワードは <span class="red-text">admin</span> です。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-login.jpg"><img alt="login1" src="/docs-assets/ja/_images/ppm-login.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-login-admin.jpg"><img alt="login2" src="/docs-assets/ja/_images/ppm-login-admin.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<div class="section" id="menu">
<h3>メニュー</h3>
<p>ユーザーによるカスタマイズオプションや主要機能にアクセスするには、メニューに移動してください。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-menu.jpg"><img alt="../../../_images/ppm-menu.jpg" class="align-center" src="/docs-assets/ja/_images/ppm-menu.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="devices-discovery">
<span id="id2"></span><h3>デバイスの検出</h3>
<p>ログインに成功すると、ホームページが <span class="red-text">left</span> 画像のように表示されます。そのエリアで利用可能なネットワークとデバイスを素早く検出するには、ホームページから <span class="red-text">Start Device Discovery</span> 機能を起動します。検出とスキャンのプロセスが終了するまで待ちます。検出されたネットワークとデバイスは <span class="red-text">right</span> 画像のように一覧表示されます。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-home-page.jpg"><img alt="discovery1" src="/docs-assets/ja/_images/ppm-home-page.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network1.jpg"><img alt="discovery2" src="/docs-assets/ja/_images/ppm-assign-network1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="network-configuration">
<h3>ネットワーク構成</h3>
<ul>
<li><p>ネットワークの作成</p>
<blockquote>
<div><ul class="simple">
<li><p>ネットワークを設定するデバイスを選択します。</p></li>
<li><p>ネットワーク名の入力を求めるダイアログボックスが表示されます。</p></li>
<li><p>希望するネットワーク名を入力してください。</p></li>
<li><p>アプリケーションがネットワークを作成します。</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-assign-network5.jpg"><img alt="nt1" src="/docs-assets/ja/_images/ppm-assign-network5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network6.jpg"><img alt="nt2" src="/docs-assets/ja/_images/ppm-assign-network6.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network7.jpg"><img alt="nt3" src="/docs-assets/ja/_images/ppm-assign-network7.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>複数のデバイスの割り当て</p>
<blockquote>
<div><ul class="simple">
<li><p>複数のデバイスをネットワークに追加するには、リスト内のデバイスを長押しします。</p></li>
<li><p>その後、アプリケーションは複数のデバイスを割り当てます。</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-assign-network8.jpg"><img alt="as1" src="/docs-assets/ja/_images/ppm-assign-network8.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network9.jpg"><img alt="as2" src="/docs-assets/ja/_images/ppm-assign-network9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network11.jpg"><img alt="as3" src="/docs-assets/ja/_images/ppm-assign-network11.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul class="simple">
<li><p>ネットワークが既に利用可能な場合は、それを選択してください。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-2.jpg"><img alt="nw1" src="/docs-assets/ja/_images/ppm-network-2.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-network-1.jpg"><img alt="nw2" src="/docs-assets/ja/_images/ppm-network-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>選択したデバイスの詳細情報を表示するには、デバイスをクリックします。詳細情報は下に表示されます。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-network-3.jpg"><img alt="../../../_images/ppm-network-3.jpg" class="align-center" src="/docs-assets/ja/_images/ppm-network-3.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
</li>
<li><p>デバイスをネットワークから削除するには、デバイスを右にスワイプします。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-assign-network13.jpg"><img alt="../../../_images/ppm-assign-network13.jpg" class="align-center" src="/docs-assets/ja/_images/ppm-assign-network13.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="device-configuration">
<h3>デバイス構成</h3>
<p>ノードを設定するには、あらかじめノードを特定のネットワークに割り当てる必要があります。</p>
<ul class="simple">
<li><p>指定されたノードを含むネットワークを選択すると、ネットワークの詳細が表示されます。</p></li>
<li><p>画面をスワイプしてスキャンし、アプリケーションからデバイスへの接続信号があることを確認してください。</p></li>
<li><p>鉛筆アイコンが表示されている場合は、それを選択してノードを設定できます。</p></li>
</ul>
<p>次の2つの例は設定を示しています。</p>
<ul class="simple">
<li><p>左側のデバイスは <span class="red-text">タグノード</span> を表し、 <span class="red-text">NORMAL UPDATE RATE</span> と <span class="red-text">STATIONARY UPDATE RATE</span> パラメータを設定できます。</p></li>
<li><p>右側のデバイスは <span class="red-text">アンカーノード</span> を表し、 <span class="red-text">POSITION (M)</span> パラメータを設定できます。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-device-configure-a.jpg"><img alt="device1" src="/docs-assets/ja/_images/ppm-device-configure-a.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-device-configure-b.jpg"><img alt="device2" src="/docs-assets/ja/_images/ppm-device-configure-b.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="network-visualization">
<h3>ネットワーク可視化</h3>
<p><a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> ツールの主な機能は、ネットワークの正確な位置を可視化できることです。次の例は、2D モードでのネットワーク表示を示しています。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-grib-2d-1.jpg"><img alt="2d1" src="/docs-assets/ja/_images/ppm-grib-2d-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-grib-2d-3.jpg"><img alt="2d2" src="/docs-assets/ja/_images/ppm-grib-2d-3.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p>ネットワークを 3D で表示するには、次の例のように 3D モードでのネットワーク表示を示します。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-grib-3d-0.jpg"><img alt="3d1" src="/docs-assets/ja/_images/ppm-grib-3d-0.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-grib-3d-1.jpg"><img alt="3d2" src="/docs-assets/ja/_images/ppm-grib-3d-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="position-logs">
<h3>位置ログ</h3>
<p>ネットワーク内の各デバイスの詳細と静的データを表示するには、次の例のようにデバイスとその位置を示します。</p>
<a class="reference internal image-reference" href="../../../_images/ppm-positiong-logs.jpg"><img alt="../../../_images/ppm-positiong-logs.jpg" class="align-center" src="/docs-assets/ja/_images/ppm-positiong-logs.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="auto-positioning">
<h3>オートポジショニング</h3>
<p>もう 1 つの重要な機能である自動配置は、ユーザーがネットワークを自動で迅速に初期化するのに役立ちます。</p>
<p><span class="red-text">自動配置</span> にアクセスします。アプリケーション内で <span class="red-text">オプションメニュー</span> （縦に 3 つの点）をタップします。</p>
<ul class="simple">
<li><p>次の例は、自動配置プロセス完了後の結果を示しています。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-menu.jpg"><img alt="am1" src="/docs-assets/ja/_images/ppm-network-menu.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-1.jpg"><img alt="am2" src="/docs-assets/ja/_images/ppm-auto-positioning-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-2.jpg"><img alt="am3" src="/docs-assets/ja/_images/ppm-auto-positioning-2.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul class="simple">
<li><p>完了するまでお待ちください。ノードの位置情報が表示されます。<span class="red-text">SAVE</span> を押して結果を保存します。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-3.jpg"><img alt="au1" src="/docs-assets/ja/_images/ppm-auto-positioning-3.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-4.jpg"><img alt="au2" src="/docs-assets/ja/_images/ppm-auto-positioning-4.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-5.jpg"><img alt="au3" src="/docs-assets/ja/_images/ppm-auto-positioning-5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="firmware-update-over-ble">
<span id="id3"></span><h3>BLE経由のファームウェアアップデート</h3>
<p>ファームウェアステータスにアクセスします。 アプリケーション内の <span class="red-text">オプションメニュー</span> をタップします。 (<em>縦に3つの点で表示</em>) をタップします。 <span class="red-text">Firmware status</span> オプションを探し、選択します。</p>
<p>アップデートするデバイスを選択します。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-menu.jpg"><img alt="fw1" src="/docs-assets/ja/_images/ppm-network-menu.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-firmware-update.jpg"><img alt="fw2" src="/docs-assets/ja/_images/ppm-firmware-update.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="troubleshooting">
<h2>トラブルシューティング</h2>
<ul class="simple">
<li><p>BLE接続が安定していること、およびデバイスが通信範囲内にあることを常に確認してください。</p></li>
</ul>
</div>
</div>


           </div>
