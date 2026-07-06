# Data Science Bootcamp - OOP & Advanced Python Homework (HW_L2_2)

این مخزن شامل پاسخ تکالیف و تمرین‌های بخش شیءگرایی (OOP) و پایتون پیشرفته در بوت‌کمپ دیتاساینس است.
This repository contains the solutions for the Object-Oriented Programming (OOP) and Advanced Python homework assignments in the Data Science Bootcamp.

---

## 📌 صورت سوالات و تمرین‌ها (Assignments Description)

### 1️⃣ تمرین اول: شمارش فراوانی کلمات (Practice 1: Word Frequency Dictionary)
* **فایل کد:** `Practice1.py`
* **توضیحات (FA):** برنامه‌ای بنویسید که یک رشته را از ورودی دریافت کرده، فراوانی هر کلمه را شمارش کند و نتیجه را در یک دیکشنری ذخیره و چاپ کند.
* **Description (EN):** Write a program that takes a string as input, counts the frequency of each word, and stores the results in a dictionary.

---

### 2️⃣ تمرین دوم: فیلتر و دسته‌بندی سنین با `*args` (Practice 2: Age Filtering & Categorization)
* **فایل کد:** `Practice2.py`
* **توضیحات (FA):** تابعی به نام `age_filter` بنویسید که یک مقدار `value` و تعداد نامشخصی سن (`*args`) دریافت کند. با استفاده از `filter` و `map` سنین کمتر از `value` را حذف کرده و باقی‌مانده را به سه گروه (Young < 40، Middle-aged < 65، Old >= 65) دسته‌بندی کند.
* **Description (EN):** Implement an `age_filter` function using `*args`, `filter()`, and `map()` to remove ages below a given `value` and categorize the remaining ones into "Young", "Middle-aged", or "Old".

---

### 3️⃣ تمرین سوم: اعتبار سنجی اطلاعات مشتری (Practice 3: Customer Data Validation Class)
* **فایل کد:** `Practice3.py`
* **توضیحات (FA):** کلاسی به نام `Customer` با ویژگی‌های نام، ایمیل و شماره تلفن بسازید. توابع `is_valid_email` و `is_valid_phone` را برای بررسی ساختار صحیح ایمیل و شماره تلفن (حداقل ۱۰ رقم، شامل ارقام و علائم مجاز) پیاده‌سازی کنید.
* **Description (EN):** Create a `Customer` class with attributes for name, email, and phone number. Implement validation methods `is_valid_email()` and `is_valid_phone()` to ensure inputs follow standard formats.

---

### 4️⃣ تمرین چهارم: سیستم مدیریت وسایل نقلیه - شیءگرایی (Practice 4: Vehicle Management System - OOP)
* **فایل کد:** `practice4.py`
* **توضیحات (FA):** کلاسی پایه به نام `Vehicle` همراه با صفت خصوصی `model` (دارای Getter/Setter)، متد محاسبه قیمت و متد مقایسه ابجکت‌ها (`__eq__`) بسازید. سپس کلاس‌های فرزند `Car`، `Motorcycle` و `Bicycle` را با ارث‌بری پیاده‌سازی کرده و متدهای نمایش اطلاعات و محاسبه قیمت را بازنویسی (Override) کنید.
* **Description (EN):** Develop a comprehensive `Vehicle` base class with a private `model` attribute (using getter/setter properties), price calculation, and equality comparison. Extend this class into `Car`, `Motorcycle`, and `Bicycle` subclasses, overriding methods for custom behaviors.

---

## 👨‍💻 نویسنده (Author)
* **Zargol Kanani** (زرگل کنعانی)
