<!DOCTYPE html>
<html>
<head>
    <?php include("./head.php");?>
    <style>
    .inset-0 {
        top: 0px;
        right: 0px;
        bottom: 0px;
        left: 0px;
    }
    .opacity-25 {
        opacity: 0.25;
    }
    .max-w-sm {
        max-width: 24rem;
    }
    .p-5, .p-6 {
        padding: 1.25rem;
    }
    </style>
</head>

<body class="text-blueGray-700 antialiased">
    <div id="root">
        <!-- menu -->
        <?php include("./menu.php");?>

        <main>
            <div class="relative pt-16 flex content-center items-center justify-center">
                <div class="absolute top-0 w-full h-full bg-center bg-cover" style="
            background-image: url('https://newsimg.hankookilbo.com/cms/articlerelease/2019/02/17/201902171109795612_23.jpg');
          ">
                    <span id="blackOverlay" class="w-full h-full absolute opacity-75 bg-black"></span>
                </div>


                <div class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px"
                    style="transform: translateZ(0px)">
                    <svg class="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg"
                        preserveAspectRatio="none" version="1.1" viewBox="0 0 2560 100" x="0" y="0">
                        <polygon class="text-blueGray-200 fill-current" points="2560 0 2560 100 0 100"></polygon>
                    </svg>
                </div>
            </div>


            <section class="relative py-20">
                <div class="bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20"
                    style="transform: translateZ(0px)">
                    <svg class="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg"
                        preserveAspectRatio="none" version="1.1" viewBox="0 0 2560 100" x="0" y="0">
                        <polygon class="text-white fill-current" points="2560 0 2560 100 0 100"></polygon>
                    </svg>
                </div>
                <div class="container mx-auto px-4">
                    <div class="items-center flex flex-wrap">
                        <div class="w-full md:w-4/12 ml-auto mr-auto px-4">
                            <img alt="..." class="max-w-full rounded-lg shadow-lg"
                                src="https://newsimg.hankookilbo.com/cms/articlerelease/2019/02/17/201902171109795612_23.jpg">
                        </div>
                        <div class="w-full md:w-5/12 ml-auto mr-auto px-4">
                            <div class="md:pr-12">
                                <div
                                    class=" hidden text-pink-600 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-pink-300">
                                    <i class="fas fa-rocket text-xl"></i>
                                </div>
                                <h3 class="text-3xl font-semibold mt-4">혼자 끙끙 앓지 마세요!</h3>
                                <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
                                    AICARE가 여러분의 마음을 잘 아시는 상담사분들 추천해드립니다!
                                </p>
                                <ul class="list-none mt-6">
                                    <li class="py-2">
                                        <div class="flex items-center">
                                            <div>
                                                <span
                                                    class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-pink-600 bg-pink-200 mr-3"><i
                                                        class="fas fa-fingerprint"></i></span>
                                            </div>
                                            <div>
                                                <h4 class="text-blueGray-500">
                                                    개인화 맞춤 추천알고리즘
                                                </h4>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="py-2">
                                        <div class="flex items-center">
                                            <div>
                                                <span
                                                    class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-pink-600 bg-pink-200 mr-3"><i
                                                        class="fab fa-html5"></i></span>
                                            </div>
                                            <div>
                                                <h4 class="text-blueGray-500">100% 익명보안 된 상담내역</h4>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="py-2">
                                        <div class="flex items-center">
                                            <div>
                                                <span
                                                    class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-pink-600 bg-pink-200 mr-3"><i
                                                        class="far fa-paper-plane"></i></span>
                                            </div>
                                            <div>
                                                <h4 class="text-blueGray-500">쉽고 빠른 상담연결</h4>
                                            </div>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section class="pt-8 pb-48">
                <div class="container mx-auto px-4">
                    <div class="flex flex-wrap">
                        <div class="w-full md:w-6/12 lg:w-3/12 lg:mb-0 mb-12 px-4">
                            <div class="px-6">
                                <img alt="..." src="http://www.ynkclinic.com/images/introduction/doctor_img01.gif"
                                    class="shadow-lg rounded-full mx-auto max-w-120-px">
                                <div class="pt-6 text-center">
                                    <h5 class="text-xl font-bold">유상우 원장</h5>
                                    <p class="mt-1 text-sm text-blueGray-600 uppercase font-semibold">
                                        공황장애, 사회불안장애, 인지행동치료
                                    </p>
                                    <p class="mt-1 text-sm text-blueGray-400 uppercase">
                                        정신건강의학과 전문의/의학박사<BR>
                                        연세 Yoo&Kim 정신건강의학과 원장<BR>
                                        現 연세의대 정신과학 교실 임상/외래교수<BR>
                                        現 한림의대 정신과학 교실 외래교수
                                    </p>
                                    <div class="mt-6">
                                        <button
                                            class="bg-lightBlue-400 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-6"
                                            type="button">
                                            <i class="fab fa-twitter"></i></button><button
                                            class="bg-lightBlue-600 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1"
                                            type="button">
                                            <i class="fab fa-facebook-f"></i></button><button
                                            class="bg-pink-500 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1"
                                            type="button">
                                            <i class="fab fa-dribbble"></i>
                                        </button>
                                        <BR>
                                        <button
                                            class="bg-amber-500 text-white active:bg-amber-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                            type="button">
                                            <i class="fas fa-heart"></i> 상담신청하기
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="w-full md:w-6/12 lg:w-3/12 lg:mb-0 mb-12 px-4">
                            <div class="px-6">
                                <img alt="..." src="http://mentor.d21.org/images/contents/cnt1501_img12.jpg"
                                    class="shadow-lg rounded-full mx-auto max-w-120-px">
                                <div class="pt-6 text-center">
                                    <h5 class="text-xl font-bold">김신희 상담사</h5>
                                    <p class="mt-1 text-sm text-blueGray-600 uppercase font-semibold">
                                        청소년, 성인 / 성격, 대인관계, 정서, 미술치료
                                    </p>
                                    <p class="mt-1 text-sm text-blueGray-400 uppercase">
                                        상담심리사 2급(한국상담심리학회)<BR>
                                        청소년 상담사 2급(여성가족부) <BR>
                                        MBTI 일반강사(한국MBTI연구소) <BR>
                                        미술심리상담사 2급(한국심성교육개발원)

                                    </p>
                                    <div class="mt-6">
                                        <button
                                            class="bg-lightBlue-400 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-6"
                                            type="button">
                                            <i class="fab fa-twitter"></i></button><button
                                            class="bg-lightBlue-600 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1"
                                            type="button">
                                            <i class="fab fa-facebook-f"></i></button><button
                                            class="bg-pink-500 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1"
                                            type="button">
                                            <i class="fab fa-dribbble"></i>
                                        </button><br>
                                        <button
                                            class="bg-amber-500 text-white active:bg-amber-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                            type="button">
                                            <i class="fas fa-heart"></i> 상담신청하기
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section class="relative block py-24 lg:pt-0 bg-blueGray-800 ">
                <div class="container mx-auto px-4">
                    <div class="flex flex-wrap justify-center lg:-mt-64 -mt-48">
                        <div class="w-full lg:w-6/12 px-4">
                            <div
                                class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200">
                                <div class="flex-auto p-5 lg:p-10">
                                    <h4 class="text-2xl font-semibold">상담과정에서 불편한 점이 있으세요?</h4>
                                    <p class="leading-relaxed mt-1 mb-4 text-blueGray-500">
                                        밑에 카드를 작성해서 보내주시면 24시간내에 연락드립니다.
                                    </p>
                                    <div class="relative w-full mb-3 mt-8">
                                        <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                                            for="full-name">이름</label><input type="text"
                                            class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                                            placeholder="Full Name">
                                    </div>
                                    <div class="relative w-full mb-3">
                                        <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                                            for="email">Email</label><input type="email"
                                            class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                                            placeholder="Email">
                                    </div>
                                    <div class="relative w-full mb-3">
                                        <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                                            for="message">내용</label><textarea rows="4" cols="80"
                                            class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                                            placeholder="Type a message..."></textarea>
                                    </div>
                                    <div class="text-center mt-6">
                                        <button
                                            class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                                            type="button">
                                            보내기
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </main>

        <?php include("./footer.php");?>

    </div>
    </div>
    </div>


    <script src="https://unpkg.com/@popperjs/core@2/dist/umd/popper.js"></script>
    <script>
    function toggleModal(modalID) {
        document.getElementById(modalID).classList.toggle("hidden");
        document.getElementById(modalID + "-backdrop").classList.toggle("hidden");
        document.getElementById(modalID).classList.toggle("flex");
        document.getElementById(modalID + "-backdrop").classList.toggle("flex");
    }
    </script>
</body>

</html>