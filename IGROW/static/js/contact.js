
// contact 이메일 보내기 기능
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // 기본 폼 제출 방지

        const formData = new FormData(form);

        fetch("/api/send-email/", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                alert("문의가 성공적으로 전송되었습니다.");
                form.reset();
            } else {
                alert("오류 발생: " + data.message);
            }
        })
        .catch(error => {
            alert("메일 전송 중 문제가 발생했습니다.");
            console.error("Error:", error);
        });
    });
});


// 보류// recruit 내부 이동 기능
// document.addEventListener("DOMContentLoaded", function () {
//     // 현재 URL에서 target 파라미터 가져오기
//     const urlParams = new URLSearchParams(window.location.search);
//     const targetId = urlParams.get("target");

//     if (targetId) {
//         const targetElement = document.getElementById(targetId);
//         if (targetElement) {
//             // 부드럽게 스크롤 이동
//             setTimeout(() => {
//                 targetElement.scrollIntoView({ behavior: "smooth" });
//             }, 500); // 페이지가 완전히 로드된 후 이동하도록 약간의 딜레이 추가
//         }
//     }

//     // 같은 페이지에서 버튼 클릭 시 동작
//     document.querySelectorAll('a[href*="?target="]').forEach(anchor => {
//         anchor.addEventListener("click", function (e) {
//             const url = new URL(this.href);
//             const clickedTarget = url.searchParams.get("target");

//             if (window.location.pathname === url.pathname) {
//                 e.preventDefault(); // 페이지 이동 방지
//                 const targetElement = document.getElementById(clickedTarget);
//                 if (targetElement) {
//                     targetElement.scrollIntoView({ behavior: "smooth" });
//                 }
//             }
//         });
//     });
// });