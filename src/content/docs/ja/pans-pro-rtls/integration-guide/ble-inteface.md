---
title: "BLE インターフェース"
lang: ja
slug: "pans-pro-rtls/integration-guide/ble-inteface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/ble-inteface/"
order: 97
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="ble-interface">
<span id="pans-ble-interface"></span><h1>BLE インターフェース</h1>
<p>BLE API 設計では、DWM モジュールは BLE 周辺機器として機能し、API を介して BLE 中央デバイスと通信できます。このドキュメントでは、BLE 中央デバイスが通信に使用できる API を紹介します。BLE API を実行するために、Android アプリケーションと PANS PRO Manager が提供されています。</p>
<p>BLE 中央デバイスは、ネットワーク ノードに直接接続してパラメータを設定および取得します。設定/制御するには各デバイスに個別に接続する必要があります。</p>
<p>BLE スキームでは、読み取り、書き込み、通知を含む通常の GATT 操作が提供されます。</p>
<blockquote>
<div><div class="figure align-default">
<a class="reference internal image-reference" href="../../../_images/image31.png"><img alt="../../../_images/image31.png" src="/docs-assets/ja/_images/image31.png" style="width: 5.70833in; height: 2.01111in;"></a>
</div>
</div></blockquote>
<p>上の図は、DWM1001 BLE イベント ハンドラーが GATT 操作を汎用 API コマンドに変換していることを示しています。その間、BLE 関連のイベントが発生すると、BLE イベント ハンドラーは対応する通知を BLE クライアントに送信します。</p>
<p>詳細な BLE API は、<em>BLE API</em> セクションで紹介されています。</p>
<hr class="docutils">
<div class="section" id="le-gatt-model">
<h2>LE GATTモデル</h2>
<p><strong>ネットワーク ノード サービス</strong> UUID は <strong>680c21d9-c946-4c1f-9c11-baa1c21329e7</strong> です。すべての特性値は、BLE 仕様が示唆するリトル エンディアンとしてエンコードされます。</p>
<div class="section" id="network-node-characteristics">
<h3>ネットワークノードの特性</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 28%">
<col style="width: 15%">
<col style="width: 11%">
<col style="width: 38%">
<col style="width: 8%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>uuid</p></th>
<th class="head"><p>名前</p></th>
<th class="head"><p>長さ</p></th>
<th class="head"><p>値</p></th>
<th class="head"><p>フラグ</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>"標準 GAP サービス、ラベル0x2A00"</p></td>
<td><p>ラベル</p></td>
<td><p>Var</p></td>
<td><p>UTF-8 でエンコードされた文字列</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p>3f0afd88-7770-46b0-b5e7-9fc099598964</p></td>
<td><p>動作モード</p></td>
<td><p>2バイト</p></td>
<td><p>以下のセクションを参照してくださいデータエンコーディングの詳細については</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-even"><td><p>80f9d8bc-3bff-45bb-a181-2d6a37991208</p></td>
<td><p>ネットワークID</p></td>
<td><p>2バイト</p></td>
<td><p>ネットワークの一意の識別 (PAN ID)</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p>a02b947e-df97-4516-996a-1882521e0ead</p></td>
<td><p>位置データモード</p></td>
<td><p>1バイト</p></td>
<td><p>0 - 位置 1 - 距離 2 - 位置 + 距離"</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-even"><td><p>003bbdf2-c634-4b3d-ab56-7ec889b89a37</p></td>
<td><p>位置データ</p></td>
<td><p>最大 106 バイト</p></td>
<td><p>以下のセクションを参照してくださいデータエンコーディングの詳細については</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>f4a67d7d-379d-4183-9c03-4b6ea5103291</p></td>
<td><p>プロキシの位置</p></td>
<td><p>最大 76 バイト</p></td>
<td><p>BLE セントラルの新しいタグ位置に関する通知としてモジュールによって使用されます。</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p>1e63b1eb-d4ed-444e-af54-c1e965192501</p></td>
<td><p>デバイス情報</p></td>
<td><p>29バイト</p></td>
<td><p>ノード ID (8 バイト)、HW バージョン (4 バイト)、FW1 バージョン (4 バイト)、FW2 バージョン (4 バイト)、FW1 チェックサム (4 バイト)、FW2 チェックサム (4 バイト)、RDonly 動作フラグ (1)バイト）</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>1e630001-d4ed-444e-af54-c1e965192501
[PANS PRO]</p></td>
<td><p>デバイスのステータス</p></td>
<td><p>8バイト</p></td>
<td><p>稼働時間 (4 バイト、符号なし整数)、バッテリー レベル (1 バイト、符号なし整数)、予約済み (1 バイト)、温度 (2 バイト、整数)</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p>0eb2bc59-baf1-4c1c-8535-8a0204c69de5</p></td>
<td><p>統計</p></td>
<td><p>120バイト</p></td>
<td><p>ノード統計</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>5955aa10-e085-4030-8aa6-bdfac89ac32b</p></td>
<td><p>FWアップデートのプッシュ</p></td>
<td><p>最大 37 バイト</p></td>
<td><p>構造化データ (FW 更新パケット) をモジュール (BLE ペリフェラル) に送信するために使用され、サイズは最大送信単位 (MTU) に従って設定されます。データのエンコードの詳細については、以下のセクションを参照してください。</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p>9eed0e27-09c0-4d1c-bd92-7c441daba850</p></td>
<td><p>FW アップデートのポーリング</p></td>
<td><p>9バイト</p></td>
<td><p>モジュールによって次のように使用されます。 BLE セントラルの応答/通知。データ エンコーディングの詳細については、以下のセクションを参照してください。</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>ed83b848-da03-4a0a-a2dc-8b401080e473</p></td>
<td><p>切断</p></td>
<td><p>1バイト</p></td>
<td><p>value=1 を書き込むことで BLE ペリフェラルから明示的に切断するために使用されます (Android の動作による回避策)</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p>"5b10c428-af2f-486f-aee1-9dbd79b6bccb [PANS PRO 修正済み]"</p></td>
<td><p>アンカーリスト</p></td>
<td><p>65バイト</p></td>
<td><p>カウント (1 バイト)、ノード ID のリスト (2 バイト)、RSSI (1 バイト)、シート (1 バイト) リスト内の最大 16 要素</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>9d5ab03b-cbf8-4ae5-9f11-63e45f538ada</p></td>
<td><p>AES キー</p></td>
<td><p>16バイト</p></td>
<td><p>AES 対称キー R2 で実装予定</p></td>
<td><p>RW</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>ラベルの特性は特別なものです。これは、標準の名前特性 (0x2A00) の下にある標準の必須 GAP サービス (0x1800) の一部です。</p>
</div>
</div>
<div class="section" id="operation-mode-characteristic">
<h3>動作モードの特性</h3>
<p>動作モード特性は 2 バイトで、ノードの構成情報が含まれます。形式は次のように定義されます。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>1 番目のバイト (ビット 7 から 0 まで)</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Bit</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>7</p></td>
<td><p>タグ (0)、アンカー (#.</p></td>
</tr>
<tr class="row-even"><td><p>6 - 5</p></td>
<td><p>UWB - オフ (0)、パッシブ (#.、アクティブ (2))</p></td>
</tr>
<tr class="row-odd"><td><p>4</p></td>
<td><p>ファームウェア 1 (0)、ファームウェア 2 (#.</p></td>
</tr>
<tr class="row-even"><td><p>3</p></td>
<td><p>加速度計の有効化 (0, #.</p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p>LED 表示が有効になりました (0、#.</p></td>
</tr>
<tr class="row-even"><td><p>1</p></td>
<td><p>ファームウェアアップデートの有効化 (0, #.</p></td>
</tr>
<tr class="row-odd"><td><p>0</p></td>
<td><p>BLE が有効になっています (0,#.</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>2 番目のバイト (ビット 7 から 0 まで)</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Bit</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>7</p></td>
<td><p>イニシエーター有効、アンカー固有 (0、#.</p></td>
</tr>
<tr class="row-even"><td><p>6</p></td>
<td><p>低電力モード有効、タグ固有 (0、#.</p></td>
</tr>
<tr class="row-odd"><td><p>5</p></td>
<td><p>位置情報エンジン有効、タグ固有 (0、#.</p></td>
</tr>
<tr class="row-even"><td><p>4 - 0</p></td>
<td><p>予約済み</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="location-data-characteristic">
<h3>位置データの特性</h3>
<p>位置データの特性には、位置、距離、またはその両方を含めることができます。位置と距離の形式は次のように定義されます:</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>タイプ (1 バイト)</p></th>
<th class="head"><p>値</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>0 - 位置のみ</p></td>
<td><p>X、Y、Z 座標 (各 4 バイト) + 品質係数 (1 バイト)、サイズ: 13 バイト</p></td>
</tr>
<tr class="row-odd"><td><p>1 - 距離</p></td>
<td><p>最初のバイトは距離カウント (1 バイト) です。</p>
<p>ノード ID (2 バイト)、距離 (4 バイト)、および品質係数 (1 バイト) のシーケンス。</p>
<p>最大値には 15 個の要素が含まれ、サイズ: 8 ～ 106。</p>
</td>
</tr>
<tr class="row-even"><td><p>2 - 位置と距離</p></td>
<td><p>エンコードされた位置 (上記の通り、13 バイト) エンコードされた距離 (上記の通り、8 ～ 29 バイト) - 位置と距離はタグによって送信され、測距アンカーの数は最大 4 です。</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>特性値は完全に空 (長さゼロ) である可能性があります。これは、既知の位置も既知の距離も存在しないことを意味します。</p>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>位置データ モードには位置と距離が含まれますが、位置が不明な場合は特性でのみ距離を受信することも可能です。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="proxy-positions-characteristic">
<h3>プロキシ位置の特性</h3>
<p>この特性は、BLE セントラル (モバイル デバイス) に同時に接続されたノードの制限を克服するために提供されています。パッシブ ノードはこの特性を使用して、タグ位置の更新をストリーミング/通知します。</p>
<p>この特性では、データは次のようにエンコードされます。</p>
<ul class="simple">
<li><p>1バイト: エレメント数(最大5)</p></li>
<li><p>[シーケンス] タグの位置: 2 バイトのノード ID、13 バイトの位置</p></li>
</ul>
<p>したがって、5 つのタグ位置の最大サイズは 76 バイトです。</p>
</div>
<hr class="docutils">
<div class="section" id="anchor-specific-characteristics">
<h3>アンカー固有の特性</h3>
<p>アンカーは、 ‘ゲートウェイ’ および ‘イニシエーター’ と呼ばれる特別なモードで動作する場合があります。これらは直交しており、互いに影響しません。ゲートウェイ フラグは読み取り専用ですが、ユーザーはイニシエータを設定できます。また、各アンカーにはそのクラスター内のシート番号があります。</p>
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
<th class="head"><p>名前</p></th>
<th class="head"><p>長さ</p></th>
<th class="head"><p>値</p></th>
<th class="head"><p>フラグ</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>3f0af
d88-7770-46
b0-b5
e7-9fc09959
8964</strong></p></td>
<td><p>動作モード (上記を参照)</p></td>
<td><p>2バイト</p></td>
<td><p>2 バイト目のビット 7:</p>
<p>イニシエータ イネーブル (0、#. (詳細については、サブセクション <code class="docutils literal notranslate"><span class="pre">動作モードの特性</span></code> を参照)、</p>
</td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>1e63
b1eb-d4ed-4
44e-a
f54-c1e9651
92501</strong></p></td>
<td><p>デバイス情報 (<code class="docutils literal notranslate"><span class="pre">その上</span></code>)</p></td>
<td></td>
<td><p>RD のみ</p>
<p>操作フラグ: BXXXXXXX B: ゲートウェイ 1/0</p>
</td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p><strong>f0f26c
9b-2c8c-49a
c-ab6
0-fe03def1b
40c</strong></p></td>
<td><dl class="simple">
<dt>永続化</dt><dd><p>位置</p>
</dd>
</dl>
</td>
<td><p>13バイト</p></td>
<td><blockquote>
<div><p>X,Y,Z</p>
</div></blockquote>
<p>各 4 バイトの精度 + 品質係数を調整します (1 バイト、値 1 ～ 100)</p>
</td>
<td><p>WO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>28d0
1d60-89de-4
bfa-b
6e9-651ba59
6232c</strong></p></td>
<td><p>MACスタッツ</p></td>
<td><p>4バイト</p></td>
<td><p>内部デバッグ MAC 統計用に予約されています</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p><strong>17b16
13e-98f2-44
36-bc
de-23af17a1
0c72</strong></p></td>
<td><p>クラスター情報</p></td>
<td><p>5バイト</p></td>
<td><p>座席番号 (1 バイト)/クラスター マップ (2 バイト)/クラスターの近隣マップ (2 バイト)</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>5b10c4
28-af2f-486
f-aee
1-9dbd79b6b
ccb</strong>
<strong>[Not in
PANS</strong>
<strong>PRO]</strong></p></td>
<td><p>アンカーリスト</p></td>
<td><p>65バイト</p></td>
<td><p>カウント (1 バイト)、ノード ID のリスト (2 バイト)、RSSI (1 バイト)、シート (1 バイト) リスト内の最大 16 要素 [アンカー固有ではなくなったため、PANS PRO では使用できなくなりました]</p></td>
<td><p>RO</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="tag-specific-characteristics">
<h3>タグ固有の特性</h3>
<p>各タグは、周囲の 4 つのアンカーによって送信された情報に基づいてその位置を決定します。タグは、その位置の計算方法に関する完全な情報を提供します (読み取り専用)。</p>
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
<th class="head"><p>名前</p></th>
<th class="head"><p>長さ</p></th>
<th class="head"><p>値</p></th>
<th class="head"><p>フラグ</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>3f0a
fd88-7770-4
6b0-
b5e7-9fc099
598964</strong></p></td>
<td><p>動作モード (上記を参照)</p></td>
<td><p>2バイト</p></td>
<td><p>2 バイト目のビット 6: 低電力モード有効 (0、#。2 バイトのビット 5: 位置エンジン有効 (0、#。詳細については、サブセクション``動作モード特性``を参照)</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>7bd4
7f30-5602-4
389
-b069-83057
31308b6</strong></p></td>
<td><p>更新レート</p></td>
<td><p>8バイト</p></td>
<td><p>レイアウト: U1 (4 バイト)、U2 (4 バイト) 移動中は <em>U1</em> ミリ秒ごとに新しい位置をブロードキャストし、静止している場合は <em>U2</em> ミリ秒ごとに新しい位置をブロードキャストします。</p></td>
<td><p>RW</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="ble-auto-positioning">
<h2>BLE 自動位置決め</h2>
<p>BLE API を使用すると、自動位置決めプロセスを開始することもできます。モバイルデバイス上で自動位置決めプロセスが完了します (位置が計算されます)。 BLE API を使用すると、距離の測定と取得を開始できます。ワークフローは次のとおりです:</p>
<ol class="arabic">
<li><p>測る：</p>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>イニシエータが見つかり、検証されました (ノードは <em>イニシエータ</em> として <em>構成</em> されているだけでなく、<em>実際のイニシエータ</em> である必要があります)。</p></li>
<li><p>イニシエータ/ネットワークは距離測定モードに設定されます:</p>
<ol class="lowerroman simple">
<li><p>位置データ モードが距離または位置と距離に設定されていることを確認してください。</p></li>
<li><p>位置データの特性の監視を開始します (cccd 通知のセットアップ)。</p></li>
<li><p>イニシエーターからすべての測定距離を受信し、測定距離をマトリックスに保存します。</p></li>
<li><p>観察を停止します。</p></li>
</ol>
</li>
<li><p>他のすべての (非イニシエーター) ノードからの距離が取得されます。</p>
<ol class="lowerroman simple">
<li><p>接続します。</p></li>
<li><p>位置データ モードが距離または位置と距離に設定されていることを確認してください。</p></li>
<li><p>位置データ特性に保存されている値を (直接) 取得し、測定された距離をマトリックスに保存します</p></li>
<li><p>切断します。</p></li>
</ol>
</li>
</ol>
</div></blockquote>
</li>
<li><p>評価: 測定距離を評価し、直交性をチェックし、位置を計算します。</p></li>
<li><p>計算された位置をノードに保存します (ユーザーの要求に応じて)。</p></li>
</ol>
</div>
<hr class="docutils">
<div class="section" id="ble-advertisements">
<h2>BLE アドバタイズメント</h2>
<p>BLE アドバタイズメントは、周辺デバイスがその存在を他のデバイスに知らせる一般的な方法です。 BLE 仕様によれば、ブロードキャスト ペイロードは 3 つの要素、つまり [長さ、タイプ、&lt;データ&gt;] で構成されます。アンカーとタグは、<strong>存在と動作モード</strong> に関する基本情報をブロードキャストします。 BLE アドバタイズメントは、位置情報を含めるのに十分な長さではありません。</p>
<p>BLE アドバタイズメントでは、31 バイトが使用されます。</p>
<ul class="simple">
<li><p>3 バイトは必須フラグです (1 つの AD トリプレット)。</p></li>
<li><p>アプリは残りの 28 バイトを使用して AD レコードを埋めることができます (各レコードには 2 バイトの長さと型のオーバーヘッドがあります)。</p></li>
</ul>
<div class="section" id="presence-broadcast">
<h3>プレゼンスブロードキャスト</h3>
<p>DWM モジュールの BLE は、接続可能なアンダイレクト モードで動作します。サービスの可用性と一部のサービス データを含むプレゼンス ブロードキャストをアドバタイズします。プレゼンス ブロードキャストは BLE アドバタイズメント フレーム構造に従い、28 バイトを使用して情報を表示します。</p>
<p>プレゼンスは接続可能フラグが true に設定されたブロードキャストであるため、潜在的な Android BLE スタックのバグを克服するために、8 バイトの短縮ローカル名 AD レコードをここに含める必要があります (<em>[1]</em> で説明されているように)。残りのバイトはサービス データで埋められます。AD レコード ヘッダー用の 2 バイト、UUID 16 バイト、短縮操作モード 1 バイト、および変更カウンター 1 バイトです。</p>
<p>プレゼンス ブロードキャスト フレームは、合計 3 + 20 + 8 バイト、つまり 31 バイト（31 バイト中）です。フレーム構造を次の表に示します。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 42%">
<col style="width: 58%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>AD トリプレット - 部分の識別</strong></p></th>
<th class="head"><p><strong>値</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x02</p></td>
</tr>
<tr class="row-odd"><td><p>タイプ</p></td>
<td><p>0x01 (フラグ)</p></td>
</tr>
<tr class="row-even"><td><p>値</p></td>
<td><p>デバイス/アドバタイズメントフラグ - 接続可能</p></td>
</tr>
<tr class="row-odd"><td><p>LEN</p></td>
<td><p>0x13（進数で19）</p></td>
</tr>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>0x21 (SERVICE_DAT).</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>値</p></td>
<td><dl class="simple">
<dt>680c21d9-c946-4c1f-9c11-baa1c21329e7</dt><dd><p>（16 バイト）</p>
</dd>
</dl>
</td>
</tr>
<tr class="row-even"><td><p>ビット レイアウト: OXXEFFUU (1 バイト) O - 動作モード (タグ 0、アンカー #. XX - 予約済み E - エラー表示 FF - フラグ: イニシエーター、ゲートウェイ UU - UWB: オフ (0)、パッシブ (#.、アクティブ (2))</p></td>
</tr>
<tr class="row-odd"><td><p>変更カウンタ (1 バイト) - 変更カウンタは、特性が変更されるたびに変更されます (ノード統計および特にタグ: location dat# を除く)。</p></td>
</tr>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x07 (最大)</p></td>
</tr>
<tr class="row-odd"><td><p>タイプ</p></td>
<td><p>0x08 (短縮されたローカル名)</p></td>
</tr>
<tr class="row-even"><td><p>値</p></td>
<td><p>GATT 仕様で定義されているデバイス ローカル名の最初の 6 文字 (またはそれ以下)。</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="ble-firmware-update">
<h2>BLE ファームウェアのアップデート</h2>
<p>ファームウェア更新機能は、モジュールのファームウェアを更新するために使用されます。これは、UWB または BLE 経由で実行できます。このセクションでは、制御とデータは BLE 経由で流れます。</p>
<p>FW アップデート中に、<strong>FW アップデート プッシュ</strong> と <strong>FW アップデート ポーリング</strong> という 2 つの特性を使用して、要求/応答プロトコルが実装されます。</p>
<p><strong>FW アップデートを開始しています</strong></p>
<p>手順:</p>
<ol class="arabic simple">
<li><p><em>モバイル デバイス</em> (BLE セントラル) は、<strong>FW アップデート ポーリング</strong> 特性変更 (CCCD) に関する表示をセットアップします。</p></li>
<li><p><em>モバイル デバイス</em> は、アップデート要求/オファー パケットを <strong>FW アップデート プッシュ</strong> 特性に送信することで、ネットワーク ノードにアップデートを実行する意思があるかどうかを尋ねます。この初期化パケットには、ファームウェアのバージョン、チェックサム、およびファームウェア全体のバイナリ サイズ (バイト単位) が含まれます。このプロセスは信頼性の高い書き込みであり、応答付き書き込みとも呼ばれます。</p></li>
</ol>
<ol class="arabic simple" start="3">
<li><p><em>ネットワーク ノード</em> は、次の 2 つの場合に <em>FW 更新ポーリング</em> の指示で応答します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ケース 1: はい、<code class="docutils literal notranslate"><span class="pre">最初のデータ</span> <span class="pre">バッファーを送信してください</span></code>。詳細については、<em>FW バイナリの送信</em> セクションを参照してください。</p></li>
<li><p>ケース 2: いいえ、<em>エラー コード</em> が拒否理由を示します。</p></li>
</ul>
</div></blockquote>
<p>エラー状態:</p>
<p><strong>モバイルデバイス</strong>: エラーコード/理由とともに明示的な NO 表示を受信しました。 <strong>解決策</strong>: <em>モバイル デバイス</em> は、 <em>FW アップデート ポーリング</em> で CCCD 表示を無効にし、拒否された理由について上位層に通知します。 <strong>ネットワーク ノード</strong>: 突然の接続切断 <strong>解決策</strong>: FW 更新モードを終了し、FW 更新が行われなかったかのように現在の状態をリセットします。 <strong>モバイル デバイス</strong>: 接続が閉じられたことを検出します。 <strong>解決策</strong>: 再試行します。FW 更新の初期化から 30 秒経過してもまだ成功しない場合は、上位層に報告します。ユーザーの要求に応じてファームウェア更新を再開できるようにします。</p>
<hr class="docutils">
<div class="section" id="transmitting-the-fw-binary">
<h3>FWバイナリを送信しています</h3>
<p>このセクションは <em>[2]</em> からインスピレーションを受けています。</p>
<p>ネットワーク ノードはデータ送信を開始し、モバイル デバイスにどのデータ バッファが必要かを正確に伝えます。この通信は、<em>FW バッファー要求</em>: サイズとオフセットを使用して行われます。モバイル デバイスは、応答なしで書き込みコマンドを使用して、要求されたバッファを小さなチャンクで送信し始めるため、完全なラウンド トリップは発生しません。基本チャンク サイズは、単一の送信パケットに収まる MTU に等しくなります。チャンクは次のもので構成されます。</p>
<ul class="simple">
<li><p>データ: サイズは 2 の累乗に丸める必要があります。現在のチャンク サイズは 32 バイトに設定されています。</p></li>
<li><p>相対オフセット (最初から): 4 バイト。</p></li>
<li><p>メッセージ タイプの識別: FIRMWARE_DATA_CHUNK (= 0x1): 1 バイト</p></li>
</ul>
<p>ネットワーク ノードがデータ送信を完全に推進します。データ バッファが送信された後、モバイル デバイスはさらなる命令を待ちます。送信中、ネットワーク ノードは通常、ファームウェアの連続したバイト シーケンスを取得するために、データ バッファを 1 つずつ順番に要求します。たとえば、例外が発生した場合、特に現在のバッファの送信が失敗した場合、ノードは予期しないバッファを要求することがあります。</p>
<p>エラー状態:</p>
<p><strong>ネットワーク ノード</strong>: 受信時にデータ チャンクが欠落している (連続していないシーケンス)、または順序が乱れているチャンク。<strong>解決策</strong>: 欠落しているチャンクと残りのバッファーを指定して <em>FW バッファー要求</em> を送信します。<strong>モバイル デバイス</strong>: 進行中のデータ送信中に <em>FW バッファー要求</em> を受信します。<strong>解決策</strong>: データの送信を停止し、現在のオフセットを <em>FW バッファー要求</em> のオフセットに設定して、データ送信を再開します。</p>
</div>
<hr class="docutils">
<div class="section" id="finishing-the-transmission">
<h3>送信を終了しています</h3>
<p>一度最後のデータ バッファが正常に受信されると、ネットワーク ノードは、<em>FW 更新ポーリング</em> の表示を通じて、完全なファームウェア バイナリを受信したことをモバイル デバイスに通知します。</p>
<p>受信すると、モバイル デバイスは次の処理を行います。</p>
<ul class="simple">
<li><p>ネットワーク ノードから切断します。</p></li>
<li><p>500 ミリ秒待ちます。</p></li>
<li><p>ネットワーク ノードに再度接続して、ファームウェアの状態を確認します。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="fw-update-push-poll-format">
<h3>FW アップデートのプッシュ/ポーリング形式</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 28%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 15%">
<col style="width: 16%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>FWアップデートのプッシュ</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>アップデートオファー/リクエスト - ファームウェアメタ</p></td>
<td><p>タイプ == 0 (1 バイト)</p></td>
<td><p>HW バージョン (4 バイト)</p></td>
<td><p>FWバージョン(4バイト)</p></td>
<td><p>FW チェックサム (4 バイト)</p></td>
<td><p>サイズ (4 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>ファームウェアデータチャンク</p></td>
<td><p>タイプ == 1 (1 バイト)</p></td>
<td><p>オフセット (4 バイト)</p></td>
<td colspan="3"><p>データ (最大 32 バイト)</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 34%">
<col style="width: 18%">
<col style="width: 15%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>FW アップデートのポーリング</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ファームウェアバッファリクエスト</p></td>
<td><p>タイプ == 1 (1 バイト)</p></td>
<td><p>オフセット (4 バイト)</p></td>
<td><p>サイズ (4 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>シグナル</p></td>
<td><p>type == 0 (アップロード拒否)、2 (アップロード完了)、3 (保存失敗) 14 (保存失敗、無効なチェックサム) (1バイト）</p></td>
<td colspan="2"><p>0 バイト</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
