# features/tutorials.py

tutorials = {
    "أمن الويب": """
🔐 شروحات أمن الويب:

1. SQL Injection
2. XSS – Cross Site Scripting
3. CSRF – Cross Site Request Forgery
4. Clickjacking
5. Broken Authentication
6. Security Headers

📚 تعلم الأساسيات وطرق الحماية بالتفصيل.
""",
    "أمن الشبكات": """
🌐 شروحات أمن الشبكات:

1. أنواع الشبكات (LAN, WAN)
2. الجدران النارية (Firewalls)
3. IDS / IPS
4. VPN – الشبكات الخاصة الافتراضية
5. تحليل الترافيك – Wireshark

📚 خطوات عملية للفهم والتطبيق.
""",
    "التشفير": """
🔒 شروحات التشفير:

1. التشفير الكلاسيكي: Caesar, Vigenère
2. التشفير الحديث: AES, RSA
3. Diffie-Hellman
4. Hashing: MD5, SHA

📚 كيف تعمل؟ كيف تُستخدم؟ كيف تُكسر؟
""",
    "مقدمة الأمن السيبراني": """
🛡️ مقدمة في الأمن السيبراني:

1. المفاهيم الأساسية
2. أنواع الهجمات
3. أدوات الدفاع
4. المجالات المختلفة

💡 دليلك لفهم مجال السيبراني من البداية حتى الاحتراف.
"""
}

def get_tutorial(topic: str) -> str:
    return tutorials.get(topic.strip(), "❌ عذرًا، لم يتم العثور على شرح بهذا العنوان.")
