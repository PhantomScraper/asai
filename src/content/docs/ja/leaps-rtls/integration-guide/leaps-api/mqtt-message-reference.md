---
title: "MQTT メッセージ参照"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/mqtt-message-reference"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference/"
order: 79
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-message-reference">
<span id="leaps-mqtt-message-reference"></span><h1>MQTT メッセージ参照</h1>
<hr class="docutils">
<div class="section" id="common">
<h2>共通</h2>
<div class="section" id="anchor-config">
<span id="id1"></span><h3>anchor_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 35%">
<col style="width: 12%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>イニシエーター</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>UWBイニシエーターモードの有効化。</p></td>
</tr>
<tr class="row-odd"><td><p>場所</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">ノード位置</span></a></p></td>
<td><p>必須</p></td>
<td><p>ノードの位置。</p></td>
</tr>
<tr class="row-even"><td><p>ルーティング</p></td>
<td><p><a class="reference internal" href="#routing-config"><span class="std std-ref">routing_config</span></a></p></td>
<td><p>必須</p></td>
<td><p>ルーティング設定。</p></td>
</tr>
<tr class="row-odd"><td><p>ブリッジ</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>UWBブリッジモード有効。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="node-location">
<span id="id2"></span><h3>ノード位置</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 6%">
<col style="width: 33%">
<col style="width: 7%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>フロート</p></td>
<td><p>必須</p></td>
<td><p>X座標（メートル）。</p></td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>フロート</p></td>
<td><p>必須</p></td>
<td><p>Y座標（メートル）。</p></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>フロート</p></td>
<td><p>必須</p></td>
<td><p>Z座標（メートル）。</p></td>
</tr>
<tr class="row-odd"><td><p>品質</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>品質係数（0%～100%）。</p></td>
</tr>
<tr class="row-even"><td><p>sd_x</p></td>
<td><p>フロート</p></td>
<td><p>オプション</p></td>
<td><p>X座標の標準偏差（メートル）。</p></td>
</tr>
<tr class="row-odd"><td><p>sd_y</p></td>
<td><p>フロート</p></td>
<td><p>オプション</p></td>
<td><p>Y座標の標準偏差（メートル）。</p></td>
</tr>
<tr class="row-even"><td><p>sd_z</p></td>
<td><p>フロート</p></td>
<td><p>オプション</p></td>
<td><p>Z座標の標準偏差（メートル）。</p></td>
</tr>
<tr class="row-odd"><td><p>r95</p></td>
<td><p>フロート</p></td>
<td><p>オプション</p></td>
<td><p>位置のR95（メートル）。</p></td>
</tr>
<tr class="row-even"><td><p>x_err</p></td>
<td><p>フロート</p></td>
<td><p>オプション</p></td>
<td><p>基準位置と比較したX座標の誤差（メートル単位）。</p></td>
</tr>
<tr class="row-odd"><td><p>y_err</p></td>
<td><p>フロート</p></td>
<td><p>オプション</p></td>
<td><p>基準位置と比較したY座標の誤差（メートル単位）。</p></td>
</tr>
<tr class="row-even"><td><p>z_err</p></td>
<td><p>フロート</p></td>
<td><p>オプション</p></td>
<td><p>基準位置と比較したZ座標の誤差（メートル単位）。</p></td>
</tr>
<tr class="row-odd"><td><p>toa</p></td>
<td><p><a class="reference internal" href="#node-toa-measurement-statistics"><span class="std std-ref">node_toa_measurement_statistics</span></a></p></td>
<td><p>繰り返し</p></td>
<td><p>到着時間測定の統計情報。</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="node-status">
<h3>ノードステータス</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 22%">
<col style="width: 8%">
<col style="width: 57%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>出自</p></td>
<td><p><a class="reference internal" href="#origin-info"><span class="std std-ref">origin_info</span></a></p></td>
<td><p>繰り返し</p></td>
<td><p>起点のリスト。</p></td>
</tr>
<tr class="row-odd"><td><p>プロファイル</p></td>
<td><p><a class="reference internal" href="#uwb-profile"><span class="std std-ref">uwb_profile</span></a></p></td>
<td><p>オプション</p></td>
<td><p>現在のUWBプロファイル。</p></td>
</tr>
<tr class="row-even"><td><p>uwb</p></td>
<td><p><a class="reference internal" href="#uwb-status"><span class="std std-ref">uwb_status</span></a></p></td>
<td><p>オプション</p></td>
<td><p>UWBステータス。</p></td>
</tr>
<tr class="row-odd"><td><p>センサー</p></td>
<td><p><a class="reference internal" href="#sensor-status"><span class="std std-ref">センサーステータス</span></a></p></td>
<td><p>オプション</p></td>
<td><p>センサーのステータス。</p></td>
</tr>
<tr class="row-even"><td><p>route_active</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>ゲートウェイがノードのルート候補であることを示します。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="node-toa-measurement-statistics">
<span id="id3"></span><h3>node_toa_measurement_statistics</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 11%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>anchor_id</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>アンカーID。</p></td>
</tr>
<tr class="row-odd"><td><p>sd_tdoa</p></td>
<td><p>フロート</p></td>
<td><p>必須</p></td>
<td><p>到着時刻測定の標準偏差。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="origin-info">
<span id="id4"></span><h3>origin_info</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 24%">
<col style="width: 22%">
<col style="width: 30%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>id</p></td>
<td><p>uint64</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>hop_level</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="sensor-status">
<span id="id5"></span><h3>センサーステータス</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>バッテリーレベル（mV）。</p></td>
</tr>
<tr class="row-odd"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>Indicates the battery status, 0-Unknown | 1-Empty | 2-Low | 3-Medium | 4-Full.</p></td>
</tr>
<tr class="row-even"><td><p>temp</p></td>
<td><p>int32</p></td>
<td><p>必須</p></td>
<td><p>温度（度）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="service-data">
<span id="id6"></span><h3>サービスデータ</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 4%">
<col style="width: 20%">
<col style="width: 7%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p><a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a></p></td>
<td><p>必須</p></td>
<td><p>サービスリクエストのタイプまたはレスポンスのタイプ。<a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a> を参照してください。</p></td>
</tr>
<tr class="row-odd"><td><p>データ</p></td>
<td><p>バイト</p></td>
<td><p>オプション</p></td>
<td><p>Base64 でエンコードされた不透明サービスデータバイト。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="signup-request">
<span id="id7"></span><h3>signup_request</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 34%">
<col style="width: 13%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>リリース</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>オプション</p></td>
<td><p>リリースのバージョン。</p></td>
</tr>
<tr class="row-odd"><td><p>ファームウェア</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>繰り返し</p></td>
<td><p>ファームウェアのバージョン。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="signup-response">
<span id="id8"></span><h3>signup_response</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 29%">
<col style="width: 12%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ステータス</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>サインアップのステータス/結果。</p></td>
</tr>
<tr class="row-odd"><td><p>ファームウェア</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>必須</p></td>
<td><p>ファームウェアの現在のバージョン。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="tag-config">
<span id="id9"></span><h3>tag_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 19%">
<col style="width: 7%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>location_engine</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>内部位置情報エンジンの有効化。</p></td>
</tr>
<tr class="row-odd"><td><p>low_power</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>低電力モードの有効化。</p></td>
</tr>
<tr class="row-even"><td><p>stationary_detection</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>静止検知の有効化。</p></td>
</tr>
<tr class="row-odd"><td><p>update_rate_nominal</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>公称更新レート（スーパーフレーム間隔の倍数）。</p></td>
</tr>
<tr class="row-even"><td><p>update_rate_stationary</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>定常更新レート（スーパーフレーム間隔の倍数）。</p></td>
</tr>
<tr class="row-odd"><td><p>reference_location</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">ノード位置</span></a></p></td>
<td><p>オプション</p></td>
<td><p>タグの参照位置。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-profile">
<span id="id10"></span><h3>uwb_profile</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 16%">
<col style="width: 20%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>sfn_range</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>スーパーフレーム番号の範囲。</p></td>
</tr>
<tr class="row-odd"><td><p>microseconds_per_sf</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>スーパーフレームあたりのマイクロ秒数。</p></td>
</tr>
<tr class="row-even"><td><p>microseconds_per_slot</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>スロットあたりのマイクロ秒数。</p></td>
</tr>
<tr class="row-odd"><td><p>update_rate_default</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>更新レートはスーパーフレームの倍数です。</p></td>
</tr>
<tr class="row-even"><td><p>uplink_latency</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>受信した到着時刻データが内部の位置情報エンジンによって処理されるまでに待機するスロット数。</p></td>
</tr>
<tr class="row-odd"><td><p>node_signup_optional</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>このパラメータを "true" に設定すると、どのエッジノード（ゲートウェイノードを除く）でもサインアップは不要になります。</p></td>
</tr>
<tr class="row-even"><td><p>レイテンシー</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>スーパーフレーム数で表したイーサネット遅延。この遅延はダウンリンク送信時に考慮されます。このパラメータが設定されていない場合、遅延は0になります。</p></td>
</tr>
<tr class="row-odd"><td><p>max_buffer_size_downlink</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>サイズは設定されていない場合、無制限になります。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-rf-config">
<span id="id11"></span><h3>uwb_rf_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 10%">
<col style="width: 12%">
<col style="width: 69%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>chnl</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>Channel configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>rf_cpl</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>RF compliance configuration.</p></td>
</tr>
<tr class="row-even"><td><p>pcode</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>Preamble code configuration.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="version-info">
<span id="id12"></span><h3>version_info</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 27%">
<col style="width: 24%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>maj</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>min</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>patch</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>var</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="wifi-config">
<span id="id13"></span><h3>wifi_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 41%">
<col style="width: 17%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
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
<td><p><a class="reference internal" href="#wifi-region"><span class="std std-ref">wifi_region</span></a></p></td>
<td><p>オプション</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="interface-config">
<span id="id14"></span><h3>interface_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 24%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ETHERNET</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>WIFI</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="mac-address-type">
<span id="id15"></span><h3>mac_address_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 7%">
<col style="width: 75%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>空</p></td>
<td><p>0</p></td>
<td><p>MACアドレスが空の場合、インターフェースは存在しません。</p></td>
</tr>
<tr class="row-odd"><td><p>デフォルト</p></td>
<td><p>1</p></td>
<td><p>デフォルトのMACアドレス（変更不可）。</p></td>
</tr>
<tr class="row-even"><td><p>USER_SPECIFIED</p></td>
<td><p>2</p></td>
<td><p>ユーザーが指定したMACアドレス（変更可能）。</p></td>
</tr>
<tr class="row-odd"><td><p>MUTABLE_DEFAULT</p></td>
<td><p>3</p></td>
<td><p>ユーザーが一度だけ変更できるデフォルトのMACアドレス。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="routing-config">
<span id="id16"></span><h3>routing_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 14%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_OFF</p></td>
<td><p>0</p></td>
<td><p>UWBルーティングはオフになっています。</p></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_ON</p></td>
<td><p>1</p></td>
<td><p>UWBルーティングはアクティブです。</p></td>
</tr>
<tr class="row-even"><td><p>ROUTING_AUTO</p></td>
<td><p>2</p></td>
<td><p>自動UWBルーティング。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="service-type">
<span id="id17"></span><h3>service_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 11%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>GET_CONFIG</p></td>
<td><p>0</p></td>
<td><p>設定送信要求。</p></td>
</tr>
<tr class="row-odd"><td><p>TLV_API_CMD</p></td>
<td><p>1</p></td>
<td><p>TLV APIコマンド。</p></td>
</tr>
<tr class="row-even"><td><p>TLV_API_ACK</p></td>
<td><p>2</p></td>
<td><p>TLV APIコマンドの肯定応答。</p></td>
</tr>
<tr class="row-odd"><td><p>TLV_API_NACK</p></td>
<td><p>3</p></td>
<td><p>TLV APIコマンドの否定応答。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="tls-config">
<span id="id18"></span><h3>tls_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 5%">
<col style="width: 86%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>オフ</p></td>
<td><p>0</p></td>
<td><p>TLS/SSL がオフになっています。</p></td>
</tr>
<tr class="row-odd"><td><p>サーバー</p></td>
<td><p>1</p></td>
<td><p>サーバーの TLS 認証。</p></td>
</tr>
<tr class="row-even"><td><p>相互</p></td>
<td><p>2</p></td>
<td><p>サーバーとゲートウェイ/クライアント間の双方向 TLS 認証。</p></td>
</tr>
<tr class="row-odd"><td><p>SERVER_CN</p></td>
<td><p>3</p></td>
<td><p>サーバーの TLS 認証（'共通名' の確認を含む）。</p></td>
</tr>
<tr class="row-even"><td><p>MUTUAL_CN</p></td>
<td><p>4</p></td>
<td><p>サーバーとゲートウェイ/クライアント間の双方向 TLS 認証（'共通名' の確認を含む）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-mode-config">
<span id="id19"></span><h3>uwb_mode_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 18%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
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
<hr class="docutils">
</div>
<div class="section" id="uwb-status">
<span id="id20"></span><h3>uwb_status</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 11%">
<col style="width: 65%">
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
<td><p>UWB ネットワークから切断されています。</p></td>
</tr>
<tr class="row-odd"><td><p>已连接</p></td>
<td><p>1</p></td>
<td><p>UWB ネットワークに接続されています。</p></td>
</tr>
<tr class="row-even"><td><p>接続されました</p></td>
<td><p>2</p></td>
<td><p>接続済み、バックホール可能です。</p></td>
</tr>
<tr class="row-odd"><td><p>UPDATING_FW</p></td>
<td><p>3</p></td>
<td><p>UWBファームウェアのアップデートが進行中です。</p></td>
</tr>
<tr class="row-even"><td><p>UWBS_INACTIVE</p></td>
<td><p>4</p></td>
<td><p>UWBSからのデータが来ない</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="wifi-region">
<span id="id21"></span><h3>wifi_region</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 43%">
<col style="width: 20%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ヨーロッパ</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>北米</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>アジア</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="leaps-api">
<h2>leaps_api</h2>
<div class="section" id="leaps-api-inet-config">
<span id="id22"></span><h3>leaps_api.inet_config</h3>
<p>TCP/IP設定オプション</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 49%">
<col style="width: 9%">
<col style="width: 30%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ip</p></td>
<td><p><a class="reference internal" href="#leaps-api-ip-config"><span class="std std-ref">leaps_api.ip_config</span></a></p></td>
<td><p>繰り返し</p></td>
<td><p>IP設定</p></td>
</tr>
<tr class="row-odd"><td><p>dns</p></td>
<td><p>文字列</p></td>
<td><p>繰り返し</p></td>
<td><p>DNSホスト</p></td>
</tr>
<tr class="row-even"><td><p>iface</p></td>
<td><p><a class="reference internal" href="#interface-config"><span class="std std-ref">interface_config</span></a></p></td>
<td><p>必須</p></td>
<td><p>インターフェース選択</p></td>
</tr>
<tr class="row-odd"><td><p>tls</p></td>
<td><p><a class="reference internal" href="#tls-config"><span class="std std-ref">tls_config</span></a></p></td>
<td><p>必須</p></td>
<td><p>TLS/SSL設定</p></td>
</tr>
<tr class="row-even"><td><p>dhcp</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>DHCPは有効ですか？</p></td>
</tr>
<tr class="row-odd"><td><p>mac_filter</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>MACフィルターは有効ですか？</p></td>
</tr>
<tr class="row-even"><td><p>サーバー</p></td>
<td><p><a class="reference internal" href="#leaps-api-inet-config-server-config"><span class="std std-ref">leaps_api.inet_config.server_config</span></a></p></td>
<td><p>必須</p></td>
<td><p>Leaps server設定</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-inet-config-server-config">
<span id="id23"></span><h3>leaps_api.inet_config.server_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 17%">
<col style="width: 15%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ホスト</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>Leaps serverのホスト設定。</p></td>
</tr>
<tr class="row-odd"><td><p>ポート</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>Leaps serverのポート設定。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-ip-config">
<span id="id24"></span><h3>leaps_api.ip_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 21%">
<col style="width: 19%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>アドレス</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>IPアドレス。</p></td>
</tr>
<tr class="row-odd"><td><p>マスク</p></td>
<td><p>文字列</p></td>
<td><p>オプション</p></td>
<td><p>IPアドレスマスク。</p></td>
</tr>
<tr class="row-even"><td><p>ゲートウェイ</p></td>
<td><p>文字列</p></td>
<td><p>オプション</p></td>
<td><p>ゲートウェイIPアドレス。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-location">
<span id="id25"></span><h3>leaps_api.location</h3>
<p>Topic: {prefix}/{panId/}node/uplink/location/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 34%">
<col style="width: 12%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>場所</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">ノード位置</span></a></p></td>
<td><p>必須</p></td>
<td><p>デバイスの位置情報。</p></td>
</tr>
<tr class="row-odd"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>タイムスタンプ（マイクロ秒）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-mac-config">
<span id="id26"></span><h3>leaps_api.mac_config</h3>
<p>MACアドレスの設定。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 23%">
<col style="width: 7%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>アドレス</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>ドット表記のMACアドレス。</p></td>
</tr>
<tr class="row-odd"><td><p>タイプ</p></td>
<td><p><a class="reference internal" href="#mac-address-type"><span class="std std-ref">mac_address_type</span></a></p></td>
<td><p>必須</p></td>
<td><p>MACアドレスの種類。<a class="reference internal" href="#mac-address-type"><span class="std std-ref">mac_address_type</span></a> を参照してください。</p></td>
</tr>
<tr class="row-even"><td><p>iface</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>MACアドレスが属するインターフェース。mac_address_interface を参照してください。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-node-config">
<span id="id27"></span><h3>leaps_api.node_config</h3>
<p>Topic: {prefix}/{panId/}{node|gateway}/{uplink|downlink}/config/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 28%">
<col style="width: 7%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ラベル</p></td>
<td><p>文字列</p></td>
<td><p>必須</p></td>
<td><p>デバイスラベル。</p></td>
</tr>
<tr class="row-odd"><td><p>uwb_mode</p></td>
<td><p><a class="reference internal" href="#uwb-mode-config"><span class="std std-ref">uwb_mode_config</span></a></p></td>
<td><p>必須</p></td>
<td><p>UWBモードの設定。</p></td>
</tr>
<tr class="row-even"><td><p>ble</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>BLEは有効ですか？</p></td>
</tr>
<tr class="row-odd"><td><p>leds</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>LEDは有効ですか？</p></td>
</tr>
<tr class="row-even"><td><p>fw_update</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>ファームウェアアップデートは有効ですか？</p></td>
</tr>
<tr class="row-odd"><td><p>アンカー</p></td>
<td><p><a class="reference internal" href="#anchor-config"><span class="std std-ref">anchor_config</span></a></p></td>
<td><p>オプション</p></td>
<td><p>アンカー固有の設定。</p></td>
</tr>
<tr class="row-even"><td><p>タグ</p></td>
<td><p><a class="reference internal" href="#tag-config"><span class="std std-ref">tag_config</span></a></p></td>
<td><p>オプション</p></td>
<td><p>タグ固有の設定。</p></td>
</tr>
<tr class="row-odd"><td><p>inet</p></td>
<td><p><a class="reference internal" href="#leaps-api-inet-config"><span class="std std-ref">leaps_api.inet_config</span></a></p></td>
<td><p>オプション</p></td>
<td><p>TCP/IPの設定</p></td>
</tr>
<tr class="row-even"><td><p>wifi</p></td>
<td><p><a class="reference internal" href="#wifi-config"><span class="std std-ref">wifi_config</span></a></p></td>
<td><p>オプション</p></td>
<td><p>Wi-Fi 設定。</p></td>
</tr>
<tr class="row-odd"><td><p>mac</p></td>
<td><p><a class="reference internal" href="#leaps-api-mac-config"><span class="std std-ref">leaps_api.mac_config</span></a></p></td>
<td><p>繰り返し</p></td>
<td><p>MAC アドレス設定。</p></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>タイムスタンプ（マイクロ秒）。</p></td>
</tr>
<tr class="row-odd"><td><p>uwb_rf_config</p></td>
<td><p><a class="reference internal" href="#uwb-rf-config"><span class="std std-ref">uwb_rf_config</span></a></p></td>
<td><p>オプション</p></td>
<td><p>UWB channel, preamble code and RF compliance configuration.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-tdoa-external-le">
<span id="id28"></span><h3>leaps_api.tdoa_external_le</h3>
<p>Topic: {prefix}/{panId/}{node|gateway}/uplink/toa/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 36%">
<col style="width: 9%">
<col style="width: 35%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p><a class="reference internal" href="#time-of-arrival-data-type"><span class="std std-ref">time_of_arrival_data_type</span></a></p></td>
<td><p>必須</p></td>
<td><p>Type of TOA data</p></td>
</tr>
<tr class="row-odd"><td><p>from</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>Id of transmitting device</p></td>
</tr>
<tr class="row-even"><td><p>to</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>Id of receiving device</p></td>
</tr>
<tr class="row-odd"><td><p>rx_timestamp</p></td>
<td><p>uint64</p></td>
<td><p>必須</p></td>
<td><p>Receive timestamp (uwb clock)</p></td>
</tr>
<tr class="row-even"><td><p>tx_timestamp</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>Transmit timestamp (uwb clock)</p></td>
</tr>
<tr class="row-odd"><td><p>tag_blink_index</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>Tag blink index</p></td>
</tr>
<tr class="row-even"><td><p>frame</p></td>
<td><p>uint32</p></td>
<td><p>必須</p></td>
<td><p>Frame number</p></td>
</tr>
<tr class="row-odd"><td><p>tn_stat</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>TN stationary status</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="time-of-arrival-data-type">
<span id="id29"></span><h3>time_of_arrival_data_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 15%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UNKNOWN</p></td>
<td><p>0</p></td>
<td><p>Unknown</p></td>
</tr>
<tr class="row-odd"><td><p>TWR</p></td>
<td><p>1</p></td>
<td><p>TWR</p></td>
</tr>
<tr class="row-even"><td><p>TDOA_BLINK</p></td>
<td><p>2</p></td>
<td><p>TDoA Blink</p></td>
</tr>
<tr class="row-odd"><td><p>TDOA_BCN</p></td>
<td><p>3</p></td>
<td><p>TDoA Beacon</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-server-status">
<span id="id30"></span><h3>leaps_api.server_status</h3>
<p>Leaps server status uplink topic: {prefix}/server/status.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 38%">
<col style="width: 7%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>状態</p></td>
<td><p><a class="reference internal" href="#leaps-api-connection-state"><span class="std std-ref">leaps_api.connection_state</span></a></p></td>
<td><p>オプション</p></td>
<td><p>LEAPS Serverのステータス。server_state を参照してください。</p></td>
</tr>
<tr class="row-odd"><td><p>バージョン</p></td>
<td><p>文字列</p></td>
<td><p>オプション</p></td>
<td><p>Leaps serverーのバージョン。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-server-request">
<span id="id31"></span><h3>leaps_api.server_request</h3>
<p>Leaps serverー要求ダウンリンクトピック: {prefix}/server/request。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 34%">
<col style="width: 7%">
<col style="width: 51%">
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
<td><p><a class="reference internal" href="#leaps-api-server-request-type"><span class="std std-ref">leaps_api.server_request.type:</span></a></p></td>
<td><p>オプション</p></td>
<td><p>Request to the Leaps server.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="leaps-api-server-request-type">
<span id="id32"></span><h3>leaps_api.server_request.type:</h3>
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
<td><p>DEPRECATED: Same as PUBLISH_ALL_TOPICS.</p></td>
</tr>
<tr class="row-odd"><td><p>PUBLISH_ALL_TOPICS</p></td>
<td><p>1</p></td>
<td><p>すべてのノードのすべてのメッセージをただちに公開するようリクエストします。</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="leaps-api-service-data">
<span id="id33"></span><h3>leaps_api.service_data</h3>
<p>トピック: {prefix}/{panId/node/{uplink|downlink}/service/{deviceId}。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 31%">
<col style="width: 11%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p><a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a></p></td>
<td><p>必須</p></td>
<td><p>サーバーデータの種類。</p></td>
</tr>
<tr class="row-odd"><td><p>データ</p></td>
<td><p>バイト</p></td>
<td><p>オプション</p></td>
<td><p>base64でエンコードされたデータバイト。</p></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>タイムスタンプ（マイクロ秒）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-status">
<span id="id34"></span><h3>leaps_api.status</h3>
<p>トピック: {prefix}/{panId}/{node|gateway}/uplink/status/{deviceId}。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 15%">
<col style="width: 7%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>現在</p></td>
<td><p>ブール値</p></td>
<td><p>必須</p></td>
<td><p>デバイスは存在しますか？</p></td>
</tr>
<tr class="row-odd"><td><p>ダウンリンク</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>デバイスへのダウンリンク送信は可能ですか？</p></td>
</tr>
<tr class="row-even"><td><p>uwb</p></td>
<td><p><a class="reference internal" href="#uwb-status"><span class="std std-ref">uwb_status</span></a></p></td>
<td><p>オプション</p></td>
<td><p>UWBレイヤーのステータス。</p></td>
</tr>
<tr class="row-odd"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>Battery status in mV.</p></td>
</tr>
<tr class="row-even"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>オプション</p></td>
<td><p>Indicates the battery status, 0-Unknown | 1-Empty | 2-Low | 3-Medium | 4-Full.</p></td>
</tr>
<tr class="row-odd"><td><p>temp</p></td>
<td><p>int32</p></td>
<td><p>オプション</p></td>
<td><p>温度（度）。</p></td>
</tr>
<tr class="row-even"><td><p>出自</p></td>
<td><p><a class="reference internal" href="#origin-info"><span class="std std-ref">origin_info</span></a></p></td>
<td><p>繰り返し</p></td>
<td><p>UWB送信元リスト。</p></td>
</tr>
<tr class="row-odd"><td><p>プロファイル</p></td>
<td><p><a class="reference internal" href="#uwb-profile"><span class="std std-ref">uwb_profile</span></a></p></td>
<td><p>オプション</p></td>
<td><p>現在のUWBプロファイルのステータス。</p></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>タイムスタンプ（マイクロ秒）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-user-data">
<span id="id35"></span><h3>leaps_api.user_data</h3>
<p>トピック: {prefix}/{panId}/node/{uplink|downlink}/data/{deviceId}。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 14%">
<col style="width: 56%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>フィールド</p></th>
<th class="head"><p>タイプ</p></th>
<th class="head"><p>ラベル</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>データ</p></td>
<td><p>バイト</p></td>
<td><p>必須</p></td>
<td><p>base64でエンコードされたデータバイト。</p></td>
</tr>
<tr class="row-odd"><td><p>上書き</p></td>
<td><p>ブール値</p></td>
<td><p>オプション</p></td>
<td><p>保留中のデータを上書きしますか？</p></td>
</tr>
<tr class="row-even"><td><p>タイムスタンプ</p></td>
<td><p>uint64</p></td>
<td><p>オプション</p></td>
<td><p>タイムスタンプ（マイクロ秒）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-mac-address-interface">
<span id="id36"></span><h3>leaps_api.mac_address_interface</h3>
<p>MACアドレス設定でサポートされているインターフェース。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 24%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名前</p></th>
<th class="head"><p>数値</p></th>
<th class="head"><p>説明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>BLE</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ETHERNET</p></td>
<td><p>2</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>WIFI</p></td>
<td><p>3</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-connection-state">
<span id="id37"></span><h3>leaps_api.connection_state</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 9%">
<col style="width: 73%">
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
<td><p>Leaps server is disconnected from MQTT broker.</p></td>
</tr>
<tr class="row-odd"><td><p>已连接</p></td>
<td><p>1</p></td>
<td><p>Leaps server is connected to MQTT broker.</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
