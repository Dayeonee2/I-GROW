from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt  # 추가(MG)
from django.conf import settings  # 추가(MG)

def main(request):
    return render(request, 'main.html')

def contact(request):
    return render(request, 'contact.html')

@csrf_exempt  # CSRF 예외 처리 추가
def send_contact_email(request):
    if request.method == "POST":
        company = request.POST.get("company", "")
        name = request.POST.get("name", "")
        user_email = request.POST.get("email", "")  # 사용자가 입력한 이메일
        phone = request.POST.get("phone", "")
        body = request.POST.get("body", "")

        subject = f"문의사항 from {name} ({company})"
        message = f"""
        회사명: {company}
        성함: {name}
        이메일: {user_email}
        연락처: {phone}

        문의 내용:
        {body}
        """

        recipient_email = "ekdus2561@naver.com"  # 문의를 받을 관리자 이메일
        sender_email = settings.EMAIL_HOST_USER  # 발신자 이메일 (네이버 계정)

        try:
            send_mail(
                subject,
                message,
                sender_email,  # ✅ 발신자를 네이버 계정으로 설정
                [recipient_email],
                fail_silently=False,
            )
            return JsonResponse({"status": "success", "message": "문의가 성공적으로 전송되었습니다."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"메일 전송 중 오류가 발생했습니다: {str(e)}"})

    return JsonResponse({"status": "error", "message": "잘못된 요청입니다."}, status=400)