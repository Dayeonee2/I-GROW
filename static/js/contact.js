document.addEventListener("DOMContentLoaded", function () {
    // 폼 제출 이벤트 추가 (폼이 존재하는 경우에만)
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // 기본 폼 제출 방지
            const formData = new FormData(form);

            fetch("/api/send-email/", {
                method: "POST",
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`서버 오류: ${response.status}`);
                }
                return response.json();
            })
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
    }

    // Intersection Observer 설정
    const boxes = document.querySelectorAll(".showshow");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            } else {
                entry.target.classList.remove("show");
            }
        });
    }, { threshold: 0.3 });

    boxes.forEach(box => observer.observe(box));
});
