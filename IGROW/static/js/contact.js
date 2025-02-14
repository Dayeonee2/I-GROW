
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