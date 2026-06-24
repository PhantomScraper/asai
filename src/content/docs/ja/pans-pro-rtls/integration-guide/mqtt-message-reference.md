---
title: "MQTT メッセージ参照"
lang: ja
slug: "pans-pro-rtls/integration-guide/mqtt-message-reference"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/mqtt-message-reference/"
order: 75
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-message-reference">
<span id="pans-mqtt-message-reference"></span><h1>MQTT メッセージ参照</h1>
<p>このページでは各API定義の詳細について説明します。</p>
<div class="section" id="anchorconfiguration">
<span id="id1"></span><h2>锚点構成</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>イニシエーター</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>位置</p></td>
<td><p>位置</p></td>
<td><p>オプション</p></td>
<td><p>アンカー位置座標</p></td>
</tr>
<tr class="row-even"><td><p>路由配置</p></td>
<td><p>路由锚点構成</p></td>
<td><p>必須</p></td>
<td><p>ルーティング設定</p></td>
</tr>
<tr class="row-odd"><td><p>ルーティングステータス</p></td>
<td><p>路由锚点状態态</p></td>
<td><p>オプション</p></td>
<td><p>ルーティング情報 - アップリンクのみに有効、読み取り専用</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="fwversion">
<h2>Fw バージョン</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>リリース</p></td>
<td><p>文字列</p></td>
<td><p>オプション</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>ファームウェア</p></td>
<td><p>文字列</p></td>
<td><p>繰り返し</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="kernelposition">
<h2>カーネル位置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>バイト</p></td>
<td><p>必須</p></td>
<td><div class="line-block">
<div class="line">不透明なバイト シーケンスとしての座標。カーネル ドライバーはカーネル空間内の浮動小数点数で動作できません</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>バイト</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>バイト</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>品質</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><div class="line-block">
<div class="line">品質係数 (0-100)、PB は可変長エンコーディングを使用しており、長さを心配する必要はありません</div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<p>MacConfig</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>アドレス</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>タイプ</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>空、デフォルト、ユーザー指定、変更可能なデフォルト</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="gatewayconfig">
<h2>ネットワーク構成</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ip地址</p></td>
<td><p>文字列</p></td>
<td><p>繰り返し</p></td>
<td><p>ipアドレス</p></td>
</tr>
<tr class="row-odd"><td><p>ipMask</p></td>
<td><p>文字列</p></td>
<td><p>繰り返し</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ipゲートウェイ</p></td>
<td><p>文字列</p></td>
<td><p>繰り返し</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>dns</p></td>
<td><p>文字列</p></td>
<td><p>繰り返し</p></td>
<td><p>DNS</p>
<p>構成</p>
</td>
</tr>
<tr class="row-even"><td><p>インターフェース</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>インターフェイスの種類 ETHERNET、WIFI、...</p></td>
</tr>
<tr class="row-odd"><td><p>dhcp</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>DHCP</p>
<p>構成</p>
</td>
</tr>
<tr class="row-even"><td><p>tls</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>TLS 構成 OFF、SERVER、MUTUAL、SERVER_CN、MUTUAL_CN</p></td>
</tr>
<tr class="row-odd"><td><p>サーバー</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>サーバーのアドレスとポート</p></td>
</tr>
<tr class="row-even"><td><p>port</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>macFilter</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>MAC フィルター</p>
<p>構成</p>
</td>
</tr>
<tr class="row-even"><td><p>wifi</p></td>
<td><p>WifiConfig</p></td>
<td><p>オプション</p></td>
<td><p>WIFI 設定。WIFI は利用可能であり、このフィールドがアップリンク メッセージに表示される場合は設定できます。</p></td>
</tr>
<tr class="row-odd"><td><p>mac</p></td>
<td><p>MacConfig</p></td>
<td><p>繰り返し</p></td>
<td><div class="line-block">
<div class="line">インターフェイスの MAC アドレスの読み取り専用リスト</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>ラベル</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>UWB ノードのラベル</p></td>
</tr>
<tr class="row-odd"><td><p>uwbMode</p></td>
<td><p>UwbMode</p></td>
<td><p>必須</p></td>
<td><p>UWB モード 0 - オフライン、1 - パッシブ、2 - アクティブ</p></td>
</tr>
<tr class="row-even"><td><p>leds</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>LED を有効または無効にします</p></td>
</tr>
<tr class="row-odd"><td><p>uw
bFirmwareUpdate</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>ファームウェアアップデートの有効化/無効化</p></td>
</tr>
<tr class="row-even"><td><p>イニシエーター</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>UWB アンカー イニシエーター</p></td>
</tr>
<tr class="row-odd"><td><p>uwbブリッジ</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>UWB ブリッジ</p></td>
</tr>
<tr class="row-even"><td><p>位置</p></td>
<td><p>位置</p></td>
<td><p>必須</p></td>
<td><p>ゲートウェイの位置</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="gatewaystatusandconfig">
<span id="pans-gatewaystatusandconfig"></span><h2>GatewayStatusAndConfig</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>networkId</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>UWBネットワークID</p></td>
</tr>
<tr class="row-odd"><td><p>bridgeNodeId</p></td>
<td><p>sfixed64</p></td>
<td><p>オプション</p></td>
<td><p>KD からサーバーに接続されているブリッジ ノードの ID</p></td>
</tr>
<tr class="row-even"><td><p>バージョン</p></td>
<td><p>Fw バージョン</p></td>
<td><p>オプション</p></td>
<td><p>ファームウェアのバージョン番号</p></td>
</tr>
<tr class="row-odd"><td><p>uwb</p></td>
<td><p>文字列</p></td>
<td><p>オプション</p></td>
<td><dl class="simple">
<dt>UWB ステータス:</dt><dd><p>接続済み、connected_bh、切断済み、updateing_fw</p>
</dd>
</dl>
</td>
</tr>
<tr class="row-even"><td><p>構成</p></td>
<td><p>ネットワーク構成</p></td>
<td><p>オプション</p></td>
<td><p>設定オプション</p></td>
</tr>
<tr class="row-odd"><td><p>デバッグログ</p></td>
<td><p>デバッグログ</p></td>
<td><p>オプション</p></td>
<td><p>ゲートウェイに渡されます</p></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>マイクロ秒単位のタイムスタンプ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfigdownlink">
<span id="id2"></span><h2>NodeConfigDownlink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 28%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>構成</p></td>
<td><p>ノード構成</p></td>
<td><p>必須</p></td>
<td><p>何が考えられますかクライアントから変更されました</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfiguplink">
<span id="id3"></span><h2>NodeConfigUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 28%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>構成</p></td>
<td><p>ノード構成</p></td>
<td><p>必須</p></td>
<td><blockquote>
<div><p>変更可能</p>
</div></blockquote>
<p>設定は API 経由で変更できます</p>
</td>
</tr>
<tr class="row-odd"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>マイクロ秒単位のタイムスタンプ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodedatadownlink">
<span id="pans-nodedatadownlink"></span><h2>NodeDataDownlink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>データ</p></td>
<td><p>バイト</p></td>
<td><p>必須</p></td>
<td><p>不透明なデータ (最大 36 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>上書き</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>フラグ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodedatauplink">
<span id="pans-nodedatauplink"></span><h2>NodeDataUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>データ</p></td>
<td><p>バイト</p></td>
<td><p>必須</p></td>
<td><p>不透明なデータ (最大 40 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>superFrameNumber</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>マイクロ秒単位のタイムスタンプ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodelocationuplink">
<span id="pans-nodelocationuplink"></span><h2>NodeLocationUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>位置</p></td>
<td><p>位置</p></td>
<td><p>必須</p></td>
<td><p>埋め込み位置</p></td>
</tr>
<tr class="row-odd"><td><p>superFrameNumber</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>スーパーフレーム</p></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>マイクロ秒単位のタイムスタンプ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeservicedownlink">
<span id="pans-nodeservicedownlink"></span><h2>NodeServiceDownlink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>TLV_API</p></td>
</tr>
<tr class="row-odd"><td><p>データ</p></td>
<td><p>バイト</p></td>
<td><p>必須</p></td>
<td><p>API 呼び出しを表す TLV エンコードされたバイナリ データ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeserviceuplink">
<span id="pans-nodeserviceuplink"></span><h2>NodeServiceUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>TLV_API_ACK,
TLV_API_NACK</p></td>
</tr>
<tr class="row-odd"><td><p>データ</p></td>
<td><p>バイト</p></td>
<td><p>オプション</p></td>
<td><p>TLV エンコードされた API 呼び出し応答</p></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>マイクロ秒単位のタイムスタンプ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodestatusuplink">
<span id="pans-nodestatusuplink"></span><h2>NodeStatusUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>現在</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>存在する場合は true、存在しない場合は false</p></td>
</tr>
<tr class="row-odd"><td><p>ダウンリンク</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>如果可能则为true，如果不可能则为false</p></td>
</tr>
<tr class="row-even"><td><p>lqi</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>可能な場合は true、不可能な場合は false</p></td>
</tr>
<tr class="row-odd"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>battery
level in
mV</p></td>
</tr>
<tr class="row-even"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>Indicates the
battery
status,
0-Unknown</p>
<ul class="simple">
<li><p>1-Empty</p></li>
<li><p>2-Low</p></li>
<li><p>3-Medium</p></li>
<li><p>4-Full.</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>temp</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>摂氏単位の温度</p></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>マイクロ秒単位のタイムスタンプ</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfiguration">
<span id="pans-nodeconfiguration"></span><h2>NodeConfiguration</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 34%">
<col style="width: 22%">
<col style="width: 22%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ラベル</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>共通の設定プロパティ</p></td>
</tr>
<tr class="row-odd"><td><p>nodeType</p></td>
<td><p>オペレーションモード</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ble</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>leds</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>uw
bFirmwareUpdate</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>アンカー</p></td>
<td><p>锚点構成</p></td>
<td><p>オプション</p></td>
<td><p>どちらか: 動作モードアンカー固有と同期</p></td>
</tr>
<tr class="row-even"><td><p>タグ</p></td>
<td><p>タグ構成</p></td>
<td><p>オプション</p></td>
<td><p>タグ固有</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="position">
<span id="pans-position"></span><h2>位置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>フロート</p></td>
<td><p>必須</p></td>
<td><p>座標</p></td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>フロート</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>フロート</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>品質</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><div class="line-block">
<div class="line">品質係数 (0-100)、PB は可変長エンコーディングを使用しており、長さを心配する必要はありません</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="tagconfiguration">
<h2>タグ構成</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>統計検出</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>静止状態の検出 ~ 加速度計</p></td>
</tr>
<tr class="row-odd"><td><p>レスポンシブ</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>レスポンシブモード ～ 低電力</p></td>
</tr>
<tr class="row-even"><td><p>ロケーションエンジン</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>見つけますか?</p></td>
</tr>
<tr class="row-odd"><td><p>nomUpdateRate</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>公称（通常）更新速度</p></td>
</tr>
<tr class="row-even"><td><p>statUpdateRate</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>静的更新レート (stat ionaryDetection がオンの場合)</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="wificonfig">
<h2>WifiConfig</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>フィールド</strong></p></th>
<th class="head"><p><strong>タイプ</strong></p></th>
<th class="head"><p><strong>ラベル</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ssid</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>パスワード</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>地域</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>ヨーロッパ、北アメリカ、アジア</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="operatingfirmware">
<h2>オペレーティングファームウェア</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名前</strong></p></th>
<th class="head"><p><strong>番号</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>FW1</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>FW2</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="operationmode">
<h2>オペレーションモード</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名前</strong></p></th>
<th class="head"><p><strong>番号</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タグ</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>アンカー</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="routinganchorconfiguration">
<h2>路由锚構成</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名前</strong></p></th>
<th class="head"><p><strong>番号</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_CFG_OFF</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_CFG_ON</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ROUTING_CFG_AUTO</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="routinganchorstatus">
<h2>ルーティングアンカーステータス</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名前</strong></p></th>
<th class="head"><p><strong>番号</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_STAT_INACTIVE</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_STAT_SELECTED</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ROUTING_STAT_ACTIVE</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="uwbmode">
<h2>UwbMode</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名前</strong></p></th>
<th class="head"><p><strong>番号</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB_MODE_OFFLINE</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>UWB_MODE_PASSIVE</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>UWB_MODE_ACTIVE</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="uwbstatus">
<h2>Uwbステータス</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>切断されました</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>已连接</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>接続されました</p></td>
<td><p>2</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>UPDATING_FW</p></td>
<td><p>3</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="serverrequest">
<span id="id4"></span><h2>サーバーリクエスト</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 21%">
<col style="width: 7%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>リフレッシュ・トピックス</p></td>
<td><p>0</p></td>
<td><p>すべてのノードのすべてのメッセージをただちに公開するようリクエストします。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="servermessage">
<span id="pans-servermessage"></span><h2>サーバーメッセージ</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 23%">
<col style="width: 23%">
<col style="width: 23%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>リクエスト</p></td>
<td><p>文字列</p></td>
<td><p>オプション</p></td>
<td><p><a class="reference internal" href="#serverrequest"><span class="std std-ref">サーバーリクエスト</span></a> を参照してください。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="servernodelist">
<span id="id5"></span><h2>サーバーノードリスト</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 14%">
<col style="width: 12%">
<col style="width: 64%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ネットワーク</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>UWBネットワークpanID。</p></td>
</tr>
<tr class="row-odd"><td><p>ノード</p></td>
<td><p>文字列</p></td>
<td><p>繰り返し</p></td>
<td><p>UWB ノード ID/アドレス (16 進数)。</p></td>
</tr>
</tbody>
</table>
</div>
</div>


           </div>
