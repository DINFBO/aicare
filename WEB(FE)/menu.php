<?php

$uri= $_SERVER['REQUEST_URI'];

$m1="text-blueGray-700 hover:text-blueGray-500";
$m2=$m1;
$m3=$m1;
$m4=$m1;
$m0=$m1;
$mi_1="text-blueGray-300"; $mi_2=$mi_1; $mi_3=$mi_1; $mi_4=$mi_1; $mi_0=$mi_1;

if(strpos($uri, "diary") !== false ||strpos($uri, "ds_") !== false ) {  
    $m1= "text-pink-500 hover:text-pink-600";
	$mi_1="text-pink-500 hover:text-pink-600";
}
else if(strpos($uri, "data") !== false) {  
    $m2= "text-pink-500 hover:text-pink-600";
	$mi_2="text-pink-500 hover:text-pink-600";
}
else if(strpos($uri, "music") !== false) {  
    $m3= "text-pink-500 hover:text-pink-600";
	$mi_3="text-pink-500 hover:text-pink-600";
}
else if(strpos($uri, "consulting") !== false) {  
    $m4= "text-pink-500 hover:text-pink-600";
	$mi_4="text-pink-500 hover:text-pink-600";
}
else {  
    $m0= "text-pink-500 hover:text-pink-600";
	$mi_0="text-pink-500 hover:text-pink-600";
}


?>

<nav
    class="md:left-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-nowrap md:overflow-hidden shadow-xl bg-white flex flex-wrap items-center justify-between relative md:w-64 z-10 py-4 px-4">
    <div
        class="md:flex-col md:items-stretch md:min-h-full md:flex-nowrap px-0 flex flex-wrap items-center justify-between w-full mx-auto">

        <a class="hidden md:block text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm uppercase font-bold p-4 px-0"
            href="./index.php">
            마음건강 플랫폼 'AICARE' <img src='./img/stethoscope.svg' style='width:30px;display:inline; '>
        </a>
        <a class="block md:hidden text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm uppercase font-bold p-2 px-0"
            href="./index.php">
            <img src='./img/stethoscope.svg'
                style='width:35px;display:inline;position:absolute;top: 24px;left: 124px; '>
            <span class=" text-blueGray-500 block font-normal ">마음건강 플랫폼</span>
            'AICARE'
        </a>
        <ul class="md:hidden items-center flex flex-wrap list-none">

            <li class="inline-block relative">
                <a class="text-blueGray-500 block" href="./memb_info.php">
                    <div class="items-center flex">
                        <span class="w-12 h-12 inline-flex items-center justify-center rounded-full">
                            <img src='./img/user.png' style='width:50px;display:inline; '>
                        </span>
                    </div>
                </a>
            </li>
        </ul>
        <div class="md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute  left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1 rounded hidden"
            id="example-collapse-sidebar">

            <!-- Navigation -->
            <hr class="border-b-1 border-blueGray-200 md:hidden">
            <ul class="md:flex-col md:min-w-full flex flex-row list-none">
                <li class="items-center items-center-m">
                    <a href="./diary.php" class="text-xs uppercase py-3 font-bold block <?=$m0?>">
                        <i class="fas fa-heart mr-2 text-sm <?=$mi_0?> bottom_ic"></i>
                        오늘마음
                    </a>
                </li>

                <li class="items-center items-center-m">
                    <a href="data.php" class="text-xs uppercase py-3 font-bold block <?=$m2?>">
                        <i class="fas fa-search mr-2 text-sm <?=$mi_2?>   bottom_ic"></i>
                        마음분석
                    </a>
                </li>

                <li class="items-center items-center-m">
                    <a href="./music.php" class="text-xs uppercase py-3 font-bold block <?=$m3?>">
                        <i class="fas fa-music mr-2 text-sm <?=$mi_3?> bottom_ic"></i>
                        추천음악
                    </a>
                </li>

                <li class="items-center items-center-m">
                    <a href="./consulting.php" class="text-xs uppercase py-3 font-bold block <?=$m4?>">
                        <i class="fas fa-tv mr-2 text-sm  <?=$mi_4?> opacity-75 bottom_ic"></i>
                        원격상담
                    </a>
                </li>
            </ul>

        </div>
    </div>
</nav>
<div class="relative md:ml-64 bg-blueGray-50">
    <nav
        class="absolute top-0 left-0 w-full z-10 bg-transparent md:flex-row md:flex-nowrap md:justify-start flex items-center p-4">
        <div class="w-full mx-autp items-center flex justify-between md:flex-nowrap flex-wrap md:px-10 px-4">
            <a class="text-white text-sm uppercase hidden lg:inline-block font-semibold" href="./index.php"> </a>
            <div style='bottom: 50px;right:70px;'
                class="absolute fixedflex-row flex-wrap items-center lg:ml-auto mr-3 md_f se_wi md:w-5/12">

            </div>
            <a class='hidden pc_display' href="./memb_info.php" style='cursor:pointer;'><i
                    style='font-size:50px;margin-top:2px;'
                    class="rounded-full  fas fa-user w-full text-blueGray-200 bottom_ic"></i></a>
        </div>
    </nav>
