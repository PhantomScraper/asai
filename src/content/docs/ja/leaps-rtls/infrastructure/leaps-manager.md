---
title: "LEAPS Manager"
lang: ja
slug: "leaps-rtls/infrastructure/leaps-manager"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/infrastructure/leaps-manager/"
order: 69
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-manager">
<span id="leapsmanager"></span><h1>LEAPS Manager</h1>
<p><a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> は、UDK (<a class="reference external" href="https://docs.leapslabs.com/UDK/">All-in-One Ultra-Wideband Development Kit</a>) および LEAPS RTLS (高度な Ultra-Wideband Real-Time Location System) にデバイス検出、デバイス構成、ネットワーク構成、ネットワーク管理、および位置情報の可視化を提供する必須ツールです。</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>デモウィザードにより、キットの事前定義されたデモセットアップを簡単かつ高速に設定できます。</p></li>
<li><p>2Dと3Dのグリッドはリアルタイムで位置を更新し、ネットワーク内のデバイスを視覚化します。</p></li>
<li><p>デバイスとの通信はBLE経由で行われ、最大6つの同時接続をサポートすることで接続の信頼性を維持します。</p></li>
<li><p>データ集中化を使用する場合、MQTT経由で <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> と通信できるため、ネットワーク全体のデバイスの管理と可視化が可能になります。</p></li>
<li><p>その他の便利な機能には、ユーザー管理、BLE経由でのファームウェア更新、アンカー自動位置決め、位置ロギング、デバッグコンソールがあります。</p></li>
</ul>
<hr class="docutils">
<div class="section" id="system-environment">
<h3>システム環境</h3>
<p><a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> は、Android APIレベル24以降に基づいて開発されています。詳細は <a class="reference external" href="https://apilevels.com">apilevels</a> を参照してください。</p>
<ul class="simple">
<li><p>最小Androidバージョン：Android 7（API 24）</p></li>
<li><p>最小メモリ：100MB（ディスク空き容量）</p></li>
<li><p>Bluetooth の最小バージョン: 4.2 (推奨: 5.0 以上)</p></li>
<li><p>Android デバイスの推奨: Google Pixel 7 (同等のデバイス)</p></li>
</ul>
<p>非推奨デバイス: <strong>Samsung Galaxy Tab A8</strong> については、既知の問題リストをご覧ください:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/f/nordic-q-a/88557/samsung-galaxy-tab-a8-does-not-work-with-nrf-mesh-android-app">デバイスが NRF メッシュ Android アプリで動作しない</a></p></li>
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/f/nordic-q-a/89631/galaxy-tab-a8-sm-x200-connection-issues-with-gatt-error-133-after-multiple-connecting-failures">複数の接続失敗後に GATT エラー 133 で接続が失敗する</a></p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="instruction">
<h3>手順</h3>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
アンドロイド</label><div class="sd-tab-content docutils">
<p>開始するには、<a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> アプリケーションをダウンロードしてください（<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.leaps&amp;hl=en_GB&amp;gl=US">Google Play</a> から入手可能）</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-qr-code.png"><img alt="../../../_images/leaps-manager-qr-code.png" src="/docs-assets/ja/_images/leaps-manager-qr-code.png" style="width: 337.5px; height: 337.5px;"></a>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
iOS</label><div class="sd-tab-content docutils">
<p>開始するには、<a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> アプリケーションをダウンロードしてください（<a class="reference external" href="https://apps.apple.com/vn/app/leaps-manager/id6737454926">App Store</a> から入手可能）</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-ios-qr-code.png"><img alt="../../../_images/leaps-manager-ios-qr-code.png" src="/docs-assets/ja/_images/leaps-manager-ios-qr-code.png" style="width: 344.09999999999997px; height: 344.09999999999997px;"></a>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="getting-started">
<h2>開始方法</h2>
<p>デフォルトでは、ユーザー管理が有効になっている場合、ユーザー名は <span class="red-text">admin</span>、パスワードは <span class="red-text">admin</span> です。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-android-login.jpg"><img alt="../../../_images/leaps-manager-android-login.jpg" src="/docs-assets/ja/_images/leaps-manager-android-login.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div>
<div class="section" id="network-configuration">
<h3>ネットワーク設定</h3>
<p>アプリを開き、割り当てられているネットワークがない場合は <span class="red-text">デバイス検出を開始</span> を選択します。既にネットワークが存在する場合は、<span class="red-text">既存のネットワーク</span> に移動します。</p>
<p>ここで、アプリケーションは利用可能なすべてのネットワークとデバイスの検出とスキャンを開始します。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-home.jpg"><img alt="lm1" src="/docs-assets/ja/_images/leaps-manager-android-home.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-tab-create-network.jpg"><img alt="lm2" src="/docs-assets/ja/_images/leaps-manager-android-tab-create-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-create-network.jpg"><img alt="lm3" src="/docs-assets/ja/_images/leaps-manager-android-create-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p>検出とスキャンのプロセスが完了するまでお待ちください。利用可能なネットワークが割り当てられていない場合は、ネットワークを指定できます。デバイスを選択して作成し、指定したネットワークに割り当てることができます。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-assign-devices.jpg"><img alt="lm4" src="/docs-assets/ja/_images/leaps-manager-android-assign-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-assigning-devices.jpg"><img alt="lm5" src="/docs-assets/ja/_images/leaps-manager-android-assigning-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-created-network.jpg"><img alt="lm6" src="/docs-assets/ja/_images/leaps-manager-android-created-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="node-configuration">
<h3>ノード設定</h3>
<p>ノードを設定するには、事前にノードを特定のネットワークに割り当てる必要があります。指定したノードを含むネットワークを選択すると、ネットワークの詳細が表示されます。</p>
<p>画面をスワイプしてスキャンし、アプリケーションからデバイスへの接続信号があることを確認してください。</p>
<p>鉛筆アイコンが表示されている場合は、それを選択してノードを設定できます。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-leaps-demo-network.jpg"><img alt="lm7" src="/docs-assets/ja/_images/leaps-manager-android-leaps-demo-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-edit-anchor.jpg"><img alt="lm8" src="/docs-assets/ja/_images/leaps-manager-android-edit-anchor.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-edit-tag.jpg"><img alt="lm9" src="/docs-assets/ja/_images/leaps-manager-android-edit-tag.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="demo-selector">
<h3>デモセレクター</h3>
<p>デモセレクターに移動し、設定するデモを選択します:</p>
<ul class="simple">
<li><p>と iPhone の周辺での対話デモ</p></li>
<li><p>到着角度(AoA)を使ったデバイスの位置特定デモ</p></li>
<li><p>インフラレス近接デモ</p></li>
<li><p>ダウンリンク TDoA RTLS デモ</p></li>
<li><p>高速ダウンリンク TDoA RTLS デモ</p></li>
<li><p>TWR RTLS およびデータテレメトリ デモ</p></li>
</ul>
<p>例: TWR RTLS およびデータテレメトリ デモ</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-demo-selector.jpg"><img alt="lm10" src="/docs-assets/ja/_images/leaps-manager-android-demo-selector.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-twr-rtls.jpg"><img alt="lm11" src="/docs-assets/ja/_images/leaps-manager-android-twr-rtls.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-config-auto.jpg"><img alt="lm12" src="/docs-assets/ja/_images/leaps-manager-android-config-auto.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning.jpg"><img alt="lm13" src="/docs-assets/ja/_images/leaps-manager-android-auto-positioning.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning-measuring.jpg"><img alt="lm14" src="/docs-assets/ja/_images/leaps-manager-android-auto-positioning-measuring.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning-save.jpg"><img alt="lm15" src="/docs-assets/ja/_images/leaps-manager-android-auto-positioning-save.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-leaps-demo-network.jpg"><img alt="lm16" src="/docs-assets/ja/_images/leaps-manager-android-leaps-demo-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-network-on-2D-grid.jpg"><img alt="lm17" src="/docs-assets/ja/_images/leaps-manager-android-network-on-2D-grid.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="configuration-information-for-10db-lna-pa-settings">
<h3>+10dB、LNA/PA 設定に関する設定情報</h3>
<p>デモでは、+10dB 低雑音増幅器 (LNA) / パワーアンプ (PA) の設定に関する詳細情報を確認できます。この設定は、特定のアプリケーションに合わせて信号強度と品質を最適化するように設計されています。</p>
<p>設定:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">FCC/ETSI</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">5</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ETSI+10</span> <span class="pre">dB</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">5</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">FCC/ETSI</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">9</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ETSI+10</span> <span class="pre">dB</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">9</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">Japan</span> <span class="pre">ARIB</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">9</span></code></p></li>
</ul>
<p>デモ版で利用可能：</p>
<ul class="simple">
<li><p>インフラレス近接デモ</p></li>
<li><p>ダウンリンク TDoA RTLS デモ</p></li>
<li><p>高速ダウンリンク TDoA RTLS デモ</p></li>
<li><p>TWR RTLS およびデータテレメトリ デモ</p></li>
</ul>
<p>設定方法：</p>
<ol class="arabic simple">
<li><p>デモ画面の右上に移動します。</p></li>
<li><p>3つの点のアイコン（メニューアイコン）をクリックします。</p></li>
<li><p>対応する設定オプションを選択して、設定を表示または選択します。</p></li>
</ol>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-fcc-etsi-ch9.jpg"><img alt="lm18" src="/docs-assets/ja/_images/leaps-manager-android-fcc-etsi-ch9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-10dB-lna-pa-settings.jpg"><img alt="lm19" src="/docs-assets/ja/_images/leaps-manager-android-10dB-lna-pa-settings.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="firmware-update-over-ble">
<span id="leaps-manager-fup-over-ble"></span><h3>BLE経由のファームウェア更新</h3>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-2" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Default Package</label><div class="sd-tab-content docutils">
<p><span class="red-text">デモセレクター</span> に移動します。また、作成したネットワークに移動して、ネットワーク内のデバイスを更新することもできます。</p>
<p>ファームウェアステータスにアクセスします。 アプリケーション内の <span class="red-text">オプションメニュー</span> をタップします。 (<em>縦に3つの点で表示</em>) をタップします。 <span class="red-text">Firmware status</span> オプションを探し、選択します。</p>
<p>更新するデバイスを選択します。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-network.jpg"><img alt="lm20" src="/docs-assets/ja/_images/leaps-manager-android-firmware-update-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-demo-selector-firmware-update.jpg"><img alt="lm21" src="/docs-assets/ja/_images/leaps-manager-android-demo-selector-firmware-update.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-status.jpg"><img alt="lm22" src="/docs-assets/ja/_images/leaps-manager-android-firmware-status.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>BLE経由のファームウェアの速度は約1.6kBpsです。</p>
</div>
<p>アプリは、更新の進行状況を示す視覚的なインジケーターまたは進行状況バーを提供します。アップデートプロセスが完了するまで、辛抱強く待ってください。</p>
<p>更新が完了すると、<span class="red-text">ステータスが完了</span> と表示されます。さらに、デバイスは更新が成功したことを示すビープ音を2回鳴らします。ボードはプロセスの一環として自動的にリセットされます。</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-eldr.jpg"><img alt="lm23" src="/docs-assets/ja/_images/leaps-manager-android-firmware-update-eldr.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-main.jpg"><img alt="lm24" src="/docs-assets/ja/_images/leaps-manager-android-firmware-update-main.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-completed.jpg"><img alt="lm25" src="/docs-assets/ja/_images/leaps-manager-android-firmware-update-completed.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Selectable Package</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Download the <a class="reference external" href="https://drive.google.com/file/d/12XES6qiCJDZ16JSx841OqcZfqSdy4OIJ/view">LEAPS-UWBS-Firmware-v1.1.0-package.zip</a> file to your PC. Use a program like WinZip or 7-Zip to extract the contents of the downloaded file.</p></li>
<li><p>Open the LM and navigate to the <span class="red-text">Demo Selector</span>. Additionally, you can navigate to the created network to update the devices in the network. Access firmware status. Tap the <span class="red-text">options menu</span> (<em>represented as three vertical dots</em>) within the application. Look for the <span class="red-text">Firmware status</span> option and select it.</p></li>
<li><p>In the top-right corner, click button to select the firmware Package.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-home-page.jpg"><img alt="lm37" src="/docs-assets/ja/_images/leaps-manager-home-page.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-package.jpg"><img alt="lm38" src="/docs-assets/ja/_images/leaps-manager-selecting-package.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-package_001.jpg"><img alt="lm39" src="/docs-assets/ja/_images/leaps-manager-selecting-package_001.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</li>
<li><p>After successfully selecting the package, choose the devices to update.</p>
<blockquote>
<div><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-devices.jpg"><img alt="lm40" src="/docs-assets/ja/_images/leaps-manager-selecting-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p>
</div></blockquote>
</li>
</ol>
<p>アプリは、更新の進行状況を示す視覚的なインジケーターまたは進行状況バーを提供します。アップデートプロセスが完了するまで、辛抱強く待ってください。</p>
<p>更新が完了すると、<span class="red-text">ステータスが完了</span> と表示されます。さらに、デバイスは更新が成功したことを示すビープ音を2回鳴らします。ボードはプロセスの一環として自動的にリセットされます。</p>
</div>
</div>
</div></blockquote>
</div>
<div class="section" id="auto-positioning">
<h3>オートポジショニング</h3>
<p><strong>1. はじめに</strong></p>
<p>このガイドでは、アプリケーションでこのツールを効果的に使用する方法について説明します。</p>
<p>自動配置機能を使用すると、選択したアンカーに基づいてノードを正確に配置できます。最適なパフォーマンスを得るには、適切な設定が不可欠です。</p>
<ul class="simple">
<li><p>はじめに</p></li>
<li><p>自動配置へのアクセス</p></li>
<li><p>アンカーの選択</p></li>
<li><p>計算モードの設定</p></li>
<li><p>測定の開始</p></li>
<li><p>位置の再計算</p></li>
<li><p>マップ上でノードの位置を表示および調整する</p></li>
<li><p>設定の保存</p></li>
<li><p>よくある質問</p></li>
</ul>
<p><strong>2. 自動配置へのアクセス</strong></p>
<p>自動配置機能にアクセスするには、ネットワークの状態に応じて、次のいずれかの方法でアクセスしてください:</p>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>メニューへのアクセス</p></li>
</ol>
<ul class="simple">
<li><p>メニューアイコンをタップ：画面の <code class="docutils literal notranslate"><span class="pre">右隅</span></code> にあるメニューアイコンをタップします。</p></li>
<li><p>メニューから <code class="docutils literal notranslate"><span class="pre">自動配置</span></code> 機能を選択します。</p></li>
</ul>
<ol class="upperalpha simple" start="2">
<li><p>自動配置を選択します。</p></li>
</ol>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">Demo</span> <span class="pre">Selector</span></code> にアクセスします。</p></li>
<li><p>そこから <code class="docutils literal notranslate"><span class="pre">自動配置</span></code> オプションを選択します。</p></li>
</ul>
</div></blockquote>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-0.jpg"><img alt="lm26" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-0.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-1.jpg"><img alt="lm27" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>3. アンカーの選択</strong></p>
<a class="reference internal image-reference" href="../../../_images/leaps-manager-auto-positioning-2.jpg"><img alt="../../../_images/leaps-manager-auto-positioning-2.jpg" class="align-right" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-2.jpg" style="width: 237.60000000000002px; height: 528.0px;"></a>
<p>アプリケーションはアンカーのリストを表示します。</p>
<p>アンカーの選択:</p>
<blockquote>
<div><ul class="simple">
<li><p>少なくとも``2つのアンカー`` の横にあるチェックボックスをオンにしてください。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">1つのアンカー</span></code> が <code class="docutils literal notranslate"><span class="pre">開始アンカー</span></code> として指定されていることを確認してください。</p></li>
<li><p>正確な位置決めを行うには、アンカーが <code class="docutils literal notranslate"><span class="pre">直立</span></code> し、互いに向き合っている必要があります。</p></li>
</ul>
</div></blockquote>
<p><strong>4. 計算モードの設定</strong> (<strong>オプション</strong>)</p>
<ul class="simple">
<li><p>計算モード: すべての設定を <code class="docutils literal notranslate"><span class="pre">計算</span></code> に設定すると、アプリケーションはノードの位置を自動的に計算します。</p></li>
<li><p>手動モード: <code class="docutils literal notranslate"><span class="pre">手動</span></code> に設定すると、手動で調整または再計算するまで、位置はほぼ固定されたままになります。</p></li>
</ul>
<p><strong>5. 測定の開始</strong></p>
<p>アンカーを選択したら、<code class="docutils literal notranslate"><span class="pre">測定</span></code> ボタンをクリックして位置決めプロセスを開始します。</p>
<ul class="simple">
<li><p>完了を待つ: プロセスが終了するまで待ちます。選択したノードの位置情報が表示されます。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-4.jpg"><img alt="lm28" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-4.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-5.jpg"><img alt="lm29" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-6.jpg"><img alt="lm30" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-6.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>6. 位置の再計算</strong> (<strong>オプション</strong>)</p>
<ul class="simple">
<li><p>調整が必要な場合は、<code class="docutils literal notranslate"><span class="pre">再計算</span></code> ボタンを押して再計算してください。</p></li>
</ul>
<p><strong>7. 2Dグリッド上のノード位置の表示と調整</strong> (<strong>オプション</strong>)</p>
<ol class="arabic simple">
<li><p>マップへのアクセス:</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">右上隅</span></code> のマップアイコンをタップすると、ノードのリアルタイム位置が表示されます。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>ノード位置の調整:</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>回転機能を使用してノードを <code class="docutils literal notranslate"><span class="pre">回転</span></code> します。</p></li>
<li><p>必要に応じて、各ノードの <code class="docutils literal notranslate"><span class="pre">特定の位置</span></code> を設定します。</p></li>
<li><p>ノードを <code class="docutils literal notranslate"><span class="pre">ホールド</span></code> すると、ノードを任意の場所に自由に移動できます。</p></li>
<li><p>このインターフェースから自動配置や再計算を行うこともできます。</p></li>
</ul>
</div></blockquote>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-8.jpg"><img alt="lm31" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-8.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-7.jpg"><img alt="lm32" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-7.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-9.jpg"><img alt="lm33" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>8. 設定の保存</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>調整が完了したら、2Dグリッドの <code class="docutils literal notranslate"><span class="pre">上部ツールバー</span></code> にある <code class="docutils literal notranslate"><span class="pre">保存</span></code> ボタンまたは保存アイコンを押します。</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-10.jpg"><img alt="lm34" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-10.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-11.jpg"><img alt="lm35" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-11.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-12.jpg"><img alt="lm36" src="/docs-assets/ja/_images/leaps-manager-auto-positioning-12.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div></blockquote>
<p>2Dグリッドに戻り、ネットワーク設定の作業を続行します。</p>
<p><strong>よくある質問</strong></p>
<ol class="arabic">
<li><div class="line-block">
<div class="line"><strong>Q:</strong> リストにアンカーが表示されない場合はどうすればよいですか？</div>
<div class="line"><strong>A:</strong> ネットワークがアクティブで、環境内でアンカーが適切に設定されていることを確認してください。</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><strong>Q:</strong> 測位に1つのアンカーを使用できますか？</div>
<div class="line"><strong>A:</strong> いいえ、正確な結果を得るには、少なくとも2つのアンカーを選択する必要があります。</div>
</div>
</li>
</ol>
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
