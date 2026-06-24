---
title: "API の汎用データ型"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/api-generic-data-types"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types/"
order: 144
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <section id="api-generic-data-types">
<h1>API の汎用データ型</h1>
<section id="id">
<h2>ID</h2>
<p>ノード ID。これは一意の 64 ビット数値です。これは、固定プレフィックス 0xDECA、MCU 固有チップ ID、および DW1000/DW3000 固有パーツ ID から派生したもので、形式は 0xDECA + 28 ビット MCU 固有チップ ID + 20 ビット DW1000 固有パーツ ID です。</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text"><strong>id</strong> = 64 ビット整数</p>
</div>
</div>
<hr class="docutils">
</section>
<section id="status-code">
<span id="statuscode"></span><h2>ステータスコード</h2>
<p>すべてのコマンドによって返されるステータス コード。</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text">‘0’ (<em>ok</em>)</p></li>
<li><p class="sd-card-text">‘1’ (<em>不明なコマンドまたは壊れた TLV フレーム</em>)</p></li>
<li><p class="sd-card-text">'2' (<em>内部エラー</em>)</p></li>
<li><p class="sd-card-text">'3' (<em>無効なパラメータ</em>)</p></li>
<li><p class="sd-card-text">‘4’ (<em>ビジー</em>)</p></li>
<li><p class="sd-card-text">‘5’ (<em>操作は許可されていません</em>)</p></li>
<li><p class="sd-card-text">'6' (<em>チェックサムエラー</em>）</p></li>
<li><p class="sd-card-text">'7' (<em>IO エラー</em>)</p></li>
<li><p class="sd-card-text">'8' (<em>サポートされていません</em>)</p></li>
<li><p class="sd-card-text">‘9’ (<em>リセットが必要で、コマンドを再度送信する必要があります</em>)</p></li>
</ul>
</div>
</div>
<hr class="docutils">
</section>
<section id="position">
<span id="id1"></span><h2>位置</h2>
<p>ノードの位置 (アンカーまたはタグ)。</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>In CARTESIAN coordinate, position = x, y, z, pqf</strong> (<em>position coordinates</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>x</strong> = 32 ビット整数 (<em>単位: ミリメートル</em>)</p></li>
<li><p class="sd-card-text"><strong>y</strong> = 32 ビット整数 (<em>単位: ミリメートル</em>)</p></li>
<li><p class="sd-card-text"><strong>z</strong> = 32 ビット整数 (<em>単位: ミリメートル</em>)</p></li>
<li><p class="sd-card-text"><strong>pqf</strong> = 8 ビット整数 (<em>パーセント単位の位置品質係数</em>)</p></li>
</ul>
</li>
<li><p class="sd-card-text"><strong>In WGS84 coordinate, position = lat, lon, 0, pqf</strong> (<em>position coordinates</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>lat</strong> = 32-bit integer (WGS84 latitude x10^7)</p></li>
<li><p class="sd-card-text"><strong>lon</strong> = 32-bit integer (WGS84 latitude x10^7)</p></li>
<li><p class="sd-card-text"><strong>0</strong></p></li>
<li><p class="sd-card-text"><strong>pqf</strong> = 8 ビット整数 (<em>パーセント単位の位置品質係数</em>)</p></li>
</ul>
</li>
</ul>
</div>
</div>
<hr class="docutils">
</section>
<section id="gpio-idx">
<span id="gpioidx"></span><h2>gpio_idx</h2>
<p>ユーザーが入力 PX.Y によって使用できる GPIO ピンのインデックス。ここで、:</p>
<ul class="simple">
<li><p>X: ポート番号</p></li>
<li><p>Y: ピンのインデックス</p></li>
</ul>
<p>お願いします以下のリストで特定のデバイスの番号/インデックスを参照してください。</p>
<ul class="simple">
<li><p>DWM1001: P0.08, P0.12, P0.13, P0.15, P0.23, P0.27</p></li>
<li><p>DWM3001: P0.06, P0.12, P0.13, P0.17, P0.20, P0.21, P1.00, P1.01, P1.05, P1.09</p></li>
<li><p>LC13/LC14 (2AB): P0.11, P0.12, P0.13, P0.14, P1.7, P1.14</p></li>
</ul>
</section>
<hr class="docutils">
<section id="fw-version">
<h2>fw_version</h2>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>fw_version</strong> = <strong>maj</strong>、<strong>min、patch、ver</strong> (<em>ファームウェア バージョン</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>maj</strong> = 8 ビットの数値（<em>選考科目</em>）</p></li>
<li><p class="sd-card-text"><strong>min</strong> = 8 ビット数値 (<em>MINOR</em>)</p></li>
<li><p class="sd-card-text"><strong>パッチ</strong> = 8 ビット数値 (<em>PATCH</em>)</p></li>
<li><p class="sd-card-text"><strong>ver</strong> = res, var</p></li>
<li><p class="sd-card-text">: <strong>res</strong> = 4 ビット数値 (<em>予約済み</em>)</p></li>
<li><p class="sd-card-text"><strong>var</strong> = 4 ビット数値 (<em>VARIANT</em>)</p></li>
</ul>
</li>
</ul>
</div>
</div>
</section>
</section>


           </div>
