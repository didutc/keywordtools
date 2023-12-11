<!--@layout(/layout/basic/layout.html)-->
<div module="product_detail">
    
    <!--@css(/css/module/product/detail.css)-->
    <!--@js(/js/module/product/detail.js)-->
    <!--
		$coupon_download_page = /coupon/coupon_productdetail.html
    -->
    <div id="titleArea">
        <h2>상품상세 정보</h2>
        <span module="Layout_MobileAction">
            <a href="#none" onclick="{$go_back}"><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/layout/btn_back.gif" width="33" alt="뒤로가기"></a>
        </span>
    </div>

    <div class="overview" module="product_image">
        <!--@js(/js/module/product/image.js)-->
        <div class="topLogo {$supply_link_display|display}">
            <span>{$supply_top_logo}</span>
            <a href="#none" onclick="{$supply_go_action}"><img src="{$supply_go_img}" alt="공급사 바로가기" /></a>
        </div>

        <div class="prdImgView"  data-price="{$product_custom|striptag}^{$product_price|striptag}^{$prd_price_sale|striptag}">
            <p class="prdImg">
                 <a href="#none" id="prdDetailImg" data-param="{$zoom_param}" >
                    <img src="{$big_img}" class="bigImage" alt="{$seo_alt_tag}"><span module="product_Imagestyle"><span class="prdIcon {$icon_class_name}" style="background-image:url('{$icon_url}');"></span></span>
                 </a>
            </p>
            <div module="Product_mobileImage">
                <!--@css(/css/module/product/mobileImage.css)-->
                <!--
                    $swipe = yes
                -->
                <ul>
                    <li data-param="{$zoom_param}">
                        <p class="thumbnail">
                            <img src="{$big_img}" class="{$thumb_img_class}" alt=""><span module="product_Imagestyle"><span class="prdIcon {$icon_class_name}" style="background-image:url('{$icon_url}');"></span></span>
                        </p>
                    </li>
                    {$aAddImage}
                </ul>
            </div>
        </div>
        <div class="color {$colorchip_display|display}">
            <div module="product_Colorchip">
                <span class="chips" style="background-color:{$color};"></span>
                <span class="chips" style="background-color:{$color};"></span>
            </div>
        </div>
        <!--@import(/product/shoppQ/hashtag.html)-->
        <div class="likeButton {$disp_likeprd_class}">
            <button type="button"><span class="title">좋아요</span>{$disp_likeprd_icon}<span class="count">{$disp_likeprd_count}</span></button>
        </div>
    </div>
    <!--상품명-->
    <h1 class="name">{$name}</h1>
    <!--요약설명-->
    <div class="summary">{$summary_desc}</div>
    <div class="price_calc">        
        <!--판매가-->
        <div class="{$product_price_display|display}">
            <div class="price">
                <strong class="sale"><span id="span_product_price_text" class="{$product_price_class} {$product_sale_strike}">{$product_price}</span>{$txt_product_price}</strong><span id="span_product_price_text">{$product_tax_type_text}</span> <span class="soldOut"></span>
                <button type="button" class="btnRestockSms {$sms_restock_display|display}" onClick="{$action_sms_restock}">재입고 알림 SMS</button>
                <button type="button" class="btnRestockMail {$restock_email_display|display}" onClick="{$action_email_restock}">재입고 알림 메일</button>
            </div>
        </div>
        <!--소비자가-->
        <div class="custom">{$product_custom|numberformat}</div>
        <!--할인율-->
        <div class="dc_rate"></div>
        <!--리뷰-->
        <div class="review">리뷰 {$review_count}개</div>
    </div>
    
    <p class="prdIcon">{$soldout_icon}{$stock_icon}{$recommend_icon}{$new_icon}{$img_mileage_icon}{$product_icons}{$today_arrival_icon}{$pickup_icon}{$benefit_icons}</p>
    <div class="prdDesc">
        <div class="ec-base-table gClearCell">
            <table border="1">
                <caption>상품 정보</caption>
                <colgroup>
                    <col style="width:100px;">
                    <col style="width:auto;">
                </colgroup>
                <tbody class="priceArea">
<!--
                    <tr class="{$product_price_display|display}">
                        <th scope="row">판매가</th>
                        <td class="price">
                            <strong class="sale"><span id="span_product_price_text" class="{$product_price_class} {$product_sale_strike}">{$product_price}</span>{$txt_product_price}</strong><span id="span_product_price_text">{$product_tax_type_text}</span> <span class="soldOut"></span>
                            <button type="button" class="btnRestockSms {$sms_restock_display|display}" onClick="{$action_sms_restock}">재입고 알림 SMS</button>
                            <button type="button" class="btnRestockMail {$restock_email_display|display}" onClick="{$action_email_restock}">재입고 알림 메일</button>
                        </td>
                    </tr>
-->
                    <tr class="{$product_sale_display|display}" id="span_product_price_mobile_p_line">
                        <th scope="row">할인판매가</th>
                        <td class="price" ><strong class="sale"><span id="span_product_price_mobile_text" class="{$product_price_class}">{$product_price_mobile}</span>{$txt_product_price_mobile}</strong></td>
                    </tr>
                    <tr class="{$optimum_discount_price_display|display}" id="span_optimum_discount_price_mobile_p_line">
                        <th scope="row">최적할인가</th>
                        <td class="price" ><strong class="sale"><span id="span_optimum_discount_price_mobile_text" class="{$optimum_discount_price_class}">{$optimum_discount_price_mobile}</span>{$txt_optimum_discount_price_mobile}</strong></td>
                    </tr>
                </tbody>
                <tbody>
                    <tr id="span_product_price_mobile_d_line" class="{$product_sale_display|display}">
                        <th scope="row">할인금액</th>
                        <td><span class="discount">총 할인금액 {$mobile_dc_price|number}원<br>(모바일할인금액 {$mobile_dc_price|number}원)</span></td>
                    </tr>
                    <tr class="mileage {$mileage_display|display}">
                        <th scope="row">{$mileage_name}</th>
                        <td>{$mileage_list}</td>
                    </tr>
                    <tr class="{$naver_mileage_display|display}">
                        <th>제휴적립금</th>
                        <td>{$naver_mileage_title} {$naver_mileage_rate}</td>
                    </tr>
                </tbody>
                <tbody class="delvtype">
                    <tr class="{$delivery_display|display}">
                        <th scope="row">배송방법</th>
                        <td>{$delivery}</td>
                    </tr>
                    <tr class="{$delivery_price_display|display}">
                        <th scope="row">배송비</th>
                        <td>{$delivery_price}</td>
                    </tr>
                    <tr class="{$additional_description_translated_display|display}">
                        <th scope="row">상품 추가설명 번역정보</th>
                        <td>{$additional_description_translated}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="ec-base-table gClearCell regularDelivery {$regular_delivery_display|display}">
            <table border="1">
                <colgroup>
                   <col style="width:100px;">
                   <col style="width:auto;">
                </colgroup>
                <tbody>
                <tr>
                    <th scope="row">구매방법</th>
                    <td>
                        <label><span class="{$one_time_purchase_display|display}">{$regular_deliveryT}</span>정기배송 <span class="badge {$regular_delivery_discount_display|display}">{$max_discount_value} <i class="icoDown">할인</i></span></label>
                        <label class="{$one_time_purchase_display|display}">{$regular_deliveryF}1회구매</label>
                    </td>
                </tr>
                <tr class="{$regular_cycle_period|display}" id="{$regular_cycle_period_id}">
                    <td colspan="2" class="shippingCycle">
                        <strong class="title">배송주기</strong>
                        {$regularPeriod}
                        <div class="info {$regular_delivery_discount_display|display}" id="{$regular_delivery_discount_id}">
                        	<strong class="title">정기배송 할인 <span class="icoSave">save</span></strong>
                            <ul class="info" module="product_regularDiscount">
                                <li>{$discount_count} 결제 시 : {$discount_value} <span class="icoDown">할인</span></li>
                                <li>{$discount_count} 결제 시 : {$discount_value} <span class="icoDown">할인</span></li>
                            </ul>
                        </div>
                   </td>
                </tr>
                </tbody>
            </table>
        </div>

        <div class="ec-base-table typeWrite gClearCell">
            <table border="1" module="product_option">
                <!--
                $use_per_add_option = yes
                $default_option = yes
                -->
                <caption>상품 옵션</caption>
                <colgroup>
                    <col style="width:100px;">
                    <col style="width:auto;">
                </colgroup>
                <tbody>
                    <tr class="{$delvtype_display|display}">
                        <th scope="row">배송</th>
                        <td class="middle">
                            <label>{$form.delvtypeA}국내배송</label>
                            <label>{$form.delvtypeB}해외배송</label>
                        </td>
                    </tr>
                </tbody>

                <tbody module="product_option">
                    <tr>
                        <th scope="row">{$option_name}</th>
                        <td class="middle">{$form.option}<p class="value">{$option_desc}</p></td>
                    </tr>
                    <tr module="product_quantity" class="quantity">
                        <th scope="row">수량</th>
                        <td>
                            <div class="ec-base-qty">
                                <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                {$form.quantity}
                                <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                            </div>
                        </td>
                    </tr>
                </tbody>
                <tbody>
                    <tr module="product_addoption">
                        <th scope="row">{$add_option_name}</th>
                        <td class="middle">
                            {$form.add_option}
                            <span class="byte" title="현재글자수/최대글자수">[ <strong class="length">0</strong> / {$option_maxlength} ]</span>
                        </td>
                    </tr>
                </tbody>
                <tbody>
                    <tr class="{$option_push_button_display|display}" id="{$option_push_button_id}">
                        <td colspan="2" class="selectButton"><button type="button" class="btnStrong" onclick="{$action_push_button}">옵션 선택</button></td>
                    </tr>
                    <tr module="product_fileoption">
                        <th scope="row">{$file_option_name}</th>
                        <td class="fileInfo">
                            {$form.file_option}
                            <ul class="ec-base-help typeDash">
                                <li>파일은 최대 5개까지 {$file_option_limit}M 이하로 개별업로드 가능합니다.</li>
                            </ul>
                        </td>
                    </tr>
                    <!-- 다중선택형 -->
                    <tr class="quantity {$quantity_display|display}">
                        <th scope="row">수량</th>
                        <td>
                            <div class="ec-base-qty">
                                <a href="javascript:;" class="down {$quantity_down_class}" ><img id="{$quantity_down_id}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                {$form.quantity}
                                <a href="javascript:;" class="up {$quantity_up_class}"><img id="{$quantity_up_id}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                            </div>
                        </td>
                    </tr>
                    <!-- 단일선택형 -->
                    <tr module="product_quantity" class="quantity">
                        <th scope="row">수량</th>
                        <td>
                            <div class="ec-base-qty">
                                <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                {$form.quantity}
                                <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!--@import(/coupon/coupon_productdetail.html)-->

        <div class="sizeGuide {$size_guide_display|display}">
            <a href="#none" class="{$size_guide_class}" product_no="{$product_no}">사이즈 가이드</a>
        </div>


        <div class="productSet ec-base-fold theme1 selected eToggle" module="product_setproduct">
            <!--
            $use_per_add_option = yes
            -->
            <div class="title">
                <h2>세트상품</h2>
            </div>
            <div class="contents">
                <ul class="product">
                    <li>
                        <div class="information">
                            <div class="thumbnail"><a href="/product/detail.html?product_no={$product_no}"><img src="{$product_image}" alt="" id="{$image_id}"></a></div>
                            <p class="name">{$product_name} <span class="qty {$set_quantity_display|display}">({$set_quantity}개씩 구매되는 상품)</span></p>
                            <p class="price {$product_price_del}">{$product_price}<span id="span_product_tax_type_text">{$product_tax_type_text}</span></p>
                            <p class="salePrice {$product_sale_price_display|display}">{$product_sale_price}</p>
                            <div class="stock">
                                <span class="ec-base-label {$stock_quantity_display|display}"><a href="#none" class="btnNormal mini" {$bind_stock_quantity}>재고수량보기</a></span>
                                <span class="{$product_restock_button_display|display}"><a href="#none" class="btnNormal mini" {$product_restock_link}>재입고 알림 SMS</a></span>
                            </div>
                        </div>
                        <div class="option">
                            <table border="1" summary="">
                            <caption>옵션 정보</caption>
                            <colgroup>
                                <col style="width:105px;">
                                <col style="width:auto;">
                            </colgroup>

                            <tbody module="product_option">
                                <tr>
                                    <th scope="row">{$option_name}</th>
                                    <td>{$form.option}<p class="value">{$option_desc}</p></td>
                                </tr>
                                <tr module="product_quantity" class="quantity">
                                    <th scope="row">수량</th>
                                    <td>
                                        <div class="ec-base-qty">
                                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                            {$form.quantity}
                                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                            <tbody module="product_noneoption">
                                <tr>
                                    <th scope="row">상품선택</th>
                                    <td>{$form.noneoption}</td>
                                </tr>
                                <tr module="product_quantity" class="quantity">
                                    <th scope="row">수량</th>
                                    <td>
                                        <div class="ec-base-qty">
                                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                            {$form.quantity}
                                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                            <tbody>
                                <tr module="product_addoption">
                                    <th scope="row">{$add_option_name}</th>
                                    <td>
                                        {$form.add_option}
                                        <span class="byte" title="현재글자수/최대글자수">[ <strong class="length">0</strong> / {$option_maxlength} ]</span>
                                    </td>
                                </tr>
                            </tbody>
                            </table>
                        </div>
                        <div class="selectButton {$add_option_push_button_display|display}" id="{$add_option_push_button_id}"><button type="button" class="btnStrong" onclick="{$add_action_push_button}">옵션 선택</button></div>
                        <div class="description eToggle" id="eDescriptionToggle_{$product_no}">
                            <div class="ec-base-button gCenter"><button type="button" class="btnBasic icoToggle eProductDetailInfo" id="eProductDetailInfo_{$product_no}"><span>상품 추가정보 보기</span></button></div>
                            <div class="inner" id="product_description_{$product_no}"></div>
                        </div>
                        <div class="sizeGuide {$size_guide_display|display}"><a href="#none" class="{$size_guide_class}" product_no="{$product_no}">사이즈 가이드</a></div>
                    </li>
                    <li>
                        <div class="information">
                            <div class="thumbnail"><a href="/product/detail.html?product_no={$product_no}"><img src="{$product_image}" alt="" id="{$image_id}"></a></div>
                            <p class="name">{$product_name} <span class="qty {$set_quantity_display|display}">({$set_quantity}개씩 구매되는 상품)</span></p>
                            <p class="price {$product_price_del}">{$product_price}<span id="span_product_tax_type_text">{$product_tax_type_text}</span></p>
                            <p class="salePrice {$product_sale_price_display|display}">{$product_sale_price}</p>
                            <div class="stock">
                                <span class="ec-base-label {$stock_quantity_display|display}"><a href="#none" class="btnNormal mini" {$bind_stock_quantity}>재고수량보기</a></span>
                                <span class="{$product_restock_button_display|display}"><a href="#none" class="btnNormal mini" {$product_restock_link}>재입고 알림 SMS</a></span>
                            </div>
                        </div>
                        <div class="option">
                            <table border="1" summary="">
                            <caption>옵션 정보</caption>
                            <colgroup>
                                <col style="width:105px;">
                                <col style="width:auto;">
                            </colgroup>

                            <tbody module="product_option">
                                <tr>
                                    <th scope="row">{$option_name}</th>
                                    <td>{$form.option}<p class="value">{$option_desc}</p></td>
                                </tr>
                                <tr module="product_quantity" class="quantity">
                                    <th scope="row">수량</th>
                                    <td>
                                       <div class="ec-base-qty">
                                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                            {$form.quantity}
                                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                            <tbody module="product_noneoption">
                                <tr>
                                    <th scope="row">상품선택</th>
                                    <td>{$form.noneoption}</td>
                                </tr>
                                <tr module="product_quantity" class="quantity">
                                    <th scope="row">수량</th>
                                    <td>
                                        <div class="ec-base-qty">
                                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                            {$form.quantity}
                                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                            <tbody>
                                <tr module="product_addoption">
                                    <th scope="row">{$add_option_name}</th>
                                    <td>
                                        {$form.add_option}
                                        <span class="byte" title="현재글자수/최대글자수">[ <strong class="length">0</strong> / {$option_maxlength} ]</span>
                                    </td>
                                </tr>
                            </tbody>
                            </table>
                        </div>
                        <div class="selectButton {$add_option_push_button_display|display}" id="{$add_option_push_button_id}"><button type="button" class="btnStrong" onclick="{$add_action_push_button}">옵션 선택</button></div>
                        <div class="description eToggle" id="eDescriptionToggle_{$product_no}">
                            <div class="ec-base-button gCenter"><button type="button" class="btnBasic icoToggle eProductDetailInfo" id="eProductDetailInfo_{$product_no}"><span>상품 추가정보 보기</span></button></div>
                            <div class="inner" id="product_description_{$product_no}"></div>
                        </div>
                        <div class="sizeGuide {$size_guide_display|display}"><a href="#none" class="{$size_guide_class}" product_no="{$product_no}">사이즈 가이드</a></div>
                    </li>
                </ul>
                <dl module="product_quantity" class="quantity set">
                    <dt>수량</dt>
                    <dd>
                        <div class="ec-base-qty">
                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                            {$form.quantity}
                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                        </div>
                    </dd>
                </dl>
            </div>
        </div>


        <div class="productSet ec-base-fold theme1 selected eToggle" module="product_addproduct">
            <!--
            $use_per_add_option = yes
            -->
            <div class="title">
                <h2>추가구성상품</h2>
            </div>
            <div class="contents">
                <ul class="product">
                    <li>
                        <div class="information">
                            <div class="thumbnail"><a href="/product/detail.html?product_no={$product_no}"><img src="{$product_image}" alt="" id="{$image_id}"></a></div>
                            <p class="name">{$product_name}</p>
                            <p class="price {$product_price_del}">{$product_price}<span id="span_product_tax_type_text">{$product_tax_type_text}</span></p>
                            <p class="salePrice {$product_sale_price_display|display}">{$product_sale_price}</p>
                        </div>
                        <div class="option">
                            <table border="1" summary="">
                            <caption>옵션 정보</caption>
                            <colgroup>
                                <col style="width:105px;">
                                <col style="width:auto;">
                            </colgroup>

                            <tbody module="product_option">
                                <tr>
                                    <th scope="row">{$option_name}</th>
                                    <td>{$form.option}<p class="value">{$option_desc}</p></td>
                                </tr>
                                <tr module="product_quantity" class="quantity">
                                    <th scope="row">수량</th>
                                    <td>
                                       <div class="ec-base-qty">
                                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                            {$form.quantity}
                                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                            <tbody module="product_noneoption">
                                <tr>
                                    <th scope="row">상품선택</th>
                                    <td>{$form.noneoption}</td>
                                </tr>
                                <tr module="product_quantity" class="quantity">
                                    <th scope="row">수량</th>
                                    <td>
                                        <div class="ec-base-qty">
                                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                            {$form.quantity}
                                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                            <tbody>
                                <tr module="product_addoption">
                                    <th scope="row">{$add_option_name}</th>
                                    <td>
                                        {$form.add_option}
                                        <span class="byte" title="현재글자수/최대글자수">[ <strong class="length">0</strong> / {$option_maxlength} ]</span>
                                    </td>
                                </tr>
                            </tbody>
                            </table>
                        </div>
                       <div class="selectButton {$add_option_push_button_display|display}" id="{$add_option_push_button_id}"><button type="button" class="btnStrong" onclick="{$add_action_push_button}">옵션 선택</button></div>
                    </li>
                    <li>
                        <div class="information">
                            <div class="thumbnail"><a href="/product/detail.html?product_no={$product_no}"><img src="{$product_image}" alt="" id="{$image_id}"></a></div>
                            <p class="name">{$product_name}</p>
                            <p class="price {$product_price_del}">{$product_price}<span id="span_product_tax_type_text">{$product_tax_type_text}</span></p>
                            <p class="salePrice {$product_sale_price_display|display}">{$product_sale_price}</p>
                        </div>
                        <div class="option">
                           <table border="1" summary="">
                            <caption>옵션 정보</caption>
                            <colgroup>
                                <col style="width:105px;">
                                <col style="width:auto;">
                            </colgroup>

                            <tbody module="product_option">
                                <tr>
                                    <th scope="row">{$option_name}</th>
                                    <td>{$form.option}<p class="value">{$option_desc}</p></td>
                                </tr>
                                <tr module="product_quantity" class="quantity">
                                    <th scope="row">수량</th>
                                    <td>
                                        <div class="ec-base-qty">
                                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                            {$form.quantity}
                                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                            <tbody module="product_noneoption">
                                <tr>
                                    <th scope="row">상품선택</th>
                                    <td>{$form.noneoption}</td>
                                </tr>
                                <tr module="product_quantity" class="quantity">
                                    <th scope="row">수량</th>
                                    <td>
                                        <div class="ec-base-qty">
                                            <a href="javascript:;" class="qtyDown eClearDown"><img id="{$quantity_down_id}" class="{$quantity_down_class}" alt="down" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_down.jpg" width="33" height="29"></a>
                                            {$form.quantity}
                                            <a href="javascript:;" class="qtyUp eClearUp"><img id="{$quantity_up_id}" class="{$quantity_up_class}" alt="up" src="//img.echosting.cafe24.com/skin/mobile/common/ico_quantity_up.jpg" width="33" height="29"></a>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                            <tbody>
                                <tr module="product_addoption">
                                    <th scope="row">{$add_option_name}</th>
                                    <td>
                                        {$form.add_option}
                                        <span class="byte" title="현재글자수/최대글자수">[ <strong class="length">0</strong> / {$option_maxlength} ]</span>
                                    </td>
                                </tr>
                            </tbody>
                            </table>
                        </div>
                       <div class="selectButton {$add_option_push_button_display|display}" id="{$add_option_push_button_id}"><button type="button" class="btnStrong" onclick="{$add_action_push_button}">옵션 선택</button></div>
                    </li>
                </ul>
            </div>
        </div>

        <div id="{$total.total_id}" class="{$total.total_display|display}">
            <table border="1" summary="">
                <caption>상품 목록</caption>
                <colgroup>
                    <col style="width:auto;">
                    <col style="width:100px;">
                    <col style="width:35px;">
                </colgroup>
                <thead>
                    <tr>
                        <th scope="col">상품 정보</th>
                        <th scope="col">가격</th>
                        <th scope="col">삭제</th>
                    </tr>
                </thead>
                <!-- 옵션선택 또는 세트상품 선택시 상품이 추가되는 영역입니다. 쇼핑몰 화면에는 아래와 같은 마크업구조로 표시됩니다. 삭제시 기능이 정상동작 하지 않습니다. -->
                <tbody>
                    <!-- 상품 목록 -->
                </tbody>
                <!-- // 옵션선택 또는 세트상품 선택시 상품이 추가되는 영역입니다. 쇼핑몰 화면에는 아래와 같은 마크업구조로 표시됩니다. 삭제시 기능이 정상동작 하지 않습니다. -->
            </table>
        </div>
        <div id="{$total.total_price_id}" class="totalPrice">
            <strong>총상품금액(수량)</strong> <span class="{$total.total_cnt}"><strong class="price">0</strong></span>
        </div>
        <p class="ec-base-help {$price_warning_class}">할인가가 적용된 최종 결제예정금액은 주문 시 확인할 수 있습니다.</p>



        <div module="product_action" id="{$fixed_action_button}">
            <div class="ec-base-button gColumn {$action_display|display}">
                <a href="#none" class="d_buy btnStrong {$buy_display|display}" onclick="{$action_buy}"><span id="{$btn_buy_mobile_id}">구매하기</span><span class="{$btn_reserve_class|display}" id="{$btn_reserve_mobile_id}">예약주문</span><span id="{$btn_regular_delivery_id}" class="{$btn_regular_delivery|display}">정기배송 신청하기</span></a>
                <button type="button" class="btnEm {$basket_display|display}" onclick="{$action_basket}" id="actionCart">장바구니</button>
                <button type="button" class="btnEm {$wishlist_display|display}" onclick="{$action_wishlist}" id="actionWish">관심상품</button>                
            </div>
            <div class="ec-base-button gColumn soldout {$action_soldout_display|display}">
                <button type="button" class="d_buy btnStrong {$soldout_display|display}">품절</button>
                <button type="button" class="btnEm btnNormal {$wishlist_display|display}" onclick="{$action_wishlist}" id="actionWishSoldout">관심상품</button>
            </div>
            <!-- 네이버 체크아웃 구매 버튼  -->
            <div id="NaverChk_Button" style="display:none;"></div>
            <!-- 상품상세페이지에 추가되는 앱 관련 결제버튼's div -->
            <div id="{$app_payment_button_box_id}"></div>
        </div>

        <div module="product_action" class="ec-base-button gFixed" id="orderFixArea">            
            <div class="ec-base-button gColumn {$action_display|display}">
                <a href="#prdReview_target" class="d_review"><i>{$review_count|numberformat}</i>리뷰보기</a>
                <button type="button" class="btnNormal cart {$basket_display|display}" id="actionCartClone">장바구니</button>   
                <a href="#none" class="d_buy btnStrong {$buy_display|display}"><span id="{$btn_buy_mobile_clone_id}">N 구매하기</span><span class="{$btn_reserve_class|display}" id="{$btn_reserve_mobile_clone_id}">예약주문</span><span id="{$btn_regular_delivery_clone_id}" class="{$btn_regular_delivery|display}">정기배송 신청하기</span></a>                     
            </div>
            <div class="ec-base-button gColumn {$action_soldout_display|display}">
                <button type="button" class="btnStrong soldout {$soldout_display|display}">SOLD OUT</button>
            </div>
        </div>
    </div>
</div>



<!--관련상품-->
<div module="product_relation">
    <!--@css(/css/module/product/relation_swipe.css)-->
    <!--
        $count = 10
        $swipe = yes
        $line = 1
        $grid =2
    -->
    <h2>RECOMMEND</h2>
    <ul class="grid2" module="product_relationlist">
        <li class="item">
            <div class="thumbnail"><a href="{$link_product_detail}"><img src="{$img_small}" alt="{$seo_alt_tag}" class="thumb" /></a></div>
            <div class="information">
                <p class="name"><a href="{$link_product_detail}">{$name}</a></p>
                <p class="price {$product_sale_strike}">{$disp_product_price}{$product_tax_type_text}</p>
                <p class="price {$sale_price_display|display}">{$disp_sale_price}</p>
            </div>
        </li>
        <li class="item">
            <div class="thumbnail"><a href="{$link_product_detail}"><img src="{$img_small}" alt="{$seo_alt_tag}" class="thumb" /></a></div>
            <div class="information">
                <p class="name"><a href="{$link_product_detail}">{$name}</a></p>
                <p class="price {$product_sale_strike}">{$disp_product_price}{$product_tax_type_text}</p>
                <p class="price {$sale_price_display|display}">{$disp_sale_price}</p>
            </div>
        </li>
    </ul>
</div>
<!--/관련상품-->


<div module="product_additional">
    <!--@css(/css/module/product/additional.css)-->
    <!--@css(/css/module/product/additional_animation.css)-->
	<div id="prdDetail_target" class="tabGap"></div>
    <div id="tabProduct" class="ec-base-tab">
        <ul>
            <li class="selected"><a href="#prdDetail_target" target="_self">상품정보</a></li>
            <li><a href="#prdInfo_target">주문안내</a></li>
            <li class="{$review_display|display}"><a href="#prdReview_target" name="use_review">상품후기({$review_count})</a></li>
            <li class="{$qna_display|display}"><a href="#prdQnA_target" name="use_qna">상품문의({$qna_count})</a></li>
        </ul>
    </div>

    <div id="prdDetail">
        <div class="button" id="prdDetailBtn">
            <a href="/product/zoom.html?product_no={$product_no}" class="btnNormal">원본보기 <span class="ico"></span></a>
        </div>
        <div id="prdDetailContent">{$product_detail}</div>
    </div>
    
    <div id="prdInfo_target" class="tabGap"></div>
    <div id="tabProduct" class="ec-base-tab">
        <ul>
            <li><a href="#prdDetail_target" target="_self">상품정보</a></li>
            <li class="selected"><a href="#prdInfo_target">주문안내</a></li>
            <li class="{$review_display|display}"><a href="#prdReview_target" name="use_review">상품후기({$review_count})</a></li>
            <li class="{$qna_display|display}"><a href="#prdQnA_target" name="use_qna">상품문의({$qna_count})</a></li>
        </ul>
    </div>

    <div id="prdInfo">
        <!--@css(/css/module/product/detaildesign.css)-->
        
        <div class="faq">
            <div class="toggle eToggle selected {$payment_info|display}">
                <div class="title">
                    <h3>결제 안내</h3>
                </div>
                <div class="contents">
                    {$payment_info}
                </div>
            </div>
            <div class="toggle eToggle selected {$shipping_info|display}">
                <div class="title">
                    <h3>배송 안내</h3>
                </div>
                <div class="contents">
                    <ul>
                        <li>배송 방법 : {$shipping_method}</li>
                        <li>배송 지역 : {$shipping_area}</li>
                        <li>배송 비용 : {$shipping_fee}</li>
                        <li>배송 기간 : {$shipping_period}</li>
                        <li>배송 안내 : {$shipping_info}</li>
                    </ul>
                </div>
            </div>
            <div class="toggle eToggle selected {$exchange_info|display}">
                <div class="title">
                    <h3>교환/반품 안내</h3>
                </div>
                <div class="contents">
                    {$exchange_info}
                </div>
            </div>
            <div class="toggle eToggle selected {$service_info|display}">
                <div class="title">
                    <h3>서비스문의 안내</h3>
                </div>
                <div class="contents">
                    {$service_info}
                </div>
            </div>
        </div>
    </div>
    <div id="use_review"></div>
    <div id="prdReview_target" class="tabGap"></div>
    <div id="tabProduct" class="ec-base-tab">
        <ul>
            <li><a href="#prdDetail_target" target="_self">상품정보</a></li>
            <li><a href="#prdInfo_target">주문안내</a></li>
            <li class="selected {$review_display|display}"><a href="#prdReview_target" name="use_review">상품후기({$review_count})</a></li>
            <li class="{$qna_display|display}"><a href="#prdQnA_target" name="use_qna">상품문의({$qna_count})</a></li>
        </ul>
    </div>

    <div id="prdReview" class="{$review_display|display}">
        <div class="board">
            <h3>상품사용후기</h3>

            <a name="use_review"></a>

            <div module="product_review">
                <!--@css(/css/module/product/review.css)-->
                <!--@js(/js/module/product/review.js)-->
                <!--
                    $count = 5
                -->

                <p class="noAccess {$deny_display|display}">글읽기 권한이 없습니다.</p>

                <div class="minor {$adult_display|display}">
                    <p><span>19세 미만의 미성년자</span>는 출입을 금합니다.</p>
                    <a class="btnBasic" href="/intro/board.html{$returnParam}">성인인증하기</a>
                </div>

                <ul class="board {$list_display|display}">
                    <li>
                        <p class="descriptions">
                            <a href="/product/provider/review_read.xml{$param_read}">
                                <strong class="summary">{$icon_re} {$icon_lock} {$icon_mobile} {$subject} <span class="commentCnt">{$comment_count}</span> {$icon_hit} {$icon_file} </strong>
                                <span class="date {$date_display|display}" title="작성일">{$write_date|date:Y-m-d}</span>
                                <span class="id" title="작성자">{$writer}</span>
                                <span class="{$hit_display|display}">조회 {$hit_count}</span>
                                <span class="{$vote_display|display}">추천 {$vote}</span>
                                <span class="point {$use_point_display|display}"><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star{$point_count}.png" alt="{$point_count}점" width="50" height="8"> {$icon_new}</span>
                            </a>
                        </p>
                    </li>
                    <li>
                        <p class="descriptions">
                            <a href="/product/provider/review_read.xml{$param_read}">
                                <strong class="summary">{$icon_re} {$icon_lock} {$icon_mobile} {$subject} <span class="commentCnt">{$comment_count}</span> {$icon_hit} {$icon_file} </strong>
                                <span class="date {$date_display|display}" title="작성일">{$write_date|date:Y-m-d}</span>
                                <span class="id" title="작성자">{$writer}</span>
                                <span class="{$hit_display|display}">조회 {$hit_count}</span>
                                <span class="{$vote_display|display}">추천 {$vote}</span>
                                <span class="point {$use_point_display|display}"><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star{$point_count}.png" alt="{$point_count}점" width="50" height="8"> {$icon_new}</span>
                            </a>
                        </p>
                    </li>
                </ul>
            </div>

            <div module="product_reviewpaging" class="ec-base-paginate typeList">
                <a href="{$param_before}" class="btnPrev">이전 페이지</a>
                <ol>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                </ol>
                <a href="{$param_next}" class="btnNext">다음 페이지</a>
            </div>
            
            <div class="ec-base-button gColumn">
                <a href="{$review_list}" class="btnEm">전체보기</a>
                <a href="{$review_write}" class="btnSubmit">상품후기 작성</a>                
            </div>
        </div>
    </div>

    <div id="use_qna"></div>
    <div id="prdQnA_target" class="tabGap"></div>
    <div id="tabProduct" class="ec-base-tab">
        <ul>
            <li><a href="#prdDetail_target" target="_self">상품정보</a></li>
            <li><a href="#prdInfo_target">주문안내</a></li>
            <li class="{$review_display|display}"><a href="#prdReview_target" name="use_review">상품후기({$review_count})</a></li>
            <li class="selected {$qna_display|display}"><a href="#prdQnA_target" name="use_qna">상품문의({$qna_count})</a></li>
        </ul>
    </div>
    
    
    <div id="prdQnA" class="{$qna_display|display}">
        <div class="board">
            <h3>상품 Q&amp;A</h3>

            <a name="use_review"></a>

            <div module="product_qna">
                <!--@css(/css/module/product/qna.css)-->
                <!--@js(/js/module/product/qna.js)-->
                <!--
                    $count = 5
                -->

                <p class="noAccess {$deny_display|display}">글읽기 권한이 없습니다.</p>

                <div class="minor {$adult_display|display}">
                    <p><span>19세 미만의 미성년자</span>는 출입을 금합니다.</p>
                    <a class="btnBasic" href="/intro/board.html{$returnParam}">성인인증하기</a>
                </div>

                <ul class="board {$list_display|display}">
                    <li>
                        <p class="descriptions">
                            <a href="/board/product/read.html{$param_read}">
                                <strong class="summary">{$icon_re} {$icon_lock} {$icon_mobile} {$subject} <span class="commentCnt">{$comment_count}</span> {$icon_hit} {$icon_file}</strong>
                                <span class="id" title="작성자">{$writer}</span>
                                <span class="date {$date_display|display}" title="작성일">{$write_date}</span>
                                <span class="{$hit_display|display}">조회 {$hit_count}</span>
                                <span class="{$vote_display|display}">추천 {$vote}</span>
                                <span class="point {$use_point_display|display}"><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star{$point_count}.png" alt="{$point_count}점" width="50" height="8"> {$icon_new}</span>
                            </a>
                        </p>
                    </li>
                    <li>
                        <p class="descriptions">
                            <a href="/board/product/read.html{$param_read}">
                                <strong class="summary">{$icon_re} {$icon_lock} {$icon_mobile} {$subject} <span class="commentCnt">{$comment_count}</span> {$icon_hit} {$icon_file}</strong>
                                <span class="id" title="작성자">{$writer}</span>
                                <span class="date {$date_display|display}" title="작성일">{$write_date}</span>
                                <span class="{$hit_display|display}">조회 {$hit_count}</span>
                                <span class="{$vote_display|display}">추천 {$vote}</span>
                                <span class="point {$use_point_display|display}"><img src="//img.echosting.cafe24.com/skin/mobile_ko_KR/board/ico_star{$point_count}.png" alt="{$point_count}점" width="50" height="8"> {$icon_new}</span>
                            </a>
                        </p>
                    </li>
                </ul>
            </div>
            <div module="product_qnapaging" class="ec-base-paginate typeList">
                <a href="{$param_before}" class="btnPrev">이전 페이지</a>
                <ol>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                    <li><a href="{$param}" class="{$param_class}">{$no}</a></li>
                </ol>
                <a href="{$param_next}" class="btnNext">다음 페이지</a>
            </div>
            
            <div class="ec-base-button gColumn">
                <a href="{$qna_list}" class="btnEm">전체보기</a>
                <a href="{$qna_write}" class="btnSubmit">상품문의 작성</a>                
            </div>
        </div>
    </div>

    <div class="supplyInfo {$supply_info_display|display}">
        <h3 module="product_headcategory">판매자 정보</h3>
        <div class="{$supply_info_display|display}">
            {$supply_info}
        </div>
    </div>
</div>


