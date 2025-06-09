import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from email.mime.application import MIMEApplication  # 用于附件
from email.header import Header # 处理中文标题/附件名

# 配置参数
SMTP_SERVER = "smtp.qiye.aliyun.com"  # 阿里企业邮箱SMTP服务器
PORT = 465  # SSL加密端口
SENDER_EMAIL = "zhaoyuhang@xiangyulife.com"  # 发件邮箱
SENDER_PASSWORD = "TCqdeeKNPFMrX4n6"  # 邮箱授权码
RECEIVER_EMAIL = "yhzhaohy@hotmail.com"  # 收件邮箱

def send_text():
    replace_text = "2025-06-06 中信银行"
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = f"{replace_text} 数据下载成功"
    msg.set_content(f"{replace_text}对账单 数据下载成功，请注意查看。")
    # 连接SMTP服务器并发送邮件（使用SSL加密）
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # 登录
            server.send_message(msg)                     # 发送邮件
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败，错误原因：{e}")


def send_mime():
    replace_text = "2025-06-06 中信银行"
    # 初始化多部分邮件（支持文本+HTML+附件）
    msg = MIMEMultipart()
    msg["From"] = Header(SENDER_EMAIL, "utf-8")
    msg["To"] = Header(RECEIVER_EMAIL, "utf-8")
    msg["Subject"] = Header(f"{replace_text} 数据下载成功", "utf-8")

    
    # 添加HTML正文（优先显示HTML，若客户端不支持则显示纯文本）
    html_content = f"""
    <html>
    <body>
        <h1>这是一封通知邮件</h1>
        <p><b>{replace_text}对账单</b> 数据下载成功 </p>
        <p><a href='https://www.python.org'>测试连接</a></p>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_content, "html", "utf-8"))  # HTML部分
    msg.attach(MIMEText("若无法显示HTML，请查看此纯文本内容", "plain", "utf-8"))  # 备用文本
    
    # 添加附件（以PDF为例，可替换为任意文件）
    with open("D:\\ioTest\\Excel_test.xlsx", "rb") as f:
        part = MIMEApplication(f.read(), Name="Excel_test.xlsx")
        part["Content-Disposition"] = f'attachment; filename="Excel_test.xlsx"'
        msg.attach(part)

    # 发送邮件
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("HTML+附件邮件发送成功！")
    except Exception as e:
        print(f"发送失败，错误原因：{e}")

if __name__ == "__main__":
    send_mime()