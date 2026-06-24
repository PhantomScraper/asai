---
title: "BLE インターフェース"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/ble-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/ble-interface/"
order: 130
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="ble-interface">
<h1>BLE インターフェース</h1>
<div class="section" id="introduction">
<h2>はじめに</h2>
<p>このページでは、Bluetooth Low Energy (BLE) リンク経由で利用できる LEAPS UWB Subsystem API (UWBS) について説明します。</p>
<p>UWBS BLE API 設計では、UWBS モジュールは BLE ペリフェラルとして機能し、API を介して BLE セントラル デバイスによって通信できます。このドキュメントでは、BLE セントラル デバイスが通信に使用できる API を紹介します。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Linux 上の Bluetooth が完全に動作しなくなった場合は、次のコマンドを使用して Bluetooth を再起動します。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">systemctl restart bluetooth.service</span>
</pre></div>
</div>
</div>
<hr class="docutils">
<div class="section" id="used-terminology">
<h3>使用されている用語</h3>
<ul class="simple">
<li><p><strong>UWBS</strong>: LEAPS UWB サブシステム モジュール。 UWBS は、BLE 通信において BLE ペリフェラルとして機能します。</p></li>
<li><p><strong>CDEV</strong>: UWBS ペリフェラルに接続する BLE 中央デバイス。</p></li>
<li><p><strong>ELDR</strong>: 拡張ローダー。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="position-representation">
<h3>ポジション代表</h3>
<p>リアルタイム測位システムで位置と距離を表示する場合、考慮すべき点が 2 つあります。</p>
<ul class="simple">
<li><p>精度</p></li>
<li><p>精度</p></li>
</ul>
<p>精度は、ノードによって報告された位置と実際の位置との間の誤差です。現在、この設計で使用されている UWBS は約 10 cm の精度を提供します。</p>
<p>精度は、表現される最下位ビット (LSB) の値です。このシステムのオンボードファームウェアでは、精度は 1 mm、つまり 0.001 メートルです。位置は 3 次元座標 (X、Y、Z) で表されます。X、Y、Z はそれぞれ 32 ビット整数 (4 バイト) です。各 LSB は 1 mm を表します。これは、値の解釈を容易にし、報告された値の計算を容易にするためです。</p>
<p>精度を決定するときは、意味のある結果を得るために、精度を考慮して精度を選択することが重要です。精度が低い場合、ユーザーに正確な値を表示しても意味がありません。現在の 10 cm の精度に対して 1 mm の精度は細かすぎます。したがって、Android アプリケーションでは 1 cm、つまり 0.01 メートルの精度が使用されます。座標/距離が 1 cm 以上変化した場合にのみ、更新された値が Android アプリケーションに表示されますか? これは、float/double 値を意味のある小数点以下の桁数に丸めるのと似ています。</p>
<hr class="docutils">
</div>
</div>
<div class="section" id="ble-communication-with-uwbs">
<span id="blecommunicationwithuwbs"></span><h2>UWBS との BLE 通信</h2>
<div class="line-block">
<div class="line">BLE 中央デバイスは UWBS に直接接続して、セットアップと取得を行います。</div>
<div class="line">パラメータ。設定/制御するには各デバイスに個別に接続する必要があります。 UWBS との通信は、要求応答モデルに基づいています (<a class="reference internal" href="#ble-gatt-model"><span class="std std-ref">BLE GATT モデル</span></a> を参照)。</div>
</div>
<div class="line-block">
<div class="line">UWBS は TLV API リクエストを受け入れ、TLV API 応答をセントラルに通知します。 BLE セントラルは、応答を受信するリクエストの前に通知を有効にする必要があります。 UWBS は一度に 1 つのリクエストのみをサポートします。UWBS が認識するすべての TLV フレームのエンコードの詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api#leapsapi"><span class="std std-ref">LEAPS API</span></a> を参照してください。リクエストを受け入れることに加えて、UWBS はイベントも生成します。イベントを有効にするには:</div>
</div>
<ul class="simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> によって UWBS のイベントを有効にします。</p></li>
<li><p>専用特性の通知を有効にします</p></li>
</ul>
<div class="line-block">
<div class="line">すべての API 要求、応答、およびイベントのペイロードは、2 バイト長の TLV ヘッダーで始まります。最初のバイトはフレームのタイプに対応し、2 番目のバイトはフレームの長さを表します。長さは、BLE 特性を介してストリーミングするときにフレームが完了しているかどうかを確認するために使用する必要があります。</div>
</div>
<hr class="docutils">
<div class="section" id="ble-lus-leaps-uart-service-interface">
<h3>BLE LUS (LEAPS UART サービス) インターフェイス</h3>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a> は追加の <strong>BLE LUS (LEAPS UART Service)</strong> インターフェイスをサポートしており、次の手順でインターフェイスを設定します。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>UART シェルが開かれている場合、BLE シェルにはアクセスできません。</p>
</div>
<ol class="arabic">
<li><p>以下のコマンドを使用して、Python ble-serial ライブラリをインストールします。</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">python -m pip install ble-serial==2.7.1</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Windows を使用している場合は、このリンク <a class="reference external" href="https://github.com/Jakeler/ble-serial">ble-serial</a> の追加手順 <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">の追加手順</span></code> に従ってください。</p>
</div>
</li>
<li><p>以下のコマンドを使用してデバイスを検索します。 LEAPS ボードは <code class="docutils literal notranslate"><span class="pre">LEAPS….</span></code> という名前で表示されます。</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">ble-scan</span>
</pre></div>
</div>
<p>および成功したスキャンの結果:</p>
<a class="reference internal image-reference" href="../../../../_images/ble-lus-scan.png"><img alt="../../../../_images/ble-lus-scan.png" class="align-center" src="/docs-assets/ja/_images/ble-lus-scan.png" style="width: 920.0px; height: 462.0px;"></a>
</li>
<li><p>シリアル ポートに接続するには、ターミナルを開き、上記の手順で見つかった MAC アドレスを使用して以下のコマンドを実行します。</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">ble-serial -d CA:E5:56:1F:57:3D -r e8573d97-6758-11e9-8860-cb4385c24b83 -w e6bfa235-6758-11e9-979f-5b24c4603eb8 -t 10</span>
</pre></div>
</div>
</li>
<li><p>成功すると、以下のように表示されます</p>
<img alt="../../../../_images/ble-lus-passed.png" class="align-center" src="/docs-assets/ja/_images/ble-lus-passed.png">
</li>
<li><p>ログとして、スクリプトは LEAPS ボード上のシリアル ポートと通信するために <code class="docutils literal notranslate"><span class="pre">/tmp/ttyBLE</span></code> という名前のシリアル ポートを作成しました。このターミナルを実行し、別のターミナルを開き、minicom としてツールを使用してこのシリアル ポートにアクセスしましょう。</p></li>
<li><p>Enter キーを 2 回押してシェルに入ります。</p></li>
</ol>
<hr class="docutils">
</div>
<div class="section" id="autodisconnect">
<span id="id1"></span><h3>自動切断</h3>
<p>CDEV が特性 “<strong>API Response</strong>“ または “<strong>API Events</strong>“ の 0x0001 を CCCD に書き込むことによる通知を有効にしていない場合、UWBS は 15 秒後に接続を自動的に終了します (<a class="reference internal" href="#ble-gatt-model"><span class="std std-ref">BLE GATT モデル</span></a> を参照)</p>
</div>
<hr class="docutils">
<div class="section" id="ble-throughput">
<h3>BLEスループット</h3>
<p>UWBS との間でデータをストリーミングするときに、最大可能な ATT MTU と最高の接続優先度を使用して、最大可能なスループットを活用します。UWBS でサポートされる最大 MTU は 150 バイトです。ノードが推奨する接続間隔は、最小 10 ミリ秒から最大 40 ミリ秒、レイテンシ 0、タイムアウト 2 秒です。Bluetooth v4.0 および v4.1 では、MTU ネゴシエーションに関係なく最大データ長がデフォルト値のままであるため、Bluetooth v4.2 以降と比較して、これらの Bluetooth バージョンの最大スループットが制限されることに注意してください。</p>
</div>
<hr class="docutils">
<div class="section" id="security-encryption">
<h3>セキュリティ/暗号化</h3>
<div class="line-block">
<div class="line">システムは、BLE で 2 つの動作モード (暗号化なしまたは暗号化のみ (AES-OFB)) をサポートしています。暗号化の機能と操作については、次のセクションで説明します。</div>
</div>
<ul class="simple">
<li><p>特徴</p>
<ul>
<li><p>アクセス制御とメッセージの整合性 (MIC/MAC - メッセージ整合性コードまたはメッセージ認証コード)</p></li>
<li><p>守秘義務</p></li>
<li><p>リプレイ保護</p></li>
</ul>
</li>
<li><p>BLE のワイヤレス暗号化では、AES OFB 128 暗号が使用されます。</p></li>
<li><p>暗号化されたネットワークでは、通信に参加したい各ノードは、ユーザーが次の方法で設定した 128 ビットの対称キーを持っている必要があります。</p>
<ul>
<li><p>LEAPS Android Manager: 設定経由</p></li>
<li><p>モジュール上: UART/SPI/UserApp/Shell API</p></li>
</ul>
</li>
<li><p>暗号化/復号化はブロック単位で行われ、各ブロックのサイズは 16 バイトに固定されています。したがって、暗号化されたペイロードのサイズは 16 バイトの倍数に丸められる必要があります。つまり、セキュリティが有効になっている場合、メッセージのペイロードは 16 バイトの倍数に揃える必要があります。暗号化が無効になっている場合、ペイロードは 16 バイトに揃えてはなりません。</p></li>
<li><p>各メッセージには次の内容が含まれます</p>
<ul>
<li><p>ナンス - 16 バイト</p></li>
<li><p>MIC/MAC - 2バイト</p></li>
<li><p>ペイロード (暗号化が有効な場合は 16 バイトに調整されます)</p></li>
<li><p>See also <a class="reference internal" href="#messageencoding"><span class="std std-ref">メッセージのエンコーディング</span></a></p></li>
</ul>
</li>
<li><p>下の図は、AES を使用してデータがどのように暗号化されるかを説明しています。</p>
<ul>
<li><p>赤色: 秘密キーであり、保護する必要があります</p></li>
<li><p>青色: 公開データ - すべての BLE メッセージで配布されます</p></li>
<li><p>灰色: 暗号化アクセラレータ/コントローラ</p></li>
<li><p>黄色: 計算/暗号化されたブロック</p></li>
<li><p>緑色: 平文/復号化されたブロック</p></li>
</ul>
</li>
</ul>
<img alt="../../../../_images/encryptedusingaes.png" class="align-center" src="/docs-assets/ja/_images/encryptedusingaes.png">
<ul class="simple">
<li><p>下の図は、AES OFB を使用してデータがどのように暗号化され、チェーンされるかを説明しています。</p></li>
</ul>
<img alt="../../../../_images/aes_ofb.png" class="align-center" src="/docs-assets/ja/_images/aes_ofb.png">
<img alt="../../../../_images/aes_ofb_02.png" class="align-center" src="/docs-assets/ja/_images/aes_ofb_02.png">
<ul class="simple">
<li><p>暗号化されたネットワークに参加したいノードの要件</p>
<ul>
<li><p>暗号化/復号化に正しい Nonce を使用する</p></li>
<li><p>128 ビット AES キーを持つ</p></li>
</ul>
</li>
<li><p>nonce には、メッセージの暗号化/復号化に使用される nonce と、メッセージの整合性チェックに使用される nonce の 2 種類があります。</p>
<ul>
<li><p>各暗号化/復号化ノンスの長さは 16 バイトです。送信者は nonce を生成し、送信メッセージに埋め込みます。受信者は、受信したノンスを復号化中に初期化ベクトル (IV) として使用します。</p></li>
<li><p>各整合性ノンスの長さは 16 バイトです。これは、受信したメッセージの nonce を 1 ずつインクリメントすることで、その nonce から導出されます。</p></li>
</ul>
</li>
<li><p>リレー攻撃に対抗するには、すべてのノンスが一意である必要があり、ネットワーク内でいつでもどのメッセージに対してもノンスを再利用してはなりません。</p></li>
</ul>
<hr class="docutils">
</div>
<div class="section" id="ble-gatt-model">
<span id="id2"></span><h3>BLE GATT モデル</h3>
<p><strong>UWBS サービス</strong> UUID は <strong>680c21d9-c946-4c1f-9c11-baa1c21329e7</strong> です。すべての特性値は、BLE 仕様が示唆するリトル エンディアンとしてエンコードされます。</p>
<hr class="docutils">
<div class="section" id="uwbs-characteristics">
<h4>UWBS の特性</h4>
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
<tr class="row-even"><td><p>Std.GAP サービス、ラベル <strong>0x2A00</strong></p></td>
<td><p>ラベル</p></td>
<td><p>Var</p></td>
<td><p>UTF-8 でエンコードされた文字列</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>e6bfa234-
6758-11e9-
979f-5b2
4c4603eb8</strong></p></td>
<td><p>API リクエスト</p></td>
<td><p>Var 最大 50 バイト</p></td>
<td><p>メッセージヘッダー + TLV エンコードされた API リクエスト</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p><strong>e8573d96-
6758-11e9-
8860-cb4
385c24b83</strong></p></td>
<td><p>API レスポンス</p></td>
<td><p>Var 最大 273 バイト</p></td>
<td><p>メッセージヘッダー + TLV エンコードされた API 応答</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>003bbdf2-
c634-4b3d-
ab56-7ec889
b89a37</strong></p></td>
<td><p>API イベント</p></td>
<td><p>Var 最大 273 バイト</p></td>
<td><p>メッセージ ヘッダー + TLV エンコードされた API イベント</p></td>
<td><p>RO</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>ラベルの特性は特別なものです。これは、標準の名前特性 (0x2A00) の下にある標準の必須 GAP サービス (0x1800) の一部です。</p>
</div>
<hr class="docutils">
</div>
<div class="section" id="message-encoding">
<span id="messageencoding"></span><h4>メッセージのエンコーディング</h4>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 37%">
<col style="width: 26%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>アイテム</p></th>
<th class="head"><p>長さ</p></th>
<th class="head"><p>ペイロード</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>トランスポートヘッダー</strong></p></td>
<td><p>2バイト</p></td>
<td><p>インデックス (1 バイト) 合計 (1 バイト)</p></td>
</tr>
<tr class="row-odd"><td><p><strong>ノンス</strong></p></td>
<td><p>16バイト</p></td>
<td><p>メッセージ nonce、セキュリティがオフになっている場合は関係ありません</p></td>
</tr>
<tr class="row-even"><td><p><strong>mic/mac</strong></p></td>
<td><p>2バイト</p></td>
<td><p>暗号化が有効な場合はメッセージの整合性チェック、暗号化が無効な場合はペイロードの単純なバイト数の合計</p></td>
</tr>
<tr class="row-odd"><td><p><strong>ペイロード</strong></p></td>
<td><p>0 ～ 255バイト</p></td>
<td><p>値または TLV エンコードされたフレーム (特定の特性に応じて)</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="operation-mode">
<span id="operationmode"></span><h4>動作モード</h4>
<p>API リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-get#leaps-cfg-get"><span class="std std-ref">leaps_cfg_get</span></a> を使用して、現在の設定を読み取ります。 UWBS 構成を設定するには、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set#leaps-cfg-anchor-set"><span class="std std-ref">leaps_cfg_anchor_set</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set#leaps-cfg-tag-set"><span class="std std-ref">leaps_cfg_tag_set</span></a> API リクエストを使用します。</p>
</div>
<hr class="docutils">
<div class="section" id="location-data">
<h4>位置データ</h4>
<p>API リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-loc-get#leaps-loc-get"><span class="std std-ref">leaps_loc_get</span></a> を使用して、位置、距離、またはその両方を含む位置データを読み取ります。 UWBS 位置のみを操作するには、リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-pos-set#leaps-pos-set"><span class="std std-ref">leaps_pos_set</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-pos-get#leaps-pos-get"><span class="std std-ref">leaps_pos_get</span></a> を使用します。</p>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> によってイベント <code class="docutils literal notranslate"><span class="pre">位置データ準備完了</span></code> を有効にし、特性 <code class="docutils literal notranslate"><span class="pre">イベント</span></code> に関する通知を受信して​​、UWBS から現在位置と距離を自動的に取得します。</p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>位置データのエンコーディング、特性 <code class="docutils literal notranslate"><span class="pre">イベント</span></code> の BLE 通知として受信</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="4"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>int32_t - リトルエンディアン、ミリメートル単位の X 座標です</p></td>
<td><p>int32_t - リトルエンディアン、y 座標 (ミリメートル単位)</p></td>
<td><p>int32_t - リトルエンディアン、ミリメートル単位の Z 座標です</p></td>
<td><p>uint8_t- は位置品質係数です。パーセント (0 ～ 100)</p></td>
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
<div class="line">タイプ 0x40 はリクエスト/コマンドを意味します状態</div>
<div class="line">タイプ 0x41 は位置を意味します</div>
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
<tr class="row-odd"><th class="head" colspan="8"><p>前のテーブルのフレームの残り</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="6"><p>値</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><p>uint8_t - 値にエンコードされた距離の数</p></td>
<td><p>uint16_t - UWB アドレスリトルエンディアンで</p></td>
<td><p>uint32_t - リトルエンディアンでのミリメートル単位の距離</p></td>
<td><p>uint8_t - パーセント単位の距離品質係数 (0 ～ 100)</p></td>
<td><p>標準の 13 バイト形式での位置 (x、y、z、qf)</p></td>
<td><p>...</p></td>
</tr>
<tr class="row-even"><td><p>0x49</p></td>
<td><p>0x51</p></td>
<td><p>0x04</p></td>
<td colspan="4"><p>位置と距離番号。 1</p></td>
<td><p>nr. 2, 3, 4</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x49 は測距アンカーの位置と距離を意味します</p>
<hr class="docutils">
</div>
<div class="section" id="user-data">
<span id="userdata"></span><h4>ユーザーデータ</h4>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> によってイベント <code class="docutils literal notranslate"><span class="pre">ユーザー</span> <span class="pre">データ準備完了</span></code> を有効にし、特性 <code class="docutils literal notranslate"><span class="pre">イベント</span></code> に関する通知を受信して​​、UWBS から BLE ユーザー データを自動的に受信します。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>BLE ユーザー データ エンコーディング、特性 <code class="docutils literal notranslate"><span class="pre">イベント</span></code> の BLE 通知として受信</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>最大 128 バイト</p></td>
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
<span id="id3"></span><h4>ノードID</h4>
<p>UWBS のアドレスを取得するには、要求 <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-node-id-get#leaps-node-id-get"><span class="std std-ref">leaps_node_id_get</span></a> を使用します。</p>
</div>
<div class="section" id="network-id">
<span id="networkid"></span><h4>ネットワークID</h4>
<p>リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-panid-set#leaps-panid-set"><span class="std std-ref">leaps_panid_set</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-panid-get#leaps-panid-get"><span class="std std-ref">leaps_panid_get</span></a> を使用して、ネットワークの ID を操作します。</p>
</div>
<div class="section" id="reset-or-reboot">
<span id="id4"></span><h4>リセットまたは再起動</h4>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a> や <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-factory-reset#leaps-factory-reset"><span class="std std-ref">leaps_factory_reset</span></a> などの UWBS をリセットするリクエストは、リセット前に BLE セントラルを切断します。中央は再度接続する前に 1 秒待つ必要があります。</p>
</div>
<div class="section" id="anchor-list">
<span id="id5"></span><h4>アンカーリスト</h4>
<p>リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get#leaps-anchor-list-get"><span class="std std-ref">leaps_anchor_list_get</span></a> を参照してください。</p>
</div>
<div class="section" id="device-info">
<span id="deviceinfo"></span><h4>デバイス情報</h4>
<p>ファームウェア、ハードウェア、構成のバージョンを読み取るには、リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get#leaps-dev-info-get"><span class="std std-ref">leaps_dev_info_get</span></a> を参照してください。</p>
</div>
<div class="section" id="update-rate">
<span id="updaterate"></span><h4>更新レート</h4>
<p>タグ ノードの更新レートを変更するには、リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-set#leaps-upd-rate-set"><span class="std std-ref">leaps_upd_rate_set</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-get#leaps-upd-rate-get"><span class="std std-ref">leaps_upd_rate_get</span></a> を参照してください。</p>
<hr class="docutils">
</div>
</div>
<div class="section" id="auto-positioning">
<span id="autopositioning"></span><h3>オートポジショニング</h3>
<p>BLE API を使用すると、自動位置決めプロセスを開始することもできます。 CDEV 上で自動位置決めプロセスが終了します (位置が計算されます)。 BLE API を使用すると、距離の測定と取得を開始できるようになります。ワークフローは次のとおりです。</p>
<ol class="arabic">
<li><p>測る：</p>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>イニシエータが見つかり、検証されました (ノードは <em>イニシエータとして構成されている</em> だけでなく、<em>実際のイニシエータ</em> である必要があります。<a class="reference internal" href="#operationmode"><span class="std std-ref">動作モード</span></a> と <a class="reference internal" href="#bleadvertisements"><span class="std std-ref">BLE アドバタイズメント</span></a> を参照してください)</p></li>
<li><p>イニシエーターに接続します。</p></li>
<li><p>まだ有効になっていない場合は、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> によって <code class="docutils literal notranslate"><span class="pre">location</span> <span class="pre">Ready</span></code> イベントを有効にします (特性に関する BLE cccd 通知を有効にすることを忘れないでください)。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-autopos-start#leaps-autopos-start"><span class="std std-ref">leaps_autopos_start</span></a> リクエストにより自動位置決めを開始します。</p></li>
<li><p>イニシエーターからすべての測定距離を受信しました。測定距離をマトリックスに保存します。</p></li>
<li><p>イニシエータから切断します。</p></li>
<li><p>他のすべての (非イニシエーター) ノードからの距離を取得します。</p></li>
</ol>
<blockquote>
<div><ol class="lowerroman simple">
<li><p>接続</p></li>
<li><p>API リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-loc-get#leaps-loc-get"><span class="std std-ref">leaps_loc_get</span></a> を使用して UWBS から位置データを取得し、マトリックスまでの距離を保存します。</p></li>
<li><p>切断</p></li>
</ol>
</div></blockquote>
</div></blockquote>
</li>
<li><p>測定距離を評価し、直交性を確認し、位置を計算します。</p></li>
<li><p>ユーザーのリクエストに応じて、計算された位置をノードに保存します (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-pos-set#leaps-pos-set"><span class="std std-ref">leaps_pos_set</span></a> リクエストを使用します)。</p></li>
</ol>
<hr class="docutils">
</div>
<div class="section" id="ble-advertisements">
<span id="bleadvertisements"></span><h3>BLE アドバタイズメント</h3>
<p>BLE アドバタイズメントは、周辺デバイスがその存在を他のデバイスに知らせる一般的な方法です。 BLE 仕様によれば、ブロードキャスト ペイロードは 3 つの要素、つまり [長さ、タイプ、&lt;データ&gt;] で構成されます。</p>
<p>UWBS は、<strong>存在と動作モード</strong> に関する基本情報をブロードキャストします。 BLE アドバタイズメントは、位置情報を含めるのに十分な長さではありません。</p>
<p>BLE アドバタイズメントでは、31 バイトが使用されます。</p>
<ul class="simple">
<li><p>3 バイトは必須フラグです (1 つの AD トリプレット)。</p></li>
<li><p>残りの 28 バイトは、アプリが AD レコードを埋めるために使用できます (各レコードには 2 バイトの長さ + タイプのオーバーヘッドがあります)</p></li>
</ul>
<div class="section" id="presence-broadcast">
<h4>プレゼンスブロードキャスト</h4>
<p>UWBS モジュールの BLE は、接続可能なアンダイレクト モードで動作します。これは、サービスの可用性と一部のサービス データを含むプレゼンス ブロードキャストをアドバタイズします。プレゼンス ブロードキャストは BLE アドバタイズメント フレーム構造に従い、28 バイトを使用して情報を表示します。デバイス名はスキャン応答に含まれており、アクティブなスキャンが必要です。</p>
<p>プレゼンス ブロードキャストとスキャン応答のエンコーディングについては、次の表で説明します。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>広告</strong></p></th>
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
<td><p>0x19 (25 dec)</p></td>
</tr>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>0x21 (12 月 33 日、サービスデータ)</p></td>
</tr>
<tr class="row-odd"><td rowspan="8"><p>値</p></td>
<td><p><strong>680c2 1d9-c946-4c1f-9c11-baa1c21329e7</strong> (16 バイト)</p></td>
</tr>
<tr class="row-even"><td><p>PAN ID (2バイト)</p></td>
</tr>
<tr class="row-odd"><td><p>节点 ID (2バイト)</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">标志（1 バイト）</div>
<div class="line">ビットレイアウト: OXSEIBUU O - 動作モード (タグ 0、アンカー 1)</div>
<div class="line">X - 控えめ</div>
<div class="line">S - security_enabled</div>
<div class="line">E - エラー表示</div>
<div class="line">I - initiator_enabled,</div>
<div class="line">B - ゲートウェイ有効</div>
<div class="line">UU - UWB モード: オフ (0)、パッシブ (1)、アクティブ (2)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>変更カウンタ (1 バイト) - UWBS の重要な内部状態が変更されるたびに変更カウンタが変更されます (構成など)。</p></td>
</tr>
<tr class="row-even"><td><p>UWB カウンタ (1 バイト) - 低電力デバイスによって使用されるカウントダウン カウンタ。 LP デバイスのこのカウンタが 0 に達すると、デバイスの UWB アクティビティが無効になります。アンカーは、デバイス上のこのカウンタが設定された最低水準点値を下回ったことを検出すると、デバイスに接続し、カウンタをリセットしてデバイスの UWB をアクティブに保ちます。</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">UWBS フラグ (1 バイト)</div>
<div class="line">ビットレイアウト: FUSR</div>
</div>
<div class="line-block">
<div class="line">F - ファームウェアのタイプ (2ビット、0=BLDR、1=ELDR、2=MAIN)</div>
<div class="line">U - UWB システム (2 ビット、0=LEAPS RTLS、1=FIRA)</div>
<div class="line">S - UWB サブシステム (2 ビット、0=UCI、1=NIQ)</div>
<div class="line">R - 控えめ、</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>顧客情報（1バイト） 顧客固有の情報</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>スキャン応答</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x16 (22 dec)</p></td>
</tr>
<tr class="row-odd"><td><p>タイプ</p></td>
<td><p>0x09 (デバイス名、スキャン応答パケットに配置され、アクティブ スキャンを使用して検出します)</p></td>
</tr>
<tr class="row-even"><td><p>値</p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">LEAPS</span></code> プレフィックス (5 文字) + 16 進形式の完全なノード ID (16 文字)</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="section" id="firmware-update">
<span id="firmwareupdate"></span><h3>ファームウェアのアップデート</h3>
<p>ファームウェア更新機能は、UWBS のファームウェアを更新するために使用されます。このセクションでは、BLE インターフェイス上の制御とデータ フローについて説明します。ファームウェア更新プロセスの詳細については、API リクエスト <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> を参照してください。</p>
<div class="section" id="updating-the-fw-binary">
<h4>FWバイナリを更新しています</h4>
<ol class="arabic simple">
<li><p>CDEV は UWBS に接続します。</p></li>
<li><p>CDEV は <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> によって FW の更新を開始します。</p></li>
<li><p>UWBS がステータス <code class="docutils literal notranslate"><span class="pre">ok</span></code> で応答した場合、CDEV はこの手順をスキップできます。UWBS がステータス <code class="docutils literal notranslate"><span class="pre">again</span></code> で応答した場合、CDEV は UWBS をリセットし、UWBS の再起動後に再接続し、CDEV は更新を再度開始します。UWBS がステータス <code class="docutils literal notranslate"><span class="pre">not</span> <span class="pre">permitted</span></code> で応答した場合、FW の更新は不可能です。UWBS で FW の更新が無効になっている可能性があります。</p></li>
<li><p>CDEV は <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> によって FW のチャンクを送信します。</p></li>
<li><p>CDEV は、最後のチャンクが正常に送信された後、UWBS をリセットします。</p></li>
</ol>
</div>
<div class="section" id="updating-the-eldr-binary">
<h4>ELDR バイナリを更新しています</h4>
<ol class="arabic simple">
<li><p>CDEV は、UWBS の再起動後に再接続します。</p></li>
<li><p>CDEV は <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> によって ELDR の更新を開始します。</p></li>
<li><p>CDEV は <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> によって ELDR のチャンクを送信します。</p></li>
<li><p>CDEV は、最後のチャンクが正常に送信された後、UWBS をリセットします。</p></li>
<li><p>CDEV は UWBS の再起動後に接続し、FW 情報を観察してファームウェアが更新されて実行中であることを確認できます。</p></li>
</ol>
<p>CDEV は、UWBS の自動切断を防ぐために、UWBS に接続するたびに <strong>API 応答</strong> 特性に関する通知を有効にする必要があります (<a class="reference internal" href="#autodisconnect"><span class="std std-ref">自動切断</span></a> を参照)。</p>
<p>ファームウェアのアップデート中に UWBS が突然切断された場合は、アップデートの現在の段階に応じて、ステップ 7 またはステップ 1 からやり直すことで処理できます。</p>
</div>
<div class="section" id="transmitting-the-fw-binary">
<h4>FWバイナリを送信しています</h4>
<p>データは、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> によってファームウェアのアップデートが開始された後、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> によって UWBS に転送されます。 UWBS は、サイズとオフセットを応答にエンコードすることで、CDEV にどのデータ バッファーが必要かを正確に伝えます。 CDEV は、応答なしの書き込みを使用して、要求されたバッファ チャンクの送信を開始するため、完全な往復は必要ありません。 BLE 転送の MTU に要求されたバッファ サイズが含まれない場合、各チャンクは複数の BLE 転送で送信される可能性があることに注意してください。チャンクは次のもので構成されます:</p>
<ul class="simple">
<li><p>データ: UWBS によって要求されたサイズの FW バッファ (240)</p></li>
<li><p>相対オフセット (最初から): 4 バイト。</p></li>
</ul>
<p>データ バッファーが送信された後、CDEV はさらなる命令を待ちます。送信中、UWBS は通常、ファームウェアの連続バイト シーケンスを取得するために、データ バッファを 1 つずつ順番に要求します。現在のバッファ送信が失敗するなど、例外が発生した場合、ノードは予期しないバッファを要求する可能性があります。</p>
<p>エラーが発生するとファームウェアのアップデートが停止されるため、再度開始する必要があります。</p>
</div>
<div class="section" id="finishing-the-transmission">
<h4>送信を終了しています</h4>
<p>最後のデータ チャンクが正常に受信されると、UWBS は CDEV に完全なファームウェア バイナリを受信したことを通知します。それを受信すると:</p>
<ol class="arabic simple">
<li><p>CDEV は、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a> コマンドによって UWBS をリセットします。これにより、UWBS が CDEV から切断されます。</p></li>
<li><p>CDEV は 1 秒待機します。</p></li>
<li><p>CDEV は UWBS に再度接続してファームウェアのステータスを確認しようとします (<a class="reference internal" href="#deviceinfo"><span class="std std-ref">デバイス情報</span></a> を参照)。</p></li>
</ol>
</div>
</div>
</div>
<div class="section" id="appendix-bibliography">
<h2>付録 - 書誌</h2>
<ol class="arabic simple">
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/question/55309/connection-issues-with-android-60-marshmallow-and-nexus-6/">https://devzone.nordicsemi.com/question/55309/connection-issues-with-android-60-marshmallow-and-nexus-6/</a></p></li>
<li><p><a class="reference external" href="http://stackoverflow.com/questions/37151579/schemes-for-streaming-data-with-ble-gatt-characteristics">http://stackoverflow.com/questions/37151579/schemes-for-streaming-data-with-ble-gatt-characteristics</a></p></li>
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/nordic/nordic-blog/b/blog/posts/what-to-keep-in-mind-when-developing-your-ble-andr">BLE Android アプリを開発するときに留意すべきこと</a></p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide#leaps-rtls-integration-guie"><span class="std std-ref">統合ガイド</span></a></p></li>
</ol>
</div>
<div class="section" id="appendix-migration-from-dwm-ble-api">
<h2>付録 - DWM BLE API からの移行</h2>
<p>次の表は、以前の DWM BLE API と比較した LEAPS BLE API の変更点をまとめたものです。これは、LEAPS BLE API への移行を容易にすることを目的としています。DWM BLE API で使用されていた以前の GATT モデルは、以前のモデルよりも特性の少ない要求/応答モデルに置き換えられました。セクション <a class="reference internal" href="#blecommunicationwithuwbs"><span class="std std-ref">UWBS との BLE 通信</span></a> を参照してください。</p>
<div class="section" id="former-ble-gatt-model">
<h3>以前の BLE GATT モデル</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 37%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><div class="line-block">
<div class="line"><strong>名前</strong></div>
<div class="line"><strong>以前の GATT 特性</strong></div>
</div>
</th>
<th class="head"><p><strong>DWM と LEAPS の比較</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ラベル</p></td>
<td><div class="line-block">
<div class="line">DWM: <em>標準の名前特性 (0x2A00) の下にある標準の必須 GAP サービス (0x1800)</em></div>
<div class="line">LEAPS: 変更なし、同じまま</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>動作モード</p></td>
<td><div class="line-block">
<div class="line">DWM: UWBS の現在の構成は特別なファイルに含まれていました</div>
<div class="line">特徴</div>
<div class="line">LEAPS: UWBS の設定の読み取り/書き込みについては <a class="reference internal" href="#operationmode"><span class="std std-ref">動作モード</span></a> を参照、ファームウェア 1 とファームウェア間の切り替えについては <a class="reference internal" href="#firmwareupdate"><span class="std std-ref">ファームウェアのアップデート</span></a> を参照してください。 2.</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>更新レート</p></td>
<td><p>DWM: 現在の更新レートは特別な特性 LEAPS に含まれていました: 現在の更新レート設定の読み取り/書き込みについては、セクション <a class="reference internal" href="#updaterate"><span class="std std-ref">更新レート</span></a> を参照してください</p></td>
</tr>
<tr class="row-odd"><td><p>ネットワークID</p></td>
<td><p>DWM: 現在のネットワーク ID は特殊特性 LEAPS に含まれていました: 現在のネットワーク ID の読み取り/書き込みについては、<a class="reference internal" href="#networkid"><span class="std std-ref">ネットワークID</span></a> セクションを参照してください</p></td>
</tr>
<tr class="row-even"><td><p>位置データモード</p></td>
<td><p>DWM: <code class="docutils literal notranslate"><span class="pre">位置データ</span></code> と呼ばれる特別な特性の設定として使用されます。 LEAPS: もう必要ありません。UWBS から位置を取得するには <a class="reference internal" href="#userdata"><span class="std std-ref">ユーザーデータ</span></a> を参照し、自動位置決め手順を実行するときに距離を取得するには <a class="reference internal" href="#autopositioning"><span class="std std-ref">オートポジショニング</span></a> セクションを参照してください。</p></td>
</tr>
<tr class="row-odd"><td><p>位置データ</p></td>
<td><p>DWM: UWBS の現在位置 (自動位置決め手順を実行するときの距離も含まれます) は特別な特性 LEAPS に含まれていました: 位置と距離を取得するには、<em>位置データ</em> セクションを参照してください</p></td>
</tr>
<tr class="row-even"><td><p>永続的な位置</p></td>
<td><div class="line-block">
<div class="line">DWM: 永続化された位置は特殊な特性を介して書き込まれました</div>
<div class="line">LEAPS: UWBS に永続的な位置を書き込む方法については、<a class="reference internal" href="#userdata"><span class="std std-ref">ユーザーデータ</span></a> セクションを参照してください。</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>デバイス情報</p></td>
<td><div class="line-block">
<div class="line">DWM: 構成、ノード ID、ファームウェアなどのデバイス情報</div>
<div class="line">バージョンは特殊な特性から読み取られました</div>
<div class="line">LEAPS: ノードのファームウェアのバージョンを読み取るには <a class="reference internal" href="#deviceinfo"><span class="std std-ref">デバイス情報</span></a> セクションを参照してください。ノードの ID を読み取るには <a class="reference internal" href="#node-id"><span class="std std-ref">ノードID</span></a> セクションを参照してください。ノードの設定を読み取るには <a class="reference internal" href="#operationmode"><span class="std std-ref">動作モード</span></a> セクションを参照してください。</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>統計</p></td>
<td><p>DWM: 統計は特別な特性に含まれていました LEAPS: 統計はサポートされなくなりました</p></td>
</tr>
<tr class="row-odd"><td><p>MACスタッツ</p></td>
<td><p>DWM: MAC 統計は特別な特性に含まれていました LEAPS: MAC 統計はサポートされなくなりました</p></td>
</tr>
<tr class="row-even"><td><p>クラスター情報</p></td>
<td><p>DWM: UWB クラスター情報は特殊な特性に含まれていました LEAPS: クラスター情報はサポートされなくなりました</p></td>
</tr>
<tr class="row-odd"><td><p>アンカーリスト</p></td>
<td><div class="line-block">
<div class="line">DWM: 隣接アンカー ノードの現在のリストは特殊な特性に含まれていました</div>
<div class="line">LEAPS: アンカー ノードの現在のリストを読み取るには、セクション <a class="reference internal" href="#anchor-list"><span class="std std-ref">アンカーリスト</span></a> を参照してください。</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>FWアップデートのプッシュ</p></td>
<td><div class="line-block">
<div class="line">DWM: 新しいファームウェアを UWBS に転送するためにも使用される特別な特性を介してファームウェアの更新が開始されました。</div>
<div class="line">LEAPS: ファームウェアのアップデートを開始する方法とファームウェアをノードに転送する方法については、セクション <a class="reference internal" href="#firmwareupdate"><span class="std std-ref">ファームウェアのアップデート</span></a> を参照してください。</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>FW アップデートのポーリング</p></td>
<td><div class="line-block">
<div class="line">DWM: UWBS は、この特性に関する通知を使用して、ファームウェアの更新中に BLE セントラルに応答しました</div>
<div class="line">LEAPS: ファームウェアのアップデートの実行方法については、<a class="reference internal" href="#firmwareupdate"><span class="std std-ref">ファームウェアのアップデート</span></a> セクションを参照してください。</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>切断</p></td>
<td><div class="line-block">
<div class="line">DWM: BLE セントラルは特殊な特性を介して切断されます。これは API のバグに対処するための回避策でした</div>
<div class="line">LEAPS: バグが修正されているためサポートされていません</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
