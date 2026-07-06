# Data Science Bootcamp - Geometry Package & Advanced OOP (HW_L2_3)

این مخزن شامل پاسخ تمرین پیاده‌سازی پکیج هندسی با استفاده از مفاهیم پیشرفته شیءگرایی (برنامه‌نویسی انتزاعی)، سیستم ساختاریافته مدیریت خطا و ذخیره‌سازی داده‌ها در فایل متنی است.
This repository contains the solution for designing a comprehensive geometry package using Advanced Object-Oriented Programming (Abstract Base Classes), structured input validation error handling, and file I/O operations.

---

## 📂 ساختار پکیج و فایل‌ها (Package Structure)

* **`Geometry/`**: پوشه اصلی پکیج هندسه (Package Folder).
  * `shape.py`: کلاس انتزاعی پایه برای همه اشکال هندسی[cite: 15].
  * `square.py`: کلاس محاسبات و اعتبار سنجی مربع[cite: 16].
  * `circle.py`: کلاس محاسبات و اعتبار سنجی دایره[cite: 13].
  * `rectangle.py`: کلاس محاسبات و اعتبار سنجی مستطیل[cite: 14].
  * `triangle.py`: کلاس محاسبات، اعتبار سنجی و بررسی قانون نامساوی مثلث[cite: 17].
* **`main.py`**: فایل اصلی تست برنامه، فرخوانی اشکال و مدیریت فرآیند خروجی[cite: 12].
* **`shape_output.txt`**: فایل متنی خروجی که محاسبات موفق یا خطاهای مربوط به هر شکل را ذخیره می‌کند[cite: 11, 12].

---

## 📌 صورت سوال و ویژگی‌ها (Assignment Features)

### 1️⃣ کلاس انتزاعی پایه (Abstract Base Class)
* **توضیحات (FA):** پیاده‌سازی کلاس پایه `Shape` با استفاده از ماژول `abc` به طوری که متدهای محیط (`perimeter`) و مساحت (`area`) به صورت انتزاعی تعریف شده و تمامی اشکال ملزم به پیاده‌سازی آن‌ها باشند[cite: 15].
* **Description (EN):** Built an abstract base class `Shape` using the `abc` module, defining abstract methods for `area()` and `perimeter()` to enforce uniform structure across all geometric sub-classes[cite: 15].

### 2️⃣ سیستم جامع اعتبار سنجی داده‌ها (Robust Data Validation)
* **توضیحات (FA):** بررسی دقیق نوع داده‌های ورودی (مانند رشته نبودن ورودی‌ها)[cite: 13, 14, 16, 17]، بررسی مثبت بودن مقادیر عددی[cite: 13, 14, 16, 17] و کنترل قوانین هندسی (مانند صدق کردن اضلاع در قانون نامساوی مثلث)[cite: 17]. در صورت بروز هرگونه مشکل، وضعیت `valid` تغییر کرده و خطاها در لیست `errors` ذخیره می‌شوند[cite: 13, 14, 16, 17].
* **Description (EN):** Implemented strict input validation including data type checks[cite: 13, 14, 16, 17], positive-value enforcement[cite: 13, 14, 16, 17], and geometric rules (e.g., Triangle Inequality Theorem)[cite: 17]. Errors are caught gracefully and stored in a stateful `errors` list[cite: 13, 14, 16, 17].

### 3️⃣ سیستم ذخیره‌سازی خروجی (File Output System)
* **توضیحات (FA):** پس از بررسی لیستی از اشکال گوناگون (با مقادیر درست و نادرست)، برنامه نتایج محاسبات اشکال صحیح را تا دو رقم اعشار و همچنین لیست خطاهای اشکال نامعتبر را به صورت خودکار در فایل `shape_output.txt` ذخیره می‌کند[cite: 11, 12].
* **Description (EN):** Evaluates a test list of various shapes (both valid and erroneous)[cite: 12]. Valid shapes have their calculated area and perimeter logged, while invalid shapes have their specific validation errors recorded directly into `shape_output.txt`[cite: 11, 12].

---

## 👨‍💻 نویسنده (Author)
* **Zargol Kanani** (زرگل کنعانی)
