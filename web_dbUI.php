<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link href="style_2208A.css" rel="stylesheet" type="text/css">
        <title>SUROS 蘇羅士科技</title>
    </head>
    <body>
        <span class="block_head">    <!--banner-->
            <span class="block_25x20">
                <img class="logo_suros" src="image/suros_2208A.jpg" />
            </span>
            <span class="block_75x20">
                <span class="title_head">外部資產調查報告查詢</span>
            </span>
        </span>
        <div class="block_body">
            <form method="post">
                <div class="block_35x30">    <!--search-->
                    <input class ="search_bar1" type="text" name="search_name" id="searcsth_nameKey" placeholder="請輸公司名" />
                    <input class ="search_bar2" type="text" name="search_url" id="search_urlKey" />    <!--placeholder="請輸入網址"-->
                    <button class="icon_search" type="submit" name="go_search" id="searchBtn" onclick="<?php print_r ($phpArr2D); ?>"><img src="image/search_2208A.png" /></button>
                    <button class="icon_del" type="reset" name="clear_input" id="clearBtn"><img src="image/del_2208A.png" /></button>
                </div>
                <hr class="line_35A" />
                <div class="block_35x50">    <!--filter-->
                    <input class="check_box" type="checkbox" name="filterA[]" value="edu" />
                    <label class="txt_with_box">教育知識</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="fin" />
                    <label class="txt_with_box">金融業</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="gov" />
                    <label class="txt_with_box">政府機關</label>
                    <br />
                    <input class="check_box" type="checkbox" name="filterA[]" value="life" />
                    <label class="txt_with_box">能源環境</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="medi" />
                    <label class="txt_with_box">醫藥業</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="net" />
                    <label class="txt_with_box">電網資訊</label>
                    <br />
                    <input class="check_box" type="checkbox" name="filterA[]" value="manu" />
                    <label class="txt_with_box">傳統產業</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="serv" />
                    <label class="txt_with_box">服務業</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="stor" />
                    <label class="txt_with_box">百貨零售</label>
                    <br />
                    <input class="check_box" type="checkbox" name="filterA[]" value="tech" />
                    <label class="txt_with_box">電子科技</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="com" />
                    <label class="txt_with_box">其它</label>
                    <hr class="line_35B1" />
                    <br />
                    <br />
                    <br />
                    <br />
                    <input class="check_box" type="checkbox" name="filterA[]" value="上市" />
                    <label class="txt_with_box">上市</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="上櫃" />
                    <label class="txt_with_box">上櫃</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="興櫃" />
                    <label class="txt_with_box">興櫃</label>
                    <hr class="line_35B2" />
                    <br />
                    <br />
                    <br />
                    <br />
                    <input class="check_box" type="checkbox" name="filterA[]" value="100" />
                    <label class="txt_with_box">100大</label>
                    <input class="check_box" type="checkbox" name="filterA[]" value="300" />
                    <label class="txt_with_box">300大</label>
                    <hr class="line_35B3" />
                    <br />
                    <br />
                    <br />
                    <br />
                    <input class="check_box" type="checkbox" name="filterA[]" value="台50" />
                    <label class="txt_with_box">台50</label>
                    <br />
                    <br />
                    <!--<button class="icon_filter" type="submit" name="go_filter" id="filterBtn" onclick="<?php //print_r ($phpArr2D); ?>"><img src="image/filter_2208A.png"></button>
                    <button class="icon_no_filter" type="reset" name="clear_filters" id="clearBtn"><img src="image/no_filter_2208A.png"></button>-->
                </div>
            </form>
            <div class="block_65x80">    <!--result list-->
                <ul class="list_header">
                    <li class="list_name">　公　　司　　名　　稱　　</li>
                    <li class="list_date">日　期　</li>
                    <li class="list_file">報告檔案　</li>
                </ul>
                <div class="list_row">
                    <?php
                    function go_search ($searchKey) {
                        $pathPySearch = 'python web_dbAPI_search.py ';    //python file path with one space in the end
                        $pyReSearch = exec ($pathPySearch.$searchKey);    //execute cmd to run python
                        $pyReSearch = iconv('big5', 'utf-8', $pyReSearch);    //get python search result
                        if (empty($pyReSearch) == true) {
                            return 0;
                        } else {
                            return $pyReSearch;
                        }
                    }

                    
                    function go_filter ($filterKey) {
                        $iptFilterA = '';
                        for ($i = 0; $i < count($filterKey); $i++){
                            if ($i == 0){
                                $iptFilterA = $filterKey[$i];
                            } else {
                                $iptFilterA.=',';
                                $iptFilterA.=$filterKey[$i];
                            }
                        }
                        $pathPyFilter = 'python_test.py ';    //python file path with one space in the end
                        $pyReFilter = exec ($pathPyFilter.$iptFilterA);    //execute cmd to run python
                        $pyReFilter = iconv('big5', 'utf-8', $pyReFilter);    //get python filter result
                        if (empty($pyReFilter) == true) {
                            return 0;
                        } else {
                            return $pyReFilter;
                        }
                    }
                    
                    
                    function str2arr ($str) {
                        $phpStr = str_replace(array('[', ']', "'",), '',$str);
                        
                        $phpArr = explode(',',$phpStr);    //split php string by ','
                        for ($k = 0; $k < count($phpArr); $k++ ){    //get list to array
                            $i = floor($k/4);
                            $j = $k%4;
                            $arr2D [$i][$j] = $phpArr[$k];
                        }
                        return $arr2D;
                    }
                    
                    
                    function get_pyList () {
                        if (isset ($_POST['search_name']) == true) {
                            $pyReStrS = go_search ($_POST['search_name']);
                            if (empty ($pyReStrS) == true) {
                                return 0;
                            } else {
                                $phpArrS = str2arr ($pyReStrS);
                                return $phpArrS;
                            }
                        } else {
                            $iptFilters = $_POST['filterA'];
                            $filterArr = implode (",", $iptFilters);
                            $pyReStrF = go_filter ($filterArr);
                            if (empty ($pyReStrF) == true) {
                                return 0;
                            } else {
                                $phpArrF = str2arr ($pyReStrF);
                                return $phpArrF;
                            }
                        }
                    }

                    
                    $phpArr2D = get_pyList ();
                    if (empty ($phpArr2D) == false) {
                        for ($i = 0; $i < count($phpArr2D); $i++ ){
                            echo '<ul>';
                            print_r ('<li class="list_name">'.$phpArr2D[$i][0].'</li>');
                            $cellDate = '20'.substr($phpArr2D[$i][1], 1, 2).'/'.substr($phpArr2D[$i][1], 3, 2).'/'.substr($phpArr2D[$i][1], -2, 2);
                            echo ('<li class="list_date">'.$cellDate.'</li>');
                            if ($phpArr2D[$i][2] == 'False') {
                                echo '<li class="list_file">';
                            } else {
                                $pdfUrl = str_replace ('\\\\', '/', $phpArr2D[$i][2]);
                                $pdfUrl = str_replace ('C:/SUROS_BI/', '/', $pdfUrl);
                                echo '<li class="list_file">　<a href="'.$pdfUrl.'"><img src="image/pdf_2208A.png" class="img" /></a>';
                            }
                            if ($phpArr2D[$i][3] == 'False') {
                                echo '</li></ul>';
                            } else {
                                $csvUrl = str_replace('\\\\', '/', $phpArr2D[$i][3]);
                                $csvUrl = str_replace ('C:/SUROS_BI/', '/', $csvUrl);
                                echo '　<a href="'.$csvUrl.'"><img src="image/csv_2208A.png" class="img" /></a></li></ul>';
                            }
                        }
                    } else {
                        echo '<ul>';
                        echo '<li class="list_name">SORRY, NO DATA...</li></ul>';
                    }
                    ?>
                </div>
            <footer>
                <p>Copyright © 2022 SUROS Inc. 蘇羅士科技股份有限公司</p>
            </footer>
        </div>
    </body>
</html>
